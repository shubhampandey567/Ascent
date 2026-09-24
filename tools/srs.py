#!/usr/bin/env python3
"""Spaced-repetition scheduler for the AI learning path.

Normally used through tools/tracker.py, which records every quiz and review and calls
record() here. Run it directly for look-ups (today, list, upcoming, stats) or when
studying without an AI agent. Standard library only.

Data: tracker/review-queue.csv (one row per topic). Change it only through these tools.

Scheduling is a lightly modified SM-2 (SuperMemo-2, Wozniak 1990):
  * a quiz score 0-100 becomes a grade q in 0..5  (90+ = 5, 75+ = 4, 60+ = 3, 40+ = 2, 20+ = 1)
  * q < 3  -> forgotten: repetitions restart and the topic comes back tomorrow
  * q >= 3 -> next gap is 1 day, then 3 days, then previous gap x ease (capped at 180 days)
  * ease starts at 2.5 and moves after every grade: ease += 0.1 - (5-q)*(0.08 + (5-q)*0.02), floor 1.3
  * a topic reviewed late but still remembered well (q >= 4) gets credit for half the extra delay

A topic learned today and remembered well comes back after about 1, 3, 8, 21, 55 days...

Commands:
  python tools/srs.py today                    what is due now, most urgent first
  python tools/srs.py add ID "Title" --score 80
                                               new topic, graded by its first quiz
  python tools/srs.py grade ID 65              record a review score (0-100)
  python tools/srs.py list [--phase 1] [--due] every topic and its schedule
  python tools/srs.py upcoming [--days 14]     review load for the coming days
  python tools/srs.py stats                    retention and progress numbers
  python tools/srs.py remove ID                delete a topic added by mistake

Put --date YYYY-MM-DD before the command to act as if today were another day.
"""

from __future__ import annotations

import argparse
import csv
import difflib
import os
import re
import sys
import tempfile
from dataclasses import asdict, dataclass, fields
from datetime import date, timedelta
from pathlib import Path

QUEUE = Path(__file__).resolve().parent.parent / "tracker" / "review-queue.csv"
START_EASE = 2.5
MIN_EASE = 1.3
MAX_INTERVAL = 180
DAILY_CAP = 8  # more than this many reviews in one sitting stops being useful


@dataclass
class Topic:
    id: str
    title: str
    phase: str = ""
    added: str = ""
    last_review: str = ""
    due: str = ""
    interval: int = 0
    ease: float = START_EASE
    reps: int = 0
    lapses: int = 0
    reviews: int = 0
    last_score: str = ""
    history: str = ""  # space-separated "YYYY-MM-DD:score" entries


COLUMNS = [f.name for f in fields(Topic)]


def load() -> list[Topic]:
    if not QUEUE.exists():
        return []
    with QUEUE.open(newline="", encoding="utf-8") as fh:
        topics = []
        for row in csv.DictReader(fh):
            row = {k: (v or "") for k, v in row.items() if k in COLUMNS}
            topics.append(Topic(
                id=row["id"], title=row.get("title", ""), phase=row.get("phase", ""),
                added=row.get("added", ""), last_review=row.get("last_review", ""),
                due=row.get("due", ""), interval=int(row.get("interval") or 0),
                ease=float(row.get("ease") or START_EASE), reps=int(row.get("reps") or 0),
                lapses=int(row.get("lapses") or 0), reviews=int(row.get("reviews") or 0),
                last_score=row.get("last_score", ""), history=row.get("history", ""),
            ))
        return topics


def save(topics: list[Topic]) -> None:
    QUEUE.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=QUEUE.parent, suffix=".tmp")
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=COLUMNS)
        writer.writeheader()
        for t in sorted(topics, key=lambda t: (t.due, t.id)):
            writer.writerow(asdict(t))
    os.replace(tmp, QUEUE)  # atomic: a crash never leaves a half-written file


def quality(score: float) -> int:
    for q, floor in ((5, 90), (4, 75), (3, 60), (2, 40), (1, 20)):
        if score >= floor:
            return q
    return 0


def schedule(t: Topic, score: float, today: date) -> None:
    q = quality(score)
    elapsed = (today - date.fromisoformat(t.last_review)).days if t.last_review else 0
    if t.last_review == today.isoformat() and q >= 3:
        # Same-day retest: no time has passed, so a good score proves nothing about spacing.
        t.reviews += 1
        t.last_score = str(round(score))
        t.history = f"{t.history} {today.isoformat()}:{round(score)}".strip()
        return
    if q < 3:
        if t.reps > 0:
            t.lapses += 1
        t.reps = 0
        t.interval = 1
    else:
        t.reps += 1
        if t.reps == 1:
            t.interval = 1
        elif t.reps == 2:
            t.interval = 3
        else:
            # Remembered well despite a late review: credit half the extra delay (like Anki).
            base = (t.interval + elapsed) / 2 if q >= 4 and elapsed > t.interval else t.interval
            t.interval = min(MAX_INTERVAL, max(t.interval + 1, round(base * t.ease)))
    t.ease = round(max(MIN_EASE, t.ease + 0.1 - (5 - q) * (0.08 + (5 - q) * 0.02)), 2)
    t.reviews += 1
    t.last_score = str(round(score))
    t.last_review = today.isoformat()
    t.due = (today + timedelta(days=t.interval)).isoformat()
    t.history = f"{t.history} {today.isoformat()}:{round(score)}".strip()


def lookup(topics: list[Topic], topic_id: str) -> Topic | None:
    wanted = topic_id.strip().upper()
    return next((t for t in topics if t.id.upper() == wanted), None)


def find(topics: list[Topic], topic_id: str) -> Topic:
    if t := lookup(topics, topic_id):
        return t
    close = difflib.get_close_matches(topic_id.strip().upper(), [t.id.upper() for t in topics], n=3)
    hint = f" Did you mean: {', '.join(close)}?" if close else ""
    sys.exit(f"error: no topic with id {topic_id!r}.{hint}")


def infer_phase(topic_id: str) -> str:
    m = re.match(r"P(\d+)-", topic_id.upper())  # P3-W2-L1 -> 3
    return m.group(1) if m else ""


def record(topic_id: str, title: str, score: float, today: date) -> Topic:
    """Add the topic if it is new, then schedule it from this score (used by tools/tracker.py)."""
    topics = load()
    t = lookup(topics, topic_id)
    if t is None:
        t = Topic(id=topic_id.strip().upper(), title=title, phase=infer_phase(topic_id), added=today.isoformat())
        topics.append(t)
    schedule(t, check_score(score), today)
    save(topics)
    return t


def check_score(score: float) -> float:
    if not 0 <= score <= 100:
        sys.exit("error: score must be between 0 and 100")
    return score


def due_topics(topics: list[Topic], today: date) -> list[Topic]:
    due = [t for t in topics if t.due and date.fromisoformat(t.due) <= today]

    def urgency(t: Topic) -> tuple[float, float]:
        overdue = (today - date.fromisoformat(t.due)).days
        return (-overdue / max(t.interval, 1), t.ease)  # most overdue relative to its gap, then hardest

    return sorted(due, key=urgency)


def table(rows: list[list[str]], header: list[str]) -> None:
    widths = [max(len(str(x)) for x in col) for col in zip(header, *rows)]
    for line in [header, ["-" * w for w in widths], *rows]:
        print("  ".join(str(x).ljust(w) for x, w in zip(line, widths)).rstrip())


def clip(text: str, width: int = 44) -> str:
    return text if len(text) <= width else text[: width - 3] + "..."


def cmd_today(topics: list[Topic], today: date, args: argparse.Namespace) -> None:
    print(f"Today is {today:%a} {today.isoformat()}.")
    due = due_topics(topics, today)
    if not due:
        print("No reviews due. Go straight to new learning.")
    else:
        print(f"Reviews due: {len(due)} (most urgent first). Do at most {DAILY_CAP} today; the rest wait.\n")
        rows = [[str(i), t.id, clip(t.title), t.due, t.last_score, f"{t.ease:.2f}"]
                for i, t in enumerate(due, 1)]
        table(rows, ["#", "ID", "Title", "Due", "Last", "Ease"])
    week = [sum(1 for t in topics if t.due == (today + timedelta(days=d)).isoformat()) for d in range(1, 8)]
    print(f"\nComing up, next 7 days: {', '.join(map(str, week))}")


def cmd_add(topics: list[Topic], today: date, args: argparse.Namespace) -> None:
    topic_id = args.id.strip().upper()
    if any(t.id.upper() == topic_id for t in topics):
        sys.exit(f"error: {topic_id} already exists. Use: python tools/srs.py grade {topic_id} <score>")
    phase = args.phase if args.phase is not None else infer_phase(topic_id)
    t = Topic(id=topic_id, title=args.title, phase=phase, added=today.isoformat())
    if args.score is None:
        t.interval, t.due = 1, (today + timedelta(days=1)).isoformat()
    else:
        schedule(t, check_score(args.score), today)
    topics.append(t)
    save(topics)
    print(f"Added {t.id} '{t.title}'. Next review: {t.due} (in {t.interval} day(s)).")


def cmd_grade(topics: list[Topic], today: date, args: argparse.Namespace) -> None:
    t = find(topics, args.id)
    before, same_day = t.interval, t.last_review == today.isoformat()
    schedule(t, check_score(args.score), today)
    save(topics)
    if quality(args.score) < 3:
        verdict = "forgotten -> relearn, back tomorrow"
    elif same_day:
        verdict = "same-day retest, schedule unchanged"
    else:
        verdict = "remembered"
    print(f"{t.id}: score {round(args.score)} ({verdict}). Gap {before} -> {t.interval} day(s). "
          f"Next review: {t.due}. Ease {t.ease:.2f}.")


def cmd_list(topics: list[Topic], today: date, args: argparse.Namespace) -> None:
    shown = [t for t in topics if args.phase is None or t.phase == str(args.phase)]
    if args.due:
        shown = due_topics(shown, today)
    else:
        shown.sort(key=lambda t: (t.due, t.id))
    if not shown:
        print("No topics yet.")
        return
    rows = [[t.id, clip(t.title), t.phase, t.due, str(t.interval), t.last_score, f"{t.ease:.2f}", str(t.reviews)]
            for t in shown]
    table(rows, ["ID", "Title", "Phase", "Due", "Gap", "Last", "Ease", "Reviews"])


def cmd_upcoming(topics: list[Topic], today: date, args: argparse.Namespace) -> None:
    overdue = sum(1 for t in topics if t.due and t.due < today.isoformat())
    print(f"Overdue now: {overdue}")
    for d in range(args.days + 1):
        day = today + timedelta(days=d)
        n = sum(1 for t in topics if t.due == day.isoformat())
        print(f"{day:%a} {day.isoformat()}  {n:>3}  {'#' * n}")


def cmd_stats(topics: list[Topic], today: date, args: argparse.Namespace) -> None:
    if not topics:
        print("No topics yet. They appear after your first quiz.")
        return
    scores = [[int(h.split(":")[1]) for h in t.history.split()] for t in topics]
    reviews = [s for per_topic in scores for s in per_topic[1:]]  # skip each topic's first quiz
    by_phase: dict[str, int] = {}
    for t in topics:
        by_phase[t.phase or "?"] = by_phase.get(t.phase or "?", 0) + 1
    last = [int(t.last_score) for t in topics if t.last_score]
    print(f"Topics tracked:        {len(topics)}  ("
          + ", ".join(f"phase {p}: {n}" for p, n in sorted(by_phase.items())) + ")")
    print(f"Reviews done:          {len(reviews)} (plus {sum(1 for s in scores if s)} first quizzes)")
    if reviews:
        kept = sum(1 for s in reviews if s >= 60)
        print(f"Review retention:      {100 * kept // len(reviews)}% of reviews scored 60+")
    if last:
        print(f"Average latest score:  {sum(last) // len(last)}")
    print(f"Solid topics (gap 21+ days): {sum(1 for t in topics if t.interval >= 21)}")
    print(f"Forgotten after learning (lapses): {sum(t.lapses for t in topics)}")
    print(f"Due now: {len(due_topics(topics, today))}")
    struggling = (t for t in topics if t.last_score and (t.ease < START_EASE or int(t.last_score) < 60))
    weakest = sorted(struggling, key=lambda t: (t.ease, int(t.last_score)))[:3]
    if weakest:
        print("Hardest topics: " + "; ".join(f"{t.id} {clip(t.title, 30)}" for t in weakest))


def cmd_remove(topics: list[Topic], today: date, args: argparse.Namespace) -> None:
    t = find(topics, args.id)
    topics.remove(t)
    save(topics)
    print(f"Removed {t.id} '{t.title}'.")


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Spaced-repetition scheduler for the AI learning path.")
    parser.add_argument("--date", type=date.fromisoformat, default=date.today(), help="act as if today were YYYY-MM-DD")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("today", help="reviews due now").set_defaults(run=cmd_today)

    p = sub.add_parser("add", help="add a topic just learned")
    p.add_argument("id", help="lesson id, e.g. P1-W2-L3")
    p.add_argument("title")
    p.add_argument("--score", type=float, help="first quiz score 0-100")
    p.add_argument("--phase", help="phase number (read from the id when omitted)")
    p.set_defaults(run=cmd_add)

    p = sub.add_parser("grade", help="record a review score")
    p.add_argument("id")
    p.add_argument("score", type=float, help="0-100")
    p.set_defaults(run=cmd_grade)

    p = sub.add_parser("list", help="all topics and their schedule")
    p.add_argument("--phase")
    p.add_argument("--due", action="store_true", help="only topics due now")
    p.set_defaults(run=cmd_list)

    p = sub.add_parser("upcoming", help="review load forecast")
    p.add_argument("--days", type=int, default=14)
    p.set_defaults(run=cmd_upcoming)

    sub.add_parser("stats", help="retention and progress numbers").set_defaults(run=cmd_stats)

    p = sub.add_parser("remove", help="delete a topic")
    p.add_argument("id")
    p.set_defaults(run=cmd_remove)

    args = parser.parse_args()
    args.run(load(), args.date, args)


if __name__ == "__main__":
    main()
