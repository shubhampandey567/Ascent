#!/usr/bin/env python3
"""Progress tracker for the AI learning path: the one place where learning gets recorded.

The Mentor runs this script to record everything that happens: study sessions, lesson quizzes,
spaced reviews, projects, exams, weekly checks and weak spots. It keeps an append-only log in
tracker/events.jsonl, schedules reviews through tools/srs.py, and after every change rebuilds
two read-only views: tracker/progress.md (the dashboard) and tracker/weak-spots.md.
`weekly` also saves a dated snapshot in tracker/reports/. Standard library only.

Pace is measured against the curriculum itself: the script reads every lesson heading in
curriculum/*.md, knows which plan week each lesson belongs to, and compares what has been
finished with what the chosen pace (light, standard or intense) expects by today.

Commands (put --date YYYY-MM-DD before the command to record a past day):
  status                                         start-of-session briefing, with alerts
  setup --pace standard [--start DATE] [--goal-days 4] [--minutes 60] [--review-cap 8]
  session --minutes 70 [--energy 4] [--note TEXT]
  lesson ID --score 80 [--confident-wrong 1]     a lesson's quiz (also schedules its reviews)
  lesson ID --done                               a lesson without a quiz (project work, builds)
  review ID SCORE                                a spaced-review score (0-100)
  project ID --score 82 --verdict pass|revise
  exam ID --score 76 --verdict pass|retake [--parts A=8,B=7,C=4,D=3]
  weekly --test 72 --aioff 68 [--hours 9.5] [--energy 3] [--note TEXT]
  weak add LESSON-ID "what went wrong"  |  weak pass WS-3  |  weak fail WS-3  |  weak list
  next                                           the next lesson
  lessons [--phase N]                            every lesson, with done marks
  report                                         rebuild the dashboard views
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import date, timedelta
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS))
import srs  # noqa: E402  (sibling module)

PACE_FACTOR = {"light": 0.6, "standard": 1.0, "intense": 1.5}  # plan weeks per calendar week
CONSOLIDATION_WEEKS = (13, 28, 44, 60)
TOTAL_PLAN_WEEKS = 72
PASS_MARK = 60
WEAK_FIXED_AFTER = 3  # unaided correct recalls on different days
HEADING = re.compile(
    r"^####\s+(?P<id>(?:P\d+-W\d+|C<week>)-(?:L\d+|B|M))(?:\s+(?:and|to)\s+L(?P<to>\d+))?\s*·\s*(?P<title>.+?)\s*$",
    re.M,
)


def use_root(root: Path) -> None:
    """Point the tracker (and srs) at a workspace folder. Tests call this with a temp folder."""
    global ROOT, CURRICULUM, TRACKER, EVENTS
    ROOT = root
    CURRICULUM = root / "curriculum"
    TRACKER = root / "tracker"
    EVENTS = TRACKER / "events.jsonl"
    srs.QUEUE = TRACKER / "review-queue.csv"


use_root(TOOLS.parent)


# ---------------------------------------------------------------- curriculum

@dataclass(frozen=True)
class Item:
    id: str
    title: str
    phase: str  # "0".."9", or "C" for a consolidation week
    plan_week: int
    kind: str  # "L" lesson, "M" capstone milestone, "B" weekend build
    file: str

    @property
    def paced(self) -> bool:
        """Lessons and milestones count towards pace; weekend builds don't."""
        return self.kind in ("L", "M")


@dataclass(frozen=True)
class Phase:
    key: str
    title: str
    badge: str
    first_week: int
    last_week: int
    file: str


def _expand(match: re.Match) -> list[tuple[str, str]]:
    ident, to = match["id"], match["to"]
    if to and (m := re.search(r"-L(\d+)$", ident)):
        base = ident[: m.start()]
        return [(f"{base}-L{n}", "L") for n in range(int(m.group(1)), int(to) + 1)]
    return [(ident, ident.rsplit("-", 1)[1][0])]


def _clean_title(title: str) -> str:
    return re.sub(r"\s*\((?:~?\d+[^)]*|plan week \d+)\)\s*$", "", title).strip()


def load_curriculum() -> tuple[list[Item], dict[str, Phase]]:
    items: list[Item] = []
    phases: dict[str, Phase] = {}
    files = sorted(CURRICULUM.glob("phase-*.md"), key=lambda p: int(re.search(r"phase-(\d+)", p.name).group(1)))
    for f in files:
        text = f.read_text(encoding="utf-8")
        key = re.search(r"phase-(\d+)", f.name).group(1)
        title = re.search(r"^# Phase \d+ — (.+)$", text, re.M)
        weeks = re.search(r"Plan weeks (\d+)[–-](\d+)", text)
        badge = re.search(r"Badge: ([^*]+?)\*\*", text)
        if not (title and weeks):
            raise SystemExit(f"error: {f.name} needs a '# Phase N — Title' line and 'Plan weeks A–B'")
        phase = Phase(key, title.group(1).strip(), badge.group(1).strip() if badge else "",
                      int(weeks.group(1)), int(weeks.group(2)), f.name)
        phases[key] = phase
        for match in HEADING.finditer(text):
            for ident, kind in _expand(match):
                week = int(re.search(r"-W(\d+)-", ident).group(1))
                items.append(Item(ident, _clean_title(match["title"]), key, phase.first_week + week - 1, kind, f.name))
    consolidation = CURRICULUM / "consolidation-weeks.md"
    if consolidation.exists():
        text = consolidation.read_text(encoding="utf-8")
        for week in CONSOLIDATION_WEEKS:
            phases[f"C{week}"] = Phase(f"C{week}", f"Consolidation week {week}", "", week, week, consolidation.name)
            for match in HEADING.finditer(text):
                for ident, kind in _expand(match):
                    items.append(Item(ident.replace("<week>", str(week)), _clean_title(match["title"]),
                                      "C", week, kind, consolidation.name))
    order = {"L": 0, "M": 1, "B": 2}
    items.sort(key=lambda i: (i.plan_week, order[i.kind], int(re.search(r"(\d+)$", i.id).group(1)) if i.id[-1].isdigit() else 0))
    seen: set[str] = set()
    for i in items:
        if i.id in seen:
            raise SystemExit(f"error: lesson id {i.id} appears twice in the curriculum")
        seen.add(i.id)
    return items, phases


def phase_key(item: Item) -> str:
    return f"C{item.plan_week}" if item.phase == "C" else item.phase


# ---------------------------------------------------------------- events

def read_events() -> list[dict]:
    if not EVENTS.exists():
        return []
    events = []
    for n, line in enumerate(EVENTS.read_text(encoding="utf-8").splitlines(), 1):
        if line.strip():
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                print(f"warning: tracker/events.jsonl line {n} is not valid JSON and was skipped", file=sys.stderr)
    return events


def append_event(event: dict) -> None:
    TRACKER.mkdir(parents=True, exist_ok=True)
    with EVENTS.open("a", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(event, ensure_ascii=False) + "\n")


def d(value: str) -> date:
    return date.fromisoformat(value)


# ---------------------------------------------------------------- derived state

@dataclass
class State:
    today: date
    items: list[Item]
    phases: dict[str, Phase]
    events: list[dict]
    by_id: dict[str, Item] = field(init=False)

    def __post_init__(self) -> None:
        self.by_id = {i.id: i for i in self.items}

    def of(self, kind: str) -> list[dict]:
        return [e for e in self.events if e["type"] == kind]

    # settings -----------------------------------------------------------
    @property
    def setups(self) -> list[dict]:
        return self.of("setup")

    @property
    def settings(self) -> dict:
        merged = {"pace": "standard", "goal_days": 4, "minutes": 60, "review_cap": srs.DAILY_CAP}
        for s in self.setups:
            merged.update({k: v for k, v in s.items() if k not in ("type", "date")})
        return merged

    @property
    def start(self) -> date | None:
        starts = [d(s["start"]) for s in self.setups if s.get("start")]
        return starts[0] if starts else None

    def elapsed_plan_weeks(self) -> float:
        """Plan weeks the pace settings expect to be finished by today (piecewise over re-plans)."""
        if not self.start or self.today < self.start:
            return 0.0
        segments = [(self.start, PACE_FACTOR[self.setups[0].get("pace", "standard")])]
        for s in self.setups[1:]:
            if "pace" in s:
                segments.append((max(d(s["date"]), self.start), PACE_FACTOR[s["pace"]]))
        total = 0.0
        for (begin, factor), nxt in zip(segments, segments[1:] + [(self.today, 0)]):
            total += max((min(nxt[0], self.today) - begin).days, 0) / 7 * factor
        return total

    # progress -----------------------------------------------------------
    def lesson_events(self) -> list[dict]:
        return self.of("lesson")

    def done_ids(self) -> set[str]:
        return {e["id"] for e in self.lesson_events() if e.get("done") or e.get("score", -1) >= PASS_MARK}

    def paced_items(self) -> list[Item]:
        return [i for i in self.items if i.paced]

    def actual_done(self) -> int:
        done = self.done_ids()
        return sum(1 for i in self.paced_items() if i.id in done)

    def completed_plan_weeks(self) -> float:
        """Plan weeks finished in order: whole weeks done, plus the done fraction of the first unfinished week."""
        done = self.done_ids()
        by_week: dict[int, list[Item]] = {}
        for i in self.paced_items():
            by_week.setdefault(i.plan_week, []).append(i)
        position = 0.0
        for week in range(1, TOTAL_PLAN_WEEKS + 1):
            items = by_week.get(week, [])
            finished = sum(i.id in done for i in items)
            if finished < len(items):
                return position + finished / len(items)
            position += 1
        return position

    def gap_weeks(self) -> float:
        """Positive = ahead of the pace plan, negative = behind (in plan weeks)."""
        return self.completed_plan_weeks() - self.elapsed_plan_weeks()

    def next_item(self) -> Item | None:
        done = self.done_ids()
        return next((i for i in self.paced_items() if i.id not in done), None)

    def first_quizzes(self) -> list[dict]:
        seen, out = set(), []
        for e in self.lesson_events():
            if "score" in e and e["id"] not in seen:
                seen.add(e["id"])
                out.append(e)
        return out

    def best_score(self, item_id: str) -> int | None:
        scores = [e["score"] for e in self.lesson_events() if e["id"] == item_id and "score" in e]
        return max(scores) if scores else None

    def activity_dates(self) -> set[date]:
        kinds = ("session", "lesson", "review", "weekly", "project", "exam")
        return {d(e["date"]) for e in self.events if e["type"] in kinds}

    def last_activity(self) -> date | None:
        dates = self.activity_dates()
        return max(dates) if dates else None

    # weak spots ---------------------------------------------------------
    def weak_spots(self) -> list[dict]:
        spots: dict[str, dict] = {}
        for e in self.events:
            if e["type"] == "weak_add":
                spots[e["id"]] = {"id": e["id"], "opened": e["date"], "lesson": e["lesson"], "text": e["text"],
                                  "passes": set(), "last": "", "fixed": ""}
            elif e["type"] == "weak_check" and e["id"] in spots:
                s = spots[e["id"]]
                s["last"] = e["date"]
                if s["fixed"]:
                    continue
                if e["result"] == "pass":
                    s["passes"].add(e["date"])
                    if len(s["passes"]) >= WEAK_FIXED_AFTER:
                        s["fixed"] = e["date"]
                else:
                    s["passes"] = set()  # a miss restarts the count
        return list(spots.values())

    # phases -------------------------------------------------------------
    def phase_results(self, prefix: str, key: str) -> list[dict]:
        kind = "project" if prefix == "PR" else "exam"
        return [e for e in self.of(kind) if re.fullmatch(rf"{prefix}{key}[A-Z]?", e["id"])]

    def phase_passed(self, key: str) -> str:
        passes = [e["date"] for e in self.phase_results("EX", key) if e["verdict"] == "pass"]
        return passes[0] if passes else ""


def week_start(day: date) -> date:
    return day - timedelta(days=day.weekday())


def weekly_rows(st: State, weeks: int = 8) -> list[dict]:
    rows = []
    first = week_start(st.today) - timedelta(weeks=weeks - 1)
    if st.start and st.start <= st.today:
        first = max(first, week_start(st.start))  # no empty rows before the course began
    while first <= st.today:
        begin, first = first, first + timedelta(weeks=1)
        end = begin + timedelta(days=6)
        inside = [e for e in st.events if begin <= d(e["date"]) <= end]
        firsts = [e["score"] for e in st.first_quizzes() if begin <= d(e["date"]) <= end]
        reviews = [e["score"] for e in inside if e["type"] == "review"]
        weekly = [e for e in inside if e["type"] == "weekly"]
        energies = [e["energy"] for e in inside if e.get("energy")]
        rows.append({
            "week": begin,
            "days": len({e["date"] for e in inside if e["type"] in ("session", "lesson", "review", "weekly")}),
            "minutes": sum(e.get("minutes", 0) for e in inside if e["type"] == "session"),
            "lessons": len({e["id"] for e in inside if e["type"] == "lesson"}),
            "quiz": round(sum(firsts) / len(firsts)) if firsts else None,
            "reviews": len(reviews),
            "retention": round(100 * sum(s >= PASS_MARK for s in reviews) / len(reviews)) if reviews else None,
            "check": weekly[-1] if weekly else None,
            "energy": round(sum(energies) / len(energies), 1) if energies else None,
        })
    return rows


# ---------------------------------------------------------------- alerts

def alerts(st: State) -> list[tuple[str, str]]:
    """Rules the Mentor must act on before teaching anything new. Levels: ALERT > WARN > INFO."""
    out: list[tuple[str, str]] = []
    if not st.setups:
        return [("ALERT", "Not set up yet: run /start (it records `tracker.py setup`).")]
    s = st.settings
    last = st.last_activity()
    idle = (st.today - last).days if last else (st.today - st.start).days if st.start else 0
    if idle >= 15:
        out.append(("ALERT", f"No study for {idle} days: short re-check of the last phase, then /replan."))
    elif idle >= 7:
        out.append(("ALERT", f"No study for {idle} days: run a re-entry session (/recall on the last 2 weeks), then ~70% pace for a week."))
    elif idle >= 3:
        out.append(("WARN", f"No study for {idle} days: reviews first (max {s['review_cap']}), then a light lesson. Never miss twice."))

    gap = st.gap_weeks()
    if gap <= -2:
        out.append(("ALERT", f"Behind plan by {-gap:.1f} weeks: /replan now (lighter pace or trim optional items)."))
    elif gap <= -1:
        out.append(("WARN", f"Behind plan by {-gap:.1f} weeks: discuss /replan this week."))

    firsts = [e["score"] for e in st.first_quizzes()]
    recent, earlier = firsts[-5:], firsts[-10:-5]
    if gap >= 2 and recent and sum(recent) / len(recent) >= 85:
        out.append(("INFO", f"Ahead of plan by {gap:.1f} weeks with strong scores: offer stretch tasks or test-outs."))
    if len(recent) >= 3 and sum(recent) / len(recent) < 65:
        out.append(("WARN", f"Recent first-quiz average is {sum(recent) / len(recent):.0f}: slow down, use the 'Alt' resources, check sleep and energy."))
    elif len(earlier) == 5 and sum(recent) / len(recent) <= sum(earlier) / 5 - 10:
        out.append(("WARN", f"Quiz scores are falling ({sum(earlier) / 5:.0f} -> {sum(recent) / len(recent):.0f}): find out why before adding new lessons."))

    for e in st.first_quizzes():
        best = st.best_score(e["id"])
        if best is not None and best < PASS_MARK and (st.today - d(e["date"])).days >= 2:
            out.append(("WARN", f"{e['id']} is still below {PASS_MARK} ({best}) since {e['date']}: relearn with the Alt resource and re-quiz."))

    due = srs.due_topics(srs.load(), st.today)
    if len(due) > 2 * s["review_cap"]:
        out.append(("WARN", f"{len(due)} reviews due: reviews only today (max {s['review_cap']} per sitting) until the backlog is small."))

    reviews = [e["score"] for e in st.of("review")][-20:]
    if len(reviews) >= 8:
        kept = 100 * sum(x >= PASS_MARK for x in reviews) / len(reviews)
        if kept < 70:
            out.append(("WARN", f"Review retention is {kept:.0f}% (last {len(reviews)}): fewer new lessons, more relearning."))

    checks = st.of("weekly")
    if checks and "aioff" in checks[-1]:
        level = (checks[-1].get("test", checks[-1]["aioff"]) + checks[-1]["aioff"]) / 2
        if level < 70 and (st.today - d(checks[-1]["date"])).days <= 7:
            out.append(("WARN", f"Last weekly check averaged {level:.0f}% (< 70): this week consolidates instead of new lessons."))
    energies = [c["energy"] for c in checks if c.get("energy")][-2:]
    if len(energies) == 2 and max(energies) <= 2:
        out.append(("WARN", "Energy has been 2/5 or lower for two weeks: burnout risk. Lighten the load and use reserve days."))

    wrong = sum(e.get("confident_wrong", 0) for e in st.first_quizzes()[-5:])
    if wrong >= 3:
        out.append(("INFO", f"{wrong} confident-but-wrong answers in the last 5 quizzes: slow down and verify before answering."))

    open_spots = [w for w in st.weak_spots() if not w["fixed"]]
    if len(open_spots) >= 6:
        out.append(("WARN", f"{len(open_spots)} open weak spots: spend a session clearing them."))

    this_week = {x for x in st.activity_dates() if x >= week_start(st.today)}
    if st.today.weekday() >= 3 and len(this_week) < s["goal_days"]:
        out.append(("INFO", f"{len(this_week)} of {s['goal_days']} study days so far this week."))

    nxt = st.next_item()
    for key, ph in st.phases.items():
        if key.startswith("C"):
            continue
        phase_items = [i for i in st.paced_items() if i.phase == key]
        if phase_items and all(i.id in st.done_ids() for i in phase_items) and not st.phase_passed(key):
            if not any(e["verdict"] == "pass" for e in st.phase_results("PR", key)):
                out.append(("INFO", f"All Phase {key} lessons done: the project is next (/submit when ready)."))
            else:
                out.append(("INFO", f"Phase {key} project passed: the exam is next (/exam)."))
    if nxt:
        attempts = [e for e in st.lesson_events() if e["id"] == nxt.id]
        if attempts and (st.today - d(attempts[0]["date"])).days >= 7:
            out.append(("WARN", f"Stuck on {nxt.id} for {(st.today - d(attempts[0]['date'])).days} days: try /stuck, the Alt resource, or /explain."))
    return out


# ---------------------------------------------------------------- views

def pace_line(st: State) -> str:
    gap = st.gap_weeks()
    state = "on track" if abs(gap) < 1 else ("ahead" if gap > 0 else "behind")
    return (f"{st.settings['pace']} since {st.start} · plan weeks expected {st.elapsed_plan_weeks():.1f}, "
            f"completed {st.completed_plan_weeks():.1f} · {state} ({gap:+.1f} weeks) · "
            f"lessons done {st.actual_done()} of {len(st.paced_items())}")


def position(st: State) -> str:
    nxt = st.next_item()
    if not nxt:
        return "Course complete"
    ph = st.phases[phase_key(nxt)]
    label = ph.title if nxt.phase == "C" else f"Phase {ph.key} — {ph.title}"
    return f"plan week {nxt.plan_week} of {TOTAL_PLAN_WEEKS} · {label}"


def ago(day: date | None, today: date) -> str:
    if not day:
        return "never"
    n = (today - day).days
    return "today" if n == 0 else f"{day} ({n} day{'s' if n != 1 else ''} ago)"


def cmd_status(st: State, args: argparse.Namespace) -> None:
    print(f"Today: {st.today:%a} {st.today}")
    if not st.setups:
        print("Not set up yet. Run /start: it interviews the learner and records `tracker.py setup`.")
        return
    nxt = st.next_item()
    print(f"Position: {position(st)}")
    if nxt:
        print(f"Next lesson: {nxt.id} · {nxt.title}  [curriculum/{nxt.file}]")
    print(f"Pace: {pace_line(st)}")
    this_week = [r for r in weekly_rows(st, 1)][0]
    print(f"This week: {this_week['days']} of {st.settings['goal_days']} study days, {this_week['minutes']} min · "
          f"last activity: {ago(st.last_activity(), st.today)}")
    topics = srs.load()
    due = srs.due_topics(topics, st.today)
    spots = [w for w in st.weak_spots() if not w["fixed"]]
    print(f"Reviews due: {len(due)} (cap {st.settings['review_cap']}) · open weak spots: {len(spots)}")
    found = alerts(st)
    print("Alerts:" if found else "Alerts: none. Keep going.")
    for level, text in found:
        print(f"  {level:5} {text}")
    if due:
        print("\nDue reviews, most urgent first:")
        srs.table([[t.id, srs.clip(t.title), t.due, t.last_score] for t in due[: st.settings["review_cap"]]],
                  ["ID", "Title", "Due", "Last"])
    if spots:
        print("\nOpen weak spots:")
        for w in spots[:8]:
            print(f"  {w['id']:6} {w['lesson']:10} {srs.clip(w['text'], 60)}  ({len(w['passes'])}/{WEAK_FIXED_AFTER})")


def bar(n: int, top: int = 7) -> str:
    return "▇" * min(n, top)


def dashboard(st: State) -> str:
    lines = ["# Progress dashboard", "",
             f"_Auto-generated by `python tools/tracker.py` on {st.today}. Don't edit by hand: it is rebuilt "
             "after every recorded event from `tracker/events.jsonl`._", ""]
    if not st.setups:
        return "\n".join(lines + ["Not started yet. Open this folder in your AI agent and type `/start`.", ""])
    s = st.settings
    nxt = st.next_item()
    due = srs.due_topics(srs.load(), st.today)
    spots = st.weak_spots()
    this_week = weekly_rows(st, 1)[0]
    reviews = [e["score"] for e in st.of("review")][-20:]
    retention = f"{100 * sum(x >= PASS_MARK for x in reviews) / len(reviews):.0f}%" if reviews else "—"
    lines += ["## Now", "", "| | |", "|---|---|",
              f"| Position | {position(st)} |",
              f"| Next | **{nxt.id}** · {nxt.title} ([{nxt.file}](../curriculum/{nxt.file})) |" if nxt else "| Next | 🎓 course complete |",
              f"| Pace | {pace_line(st)} |",
              f"| This week | {this_week['days']} of {s['goal_days']} study days · {this_week['minutes']} min |",
              f"| Reviews | {len(due)} due now · retention {retention} (last {len(reviews)} reviews) |",
              f"| Weak spots | {sum(not w['fixed'] for w in spots)} open · {sum(bool(w['fixed']) for w in spots)} fixed |",
              f"| Last activity | {ago(st.last_activity(), st.today)} |", ""]
    icon = {"ALERT": "🔴", "WARN": "🟠", "INFO": "🔵"}
    found = alerts(st)
    lines += ["## Alerts", ""] + ([f"- {icon[lvl]} {text}" for lvl, text in found] or ["- ✅ None. Keep going."]) + [""]

    firsts = [e["score"] for e in st.first_quizzes()]
    recent, earlier = firsts[-5:], firsts[-10:-5]
    avg = lambda xs: f"{sum(xs) / len(xs):.0f}" if xs else "—"  # noqa: E731
    check = st.of("weekly")[-1] if st.of("weekly") else None
    check_txt = f"{check.get('test', '—')} / {check.get('aioff', '—')} ({check['date']})" if check else "—"
    lines += ["## Scores", "", "| Measure | Value |", "|---|---|",
              f"| First-quiz average, last 5 lessons (previous 5) | {avg(recent)} ({avg(earlier)}) |",
              f"| Review retention, last {len(reviews)} reviews | {retention} |",
              f"| Last weekly check: closed-book test / AI-off coding | {check_txt} |",
              f"| Confident-but-wrong answers, last 5 quizzes | {sum(e.get('confident_wrong', 0) for e in st.first_quizzes()[-5:])} |",
              f"| Topics on 21+ day review gaps | {sum(1 for t in srs.load() if t.interval >= 21)} |", ""]

    lines += ["## Last 8 weeks", "",
              "| Week of | Study days | Minutes | Lessons | Avg first quiz | Reviews | Retention | Test / AI-off | Energy |",
              "|---|---|---|---|---|---|---|---|---|"]
    for r in weekly_rows(st):
        c = r["check"]
        quiz = r["quiz"] if r["quiz"] is not None else "—"
        kept = f"{r['retention']}%" if r["retention"] is not None else "—"
        test = f"{c.get('test', '—')} / {c.get('aioff', '—')}" if c else "—"
        lines.append(f"| {r['week']} | {r['days']} {bar(r['days'])} | {r['minutes']} | {r['lessons']} | "
                     f"{quiz} | {r['reviews']} | {kept} | {test} | {r['energy'] or '—'} |")
    lines.append("")

    done = st.done_ids()
    lines += ["## Phases", "", "| Phase | Title | Plan weeks | Lessons | Project | Exam | Status |", "|---|---|---|---|---|---|---|"]
    current = phase_key(nxt) if nxt else None
    for key, ph in sorted(st.phases.items(), key=lambda kv: kv[1].first_week):
        items = [i for i in st.paced_items() if phase_key(i) == key]
        n_done = sum(i.id in done for i in items)
        if key.startswith("C"):
            proj = exam = "—"
            status = "✅" if items and n_done == len(items) else ("▶ current" if key == current else "🔒")
        else:
            projs, exams = st.phase_results("PR", key), st.phase_results("EX", key)
            proj = " ".join(f"{e['id']} {e['score']} {'✅' if e['verdict'] == 'pass' else '↺'}" for e in projs[-2:]) or "—"
            exam = " ".join(f"{e['score']}% {'✅' if e['verdict'] == 'pass' else '↺'}" for e in exams[-2:]) or "—"
            passed = st.phase_passed(key)
            status = f"✅ {passed}" if passed else ("▶ current" if key == current else ("in progress" if n_done else "🔒"))
        weeks = f"{ph.first_week}" if ph.first_week == ph.last_week else f"{ph.first_week}–{ph.last_week}"
        lines.append(f"| {key} | {ph.title} | {weeks} | {n_done}/{len(items)} | {proj} | {exam} | {status} |")
    lines.append("")

    badges = sorted(((st.phase_passed(k), ph) for k, ph in st.phases.items() if ph.badge and st.phase_passed(k)),
                    key=lambda pair: pair[0])
    lines += ["## Badges", ""] + ([f"- {day} · **{ph.badge}** (Phase {ph.key})" for day, ph in badges] or ["- None yet."]) + [""]

    lines += ["## Recent lessons", "", "| Date | Lesson | Title | First quiz | Best |", "|---|---|---|---|---|"]
    seen: dict[str, dict] = {}
    for e in st.lesson_events():
        seen.setdefault(e["id"], e)
    for e in list(seen.values())[-12:][::-1]:
        item = st.by_id.get(e["id"])
        best = st.best_score(e["id"])
        lines.append(f"| {e['date']} | {e['id']} | {item.title if item else '—'} | "
                     f"{e.get('score', 'done')} | {best if best is not None else 'done'} |")
    lines.append("")
    return "\n".join(lines)


def weak_view(st: State) -> str:
    spots = st.weak_spots()
    lines = ["# Weak spots", "",
             "_Auto-generated. Record with `python tools/tracker.py weak add|pass|fail`. A spot is fixed after "
             f"{WEAK_FIXED_AFTER} correct, unaided answers on different days; a miss restarts the count._", "",
             "## Open", "", "| ID | Opened | Lesson | What went wrong | Correct days | Last checked |", "|---|---|---|---|---|---|"]
    lines += [f"| {w['id']} | {w['opened']} | {w['lesson']} | {w['text']} | {len(w['passes'])}/{WEAK_FIXED_AFTER} | {w['last'] or '—'} |"
              for w in spots if not w["fixed"]] or ["| — | | | none | | |"]
    lines += ["", "## Fixed", "", "| ID | Opened | Fixed | Lesson | What went wrong |", "|---|---|---|---|---|"]
    lines += [f"| {w['id']} | {w['opened']} | {w['fixed']} | {w['lesson']} | {w['text']} |" for w in spots if w["fixed"]] \
        or ["| — | | | | none yet |"]
    return "\n".join(lines) + "\n"


def rebuild(st: State) -> None:
    TRACKER.mkdir(parents=True, exist_ok=True)
    (TRACKER / "progress.md").write_text(dashboard(st), encoding="utf-8", newline="\n")
    (TRACKER / "weak-spots.md").write_text(weak_view(st), encoding="utf-8", newline="\n")


# ---------------------------------------------------------------- commands

def item_or_exit(st: State, ident: str, force: bool = False) -> str:
    ident = ident.strip().upper()
    if ident in st.by_id or force:
        return ident
    close = difflib.get_close_matches(ident, list(st.by_id), n=3)
    hint = f" Did you mean: {', '.join(close)}?" if close else ""
    sys.exit(f"error: {ident} is not a lesson in the curriculum.{hint} (Use --force for a custom lesson.)")


def score_arg(value: str) -> int:
    score = round(float(value))
    if not 0 <= score <= 100:
        raise argparse.ArgumentTypeError("scores are 0-100")
    return score


def record(st: State, event: dict) -> State:
    append_event({"date": st.today.isoformat(), **event})
    fresh = State(st.today, st.items, st.phases, read_events())
    rebuild(fresh)
    return fresh


def cmd_setup(st: State, args: argparse.Namespace) -> None:
    event = {"type": "setup"}
    if not st.setups or args.start:
        event["start"] = (args.start or st.today).isoformat()
    for key in ("pace", "goal_days", "minutes", "review_cap"):
        if getattr(args, key) is not None:
            event[key] = getattr(args, key)
    st = record(st, event)
    print(f"Settings: {st.settings['pace']} pace from {st.start}, goal {st.settings['goal_days']} study days/week, "
          f"{st.settings['minutes']} min/session, review cap {st.settings['review_cap']}.")
    nxt = st.next_item()
    if nxt:
        print(f"Next lesson: {nxt.id} · {nxt.title}")


def cmd_session(st: State, args: argparse.Namespace) -> None:
    event = {"type": "session", "minutes": args.minutes}
    if args.energy:
        event["energy"] = args.energy
    if args.note:
        event["note"] = args.note
    st = record(st, event)
    row = weekly_rows(st, 1)[0]
    print(f"Session logged: {args.minutes} min. This week: {row['days']} of {st.settings['goal_days']} study days, {row['minutes']} min.")


def cmd_lesson(st: State, args: argparse.Namespace) -> None:
    ident = item_or_exit(st, args.id, args.force)
    item = st.by_id.get(ident)
    event: dict = {"type": "lesson", "id": ident}
    if args.done:
        event["done"] = True
    else:
        event["score"] = args.score
        if args.confident_wrong:
            event["confident_wrong"] = args.confident_wrong
        topic = srs.record(ident, item.title if item else ident, args.score, st.today)
    st = record(st, event)
    if args.done:
        print(f"{ident} marked done.")
    else:
        verdict = "passed" if args.score >= PASS_MARK else f"below {PASS_MARK}: relearn with the Alt resource and re-quiz next session"
        print(f"{ident}: quiz {args.score} ({verdict}). Next review: {topic.due}.")
    nxt = st.next_item()
    print(f"Next lesson: {nxt.id} · {nxt.title}" if nxt else "That was the last lesson. Congratulations!")
    print(f"Pace: {pace_line(st)}")


def cmd_review(st: State, args: argparse.Namespace) -> None:
    topic = srs.lookup(srs.load(), args.id)
    if topic is None:
        sys.exit(f"error: {args.id} has no review schedule yet. Record its first quiz with: tracker.py lesson {args.id} --score N")
    topic = srs.record(topic.id, topic.title, args.score, st.today)
    record(st, {"type": "review", "id": topic.id, "score": args.score})
    print(f"{topic.id}: review {args.score}. Next review: {topic.due} (gap {topic.interval} day(s), ease {topic.ease:.2f}).")


def cmd_project(st: State, args: argparse.Namespace) -> None:
    ident = args.id.strip().upper()
    if not re.fullmatch(r"PR\d+[A-Z]?", ident):
        sys.exit("error: project ids look like PR3 (or PR5A / PR5B)")
    record(st, {"type": "project", "id": ident, "score": args.score, "verdict": args.verdict})
    print(f"{ident}: {args.score}/100, {args.verdict.upper()}.")


def cmd_exam(st: State, args: argparse.Namespace) -> None:
    ident = args.id.strip().upper()
    if not re.fullmatch(r"EX\d+", ident):
        sys.exit("error: exam ids look like EX3")
    event = {"type": "exam", "id": ident, "score": args.score, "verdict": args.verdict}
    if args.parts:
        event["parts"] = dict(p.split("=", 1) for p in args.parts.split(","))
    st = record(st, event)
    key = ident[2:]
    ph = st.phases.get(key)
    if args.verdict == "pass" and ph:
        print(f"{ident}: {args.score}% PASS. Phase {key} complete. Badge earned: {ph.badge}.")
    else:
        print(f"{ident}: {args.score}%. Not yet: retake no sooner than {st.today + timedelta(days=3)}.")


def cmd_weekly(st: State, args: argparse.Namespace) -> None:
    event = {"type": "weekly", "test": args.test, "aioff": args.aioff}
    for key in ("hours", "energy", "note"):
        if getattr(args, key) is not None:
            event[key] = getattr(args, key)
    st = record(st, event)
    reports = TRACKER / "reports"
    reports.mkdir(exist_ok=True)
    year, week, _ = st.today.isocalendar()
    path = reports / f"{year}-W{week:02d}.md"
    summary = [f"# Weekly report {year}-W{week:02d} ({week_start(st.today)} to {week_start(st.today) + timedelta(days=6)})", "",
               f"- Closed-book test: {args.test} · AI-off coding check: {args.aioff}"
               + (f" · hours: {args.hours}" if args.hours is not None else "")
               + (f" · energy: {args.energy}/5" if args.energy else ""),
               *([f"- Note: {args.note}"] if args.note else []), "", "---", ""]
    path.write_text("\n".join(summary) + dashboard(st).split("\n", 3)[3], encoding="utf-8", newline="\n")
    gate = (args.test + args.aioff) / 2
    print(f"Weekly check saved ({path.relative_to(ROOT)}). Average {gate:.0f}%: "
          + ("next week continues with new lessons." if gate >= 70 else "next week consolidates (below 70%)."))


def cmd_weak(st: State, args: argparse.Namespace) -> None:
    spots = st.weak_spots()
    if args.action == "add":
        if len(args.rest) < 2:
            sys.exit('usage: tracker.py weak add LESSON-ID "what went wrong"')
        lesson = item_or_exit(st, args.rest[0], force=True)
        ident = f"WS-{len(spots) + 1}"
        record(st, {"type": "weak_add", "id": ident, "lesson": lesson, "text": " ".join(args.rest[1:])})
        print(f"{ident} opened for {lesson}.")
    elif args.action in ("pass", "fail"):
        if not args.rest:
            sys.exit(f"usage: tracker.py weak {args.action} WS-ID")
        ident = args.rest[0].upper()
        spot = next((w for w in spots if w["id"] == ident), None)
        if not spot:
            sys.exit(f"error: no weak spot {ident}. Open ones: {', '.join(w['id'] for w in spots if not w['fixed']) or 'none'}")
        st = record(st, {"type": "weak_check", "id": ident, "result": args.action})
        spot = next(w for w in st.weak_spots() if w["id"] == ident)
        print(f"{ident}: fixed on {spot['fixed']}." if spot["fixed"]
              else f"{ident}: {len(spot['passes'])}/{WEAK_FIXED_AFTER} correct days.")
    else:
        for w in spots:
            state = f"fixed {w['fixed']}" if w["fixed"] else f"open {len(w['passes'])}/{WEAK_FIXED_AFTER}"
            print(f"{w['id']:6} {w['lesson']:10} {state:18} {w['text']}")
        if not spots:
            print("No weak spots recorded.")


def cmd_next(st: State, args: argparse.Namespace) -> None:
    nxt = st.next_item()
    print(f"{nxt.id} · {nxt.title} · plan week {nxt.plan_week} · curriculum/{nxt.file}" if nxt else "Course complete.")


def cmd_lessons(st: State, args: argparse.Namespace) -> None:
    done = st.done_ids()
    for i in st.items:
        if args.phase is None or i.phase == str(args.phase).upper():
            best = st.best_score(i.id)
            mark = "x" if i.id in done else (" " if best is None else "!")
            print(f"[{mark}] {i.id:10} wk{i.plan_week:<3} {i.kind} {i.title}" + (f"  (best {best})" if best is not None else ""))


def cmd_report(st: State, args: argparse.Namespace) -> None:
    rebuild(st)
    print("Rebuilt tracker/progress.md and tracker/weak-spots.md")


def main(argv: list[str] | None = None) -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Progress tracker for the AI learning path.")
    parser.add_argument("--date", type=date.fromisoformat, default=date.today(), help="record as if today were YYYY-MM-DD")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("status", help="start-of-session briefing").set_defaults(run=cmd_status)

    p = sub.add_parser("setup", help="record or change pace and schedule")
    p.add_argument("--pace", choices=list(PACE_FACTOR))
    p.add_argument("--start", type=date.fromisoformat, help="course start date (first setup only, default today)")
    p.add_argument("--goal-days", type=int, dest="goal_days", help="study days per week")
    p.add_argument("--minutes", type=int, help="minutes per weekday session")
    p.add_argument("--review-cap", type=int, dest="review_cap", help="max reviews per sitting")
    p.set_defaults(run=cmd_setup)

    p = sub.add_parser("session", help="log a study session")
    p.add_argument("--minutes", type=int, required=True)
    p.add_argument("--energy", type=int, choices=range(1, 6))
    p.add_argument("--note")
    p.set_defaults(run=cmd_session)

    p = sub.add_parser("lesson", help="record a lesson's quiz (or --done)")
    p.add_argument("id")
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument("--score", type=score_arg)
    group.add_argument("--done", action="store_true")
    p.add_argument("--confident-wrong", type=int, default=0, dest="confident_wrong")
    p.add_argument("--force", action="store_true", help="allow an id that isn't in the curriculum")
    p.set_defaults(run=cmd_lesson)

    p = sub.add_parser("review", help="record a spaced-review score")
    p.add_argument("id")
    p.add_argument("score", type=score_arg)
    p.set_defaults(run=cmd_review)

    p = sub.add_parser("project", help="record a project result")
    p.add_argument("id")
    p.add_argument("--score", type=score_arg, required=True)
    p.add_argument("--verdict", choices=["pass", "revise"], required=True)
    p.set_defaults(run=cmd_project)

    p = sub.add_parser("exam", help="record a phase exam")
    p.add_argument("id")
    p.add_argument("--score", type=score_arg, required=True, help="overall percentage")
    p.add_argument("--verdict", choices=["pass", "retake"], required=True)
    p.add_argument("--parts", help="e.g. A=8,B=7,C=4,D=3")
    p.set_defaults(run=cmd_exam)

    p = sub.add_parser("weekly", help="record the Sunday check and save a weekly report")
    p.add_argument("--test", type=score_arg, required=True, help="closed-book cumulative test %%")
    p.add_argument("--aioff", type=score_arg, required=True, help="AI-off coding check %%")
    p.add_argument("--hours", type=float)
    p.add_argument("--energy", type=int, choices=range(1, 6))
    p.add_argument("--note")
    p.set_defaults(run=cmd_weekly)

    p = sub.add_parser("weak", help="weak spots: add | pass | fail | list")
    p.add_argument("action", choices=["add", "pass", "fail", "list"])
    p.add_argument("rest", nargs="*")
    p.set_defaults(run=cmd_weak)

    sub.add_parser("next", help="the next lesson").set_defaults(run=cmd_next)
    p = sub.add_parser("lessons", help="all lessons with done marks")
    p.add_argument("--phase")
    p.set_defaults(run=cmd_lessons)
    sub.add_parser("report", help="rebuild the dashboard views").set_defaults(run=cmd_report)

    args = parser.parse_args(argv)
    items, phases = load_curriculum()
    args.run(State(args.date, items, phases, read_events()), args)


if __name__ == "__main__":
    main()
