---
name: recall
description: Spaced-repetition review of the topics due today — asks recall and application questions without notes, grades each topic, and records it with tools/tracker.py so the next review is rescheduled. Use when the learner types /recall, when reviews are due at the start of a session, or when they ask to revise old topics.
---
# /recall — Spaced review

1. **Find what's due.** `python tools/tracker.py status` lists due topics, most urgent first, and the review cap. Take up to the cap, fewer if time is short. If nothing is due, say so and offer an optional mix of 3 questions from random older topics (not recorded).

2. **For each topic,** announce "Topic 2 of 5: <title>", then:
   - Look up the lesson's key concepts in the curriculum (the id tells you the phase file and week) and any open weak spots for it (`tracker/weak-spots.md`).
   - Ask 2 questions, one at a time, **no notes allowed**: (a) recall or explain; (b) apply, such as a code prediction, a small calculation or a scenario. Add a third question if the topic has an open weak spot. Don't repeat last time's questions (check the journal).
   - Give 1–3 lines of feedback after each answer.
   - Record the topic score (0–100): `python tools/tracker.py review <ID> <score>`.
   - Score below 60: reteach for 2–3 minutes from a different angle (an analogy, a tiny example) and point to the exact minutes or section to revisit. If it's a real misconception: `python tools/tracker.py weak add <ID> "..."`.
   - Weak-spot questions: `python tools/tracker.py weak pass WS-N` when answered correctly without help, otherwise `weak fail WS-N`. The tracker marks a spot fixed after 3 correct answers on different days.

3. **Summary.** A table of topics, scores and next review dates (from the tracker's output), plus one line on the pattern you see, for example "definitions solid, application weak → more code practice".
