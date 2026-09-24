# For mentors, parents and managers: following a learner's progress

This course tracks the learner closely and automatically. If a learner has asked you to follow their progress, here's what you can see and how to help.

## Getting access
The learner keeps their copy of the course in a **private** GitHub repository. They can give you read access: repository **Settings → Collaborators → Add people**. You then see everything in your browser; nothing to install.

Their AI mentor commits nothing by itself. The learner commits after each session (the course asks them to), so the repository's commit history is also a record of how regularly they study.

## What to look at

| File | What it tells you | How often |
|---|---|---|
| `tracker/progress.md` | The dashboard: current phase and week, the next lesson, **pace against the plan** (on track / ahead / behind, in weeks), study days this week vs their goal, quiz and review scores with trends, the weekly check results, phases completed, badges, and **alerts** | weekly |
| `tracker/reports/<year>-W<week>.md` | A frozen snapshot of each week, saved every Sunday | weekly |
| `tracker/weak-spots.md` | Misconceptions the mentor found, and which are fixed (a spot counts as fixed only after 3 correct answers on different days) | now and then |
| `projects/*/REVIEW.md` | The mentor's review of each project: score, evidence, the learner's answers when questioned about their own code, and the top 3 improvements | per project |
| `tracker/journal.md` | A short diary of each session in the learner's own words | if they're happy to share it |

The dashboard is rebuilt by `tools/tracker.py` every time something is recorded, so it's never out of date and nobody edits it by hand.

## What the alerts mean
The tracker raises these automatically; the AI mentor must act on them before teaching anything new.

| Alert | Meaning | A helpful response from you |
|---|---|---|
| No study for N days | The routine broke | Ask what got in the way, not why they failed. Suggest the 10-minute minimum session. |
| Behind plan by N weeks | Pace too ambitious for their life right now | Encourage a `/replan` to a lighter pace. Slower and steady beats quitting. |
| Quiz scores falling / low | Material got harder, or they're tired | Ask about sleep and workload; suggest the alternate resources. |
| Lesson still below 60 | A concept didn't land | Offer to talk it through; explaining to you helps them learn. |
| Weekly check below 70% | Last week didn't stick | Normal occasionally: the next week consolidates instead of rushing on. |
| Energy low two weeks running | Burnout risk | Support rest and reserve days. |
| Many open weak spots | Gaps are piling up | Suggest a session just for clearing them. |
| Project or exam due | They've finished a phase's lessons | Congratulate them; ask to see the project demo. |

## A 10-minute weekly check-in
1. Open `tracker/progress.md` together and look at the "Last 8 weeks" table.
2. Ask: "What did you build or understand this week that you couldn't before?" Let them explain one idea to you in plain words. Teaching you is one of the most effective study techniques.
3. Ask: "What got in the way?" Then agree on one small change for next week.

Praise effort and strategy ("you kept going after a hard week"), not talent. Never punish missed days: that's the fastest way to make someone quit.

## How much to trust the numbers
Scores come from the AI mentor grading answers against a rubric. They are consistent but not perfect. The strongest evidence of learning is the learner explaining a concept to you without notes, and the project demos. The course's exams include a "live coding" part and an "explain it to a stakeholder" part for exactly this reason.

## Privacy
The journal and notes are personal. Look at what the learner chooses to share, and keep their repository private.
