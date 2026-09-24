# Contributing to Ascent

Thank you for helping! This course only stays useful if links keep working, free tiers stay accurate, and lessons keep improving. Contributions from learners are especially welcome: you know exactly where the course confused you.

Please read the [Code of Conduct](CODE_OF_CONDUCT.md) first.

## Ways to help
| Contribution | Where | Difficulty |
|---|---|---|
| Report or fix a dead link or outdated resource | issue form "Broken link or outdated resource", or a PR | easy |
| Update a changed free tier or price | `guides/free-compute.md` | easy |
| Add a free resource in your language | the "Regional-language options" lines in phase files and `guides/resources.md` | easy |
| Share country-specific job-market facts | `guides/why-this-path.md` | easy |
| Improve a lesson: clearer key concepts, better quiz seeds, a better build task | `curriculum/phase-*.md` | medium |
| Improve the Mentor's behaviour | `.agents/skills/*/SKILL.md`, `AGENTS.md` | medium |
| Make it work well with another AI agent | `scripts/sync_agents.py`, `docs/agents.md` | medium |
| Improve the tracker or scheduler | `tools/`, with tests in `tests/` | medium |
| Translate the course | open a discussion first so we can agree on structure | large |

Not sure where to start? Look for issues labelled `good first issue`.

## Ground rules for content
1. **Free.** Every required resource must be free to use. If something is only partly free (for example a free first module or a paid certificate), say so next to the link. Never make a paid resource required.
2. **Official sources only.** Link to the creator's own channel, site or repository. No re-uploads, pirated books, or "free download" mirrors.
3. **No affiliate, referral or tracking links.**
4. **Verify every link yourself**, and check that the title matches what the lesson says. Don't add resources suggested by an AI without opening them. Run `python scripts/check_links.py <file>` before opening a PR.
5. **Date your facts.** Free tiers, prices, job-market numbers and tool behaviour change often. Write "as of <month year>" and link the source.
6. **Keep it beginner-friendly.** Plain English, short sentences, no unexplained jargon.
7. **Respect the pedagogy.** The course is built on retrieval practice, spacing and hint-based tutoring (`guides/how-to-learn.md`). Changes that make the Mentor give answers instead of hints, or that skip quizzes and reviews, won't be accepted.

## The lesson format (the tracker parses it)
Lessons are `####` headings with an id and a title, separated by `·`:

```
#### P3-W2-L1 · Dot products (~60 min)
- **Learn:** main resource (link, which minutes or sections)
- **Alt:** a different explanation of the same idea
- **Key concepts:** what the learner must be able to explain (the Mentor quizzes these)
- **Quiz seeds:** sample questions (the Mentor varies them)
- **Build:** a small hands-on task
```

- Ids: `P<phase>-W<week>-L<n>` for lessons, `-B` for weekend builds, `-M` for capstone milestones. Ranges like `#### P4-W8-L1 to L4 · Project work` are allowed.
- Each phase file starts with `# Phase N — Title` and a bold line containing `Plan weeks A–B` and `Badge: <name>`.
- Every plan week (1–72) must contain lessons, ids must be unique, and weeks must fall inside their phase. `tests/test_tracker.py` checks all of this.
- **Renaming or removing a lesson id breaks learners' progress data.** Prefer editing a lesson's content over changing its id. If an id must change, note it in `CHANGELOG.md`.

## Mentor skills and agent support
- Edit skills **only** in `.agents/skills/<name>/SKILL.md`. Then run `python scripts/sync_agents.py`, which regenerates `.claude/skills/` and `.opencode/commands/`. CI fails if they're out of sync.
- Keep each `SKILL.md` under 500 lines and `AGENTS.md` under 24 KB (Google Antigravity truncates larger rule files).
- Skill frontmatter: `name` equals the folder name (lowercase, hyphens); `description` says what the skill does and when to use it, at most 1,024 characters, with no `: ` inside.
- Test behaviour changes with at least one real agent, and say which one in your PR.
- To support a new agent: check which files it reads (most read `AGENTS.md` and `.agents/skills/`). If it needs its own format, add a generator to `scripts/sync_agents.py` and a section to `docs/agents.md`.

## Code (`tools/`, `scripts/`, `tests/`)
- `tools/` must stay **standard-library only**, so learners never need to install anything for the tracker to work. Python 3.10+.
- Add or update tests for every behaviour change. The tracker's data format (`tracker/events.jsonl`) must stay backward compatible: learners' existing logs must keep working.

## Before you open a pull request
Work in a **fresh clone of this repository**, never in your personal learning copy (it contains your progress and notes). Then run:

```bash
git clone https://github.com/shubhampandey567/Ascent.git
cd Ascent
python -m pip install -r requirements-dev.txt
python -m pytest -q
python scripts/sync_agents.py --check
python scripts/check_template.py
python scripts/check_links.py <the Markdown files you changed>
```

- Keep pull requests small and focused, and explain *why* in the description.
- Commit messages: short imperative subject, ideally with a type prefix (`content:`, `fix:`, `feat:`, `docs:`).
- A maintainer will review within about two weeks.

## Updating the research
The evidence behind the course lives in `docs/research/`. Add new research as a dated folder (`docs/research/<YYYY-MM>/`) with sources for every claim, rather than editing old notes.

## Licensing of contributions
By contributing you agree that your code contributions are licensed under the [Apache License 2.0](LICENSE) and your content contributions under [CC BY-SA 4.0](LICENSE-CONTENT).
