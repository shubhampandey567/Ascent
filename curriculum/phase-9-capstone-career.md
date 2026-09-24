# Phase 9 — Specialize, Capstone & Career

**Plan weeks 61–72 · 12 weeks · Difficulty ★★★★★ · Badge: Specialist**

## Why this phase matters
You now have broad, deep skills. This phase turns them into *career capital*: one area where you go deeper than most, one substantial project that solves a real problem end to end, and the portfolio, story and interview skills to get paid for it, either inside your current company or outside it. It also sets up the habit that keeps you valuable after this course ends: learning continuously.

## Before you start
- Phases 7 and 8 passed.
- Your projects are on GitHub with good READMEs.

## Shape of the phase
| Plan weeks | What |
|---|---|
| 61–62 | Specialisation sprint: pick a track, go deep |
| 63–70 | Capstone: discover, design, build, evaluate, launch |
| 71–72 | Career sprint: portfolio, résumé, interviews, internal moves |

---

## Weeks 1–2 (plan weeks 61–62) — Choose a track and go deep
Pick **one** main track (the Mentor can help with `/explain` and `/replan`). Each week has 4 lessons chosen from the track list plus a weekend build in that area. The Mentor fills the lesson slots `P9-W1-L1` to `P9-W2-L4` (below) from your track, notes the track in `tracker/profile.md`, and records each lesson with `tools/tracker.py` as usual.

### Track A — LLM & Agent Engineer (the default: highest demand in 2026)
- [DeepLearning.AI — Agentic AI (Andrew Ng)](https://www.deeplearning.ai/courses/agentic-ai) (31 video lessons): reflection, tool use, planning, multi-agent patterns.
- [UC Berkeley Agentic AI MOOC, Fall 2025](https://agenticai-learning.org/f25): selected lectures ([lecture 1](https://www.youtube.com/watch?v=r1qZpYAmqmg)).
- [Hugging Face Context Course](https://huggingface.co/learn/context-course): Agent Skills, MCP, plugins, sub-agents, hooks.
- [Kaggle — 5-Day AI Agents Intensive](https://www.kaggle.com/learn-guide/5-day-agents): whitepapers + codelabs.
- [OWASP Top 10 for Agentic Applications](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/): read it in full.
- Build: a voice or multi-agent extension of Project 7, or an agent evaluation harness reused across two projects.

### Track B — ML Engineer / MLOps
- [DataTalksClub — MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) (self-paced), end to end.
- [Made With ML](https://madewithml.com/), the remaining lessons.
- [Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/) (in Codespaces).
- Build: an automated training → evaluation → registry → deployment pipeline with drift-triggered retraining.

### Track C — Computer Vision
- [Stanford CS231n (Spring 2025)](https://www.youtube.com/playlist?list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16): lectures 6–9 and 16 (architectures, detection, segmentation, vision + language).
- [Hugging Face Community Computer Vision Course](https://huggingface.co/learn/computer-vision-course/unit0/welcome/welcome).
- [Ultralytics docs](https://docs.ultralytics.com/) for object detection; [3Blue1Brown × Welch Labs on diffusion models](https://www.youtube.com/watch?v=iv-5mZ_9CPY).
- Build: an object detector or a vision-language app on your own images, trained on Kaggle.

### Track D — Data Science + AI
- [ISLP](https://www.statlearning.com/), chapters on resampling, tree methods and unsupervised learning, with the [labs](https://github.com/intro-stat-learning/ISLP_labs).
- [Causal Inference: The Mixtape](https://mixtape.scunning.com/) (free), the introductory chapters.
- [Kaggle Learn — Time Series](https://www.kaggle.com/learn/time-series).
- Build: a forecasting or A/B-test analysis with a decision memo, plus an LLM-generated narrative you evaluate for accuracy.

### Track E — Research-leaning (LLM internals)
- [Stanford CS336 — Language Modeling from Scratch (Spring 2026)](https://www.youtube.com/playlist?list=PLoROMvodv4rMqXOcazWaTUHhq-yembLCV): lectures on tokenization, architecture, inference and alignment ([course site](https://cs336.stanford.edu/)).
- [Sebastian Raschka — reasoning-from-scratch](https://github.com/rasbt/reasoning-from-scratch).
- Read 4 papers in depth (three-pass method): [GPT-3](https://arxiv.org/abs/2005.14165), [InstructGPT](https://arxiv.org/abs/2203.02155), [DPO](https://arxiv.org/abs/2305.18290), [DeepSeek-R1](https://arxiv.org/abs/2501.12948).
- Build: reproduce one small result from a paper on a free GPU and write it up.

### Track F — Enterprise Java + AI (uses your Java background)
Java appears in about 18% of AI-engineer postings, and many IT services projects (especially in India) run on Java/Spring. An engineer who can build RAG and agents *inside* those systems is rare.
- [Spring AI reference](https://docs.spring.io/spring-ai/reference/): chat clients, structured output, RAG, tool calling, MCP.
- [LangChain4j docs](https://docs.langchain4j.dev/).
- [MCP Java SDK](https://github.com/modelcontextprotocol/java-sdk).
- Build: port your Project 2 RAG (or the Project 7 MCP server) to Spring Boot + Spring AI, calling a free, OpenAI-compatible provider.

### Lesson slots
The Mentor fills these slots from your chosen track and records them like any other lesson.

#### P9-W1-L1 to L4 · Track lessons 1–4 (from your chosen track)
#### P9-W1-B · Weekend: first track build
#### P9-W2-L1 to L4 · Track lessons 5–8 (from your chosen track)
#### P9-W2-B · Weekend: finish the track build and write it up

---

## Weeks 3–10 (plan weeks 63–70) — Capstone
The capstone is your flagship project: a real problem, real users (even 3), measured results, shipped.

Each week is one milestone. Record it with `tracker.py lesson P9-W<n>-M --done` when the Mentor's check passes.

#### P9-W3-M · Discover (plan week 63)
Talk to 3 potential users (colleagues, friends, a family business). Write a 1-page proposal: problem, users, why AI, success metric, data source (public or synthetic only).
*Mentor checks:* is the problem real, the metric measurable, and the scope doable in 8 weeks for free?

#### P9-W4-M · Design (plan week 64)
A design doc with architecture, eval plan, threat model and cost estimate. Build the golden eval set *before* the system.
*Mentor checks:* does the eval set reflect real use? Are the risks covered?

#### P9-W5-M · Build v1, part 1 (plan week 65)
The simplest version that runs end to end.
*Mentor checks:* does it run from the README on a fresh clone?

#### P9-W6-M · Build v1, part 2 (plan week 66)
First full eval run and error analysis.
*Mentor checks:* are the failures categorised, with counts?

#### P9-W7-M · Improve, part 1 (plan week 67)
Change one thing at a time and measure every change against the eval set.
*Mentor checks:* is every change backed by a before/after number?

#### P9-W8-M · Improve, part 2 (plan week 68)
More improvements, plus feedback from your users.
*Mentor checks:* what did users say, and what changed because of it?

#### P9-W9-M · Harden (plan week 69)
Security review, guardrails, monitoring, CI/CD with an eval gate, documentation.
*Mentor checks:* would you trust it with real users?

#### P9-W10-M · Launch (plan week 70)
Deploy; record a 3–5 minute demo video (free: [OBS Studio](https://obsproject.com/)); write a blog post; present to your team.
*Mentor checks:* can a stranger understand and use it from the README?

**Capstone ideas** (choose something you care about):
- A multilingual government-scheme finder in your local languages over official public documents, with citations.
- An agricultural advisory assistant over public agriculture-extension documents.
- A "bare acts" legal-information RAG with clear "not legal advice" guardrails.
- An IT-operations assistant that triages synthetic logs and alerts and drafts incident summaries.
- A test-case generator for Java codebases, with evals on real open-source repos.
- A SQL copilot over a sample database, with guardrails against destructive queries.

**Capstone must-haves:** the problem statement and metric; an eval set built first; a before/after table for every major change; security and privacy review; deployed or recorded demo; README, blog post and team presentation; everything free and using only public or synthetic data.

`/submit` the capstone at the end of plan week 70.

---

## Weeks 11–12 (plan weeks 71–72) — Career sprint

#### P9-W11-L1 · Portfolio (~90 min)
- GitHub profile README; pin your 6 best repositories (for example Projects 2, 4, 5, 6, 7 and the capstone). Each README starts with the problem, a demo link, the results table and the architecture.
- A simple portfolio page on [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) linking everything.

#### P9-W11-L2 · Résumé and LinkedIn (~90 min)
- Impact bullets with numbers ("raised answer accuracy from 71% to 89% on a 60-question eval set by adding hybrid search and reranking").
- LinkedIn headline, featured projects, and a plan for one post per week about something you built or learned.

#### P9-W11-L3 · Interview fundamentals (~75 min)
- Chip Huyen's free [Introduction to Machine Learning Interviews](https://huyenchip.com/ml-interviews-book/) (the process, what's asked, how to prepare).
- The interview section of the [AI Engineering Field Guide](https://github.com/alexeygrigorev/ai-engineering-field-guide/tree/main/interview): questions, take-home assignments, how people got hired.

#### P9-W11-L4 · Mock interview: ML and LLM concepts (~60 min)
- Ask the Mentor: "Run a 45-minute mock interview on ML and LLM fundamentals, one question at a time, then grade me." Weak answers are recorded with `python tools/tracker.py weak add`.

#### P9-W12-L1 · Mock interview: system design (~75 min)
- Ask the Mentor for an LLM system-design interview ("Design a support chatbot for a bank serving 1 million users"). Practise requirements → architecture → data → evals → risks → cost → scaling.

#### P9-W12-L2 · Mock interview: coding and behavioural (~75 min)
- One coding problem and one practical ML coding task without AI help; then behavioural questions using the STAR format (Situation, Task, Action, Result) with stories from your projects and your job.

#### P9-W12-L3 · The internal move (~60 min)
- Many of the best AI opportunities are inside your current company. Prepare a 10-minute demo of your capstone and ask your manager for a GenAI proof-of-concept or a transfer to an AI team. Offer to run a lunch-and-learn on RAG or evals.

#### P9-W12-L4 · Your learning system for life (~60 min)
- Decide your ongoing rhythm (below). Update `tracker/profile.md` with the next 6-month goal. Keep `/recall` running; it costs about 10 minutes a day and keeps everything you've learned alive.

**Final `/exam` (EX9):** a full mock loop: concepts, a live coding task, a system-design question, and a stakeholder explanation of your capstone.

---

## After week 72: staying ahead
| Rhythm | Habit |
|---|---|
| Daily | 10 minutes of `/recall` or Anki |
| Weekly | 1 paper from [Hugging Face Papers](https://huggingface.co/papers) (three-pass method, first pass only unless it matters); 1 newsletter: [The Batch](https://www.deeplearning.ai/the-batch/) or [Ahead of AI](https://magazine.sebastianraschka.com/) |
| Monthly | 1 small build with a new tool or technique; 1 post about it |
| Quarterly | 1 open-source contribution (docs, tests or a fix) to a library you use; teach something at work |
| Yearly | Re-run this course's `/exam`s for your weakest phases; pick a new track |

Teaching is the fastest way to keep learning, and it makes you the person your team relies on for AI. That's what hard to replace looks like.
