# My Projects

Every phase ends with a project. Projects are where learning becomes skill, and they become your portfolio.

## Folder layout

```
projects/
  pr0-hello-llm/
    README.md        problem, how to run, results, what I learned, limitations
    src/             code (or notebook.ipynb for data/ML work)
    tests/           pytest tests (from Phase 1 on)
    requirements.txt or pyproject.toml
    REVIEW.md        written by the Mentor after /submit — don't edit
```

For work done on Kaggle or Colab: put the notebook link in the README **and** download the `.ipynb` with its outputs into the folder, so the Mentor can read the results without re-running the GPU parts.

## How a submission works (`/submit pr0-hello-llm`)
1. The Mentor reads the spec in the curriculum and your folder, and runs what it can.
2. It checks every **must-have** criterion and shows evidence (file, line, output).
3. **Viva:** it asks 4–6 questions about *your* code, one at a time, and asks for one small live change. This proves you own the work.
4. It scores with the rubric in `guides/rubrics.md` and writes `REVIEW.md`.
5. **PASS** = 70+ points and every must-have met. Otherwise **REVISE** — fix and resubmit as often as you like. Revising is normal; it is how real engineering works.

## Rules for using AI in projects
| Phases | Allowed | Not allowed |
|---|---|---|
| 0–4 | Explanations, hints (`/stuck`), reviewing code you already wrote, fixing setup/installs | Generating the solution or core code |
| 5–6 | AI help for boilerplate (plots, argument parsing, file I/O); mark it with `# AI-assisted` | Generating model, training, or algorithm code |
| 7–9 | Coding agents allowed and encouraged — directing them well is a skill you are learning | Submitting anything you cannot explain line by line in the viva |

## Before you type /submit
- [ ] Runs from a fresh clone following only the README
- [ ] No API keys or secrets in the code or notebook outputs (they live in `.env`)
- [ ] README has: problem, approach, how to run, results (numbers!), limitations, what I learned
- [ ] Tests pass (Phase 1 onward)
- [ ] Pushed to GitHub
