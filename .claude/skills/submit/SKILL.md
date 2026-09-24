---
name: submit
description: Verifies a finished project — checks every must-have criterion with evidence, runs the code, holds a viva (defense questions about the learner's own code plus one live change), scores it with the rubric, records the result with tools/tracker.py and writes REVIEW.md. Use when the learner types /submit <project-folder> or says a project is ready for review.
---
# /submit — Project verification and viva

Argument: the project folder under `projects/` (for example `pr2-documentor`). Ask for it if missing.

1. **Load the spec and the work.** Read the project section of the phase file (must-haves, stretch goals, rubric notes), then the learner's folder: README, code, notebook outputs, tests.

2. **Run what you can.** Ask before installing anything. Create or refresh a virtual environment, install the requirements, run the tests and the main entry point. For GPU parts, check the saved notebook outputs or the Kaggle link instead of re-running. Never fix their code; failures become findings.

3. **Must-haves.** Check each one: ✅ or ❌ with evidence (file and line, command output, metric value).

4. **Viva: 4–6 questions, one at a time.**
   - "Walk me through what happens when <the main flow> runs."
   - "Why did you choose <design decision> over <alternative>?"
   - "What happens if <input, data or parameter> becomes <edge case>?"
   - "What is the weakest part of this project, and how would you improve it?"
   - One phase concept tied to their code (why this metric, why this chunk size, why this learning rate).
   - **Live change:** ask for one small modification (15 minutes or less), such as adding a parameter, changing a metric or handling an edge case. Check that it works.

   If the answers show they don't understand their own code, the verdict is REVISE whatever the other scores are.

5. **Score** with the project rubric in `guides/rubrics.md` (100 points). PASS = 70 or more and every must-have ✅. Otherwise REVISE with a numbered list of fixes. Resubmissions are unlimited.

6. **Write `projects/<folder>/REVIEW.md`.** Newest review at the top; keep older ones below. Include: date, verdict, score table, must-have checklist with evidence, viva summary, 3 strengths, the top 3 improvements (specific and actionable), stretch ideas.

7. **Record:** `python tools/tracker.py project PR<N> --score <points> --verdict pass|revise` (use `PR5A` / `PR5B` for two-part projects), and a journal entry. Viva answers that revealed misconceptions → `tracker.py weak add`.

8. **On PASS,** celebrate specifically, and say the exam is next (`/exam`). Suggest a career move: pin the repo on GitHub, or write a short post about it. They write it; you review it if asked.
