import json
from datetime import date

import pytest

import srs
import tracker


def state(day: str) -> tracker.State:
    items, phases = tracker.load_curriculum()
    return tracker.State(date.fromisoformat(day), items, phases, tracker.read_events())


# ---------------------------------------------------------------- curriculum

def test_every_plan_week_has_paced_lessons(workspace):
    items, phases = tracker.load_curriculum()
    weeks = {i.plan_week for i in items if i.paced}
    assert weeks == set(range(1, tracker.TOTAL_PLAN_WEEKS + 1))


def test_lesson_ids_are_unique_and_inside_their_phase(workspace):
    items, phases = tracker.load_curriculum()
    assert len({i.id for i in items}) == len(items)
    for i in items:
        if i.phase != "C":
            assert phases[i.phase].first_week <= i.plan_week <= phases[i.phase].last_week, i.id


def test_ranges_like_l1_to_l4_are_expanded(workspace):
    ids = {i.id for i in tracker.load_curriculum()[0]}
    assert {"P4-W8-L1", "P4-W8-L2", "P4-W8-L3", "P4-W8-L4", "P1-W5-L3", "P1-W5-L4"} <= ids
    assert {"C13-L1", "C60-L4", "P9-W10-M"} <= ids


def test_every_phase_has_a_badge(workspace):
    phases = tracker.load_curriculum()[1]
    assert all(ph.badge for key, ph in phases.items() if not key.startswith("C"))


# ---------------------------------------------------------------- recording

def test_not_set_up_raises_alert(workspace):
    assert tracker.alerts(state("2026-10-01"))[0][0] == "ALERT"


def test_lesson_quiz_marks_done_and_schedules_review(workspace, cli):
    cli("--date", "2026-10-01", "setup", "--pace", "standard")
    cli("--date", "2026-10-01", "lesson", "P0-W1-L1", "--score", "80")
    st = state("2026-10-01")
    assert "P0-W1-L1" in st.done_ids()
    assert st.next_item().id == "P0-W1-L2"
    [topic] = srs.load()
    assert topic.id == "P0-W1-L1" and topic.due == "2026-10-02"
    assert (workspace / "tracker" / "progress.md").read_text(encoding="utf-8").count("P0-W1-L2") >= 1


def test_failed_quiz_does_not_count_as_done(workspace, cli):
    cli("--date", "2026-10-01", "setup", "--pace", "standard")
    cli("--date", "2026-10-01", "lesson", "P0-W1-L1", "--score", "45")
    st = state("2026-10-04")
    assert st.next_item().id == "P0-W1-L1"
    assert any("still below" in text for _, text in tracker.alerts(st))


def test_unknown_lesson_is_rejected(workspace, cli):
    cli("--date", "2026-10-01", "setup", "--pace", "standard")
    with pytest.raises(SystemExit):
        cli("lesson", "P0-W9-L9", "--score", "80")


def test_review_requires_existing_schedule(workspace, cli):
    cli("--date", "2026-10-01", "setup", "--pace", "standard")
    with pytest.raises(SystemExit):
        cli("review", "P0-W1-L1", "70")


# ---------------------------------------------------------------- pace and alerts

def finish(cli, lessons: list[str], day: str) -> None:
    for lesson in lessons:
        cli("--date", day, "lesson", lesson, "--score", "85")


def test_pace_on_track_then_behind(workspace, cli):
    cli("--date", "2026-10-05", "setup", "--pace", "standard")
    finish(cli, [f"P0-W1-L{n}" for n in range(1, 5)], "2026-10-09")
    assert abs(state("2026-10-12").gap_weeks()) < 0.01  # 1 plan week done after 1 calendar week
    st = state("2026-10-26")  # 3 weeks in, still only week 1 done
    assert st.gap_weeks() == pytest.approx(-2)
    assert any(level == "ALERT" and "Behind plan" in text for level, text in tracker.alerts(st))


def test_light_pace_expects_less(workspace, cli):
    cli("--date", "2026-10-05", "setup", "--pace", "light")
    assert state("2026-10-26").elapsed_plan_weeks() == pytest.approx(1.8)


def test_replan_changes_pace_from_that_day(workspace, cli):
    cli("--date", "2026-10-05", "setup", "--pace", "standard")
    cli("--date", "2026-10-19", "setup", "--pace", "light")
    assert state("2026-11-02").elapsed_plan_weeks() == pytest.approx(2 + 2 * 0.6)


def test_inactivity_alerts(workspace, cli):
    cli("--date", "2026-10-05", "setup", "--pace", "standard")
    cli("--date", "2026-10-05", "session", "--minutes", "60")
    assert any("No study for 3 days" in t for _, t in tracker.alerts(state("2026-10-08")))
    assert any(lvl == "ALERT" and "re-entry" in t for lvl, t in tracker.alerts(state("2026-10-13")))


def test_weekly_gate_and_snapshot(workspace, cli):
    cli("--date", "2026-10-05", "setup", "--pace", "standard")
    cli("--date", "2026-10-11", "weekly", "--test", "60", "--aioff", "70", "--energy", "3")
    assert any("consolidates" in t for _, t in tracker.alerts(state("2026-10-12")))
    assert (workspace / "tracker" / "reports" / "2026-W41.md").exists()


def test_phase_completion_flow(workspace, cli):
    cli("--date", "2026-10-05", "setup", "--pace", "standard")
    phase0 = [i.id for i in state("2026-10-05").paced_items() if i.phase == "0"]
    finish(cli, phase0, "2026-10-15")
    assert any("project is next" in t for _, t in tracker.alerts(state("2026-10-16")))
    cli("--date", "2026-10-17", "project", "PR0", "--score", "82", "--verdict", "pass")
    assert any("exam is next" in t for _, t in tracker.alerts(state("2026-10-17")))
    cli("--date", "2026-10-18", "exam", "EX0", "--score", "78", "--verdict", "pass", "--parts", "A=8,B=7,C=4,D=4")
    st = state("2026-10-18")
    assert st.phase_passed("0") == "2026-10-18"
    assert "AI-Literate Developer" in (workspace / "tracker" / "progress.md").read_text(encoding="utf-8")


def test_weak_spot_fixed_after_three_distinct_days(workspace, cli):
    cli("--date", "2026-10-05", "setup", "--pace", "standard")
    cli("--date", "2026-10-05", "weak", "add", "P0-W1-L1", "confuses spacing with cramming")
    for day in ("2026-10-06", "2026-10-06", "2026-10-08"):
        cli("--date", day, "weak", "pass", "WS-1")
    cli("--date", "2026-10-09", "weak", "fail", "WS-1")  # a miss restarts the count
    for day in ("2026-10-10", "2026-10-12", "2026-10-15"):
        cli("--date", day, "weak", "pass", "WS-1")
    [spot] = state("2026-10-15").weak_spots()
    assert spot["fixed"] == "2026-10-15"


def test_events_are_append_only_json_lines(workspace, cli):
    cli("--date", "2026-10-05", "setup", "--pace", "intense", "--goal-days", "5")
    cli("--date", "2026-10-05", "session", "--minutes", "90", "--energy", "4")
    lines = (workspace / "tracker" / "events.jsonl").read_text(encoding="utf-8").splitlines()
    assert [json.loads(line)["type"] for line in lines] == ["setup", "session"]
    assert state("2026-10-05").settings["goal_days"] == 5
