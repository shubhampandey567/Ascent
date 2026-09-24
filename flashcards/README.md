# Flashcards (Anki)

Anki is a free flashcard app that schedules reviews for you. It complements the Mentor: Anki drills small facts on your phone in spare minutes (bus, queue, lunch), while `/recall` tests understanding and application.

- **Desktop (Windows):** free at https://apps.ankiweb.net
- **Android:** AnkiDroid, free on the Play Store
- **iPhone:** AnkiMobile is paid (a one-time purchase); use the free AnkiWeb site (https://ankiweb.net) in your phone's browser instead
- Sync between devices with a free AnkiWeb account.

**One-time settings** (deck options): turn on **FSRS**, set **desired retention to 0.90** (0.85 if daily reviews take more than ~20 minutes), and allow at most **10 new cards per day**. Why: [guides/how-to-learn.md](../guides/how-to-learn.md).

## Deck files
The `/cards` command appends cards to `flashcards/phase-<N>.csv`. Each file starts with these header lines, which tell Anki how to read it:

```
#separator:Semicolon
#html:false
#notetype:Basic
#deck:AI Learning
#tags column:3
```

Then one card per line: `front;back;tags`, for example:

```
What does a dot product of two unit vectors measure?;How aligned they are (cosine of the angle);P3 P3-W2-L1
```

## Importing
1. Anki desktop → File → Import → choose the CSV.
2. Check the preview: Front, Back and Tags in the right columns. Choose "Update existing notes" for duplicates so re-importing is safe.
3. Sync, then review on your phone.

## Daily habit
5–10 minutes of Anki per day. Rate cards honestly. "Again" is not a failure; it is exactly how the app learns what you need.

## Rules for good cards
- One idea per card. If an answer has "and" in it, consider two cards.
- Ask "why" and "how" more than "what".
- Cards for your own mistakes are the most valuable cards you have.
- Rewrite any Mentor-drafted card that doesn't sound like you.
- Delete cards that feel pointless. A small deck you actually review beats a big one you avoid.
