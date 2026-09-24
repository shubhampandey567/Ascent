---
name: exam
description: Phase gate exam for the AI learning path — concept questions, a live coding task, a stakeholder explanation, and a judgment scenario; the result is recorded with tools/tracker.py and passing unlocks the next phase. Use when the learner types /exam or has finished all lessons and the project of a phase.
---
# /exam — Phase gate (45–75 minutes)

**Preconditions:** every lesson of the phase is done (or tested out) and the phase project has PASSED. Check with `python tools/tracker.py status` (it says "the exam is next") or `tracker.py lessons --phase <N>`. If not, list what's missing and stop.

1. **Explain the format and the pass mark first.** No notes. Official docs are allowed only in Part B.

2. **Part A — Concepts (10 questions, one at a time).** Cover the whole phase and every level: recall, explain, apply, analyze. Include at least 3 "why" questions and 2 code-reading questions. 1 point each, 0.5 for partial.

3. **Part B — Live coding (15–25 minutes).** Use the task in the phase file's exam section, or one like it. The learner works in `projects/exams/EX<N>/`. Grade: works (4), approach (3), code quality (3) → out of 10.

4. **Part C — Explain to a stakeholder.** "Your manager (or a non-technical client) asks: <a question about the phase's big idea>. Answer in at most 6 sentences." Score 0–5 with the rubric.

5. **Part D — Judgment.** A realistic scenario with a trap, for example "the fraud model is 99% accurate — ship it?" Score 0–5 with the rubric.

6. **Result.** Total = A (10) + B (10) + C (5) + D (5) = 30 points, shown as a percentage. PASS = 70% or more overall and at least 50% in each part.
   - Record: `python tools/tracker.py exam EX<N> --score <percent> --verdict pass|retake --parts A=<a>,B=<b>,C=<c>,D=<d>`. On a pass, the dashboard marks the phase complete and shows the badge.
   - **PASS:** celebrate, name the badge and the next phase, and suggest a "learning in public" post.
   - **Not yet:** give a targeted plan listing the lessons and concepts to redo. The retake must be at least 3 days later, so that it tests memory rather than cramming.
   - Concepts missed in Part A → `tracker.py weak add` for each real misconception.
