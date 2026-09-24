---
name: progress
description: Shows and explains the learner's progress dashboard for the AI learning path — position, pace against the plan, scores and trends, review health, weak spots, phases, badges and alerts — from tools/tracker.py. Use when the learner types /progress or asks how they are doing.
---
# /progress — Dashboard

1. **Load.** Run `python tools/tracker.py report` (rebuilds the views), then read `tracker/progress.md`.

2. **Explain it in at most 15 lines:**
   - Where they are: phase, plan week, next lesson.
   - Pace: on track, ahead or behind, in weeks.
   - This week: study days vs goal and minutes; the last 8 weeks at a glance (weeks that met the goal).
   - Scores: first-quiz trend, review retention, last weekly check, confident-but-wrong answers.
   - Weak spots open and fixed; topics on long review gaps.
   - Phases, projects and badges done; the next milestone and what it takes.
   - Any alerts, and what you'll do about each one.

3. **Finish with** one sentence of honest encouragement based on the numbers and one concrete suggestion. Show weeks, not daily streaks, and never say a streak was lost.

The learner (or anyone they share the repository with) can open `tracker/progress.md` at any time; weekly snapshots are in `tracker/reports/`.
