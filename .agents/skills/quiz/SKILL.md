---
name: quiz
description: Quizzes the learner right after a lesson video or reading — 6 questions asked one at a time, graded with the rubric, recorded with tools/tracker.py, and scheduled for spaced review. Use when the learner types /quiz, says they finished a lesson or video, or shares a YouTube link to be tested on.
---
# /quiz — Post-lesson quiz

Argument: a lesson id (for example `P3-W1-L2`), a YouTube URL, or nothing, which means the next lesson (`python tools/tracker.py next`).

1. **Get the material.**
   - The lesson's key concepts and quiz seeds from the curriculum.
   - If the lesson is a video, or a URL was given, ground the questions in what was actually said: `python tools/transcript.py <url> --from <min> --to <min>` for the part watched today. If it exits with code 2 (no captions, or YouTube blocked the request), use the curriculum's key concepts.

2. **Ask 6 questions, one at a time.** Use the seeds as a starting point, but vary them.
   1. **Recall:** define or name something.
   2. **Understand:** "Explain why ... in your own words."
   3. **Apply:** predict the output of a short code snippet, do a tiny calculation, or write 3–6 lines of code.
   4. **Analyze:** find the bug, compare two approaches, or "what happens if ...?"
   5. **Feynman:** "Explain <core idea> to a smart friend outside tech in at most 5 sentences."
   6. **From earlier:** one question on an older topic, preferably a due or weak one. Label it "from earlier".

   Don't hint at answers inside questions. Avoid multiple choice except to probe a known misconception. Invite a confidence rating with each answer (for example "4/5: ..."); it's optional for the learner.

3. **After each answer:** mark ✅, 🟡 (partial) or ❌, then give 1–3 lines: what's right, what's missing, the correct idea. On ❌, give one nudge and let them retry once before you explain. A wrong answer given with high confidence (4–5) deserves the clearest correction; say so, and count it.

4. **Re-ask the misses.** After question 6, ask each ❌ question again in different words. This doesn't change the score, but getting it right once before leaving makes it stick.

5. **Score** (see `guides/rubrics.md`).
   - Questions 1–4 and 6: ✅ = 1, 🟡 = 0.5, ❌ = 0. A correct retry after a nudge = 0.5.
   - Question 5 (Feynman): 0–2 points.
   - Lesson score = points out of 7, as a percentage, rounded.

6. **Record.**
   - `python tools/tracker.py lesson <ID> --score <n> --confident-wrong <count of confident wrong answers>`. This marks the lesson passed (60+) or pending relearn, schedules its reviews, and updates the dashboard.
   - If question 6's topic was due for review: `python tools/tracker.py review <that-id> <0|50|100>`.
   - A misconception, or a mistake repeated from before: `python tools/tracker.py weak add <ID> "what went wrong → the correct idea"`.
   - A line in `tracker/journal.md`.
   - Below 60: the lesson stays next. Prescribe the alternate resource and a re-quiz next session (record the re-quiz the same way).

7. **Close.** Show a small score table, one strength, one thing to fix, any confident-but-wrong answers, and the next review date from the tracker's output. Offer `/cards` (optional).
