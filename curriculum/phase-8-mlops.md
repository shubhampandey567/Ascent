# Phase 8 — MLOps & Production

**Plan weeks 54–59 · 6 weeks · Difficulty ★★★★☆ · Badge: Production AI Engineer**

## Why this phase matters
A notebook is not a product. In 2026 postings, 87% of AI-engineer roles want skills beyond GenAI: APIs, Docker, CI/CD, cloud, monitoring. This phase turns you from someone who builds demos into someone who ships systems that keep working: packaged, tested, containerised, deployed automatically, tracked and monitored. Your IT-company experience is a real advantage here; you've seen production systems and incidents.

**Hardware plan:** Docker Desktop is too heavy for 8 GB RAM, so container work runs in **GitHub Codespaces** (120 free core-hours per month) and in **GitHub Actions**. Deployment goes to Render or a Hugging Face Space. See [guides/free-compute.md](../guides/free-compute.md).

## Before you start
- Phases 4 and 7 passed (you have a tabular model and an agent to productionise).
- A GitHub account with Codespaces available.

## You will be able to
- Structure ML/LLM code as a tested, configurable Python package with a FastAPI service.
- Containerise services with Docker and Docker Compose.
- Track experiments, version models and data, and reproduce any result.
- Build CI/CD pipelines with tests and an **eval gate** that blocks bad changes.
- Serve models efficiently; handle rate limits, retries, timeouts and caching.
- Monitor data drift, model quality, LLM behaviour and cost; plan rollbacks.

---

## Week 1 (plan week 54) — Engineering foundations for ML systems

#### P8-W1-L1 · Designing ML systems (~60 min)
- **Learn:** Google's [Rules of Machine Learning](https://developers.google.com/machine-learning/guides/rules-of-ml) (rules 1–20), then [Made With ML](https://madewithml.com/), the product design and systems design lessons.
- **Key concepts:** start without ML when you can; get the pipeline right before the model; define success metrics and constraints first; offline vs online evaluation.
- **Quiz seeds:** Why does Rule #1 say "don't be afraid to launch a product without machine learning"?

#### P8-W1-L2 · From notebook to package (~75 min)
- **Learn:** Made With ML lessons on scripting, logging, styling and pre-commit hooks.
- **Key concepts:** `src/` layout and `pyproject.toml`; configuration files instead of hard-coded values; a CLI (for example with Typer); structured logging; formatters and linters in pre-commit hooks.
- **Quiz seeds:** Why move code out of notebooks for production?

#### P8-W1-L3 · Testing ML systems (~75 min)
- **Learn:** the Made With ML lesson on testing (code, data and models).
- **Key concepts:** unit tests for code; data tests (schema, ranges, nulls); model tests (minimum performance, invariance and directional expectations); tests for LLM apps (golden cases, assertions).
- **Quiz seeds:** Give one invariance test for a sentiment model.

#### P8-W1-L4 · FastAPI in depth (~75 min)
- **Learn:** the [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/): path and query parameters, request bodies, response models, dependencies, error handling, background tasks.
- **Key concepts:** request and response schemas; dependency injection; async endpoints for I/O-bound LLM calls; timeouts; health-check endpoints.
- **Quiz seeds:** When does `async def` help an LLM service, and when doesn't it?

#### P8-W1-B · Weekend build
Refactor Project 4 (or Project 7) into a clean package with tests and a FastAPI service.

---

## Week 2 (plan week 55) — Containers

#### P8-W2-L1 · Docker concepts (~75 min)
- **Learn:** [Docker — Get started](https://docs.docker.com/get-started/), inside a [GitHub Codespace](https://docs.github.com/en/codespaces/quickstart).
- **Key concepts:** images vs containers; layers and caching; the Dockerfile; ports; volumes; why containers make "works on my machine" go away.
- **Quiz seeds:** Why put `COPY requirements.txt` and `pip install` before copying the rest of the code?

#### P8-W2-L2 · Dockerise your service (~75 min)
- **Build:** A Dockerfile for your FastAPI service: slim base image, pinned dependencies, non-root user, `.dockerignore`, a health check. Measure the image size and shrink it.
- **Key concepts:** multi-stage builds; image size vs build time; secrets as environment variables at runtime, never baked into images.

#### P8-W2-L3 · Docker Compose (~60 min)
- **Learn:** the Compose section of [Docker's docs](https://docs.docker.com/get-started/).
- **Build:** Compose your API with a vector database (Qdrant or Chroma) or Postgres, with environment files and named volumes.

#### P8-W2-L4 · Deploy a container for free (~60 min)
- **Learn:** [Render's free tier docs](https://render.com/docs/free).
- **Key concepts:** building from a Dockerfile; environment variables; cold starts on free tiers; logs.

#### P8-W2-B · Weekend
Your containerised service deployed and reachable, with the URL in the README.

---

## Week 3 (plan week 56) — Tracking, versioning, reproducibility

#### P8-W3-L1 · Experiment tracking with MLflow (~75 min)
- **Learn:** the [MLflow docs](https://mlflow.org/docs/latest/) tracking quickstart (runs locally, free).
- **Key concepts:** runs, parameters, metrics and artifacts; comparing runs; the model registry; logging LLM evaluations too.

#### P8-W3-L2 · Weights & Biases (~60 min)
- **Learn:** a module of W&B's free "Effective MLOps: Model Development" from [wandb.ai/site/courses](https://wandb.ai/site/courses/).
- **Key concepts:** hosted dashboards; sweeps for hyperparameter search; reports to share results with a team.

#### P8-W3-L3 · Versioning data and models (~60 min)
- **Learn:** the Made With ML lesson on versioning, then [DVC — Get Started](https://dvc.org/doc/start).
- **Key concepts:** code, data, model and config versions together = reproducibility; data version control; why "which data trained this model?" must have an answer.

#### P8-W3-L4 · Pipelines and orchestration (~60 min)
- **Learn:** the orchestration module of the self-paced [DataTalksClub MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp).
- **Key concepts:** pipelines as code (ingest → validate → train → evaluate → register); scheduling; retries; idempotent steps.

#### P8-W3-B · Weekend
Track every training run of your model in MLflow; register the best one; reproduce it from a clean checkout.

---

## Week 4 (plan week 57) — CI/CD

#### P8-W4-L1 · GitHub Actions (~60 min)
- **Learn:** the [GitHub Actions quickstart](https://docs.github.com/en/actions/get-started/quickstart).
- **Key concepts:** workflows, jobs, steps; triggers (push, pull request); secrets; caching dependencies; free minutes for public repos.

#### P8-W4-L2 · CI for ML and LLM apps (~75 min)
- **Learn:** [DeepLearning.AI — Automated Testing for LLMOps](https://www.deeplearning.ai/courses/automated-testing-llmops) (6 short videos).
- **Key concepts:** lint + unit tests + data checks on every pull request; an **eval gate**: run a small golden set and fail the build if quality drops below a threshold; keeping CI evals cheap.
- **Quiz seeds:** Why run a small eval set on every PR and a large one nightly?

#### P8-W4-L3 · Continuous delivery (~75 min)
- **Learn:** GitHub's docs on publishing Docker images to the free [GitHub Container Registry](https://docs.github.com/en/billing/concepts/product-billing/github-packages).
- **Build:** On merge to `main`: build the image → push to GHCR → deploy (Render deploy hook or a Hugging Face Space).

#### P8-W4-L4 · Cloud concepts without a credit card (~60 min)
- **Learn:** read-only: the core concepts (compute, storage, networking, IAM, serverless vs containers, regions, cost) from any big cloud's free learning pages. AWS appears in about 40% of AI-engineer postings, Azure 30%, GCP 27%.
- **Key concepts:** the shared responsibility model; least-privilege IAM; why surprise cloud bills happen and how to prevent them (budgets, alerts, auto-shutdown). If your employer offers a sandbox, practise there under company rules.

#### P8-W4-B · Weekend
A complete CI pipeline (lint, tests, eval gate) plus CD to your free host.

---

## Week 5 (plan week 58) — Serving, scaling, monitoring

#### P8-W5-L1 · Serving patterns (~60 min)
- **Learn:** [DeepLearning.AI — Efficiently Serving LLMs](https://www.deeplearning.ai/courses/efficiently-serving-llms) (if not done in Phase 6) and [LLMOps](https://www.deeplearning.ai/courses/llmops).
- **Key concepts:** batch vs online inference; latency vs throughput; model size and quantisation for CPU serving; ONNX; queues for slow jobs.

#### P8-W5-L2 · Reliability engineering for AI services (~60 min)
- **Key concepts:** timeouts, retries with back-off and jitter, circuit breakers, rate limiting, caching, fallbacks to a smaller model, idempotency. (Your IT experience applies directly.)
- **Build:** A small load test of your API with [Locust](https://docs.locust.io/en/stable/quickstart.html) (a few users only; free tiers are small). Record p50/p95 latency.

#### P8-W5-L3 · Monitoring ML models (~75 min)
- **Learn:** Evidently's free [ML observability course](https://www.evidentlyai.com/ml-observability-course) (selected modules).
- **Key concepts:** data drift vs concept drift; monitoring without labels; alert thresholds; retraining triggers.
- **Quiz seeds:** Inputs look the same as last month but accuracy dropped. Which kind of drift is this?

#### P8-W5-L4 · Monitoring LLM systems (~60 min)
- **Learn:** your Phase 7 tracing tool ([Langfuse](https://langfuse.com/docs) or [Phoenix](https://github.com/Arize-ai/phoenix)) dashboards and online evaluation features.
- **Key concepts:** online evals on sampled traffic; user feedback signals; cost and token dashboards; incident response and rollback; shadow and A/B deployments.

#### P8-W5-B · Weekend: Project 8 work

---

## Week 6 (plan week 59) — Project 8 and exam
#### P8-W6-L1 to L4 · Project 8 work
#### P8-W6-B · `/submit`, then `/exam`

## Project 8 — "Ship it for real" (`projects/pr8-production/`)
Productionise Project 4 or Project 7.

**Must-haves**
- [ ] A `src/` package with configuration, logging and tests; at least 70% test coverage of the core logic.
- [ ] A Dockerfile following the Week 2 practices; Docker Compose if there's more than one service.
- [ ] GitHub Actions CI: lint + tests + an **eval gate** with a threshold.
- [ ] CD: every merge to `main` deploys to a free host automatically.
- [ ] Experiment tracking (MLflow or W&B) with the deployed model's run linked from the README.
- [ ] Monitoring: an Evidently drift report (tabular model) or Langfuse/Phoenix dashboards with online evals (agent).
- [ ] A load-test result (p50/p95) and a cost estimate per 1,000 requests.
- [ ] A runbook section: how to deploy, roll back, rotate keys, and what to do when an alert fires.

**Stretch:** a canary or shadow deployment; automatic retraining when drift crosses a threshold; a status page.

**Viva focus:** what happens, step by step, when you merge a pull request; how you'd notice and roll back a bad model.

## Exam EX8
- **Part A (concepts):** packaging, testing ML, Docker layers, Compose, tracking and registries, reproducibility, CI eval gates, serving patterns, reliability patterns, drift, LLM monitoring.
- **Part B (live coding, 25 min):** write a GitHub Actions workflow that installs dependencies, runs tests and fails if an eval script scores below a threshold.
- **Part C (stakeholder):** "Explain to your delivery manager why the ML service needs monitoring even though all the tests passed."
- **Part D (judgment):** "A new model version has better offline metrics. The team wants to replace the old model for all users on Friday evening. What do you recommend?"

---

## Optional and deeper
- [Made With ML](https://madewithml.com/) in full.
- [DataTalksClub — MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) (self-paced in 2026, no live cohort).
- W&B free courses: Model CI/CD, CI/CD for ML (GitOps), data validation — [wandb.ai/site/courses](https://wandb.ai/site/courses/).
- [Kubernetes Basics (interactive tutorial)](https://kubernetes.io/docs/tutorials/kubernetes-basics/): run clusters in Codespaces, not on your laptop.
- [Full Stack Deep Learning (2022)](https://fullstackdeeplearning.com/course/2022/): dated but still full of practical wisdom.
