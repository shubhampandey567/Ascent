# How the course works inside (for contributors)

## Design principles
1. **Evidence-based learning.** Retrieval practice after every lesson, spaced reviews, interleaving, and a tutor that gives hints, not answers. See [guides/how-to-learn.md](../guides/how-to-learn.md) and [docs/research/](research/).
2. **Deterministic bookkeeping.** Language models are unreliable at dates, arithmetic and keeping tables consistent, so every date, schedule, pace calculation and dashboard is computed by Python. The model teaches and grades; the tools record.
3. **Agent-agnostic.** Plain Markdown instructions in open formats (`AGENTS.md`, Agent Skills), so any capable coding agent can be the Mentor.
4. **Free and light.** Standard-library Python only; runs on a modest laptop; heavy work goes to free cloud notebooks.
5. **A template, not a platform.** Each learner owns a private copy. There's no server and no account, and all data stays in their repository.

## Components

```
AGENTS.md ─────────────── the Mentor's rules (always loaded by the agent)
   │
   ├── .agents/skills/<command>/SKILL.md ── step-by-step procedure per command
   │      └── generated copies: .claude/skills/ (Claude Code), .opencode/commands/ (OpenCode)
   │
   ├── curriculum/*.md ─── lessons (#### ids), key concepts, quiz seeds, projects, exams
   │
   └── tools/tracker.py ── the single entry point for recording learning
          ├── reads curriculum/*.md → lesson index with plan weeks
          ├── appends tracker/events.jsonl (source of truth for progress)
          ├── calls tools/srs.py → tracker/review-queue.csv (review schedule)
          └── rebuilds views: tracker/progress.md, tracker/weak-spots.md, tracker/reports/
```

## The curriculum contract
`tools/tracker.py` parses the curriculum, so its format is an interface:
- Phase files are named `curriculum/phase-<N>-<slug>.md`, start with `# Phase N — Title`, and contain a bold line with `Plan weeks A–B` and `Badge: <name>`.
- Lessons are `#### <ID> · <Title>` headings. Ids: `P<phase>-W<week>-L<n>` (lesson), `-B` (weekend build), `-M` (capstone milestone). `L1 to L4` and `L3 and L4` ranges expand.
- A lesson's plan week = the phase's first plan week + its week number − 1.
- `curriculum/consolidation-weeks.md` uses `C<week>` placeholders, expanded for plan weeks 13, 28, 44 and 60.
- Tests check that every plan week 1–72 has lessons, ids are unique, and weeks fall inside their phase.

Lessons (`L`) and milestones (`M`) count towards pace; builds (`B`) don't.

## Data formats
**`tracker/events.jsonl`**: one JSON object per line, append-only, each with `date` and `type`:

| type | fields |
|---|---|
| `setup` | `start` (first only), `pace`, `goal_days`, `minutes`, `review_cap` |
| `session` | `minutes`, `energy`, `note` |
| `lesson` | `id`, `score` or `done`, `confident_wrong` |
| `review` | `id`, `score` |
| `project` | `id` (`PR3`, `PR5A`), `score`, `verdict` (`pass`/`revise`) |
| `exam` | `id` (`EX3`), `score` (%), `verdict` (`pass`/`retake`), `parts` |
| `weekly` | `test`, `aioff`, `hours`, `energy`, `note` |
| `weak_add` / `weak_check` | `id` (`WS-3`), `lesson`, `text` / `result` (`pass`/`fail`) |

New fields must be optional, so existing learners' logs keep working.

**`tracker/review-queue.csv`**: one row per topic with the SM-2 state (`interval`, `ease`, `reps`, `lapses`, `due`, `history`). Written only by `tools/srs.py`.

## Pace and alerts
- Pace factors: light 0.6, standard 1.0, intense 1.5 plan weeks per calendar week. Re-plans apply from their date onwards.
- "Completed plan weeks" counts whole weeks finished in order, plus the finished fraction of the first unfinished week. The gap to the expected plan weeks drives the behind/ahead alerts.
- Alert thresholds are in `tools/tracker.py` (`alerts()`); they're reasoned defaults from the learning-science notes and can be tuned with evidence.

## Scheduling
`tools/srs.py` implements a modified SM-2 (details in its docstring): score bands 90/75/60/40/20 map to grades 5–1; first gaps 1 and 3 days, then × ease; same-day retests don't grow the gap; late but good reviews earn half the extra delay; gaps are capped at 180 days.

## Adding support for another agent
Most agents read `AGENTS.md` and `.agents/skills/` directly. If one needs its own format, add a generator to `scripts/sync_agents.py`, run it, and document the agent in [docs/agents.md](agents.md). CI fails when generated files drift.

## Checks
| Command | What it guards |
|---|---|
| `python -m pytest -q` | scheduler, tracker, curriculum format |
| `python scripts/sync_agents.py --check` | skill validity and generated adapters |
| `python scripts/check_template.py` | no personal learning data in the template |
| `python scripts/check_links.py` | dead links (YouTube checked by real titles); runs weekly in CI |
