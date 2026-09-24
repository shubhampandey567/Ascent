---
name: stuck
description: Gets the learner unstuck on code or a concept with a Socratic hint ladder, without handing over the solution to graded work. Use when the learner types /stuck, pastes an error message, or says they can't solve something.
---
# /stuck — Hint ladder

Climb one rung at a time. Move to the next rung only after they've tried the current one, or have been stuck for 20+ minutes.

0. **Describe it.** Ask for the goal, expected vs actual behaviour, the full error text, and what they already tried. Explaining the problem often solves it.
1. **Point.** Ask a guiding question aimed at the right spot: "What is the shape of X just before line 12?" "What does the last line of the traceback say?"
2. **Name it.** Name the concept, tool or function that solves it, and link the official docs or the lesson that taught it.
3. **Outline.** Give pseudocode or the structure of the steps. No real code.
4. **Parallel example.** Show a minimal example of the technique on different toy data, for them to adapt.

Never write the fix into their project. Teach the debugging process as you go: read the traceback from the bottom up, print shapes and types, build a minimal reproduction, test assumptions one at a time, read the docs.

**Exception:** environment and setup problems (installs, PATH, pip conflicts, Colab or Kaggle settings, git config) are not the learning goal. Fix those directly and explain in 2 lines what was wrong.

**Log it:** a journal line "Stuck on X → solved at rung N". If the root cause was a misconception: `python tools/tracker.py weak add <lesson-id> "..."`.
