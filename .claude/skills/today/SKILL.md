---
name: today
description: Runs today's study session for the AI learning path — tracker status and alerts first, then spaced reviews, the next lesson from the curriculum and a build task, all time-boxed to the learner's budget, and logs the session. Use when the learner types /today or asks what to study now.
---
# /today — Daily session

1. **Status first.** Run `python tools/tracker.py status`. Read `tracker/profile.md` (time budget) and the last journal entry. If the time available today is unclear, ask.

2. **Act on alerts before anything new.** For every ALERT or WARN, tell the learner in one line what it means and what you'll do (for example: behind plan → suggest `/replan`; review backlog → reviews only today; weekly check below 70% → consolidation this week; relearn pending → re-quiz that lesson first).

3. **Pick the day type.**
   - Weekday → the standard session below.
   - Saturday → build day: the week's `B` task or the phase project. Reviews first if any are due.
   - Sunday → run the `weekly` skill instead.
   - After missed days → follow "Adapting to the learner" in `AGENTS.md`.

4. **Show a time-boxed plan** in at most 8 lines. Example for 75 minutes:

   | Block | Min | What |
   |---|---|---|
   | Reviews | 10–15 | 3 due topics |
   | Learn | 35 | P2-W1-L3 — resource, minutes 0–32 |
   | Quiz | 10 | `/quiz` |
   | Build | 15 | the lesson's build task |
   | Close | 5 | reflection and logging |

5. **Reviews block.** If topics are due, run the `recall` skill up to the review cap. Reviews always come before new material.

6. **Learn block.** The next lesson is the one `tracker.py status` names. Open only its week in the curriculum file (in plan weeks 13, 28, 44 and 60 that's `curriculum/consolidation-weeks.md`; in Phase 9 track weeks use the track recorded in the profile) and give the lesson:
   - exactly what to watch or read (link, which minutes or sections) and the alternate resource;
   - 2–3 **focus questions** to keep in mind while watching (questions asked before studying improve learning);
   - how to watch: pause about every 10 minutes and say or write the main point from memory; code along whenever there is code; afterwards write notes from memory in `notes/P<N>/` (see `notes/README.md`);
   - "Come back and type /quiz when you're done."

7. **When they come back,** run the `quiz` skill. For lessons without a quiz (project work, capstone milestones, weekend builds), record them when finished: `python tools/tracker.py lesson <ID> --done`.

8. **Build block.** Give the lesson's build task from the curriculum. Help only through the `stuck` skill.

9. **Close.**
   - Ask for a one-line "Me:" reflection in their own words, and their energy from 1 to 5.
   - Log the session: `python tools/tracker.py session --minutes <N> --energy <1-5>`.
   - Append the journal entry (format at the top of `tracker/journal.md`), including the minute mark if a video was left half-watched.
   - Tell them what's next (`tracker.py next`) and when reviews are due.

**Short on time (20 minutes or less):** reviews plus part of the lesson video; record the minute mark in the journal and still log the session.
