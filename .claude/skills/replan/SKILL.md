---
name: replan
description: Re-plans the AI learning path when the learner is behind, ahead, or their time budget changed — adjusts the pace with tools/tracker.py, trims optional items, and keeps reviews and projects intact. Use when the learner types /replan, when the tracker reports they are behind or ahead of plan, or when they say the plan isn't working.
---
# /replan — Adjust the plan

1. **Gather facts.** `python tools/tracker.py status` (pace line and alerts), the "Last 8 weeks" table in `tracker/progress.md` (study days, minutes, scores, energy), and what changed in their life.

2. **Ask, one question at a time:** How much time do you have now? What is draining you? What is working?

3. **Propose one revised plan,** not a menu:
   - the new pace (Light, Standard or Intense) and weekly goal of study days;
   - which optional items to drop;
   - what "back on track" looks like in 4 weeks.

   Never drop reviews, quizzes, phase projects or exams. You may drop items marked "Optional" or "Deeper", alternate resources, and stretch goals.

4. **If they're ahead,** offer test-outs and stretch tasks, or a faster pace.

5. **Record:** `python tools/tracker.py setup --pace <pace> --goal-days <N> --minutes <N>`. The tracker applies the new pace from today, so earlier weeks keep their old expectation. Update the time budget in `tracker/profile.md` and note the reason in the journal. End with the next concrete step.
