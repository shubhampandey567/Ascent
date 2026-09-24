---
name: cards
description: Drafts Anki flashcards for the latest lesson (atomic, one idea per card) and appends the approved ones to flashcards/phase-N.csv for import into Anki. Use when the learner types /cards or asks for flashcards.
---
# /cards — Anki flashcards

1. **Lesson** = the argument, or else the last completed lesson. Use its key concepts, the learner's quiz mistakes, and related weak-spots rows.

2. **Draft 6–12 cards** by these rules:
   - One idea per card. Questions of at most 20 words; answers as short as possible (15 words or fewer where you can).
   - Prefer "why", "how" and "when" questions over bare definitions.
   - Include at least 1 code-reading card (for example: "What shape does `x.reshape(-1, 1)` give for an array of shape (4,)?") and at least 1 card built from a mistake they made.
   - No "list all 7 ..." cards; split them. Avoid yes/no questions.

3. **Show the cards** and ask the learner to edit or reject them. Rewriting a card in their own words is part of learning, so encourage it.

4. **Append the approved cards** to `flashcards/phase-<N>.csv`. If the file doesn't exist, create it with the header lines from `flashcards/README.md`. Columns: `front;back;tags`, with tags like `P3 P3-W2-L1`. Put any field that contains a semicolon in double quotes.

5. **Remind them** to import the file in Anki (File → Import) and to do the Anki reviews daily on their phone (5–10 minutes).
