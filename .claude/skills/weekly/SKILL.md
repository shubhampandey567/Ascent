---
name: weekly
description: Sunday weekly retrospective for the AI learning path — a 10-question closed-book cumulative test mixing this week's and older topics, a short AI-off coding check, reflection, pace check, weak-spot analysis, next week's plan, and a saved weekly report via tools/tracker.py. Use when the learner types /weekly or at the end of a study week.
---
# /weekly — Weekly retro (60–90 minutes)

1. **Load.** Run `python tools/tracker.py status` and read `tracker/progress.md` (the "Last 8 weeks" table) and this week's journal entries.

2. **Cumulative test: 10 questions, one at a time, no notes.** 6 from this week's lessons and 4 from older topics, preferring due topics and open weak spots. Mix them; don't group by topic. Grade each answer. Record due topics with `python tools/tracker.py review <ID> <score>` and weak-spot questions with `weak pass|fail WS-N`. Test score = percentage correct.

3. **AI-off coding check (10–15 minutes).** One small task on this week's material, done without any AI help (official docs allowed). This measures real skill, because performance with AI overstates learning. Score it 0–100.

4. **Reflection, one question at a time.** What went well? What was hardest? How many hours did you actually study? Energy from 1 to 5?

5. **Record the week:** `python tools/tracker.py weekly --test <N> --aioff <N> --hours <H> --energy <1-5> --note "<one line>"`. This saves `tracker/reports/<year>-W<week>.md`. **Gate:** if the average of the two checks is below 70%, next week consolidates (redo the weakest lessons, more practice) instead of starting new lessons. Say so kindly; it's the system working, not a failure.

6. **Build checkpoint.** Where is the weekend build or the phase project? If it's ready, suggest `/submit`.

7. **Your analysis (at most 10 lines),** using the dashboard's numbers:
   - Pace vs plan (the tracker's "on track / ahead / behind").
   - Trends: first-quiz average, review retention, study days vs goal, energy.
   - The top 3 weak spots.
   - What changes next week: lighter or heavier, alternate resources, more practice, or `/replan`.
   - One career move: push work to GitHub, write a post, or discuss an AI use case with a colleague.

8. **Preview next week** in 3–5 lines: the topics and why they matter for the learner's goal. End with encouragement grounded in the numbers, for example "12 topics are now on 3-week-plus review gaps".
