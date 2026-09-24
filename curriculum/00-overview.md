# The Ascent: your map

**10 phases · 72 plan-weeks · about 16–18 months at ~10 hours per week · free resources only**

This course starts where you are: you can program in Java and Python, and you know nothing about AI. Each phase is a little harder than the one before it and ends with a project that the Mentor verifies and an exam that unlocks the next phase.

## Why this order: a spiral, not a straight line
The course teaches you to *use* AI early, then goes deeper several times. That gives you early wins (useful at work within weeks) plus the depth that makes you hard to replace.

1. **Use it** (Phases 0–2): understand what AI and LLMs are, then build and deploy an LLM app. Calling an API is easier than linear algebra, so it comes first.
2. **Understand it** (Phases 3–6): the math, classical machine learning, deep learning, and finally how transformers and LLMs work inside, down to building a small GPT yourself.
3. **Engineer it** (Phases 7–8): serious RAG, agents, MCP, evaluation, security, then production engineering (MLOps).
4. **Own it** (Phase 9): a specialization, a capstone that solves a real problem, and career moves.

Ideas come back at a deeper level each time, which is itself a form of spaced repetition:

| Idea | First meeting | Comes back in |
|---|---|---|
| Embeddings | P2: you use them for search | P3 dot products and cosine → P4 as features → P5 learned embeddings → P6 token embeddings → P7 retrieval engineering |
| Gradient descent | P3: the math | P4 inside scikit-learn → P5 backprop by hand (micrograd) → P6 training a GPT, fine-tuning |
| Evaluation | P2: a 20-question test set | P4 cross-validation and metrics → P5 confusion matrices → P6 before/after fine-tuning → P7 LLM-as-judge and agent evals → P8 monitoring |
| Probability | P3 | P4 Naive Bayes and logistic regression → P6 softmax, sampling and temperature |

## The phases

| Phase | Title | Plan weeks | Difficulty | You finish able to... | Badge |
|---|---|---|---|---|---|
| 0 | [Launchpad](phase-0-launchpad.md) | 1–2 | ★☆☆☆☆ | explain AI/ML/LLMs in plain words, use AI tools well, call an LLM from your own code | AI-Literate Developer |
| 1 | [Python & Data Toolkit](phase-1-python-data.md) | 3–7 | ★★☆☆☆ | clean, analyse and visualise real data with NumPy, Pandas and SQL; test your code | Data Wrangler |
| 2 | [LLM App Builder I](phase-2-llm-apps.md) | 8–12 | ★★☆☆☆ | build, evaluate and deploy a RAG chatbot with free APIs | LLM App Builder |
| — | Consolidation week A | 13 | — | review, polish, write about it | — |
| 3 | [Math for ML](phase-3-math.md) | 14–19 | ★★★☆☆ | use vectors, matrices, gradients and probability in NumPy; gradient descent from scratch | Math Mechanic |
| 4 | [Classical Machine Learning](phase-4-classical-ml.md) | 20–27 | ★★★☆☆ | take tabular data to an evaluated, deployed model; compete on Kaggle | ML Practitioner |
| — | Consolidation week B | 28 | — | review, polish, write about it | — |
| 5 | [Deep Learning](phase-5-deep-learning.md) | 29–36 | ★★★★☆ | build backprop from scratch, train CNNs in PyTorch, use transfer learning | Deep Learning Practitioner |
| 6 | [Transformers & LLM Internals](phase-6-transformers-llms.md) | 37–43 | ★★★★★ | build a small GPT, explain training and inference, fine-tune a small LLM with LoRA | LLM Internals Engineer |
| — | Consolidation week C | 44 | — | review, polish, write about it | — |
| 7 | [AI Engineering II: RAG, Agents, MCP, Evals](phase-7-ai-engineering.md) | 45–53 | ★★★★☆ | build secure, evaluated agentic systems with tools and MCP | AI Engineer |
| 8 | [MLOps & Production](phase-8-mlops.md) | 54–59 | ★★★★☆ | ship with Docker, CI/CD, experiment tracking and monitoring | Production AI Engineer |
| — | Consolidation week D | 60 | — | review, polish, write about it | — |
| 9 | [Specialize, Capstone & Career](phase-9-capstone-career.md) | 61–72 | ★★★★★ | go deep in one track, ship a capstone, present a portfolio, interview well | Specialist |

## Milestones you can feel
- **Week 2:** you have called an LLM from your own code, and you can explain AI, ML, deep learning and LLMs to anyone. Useful at work immediately.
- **Week 12:** you have a deployed RAG chatbot with an evaluation set. You can put your hand up for GenAI work at your company.
- **Week 27:** you can take a raw dataset to a deployed, properly evaluated model, and you have a Kaggle leaderboard entry.
- **Week 43:** you understand LLMs from the inside: you built a GPT and fine-tuned a small model.
- **Week 53:** you build agents with tools, MCP and real evals, and you know how they fail and how to secure them.
- **Week 59:** you ship AI systems like a professional: containers, CI/CD, tracking, monitoring.
- **Week 72:** a specialization, a capstone that solves a real problem, a portfolio, and interview readiness.

## A standard week (~10 hours)

| Day | Time | What |
|---|---|---|
| Mon–Thu | 60–75 min | `/today`: reviews (10–15) → lesson (30–40) → `/quiz` (10) → build (10–15) |
| Fri | 20–30 min | light day: `/recall` and Anki, or rest |
| Sat | 2–3 h | build day: the week's `B` task or the phase project |
| Sun | 60–90 min | `/weekly`: cumulative test, reflection, next week's plan |

Each week has 4 lessons (L1–L4) and a weekend build (B). The final week of each phase is mostly project work plus the exam.

**[Consolidation weeks](consolidation-weeks.md)** (13, 28, 44, 60) add no new content. Clear the review backlog and weak spots, redo your lowest-scoring quizzes, polish project READMEs, write one blog post about what you built, and rest. Research on spacing says these weeks are not lost time; they are when a lot of the forgetting gets repaired.

## Pace options (chosen during `/start`, change any time with `/replan`; the tracker measures you against it)

| Pace | Hours/week | Shape | 72 plan-weeks take |
|---|---|---|---|
| Light | ~6 | 3 weekday sessions of 45 min + 2–3 h on the weekend | ~26 months |
| Standard | ~10 | the week above | ~16–18 months |
| Intense | ~15 | 5–6 sessions a week, some days with two lessons | ~12 months |

On Light pace, skip items marked *Optional* or *Deeper*. Never skip reviews, quizzes, projects or exams: they are where the learning actually happens.

## How to read a lesson in the phase files

```
#### P3-W1-L2 · Linear transformations and matrices (~60 min)
- Learn: the main resource (link, minutes or sections)
- Alt: another explanation of the same idea, if the first one doesn't click
- Key concepts: what you must be able to explain; the Mentor quizzes these
- Quiz seeds: sample questions; the Mentor varies them
- Build: a small hands-on task
```

Weekend builds are marked `B`. Each phase ends with a **project** (spec, must-haves, stretch goals) and an **exam** (format and sample tasks).

## What makes you hard to replace, and where you build it

| Pillar | Why it matters | Built in |
|---|---|---|
| Deep fundamentals | You can debug, reason and adapt when tools change, instead of only calling APIs | P3–P6 |
| Shipping end to end | Companies pay for working systems, not notebooks | every project, especially P2, P4, P7, P8 |
| Evaluation and judgment | Anyone can make a demo; few can prove it works and find where it fails | P2 → P4 → P7 → P8 |
| Security and responsibility | Prompt injection, data leaks and bias are real risks companies fear | P2, P4, P7 |
| AI-augmented productivity | You direct coding agents well instead of competing with them | P0, P7, P9 |
| Domain knowledge | Knowing your company's business turns AI skills into solved problems | P9 capstone, weekly career moves |
| Communication and teaching | Explaining AI to stakeholders makes you the person teams rely on | Feynman questions, exam Part C, blog posts, demos |
| Learning speed | The field changes monthly; this system *is* your learning engine | the whole course |
