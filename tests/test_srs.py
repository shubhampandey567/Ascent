from datetime import date, timedelta

import pytest

import srs


def fresh(**kwargs) -> srs.Topic:
    return srs.Topic(id="P1-W1-L1", title="t", **kwargs)


@pytest.mark.parametrize("score,q", [(100, 5), (90, 5), (89, 4), (75, 4), (74, 3), (60, 3), (59, 2), (40, 2), (39, 1), (20, 1), (19, 0), (0, 0)])
def test_quality_bands(score, q):
    assert srs.quality(score) == q


def test_well_known_topic_expands_1_3_8_20_50():
    t, day, gaps = fresh(), date(2026, 1, 1), []
    srs.schedule(t, 85, day)
    for _ in range(4):
        gaps.append(t.interval)
        day = date.fromisoformat(t.due)
        srs.schedule(t, 85, day)
    gaps.append(t.interval)
    assert gaps == [1, 3, 8, 20, 50]


def test_forgotten_topic_comes_back_tomorrow_and_counts_a_lapse():
    t, day = fresh(), date(2026, 1, 1)
    srs.schedule(t, 90, day)
    srs.schedule(t, 90, day + timedelta(days=1))
    srs.schedule(t, 30, day + timedelta(days=4))
    assert (t.interval, t.reps, t.lapses) == (1, 0, 1)
    assert t.due == (day + timedelta(days=5)).isoformat()


def test_ease_never_drops_below_floor():
    t, day = fresh(), date(2026, 1, 1)
    for n in range(10):
        srs.schedule(t, 0, day + timedelta(days=n))
    assert t.ease == srs.MIN_EASE


def test_same_day_retest_keeps_schedule():
    t, day = fresh(), date(2026, 1, 1)
    srs.schedule(t, 80, day)
    before = (t.interval, t.due, t.ease)
    srs.schedule(t, 100, day)
    assert (t.interval, t.due, t.ease) == before
    assert t.history.count(":") == 2


def test_late_review_gets_half_the_extra_delay():
    t, day = fresh(), date(2026, 1, 1)
    for _ in range(3):
        srs.schedule(t, 85, day)
        day = date.fromisoformat(t.due)
    assert t.interval == 8
    srs.schedule(t, 95, date.fromisoformat(t.due) + timedelta(days=14))  # reviewed 14 days late
    assert t.interval == round((8 + 22) / 2 * 2.5)


def test_interval_is_capped():
    t = fresh(reps=10, interval=150, ease=2.5, last_review="2026-01-01")
    srs.schedule(t, 95, date(2026, 5, 31))
    assert t.interval == srs.MAX_INTERVAL


def test_record_adds_then_grades(tmp_path, monkeypatch):
    monkeypatch.setattr(srs, "QUEUE", tmp_path / "q.csv")
    srs.record("p2-w1-l1", "Tokens", 80, date(2026, 1, 1))
    srs.record("P2-W1-L1", "Tokens", 90, date(2026, 1, 2))
    [t] = srs.load()
    assert (t.id, t.phase, t.reviews, t.last_score) == ("P2-W1-L1", "2", 2, "90")


def test_score_out_of_range_is_rejected():
    with pytest.raises(SystemExit):
        srs.check_score(101)
