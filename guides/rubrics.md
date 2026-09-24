# Rubrics: how answers, projects and exams are graded

Scores exist for learning, not judgment. They tell the review scheduler when to bring a topic back, and they tell you exactly what to fix.

## 1. Quiz and review answers (per question)

| Mark | Points | Meaning |
|---|---|---|
| ✅ Correct | 1 | Accurate and complete enough to act on |
| 🟡 Partial | 0.5 | Right direction but missing a key piece, a small error, or needed one nudge |
| ❌ Not yet | 0 | Wrong, empty, or recited text without understanding |

A long but vague answer is partial at best. A short, exact answer gets full marks.

## 2. Feynman explanation (0–2 points)

| Points | Looks like |
|---|---|
| 2 | Accurate, simple words, a concrete example or analogy, and one limit ("this does *not* mean...") |
| 1 | Mostly accurate but full of jargon or vague, or one small error |
| 0 | Inaccurate, or just a recited definition |

## 3. From score to review schedule (`tools/srs.py`)

| Score | Grade | What happens next |
|---|---|---|
| 90–100 | 5 | Remembered easily: the gap grows fast and the topic gets "easier" |
| 75–89 | 4 | Remembered: the gap grows |
| 60–74 | 3 | Remembered with effort: the gap grows slowly and the topic gets "harder" |
| 40–59 | 2 | Forgotten: back tomorrow to relearn |
| 20–39 | 1 | Forgotten: back tomorrow; relearn with the alternate resource |
| 0–19 | 0 | Forgotten: back tomorrow; the Mentor reteaches it |

A lesson counts as passed when its first quiz scores 60 or more. Below that, relearn with the alternate resource and re-quiz next session.

A well-known topic comes back after roughly 1, 3, 8, 21, 55, 140 days. A hard topic comes back more often until it sticks.

## 4. Projects (100 points)

| Criterion | Points | Full marks looks like |
|---|---|---|
| Works | 30 | Runs from the README on a fresh clone; meets every must-have; handles the obvious edge cases |
| Understanding (viva) | 25 | Explains design choices and trade-offs, predicts behaviour on edge cases, makes the live change |
| Evaluation and testing | 15 | Numbers, not impressions: metrics, a test set or tests suited to the phase; honest about failures |
| Code quality | 15 | Readable names, small functions, no dead code, no secrets, reproducible (seeds, pinned dependencies) |
| Communication | 15 | README covers the problem, approach, how to run, results, limitations and what you learned; clear plots or diagrams |

- **PASS** = 70 or more **and** every must-have met.
- **REVISE** otherwise. Resubmit as often as you like.
- If the viva shows you can't explain your own code, the verdict is REVISE regardless of points.

## 5. Phase exam (30 points)

| Part | Points | What |
|---|---|---|
| A. Concepts | 10 | 10 questions across the phase, one at a time, no notes |
| B. Live coding | 10 | Works (4), approach (3), code quality (3); official docs allowed |
| C. Stakeholder explanation | 5 | See rubric below |
| D. Judgment scenario | 5 | See rubric below |

**PASS** = 70% or more overall **and** at least 50% in each part. A retake happens at least 3 days later.

**Stakeholder explanation (0–5):** accurate (2), clear with no jargon (1), a concrete example (1), honest about limits or risks (1).

**Judgment scenario (0–5):** spots the trap (2), explains why it's a trap (2), proposes what to do instead (1).

## 6. Rules the Mentor follows when grading
- Grade the answer, not the effort. Praise effort separately.
- Reviews are answered from memory. If notes were used, the topic score is capped at 50.
- Text that looks copied: ask for a rephrase without looking, and grade the rephrase.
- When in doubt between two marks, give the lower one and say exactly what would earn the higher one.
