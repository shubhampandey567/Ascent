---
name: explain
description: Explains a concept the retrieval-first way — asks what the learner already thinks, then builds intuition, a concrete example, and a tiny runnable demo, then checks understanding with a Feynman re-explanation. Use when the learner types /explain or asks what something is or why something happens.
---
# /explain — Retrieval-first explanation

1. **Ask first:** "Before I explain — what do you think <concept> is or does? A guess is fine." Wait for the answer.

2. **Build on their answer.** Keep what's right and correct what's wrong, in this order:
   - **Intuition:** one analogy personalized to them (from their tech stack, business domain, or concepts they already know from `tracker/profile.md`).
   - **Concrete example:** numbers or a small scenario from their domain or everyday life.
   - **Tiny demo** (when code helps): at most 15 lines on toy data, for them to run themselves. Never their project code.
   - **Formal version:** the precise definition or formula, only after the intuition.
   - **Where it's used later** in the course, in one line.

3. **Check:** ask them to explain it back in at most 5 sentences, then one application question. If it's still shaky, try one more angle and move on; the topic will come back in reviews. If it reveals a misconception, record it: `python tools/tracker.py weak add <lesson-id> "..."`.

4. If the concept belongs to a lesson they haven't reached, keep it brief and say which lesson covers it ("comes in P5-W2").

5. Add a journal line: the concept and how the check went.
