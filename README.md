# Ascent

**From "I can program a little" to a hard-to-replace AI engineer, with free resources and your own AI mentor.**

[![License: Apache-2.0 + CC BY-SA 4.0](https://img.shields.io/badge/license-Apache--2.0%20%2B%20CC%20BY--SA%204.0-blue)](#license)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)
[![Works with AGENTS.md agents](https://img.shields.io/badge/works%20with-Antigravity%20%C2%B7%20Claude%20Code%20%C2%B7%20Copilot%20%C2%B7%20Cursor%20%C2%B7%20Codex%20%C2%B7%20more-purple)](docs/agents.md)

**Your loss descends, you ascend.** A neural network learns by gradient descent: small steps, each corrected by feedback, until its error is low. This course climbs the same way. You start with zero AI knowledge, zero budget and no GPU, and go one lesson, quiz, review and project at a time until you're the engineer who builds, evaluates and explains AI systems, not the one AI replaces.

A complete, self-paced course (72 plan-weeks, about 16–18 months at ~10 hours a week) that turns any AI coding agent into a personal instructor. The mentor quizzes you after every video, brings topics back just before you'd forget them, checks your projects by questioning you about your own code, and tracks your progress closely, with alerts when something slips. Everything it asks you to use is free.

## Contents
- [Who it's for](#who-its-for)
- [What you get](#what-you-get)
- [How it works](#how-it-works)
- [Quick start](#quick-start)
- [Using the course, step by step](#using-the-course-step-by-step)
- [The curriculum at a glance](#the-curriculum-at-a-glance)
- [Progress tracking and monitoring](#progress-tracking-and-monitoring)
- [Finding your way around the repository](#finding-your-way-around-the-repository)
- [Plan B: when you have no AI agent](#plan-b-when-you-have-no-ai-agent)
- [Privacy and safety](#privacy-and-safety)
- [FAQ](#faq)
- [Contributing](#contributing)
- [License and credits](#license)

## Who it's for
- You can program a little in any language (Python or Java is ideal) and know **nothing about AI**.
- You have **6–15 hours a week**, for example alongside a full-time job or studies.
- You have an **ordinary laptop**: 8 GB RAM and no graphics card is enough, because heavy work runs on free cloud notebooks.
- You have **no budget**. Nothing in the course requires paying.

## What you get
- **A curriculum:** 10 phases, about 260 lessons, 10 verified projects and 10 phase exams, from "what is AI?" to production agents. Every lesson links free videos and readings, and lists the key concepts, quiz questions and a small build task. [See the map](curriculum/00-overview.md).
- **An AI mentor** defined in [AGENTS.md](AGENTS.md) and 12 command skills. It works with Google Antigravity (free), Claude Code, GitHub Copilot, Cursor, Codex, OpenCode, Gemini CLI, Windsurf and other agents that read `AGENTS.md`. It **never does your work**: it asks, hints, grades and records.
- **A memory system:** spaced repetition brings each topic back after about 1, 3, 8, 21 and 55 days (`tools/srs.py`), plus optional Anki flashcards.
- **Close progress tracking:** every session, quiz, review, project and exam is recorded (`tools/tracker.py`), and a dashboard shows your pace against the plan, trends and alerts. You can share it with a mentor or parent.
- **Guides:** [how to learn](guides/how-to-learn.md) (the evidence behind the method), [why this path](guides/why-this-path.md) (honest job-market facts), [free compute](guides/free-compute.md), [grading rubrics](guides/rubrics.md) and a [resource library](guides/resources.md).

## How it works

```
             every study day (60–75 min): type /today
 ┌────────────────────────────────────────────────────────────────────┐
 │ status &   ─► reviews ─► learn ───────► /quiz ────► build ─► log   │
 │ alerts        (/recall)   video/reading  6 questions small   session│
 │                           + focus Qs     one at a time task         │
 └──────────────────▲────────────────────────────┬────────────────────┘
                    │  each topic returns after ~1, 3, 8, 21, 55 days
                    └────────────────────────────┘
  Saturday: build day   ·   Sunday: /weekly   ·   end of phase: /submit → /exam → next phase
```

Why this design? Watching a video feels like learning, but most of it fades within days unless you pull it back out of memory. Testing yourself beats re-watching, spaced reviews beat cramming, building beats reading, and an AI tutor that gives **hints instead of answers** protects your learning. In a 2025 study, students who used unrestricted AI help scored higher in practice but lower on the exam. The research is summarised in [guides/how-to-learn.md](guides/how-to-learn.md).

## Quick start

### 1. Make your own private copy
Click **Use this template → Create a new repository** at the top of this page, and choose **Private**. Your copy will hold your progress, notes and projects, so it should be yours alone. (Forks of public repositories are public, so use the template button, not Fork.)

### 2. Get it onto your computer
Install [Git](https://git-scm.com/downloads) and [Python 3.10 or newer](https://www.python.org/downloads/) (on Windows, tick "Add python.exe to PATH"). Then clone your repository:

```bash
git clone <your-new-repository-URL>
cd Ascent
python tools/tracker.py status
```

If the last command prints "Not set up yet", everything works. (On Windows, if `python` opens the Microsoft Store or is not recognized, use `py` instead, or turn off the "python.exe" app execution alias in Settings.)

### 3. Choose your AI mentor

| If you have... | Use | How commands look |
|---|---|---|
| Nothing to spend | **[Google Antigravity](https://antigravity.google/download)** (free Individual plan) or its lighter CLI `agy` | `/today` |
| Claude Pro or higher | **Claude Code** (`claude` in the folder) | `/today` |
| VS Code + GitHub Copilot (incl. Copilot Free) | Copilot Chat in **Agent** mode | `/today` |
| Cursor | the agent chat | `/today` |
| ChatGPT (free or paid) | **Codex** | type `today` |
| Free models via OpenCode | **OpenCode** | `/today` |
| Windsurf | Cascade | `@today` |
| Any other agent | ask it to "read AGENTS.md and act as the Mentor" | type `today` |

Setup details, quotas and tips for each agent: [docs/agents.md](docs/agents.md).

### 4. Let the mentor run the course's helper scripts
When your agent first asks, allow these three commands permanently (and keep approval prompts on for anything else):

```
python tools/tracker.py      records your progress and shows the dashboard
python tools/srs.py          schedules your reviews
python tools/transcript.py   reads YouTube transcripts so quizzes match the video
```

For video-grounded quizzes, install one package once: `pip install youtube-transcript-api`. (For running unit tests or contributing, install dev dependencies with `pip install -r requirements-dev.txt`.)

### 5. Type `/start`
Open your copy in your agent and type **`/start`** (or `start`). The mentor interviews you about your time, goals and computer, gives a 10-question placement check, helps you create the free accounts you'll need (GitHub, Google for Colab, Kaggle, Hugging Face, a free LLM API key), records your pace, and gives you your first lesson.

## Using the course, step by step

### Your first day: `/start`
About 45 minutes. At the end you have a filled-in profile, a pace (Light ~6 h/week, Standard ~10 h, Intense ~15 h), a weekly goal of study days, and your first lesson.

### Every study day: `/today`
Sit down and type `/today`. The mentor:
1. runs `python tools/tracker.py status` and tells you your position, pace and any **alerts** (handled first);
2. runs your due **reviews** (`/recall`), a few minutes of questions without notes;
3. gives you the **next lesson**: what to watch or read (with exact links and minutes), plus 2–3 focus questions;
4. waits while you study. Pause every ~10 minutes and recall the main point, then write a short note from memory in `notes/`;
5. when you come back and type **`/quiz`**, asks 6 questions one at a time, grades them, and records the score (60+ passes; below 60 you relearn with an alternate resource);
6. sets a small **build task**, helping only with hints (`/stuck`);
7. logs the session (minutes, energy) and tells you what's next.

### Weekends
- **Saturday: build day.** The week's build task or the phase project.
- **Sunday: `/weekly`.** A 10-question closed-book test, a short coding check without AI, a reflection, and next week's plan. It saves a weekly report. If the week averaged below 70%, next week consolidates instead of racing ahead.

### Moving through a phase
Each phase file in [`curriculum/`](curriculum/) is organised week by week:

```
Phase file
├── Why this phase matters · Before you start · You will be able to
├── Week 1 ── #### P3-W1-L1 · Lesson title
│             - Learn / Alt / Key concepts / Quiz seeds / Build
│             ... L2, L3, L4, then P3-W1-B (weekend build)
├── Week 2 ... Week N
├── Project (must-haves, stretch goals, viva focus)
├── Exam (4 parts)
└── Optional and deeper
```

You don't have to open these files yourself; the mentor serves each lesson. But you can read ahead at any time. The end of every phase follows the same path:

1. **Finish the lessons.** The tracker alerts "the project is next".
2. **Build the project** in `projects/pr<N>-<name>/`, following its must-haves.
3. **`/submit pr<N>-<name>`.** The mentor runs your code, checks every must-have with evidence, questions you about your own code (the "viva"), asks for one small live change, and writes `REVIEW.md`. 70+ and every must-have met = PASS; otherwise fix and resubmit, as often as needed.
4. **`/exam`.** 10 concept questions, a live coding task, an explain-it-to-a-manager question and a judgment scenario. 70% overall (and 50% in each part) passes; otherwise retake after at least 3 days.
5. **The next phase unlocks**, and a badge appears on your dashboard.

**Consolidation weeks** (plan weeks 13, 28, 44 and 60) add nothing new: clear your reviews, fix weak spots, polish projects, write a short post about what you built, and rest.

### When life happens

| Situation | Do this |
|---|---|
| Missed a few days | Just type `/today`. Reviews come first; no guilt. The rule is "never miss twice". |
| Missed a week or more | `/today` runs a short re-entry session, then about 70% pace for a week. |
| Consistently behind (the tracker alerts you) | `/replan`: switch to a lighter pace or drop optional items. Reviews, projects and exams always stay. |
| Finding it too easy | Ask for a test-out: 5 questions, 85+ and the lesson counts as done. |
| Stuck on code or a concept | `/stuck` for hints, one step at a time, or `/explain <concept>`. |
| Low energy | A "minimum session": 10 minutes of reviews plus one short video. |
| Anxious about AI and jobs | Read [guides/why-this-path.md](guides/why-this-path.md), then do the next lesson. |

### Where am I? What's next?
- **`/progress`**: the mentor explains your dashboard.
- **`tracker/progress.md`**: the dashboard itself; open it any time, on GitHub or locally.
- **`python tools/tracker.py next`**: the next lesson, without asking the agent.
- **`python tools/tracker.py lessons --phase 3`**: every lesson in a phase, with done marks.

### All commands

| Command | When | What happens |
|---|---|---|
| `/start` | first session | interview, placement check, setup |
| `/today` | whenever you sit down to study | status → reviews → lesson → quiz → build → log |
| `/quiz [lesson or YouTube URL]` | after a video or reading | 6 questions, graded, recorded, scheduled |
| `/recall` | reviews are due | spaced review without notes |
| `/explain <concept>` | any time | starts from what you think, then explains and checks |
| `/stuck [problem]` | blocked | hints one level at a time, never the answer |
| `/submit <project-folder>` | project finished | checks, viva, score, `REVIEW.md` |
| `/weekly` | Sundays | cumulative test, AI-off check, weekly report |
| `/exam` | end of a phase | gate to the next phase |
| `/cards` | after a lesson (optional) | Anki flashcards |
| `/replan` | behind, ahead, or life changed | new pace and plan |
| `/progress` | any time | your dashboard, explained |

## The curriculum at a glance

| Phase | Title | Plan weeks | You finish able to... | Project |
|---|---|---|---|---|
| 0 | [Launchpad](curriculum/phase-0-launchpad.md) | 1–2 | explain AI and LLMs; call an LLM from your code | Error-explainer CLI |
| 1 | [Python & Data Toolkit](curriculum/phase-1-python-data.md) | 3–7 | clean, analyse and chart real data; SQL; tests | Data Detective |
| 2 | [LLM App Builder I](curriculum/phase-2-llm-apps.md) | 8–12 | build, evaluate and deploy a RAG chatbot | DocuMentor |
| — | [Consolidation](curriculum/consolidation-weeks.md) | 13 | | |
| 3 | [Math for ML](curriculum/phase-3-math.md) | 14–19 | vectors, gradients, probability, in NumPy | Math Engine |
| 4 | [Classical Machine Learning](curriculum/phase-4-classical-ml.md) | 20–27 | take tabular data to a deployed, evaluated model | End-to-End Predictor |
| — | [Consolidation](curriculum/consolidation-weeks.md) | 28 | | |
| 5 | [Deep Learning](curriculum/phase-5-deep-learning.md) | 29–36 | backprop from scratch; CNNs; transfer learning | micrograd + image classifier |
| 6 | [Transformers & LLM Internals](curriculum/phase-6-transformers-llms.md) | 37–43 | build a GPT; fine-tune a small LLM | Inside the LLM |
| — | [Consolidation](curriculum/consolidation-weeks.md) | 44 | | |
| 7 | [AI Engineering II: RAG, Agents, MCP, Evals](curriculum/phase-7-ai-engineering.md) | 45–53 | secure, evaluated agents with tools and MCP | Agentic assistant |
| 8 | [MLOps & Production](curriculum/phase-8-mlops.md) | 54–59 | Docker, CI/CD, tracking, monitoring | Ship it for real |
| — | [Consolidation](curriculum/consolidation-weeks.md) | 60 | | |
| 9 | [Specialize, Capstone & Career](curriculum/phase-9-capstone-career.md) | 61–72 | a specialisation, a capstone, a portfolio, interviews | Capstone |

The easy part comes first on purpose: you build a working LLM app by week 12, then go deep into the maths and internals, then come back to engineering at a higher level. Full map, milestones and pace options: [curriculum/00-overview.md](curriculum/00-overview.md).

## Progress tracking and monitoring
Everything is recorded by `tools/tracker.py` into `tracker/events.jsonl`, never edited by hand, and turned into readable views after every event:

- **[tracker/progress.md](tracker/progress.md)**, the dashboard:
  - where you are, and your next lesson;
  - pace against the plan (on track, ahead or behind, in weeks);
  - study days this week vs your goal;
  - first-quiz and review-retention trends; weekly check results; confident-but-wrong answers;
  - an 8-week history table;
  - every phase with its lessons, project and exam status;
  - badges and alerts.
- **tracker/weak-spots.md:** misconceptions, and which are fixed (after 3 correct answers on different days).
- **tracker/reports/:** a snapshot every Sunday.
- **projects/\*/REVIEW.md:** every project verdict, with evidence.

**Alerts** fire automatically for: days without study, falling behind or getting ahead of plan, low or falling quiz scores, a lesson stuck below 60, a review backlog, low retention, a weekly check below 70%, low energy two weeks running, overconfidence, many open weak spots, a project or exam being due, and being stuck on one lesson for a week. The mentor must deal with alerts before teaching anything new.

**Sharing with a mentor, parent or manager:** add them as a read-only collaborator on your private repository and commit after each session. [docs/for-mentors.md](docs/for-mentors.md) explains what they'll see and how to help.

## Finding your way around the repository

| Path | What it is | When you open it |
|---|---|---|
| [AGENTS.md](AGENTS.md) | the mentor's rules (every agent reads it) | curious how the mentor works |
| [curriculum/](curriculum/) | the course: overview, 10 phases, consolidation weeks | reading ahead; checking a project spec |
| [guides/](guides/) | how to learn, why this path, free compute, rubrics, resources | when the mentor points you there |
| [tracker/](tracker/) | your profile, dashboard, journal, weak spots, weekly reports | checking progress |
| [notes/](notes/) | your notes, written from memory | after each lesson |
| [projects/](projects/) | your projects and their reviews | build days |
| [flashcards/](flashcards/) | Anki decks from `/cards` | optional daily drill |
| [tools/](tools/) | tracker, review scheduler, transcript reader | rarely by hand |
| `.agents/skills/` | one folder per command | editing how a command behaves |
| [docs/](docs/) | agent setup, mentor guide, architecture, research | setup and contributing |

## Plan B: when you have no AI agent
Free agent quotas run out. The course keeps working:
1. **Reviews:** do your Anki deck on your phone, or `python tools/srs.py today` to see what's due.
2. **Lessons:** `python tools/tracker.py next` names the lesson; study it and write notes from memory.
3. **Self-quiz:** answer the lesson's quiz seeds on paper *before* looking at the key concepts, grade yourself honestly with [guides/rubrics.md](guides/rubrics.md), and record it: `python tools/tracker.py lesson P1-W2-L1 --score 70`. Record reviews with `python tools/tracker.py review <ID> <score>` and your study time with `python tools/tracker.py session --minutes 60`.
4. **Or paste this into any free chat app** (Gemini, ChatGPT, Claude):

   > You are my strict but kind AI tutor. I just studied: <lesson title and link>. Key concepts: <paste from the curriculum>. Ask me 6 questions ONE AT A TIME: recall, explain, apply (a tiny code or math example), find-the-bug, explain-it-to-a-friend, and one on an older topic: <topic>. Wait for each answer, mark it ✅/🟡/❌ with a two-line correction, and give me a score out of 100 at the end. Never give me an answer before I try.

When the agent is back, it picks up from the tracker as if nothing happened.

## Privacy and safety
- Keep your copy **private**: it holds your progress, notes and journal.
- API keys go only in `.env` (copy `.env.example`); `.env` is gitignored. Never paste keys into chat, code, notebooks or issues.
- **Never paste your employer's code or confidential data** into any free AI tool, including your mentor. Free tiers may use prompts for training. Use public or synthetic data.
- Keep your agent's approval prompts on for everything except the three course scripts. See [SECURITY.md](SECURITY.md).

## FAQ
- **Do I really need nothing paid?** Correct. Google Antigravity's free plan works as the mentor, and every resource is free. Some optional certificates cost money; the course says so wherever that applies.
- **My laptop is old.** Use it for editing, the mentor and small scripts. Anything that needs a GPU or big data runs on Kaggle or Colab ([guides/free-compute.md](guides/free-compute.md)).
- **The mentor gave me the full answer.** Tell it "hints only, as AGENTS.md says". It must follow the hint ladder.
- **I'm behind schedule.** Normal. `/replan`. A lighter pace that you keep beats a fast one that you quit.
- **Can I skip ahead?** Yes: test-outs let you pass lessons you already know. Each phase lists its prerequisites.
- **Can I learn in my own language?** Tell the mentor during `/start`; it explains in your language, and lessons list regional-language alternates where contributors have added them.
- **A link is dead.** Tell the mentor (it will find the resource on the creator's channel or use the alternate) and please [report it](../../issues/new/choose).
- **How do I get course updates in my copy?** Template copies don't sync automatically. Occasionally copy updated `curriculum/`, `guides/`, `.agents/skills/` and `tools/` folders from the upstream repository into yours (never overwrite your `tracker/`, `notes/` or `projects/`), then run `python scripts/sync_agents.py`.

## Contributing
Corrections, dead-link reports, better free resources (especially in other languages), lesson improvements and support for more AI agents are all very welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) and the [Code of Conduct](CODE_OF_CONDUCT.md). Please contribute from a fresh clone of this repository, not from your personal learning copy.

## License
- Code (`tools/`, `scripts/`, `tests/`, `.github/`): [Apache License 2.0](LICENSE).
- Course content (curriculum, guides, docs, mentor instructions and skills): [CC BY-SA 4.0](LICENSE-CONTENT). You may share and adapt it, with credit, under the same license.
- Linked videos, courses, books and sites belong to their creators.

## Credits
This course stands on the generosity of people who teach for free, including 3Blue1Brown, StatQuest, Andrej Karpathy, fast.ai, Hugging Face, DeepLearning.AI, Google, Microsoft, Kaggle, Stanford, MIT, Harvard CS50, DataTalksClub, Sebastian Raschka, Jay Alammar, Umar Jamil and many more. Please support them.

_Not affiliated with any company or tool mentioned. Free tiers, prices and links were checked in September 2026 and change often; the link checker runs weekly, and corrections are welcome._
