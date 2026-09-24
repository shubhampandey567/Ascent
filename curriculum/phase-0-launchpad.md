# Phase 0 — Launchpad

**Plan weeks 1–2 · 2 weeks · Difficulty ★☆☆☆☆ · Badge: AI-Literate Developer**

## Why this phase matters
Before learning AI, set up the machine that will do the learning: the habits, the tools and this mentor system. Then get a clear, honest picture of what AI is and isn't, and finish with a real win: your own code talking to a large language model. Anxiety about AI shrinks fast once you've seen how it works and made it do something useful.

## Before you start
Nothing. This phase assumes zero AI knowledge. You need a laptop, internet, and the setup in `README.md` → "Quick start" (the Mentor walks you through the free accounts during `/start`).

## You will be able to
- Explain how this learning system works and why (retrieval, spacing, building).
- Explain AI, machine learning, deep learning, generative AI, LLMs and agents in plain words.
- Describe how an LLM is made and why it sometimes makes things up.
- Use chat assistants and coding agents well, and safely, at work.
- Call an LLM from your own Python code, with the API key stored safely.

---

## Week 1 (plan week 1) — Learn how to learn, set up, and meet AI

#### P0-W1-L1 · How learning works (~60 min)
- **Learn:** [Barbara Oakley — Learning how to learn (TEDx)](https://www.youtube.com/watch?v=O96fE1E-rf8) (17 min), then read [guides/how-to-learn.md](../guides/how-to-learn.md).
- **Alt / deeper:** [Coursera — Learning How to Learn](https://www.coursera.org/learn/learning-how-to-learn) (free, 4 modules). A good background course for your first month.
- **Key concepts:** focused vs diffuse thinking; chunking; the illusion of competence (re-watching feels like learning but isn't); retrieval practice; spacing; interleaving; sleep; procrastination and the Pomodoro technique.
- **Quiz seeds:** Why does re-watching a video feel effective even when it isn't? When is diffuse thinking useful? Why do reviews come back after 1, 3 and 8 days instead of all on one day?
- **Build:** Write your "After ___, I will open the mentor and type /today" plan in `tracker/profile.md`. Block your study times in your phone calendar.

#### P0-W1-L2 · Your workshop: shell, Python, Git, secrets (~75 min)
- **Learn:** follow `README.md` → "Quick start" (whatever is left after `/start`), then watch the first half of [MIT Missing Semester 2026 — Lecture 1: Course Overview + Introduction to the Shell](https://www.youtube.com/watch?v=MSgoeuMqUmU).
- **Alt:** [Corey Schafer — Git Tutorial for Beginners: Command-Line Fundamentals](https://www.youtube.com/watch?v=HVsySz-h9r4)
- **Key concepts:** terminal and shell; paths; environment variables and `PATH`; Python virtual environments (`python -m venv .venv`) and `pip`; `git init/add/commit/push`; why API keys live in `.env` and never in code.
- **Quiz seeds:** What does `PATH` do, and why does "python is not recognized" happen? What is the difference between `git commit` and `git push`? Why must `.env` be in `.gitignore`?
- **Build:** Push this folder to a **private** GitHub repository. Run `python tools/tracker.py status` and see it work.

#### P0-W1-L3 · What AI actually is (~60 min)
- **Learn:** [Elements of AI — Introduction to AI](https://course.elementsofai.com/), chapter 1 "What is AI?" (free, no maths or code; do the exercises).
- **Alt:** [MIT 6.S191 (2026) — Introduction to Deep Learning](https://www.youtube.com/watch?v=II4giR4vOOo), first 20 minutes.
- **Key concepts:** AI vs machine learning vs deep learning vs generative AI; narrow AI vs general AI; "AI" as a moving target; machine learning = learning patterns from examples instead of hand-written rules; supervised, unsupervised and reinforcement learning (names only for now).
- **Quiz seeds:** Give one example each of rule-based software and machine learning from apps you use. Why is "AI" hard to define? Where does ChatGPT sit in the AI → ML → DL → LLM picture?
- **Build:** In `notes/P0/`, draw your "AI map": nested boxes AI ⊃ ML ⊃ deep learning ⊃ LLMs, with two real examples in each.

#### P0-W1-L4 · How LLMs work: the short and the long version, part 1 (~75 min)
- **Learn:** [3Blue1Brown — Large Language Models explained briefly](https://www.youtube.com/watch?v=LPZh9BOjkQs) (7 min), then [Karpathy — Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g), **first ~30 minutes**.
- **Key concepts:** an LLM predicts the next token, over and over; parameters ("two files": weights + code); pretraining on internet text as a kind of compression; base model vs assistant; fine-tuning and human feedback turn a document-completer into a helpful assistant; why hallucinations happen.
- **Quiz seeds:** What's in the "two files" of an LLM? Why can an LLM state false facts confidently? What's the difference between a base model and an assistant model?
- **Build:** Ask the same 3 questions (one factual, one reasoning, one about a recent event) to two free chatbots. Record where they differ or are wrong.

#### P0-W1-B · Weekend
Read [guides/why-this-path.md](../guides/why-this-path.md). Rewrite your "AI map" note from memory, then compare with the original. Do your first `/weekly`.

---

## Week 2 (plan week 2) — Use AI well, then build with it

#### P0-W2-L1 · LLMs part 2: tools, the future, and security (~60 min)
- **Learn:** [Karpathy — Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g), **~30 min to the end**.
- **Key concepts:** tool use (browser, calculator, code); multimodality; "System 1 vs System 2" thinking; the "LLM as an operating system" analogy; jailbreaks; **prompt injection**; data poisoning.
- **Quiz seeds:** What is prompt injection, and why is it dangerous for an app that reads your emails? How is a jailbreak different from a prompt injection?
- **Build:** Write 3 realistic prompt-injection examples from a workplace (for example hidden text inside a résumé PDF) and one defence for each.

#### P0-W2-L2 · Using chat assistants like a pro (~75 min)
- **Learn:** [Karpathy — How I use LLMs](https://www.youtube.com/watch?v=EWvNQjAaOHw): watch the parts on the context window, "thinking" models, search, deep research, file uploads and code execution (about the first hour; the chapter list helps).
- **Key concepts:** the context window as working memory (start a new chat for a new topic); thinking vs non-thinking models; when to use search; uploading documents; checking answers instead of trusting them; **never paste confidential company data into free tools**.
- **Quiz seeds:** Why start a new chat for an unrelated question? When is a "thinking" model worth the wait? How would you verify an LLM's answer about a Java library method?
- **Build:** Take a confusing piece of *public* code (open-source, not from work). Ask a chatbot to explain it, then verify one claim by running the code.

#### P0-W2-L3 · The AI-augmented developer (~75 min)
- **Learn:** [MIT Missing Semester 2026 — Agentic Coding](https://www.youtube.com/watch?v=sTdz6PZoAnw), then the first lessons of [Anthropic Academy — AI Fluency: Framework and Foundations](https://academy.claude.com/) (free).
- **Key concepts:** coding agents read files and run commands on your machine; the loop *specify → plan → review → test*; context files such as `AGENTS.md` (your mentor is built this way); reviewing AI output line by line; approving commands; **learning mode vs work mode**.
- **Quiz seeds:** Why does this course restrict AI-written code in the first phases? Name three things to check before accepting an AI-written function. What does `AGENTS.md` do in this folder?
- **Build:** Read this folder's `AGENTS.md` and one skill in `.agents/skills/`. In `notes/P0/`, explain in 6 sentences how your mentor works.

#### P0-W2-L4 · Your first LLM API call (~90 min)
- **Learn:** the "Free LLM APIs" section of [guides/free-compute.md](../guides/free-compute.md), then the [Groq quickstart](https://console.groq.com/docs/quickstart) and the [Gemini API quickstart](https://ai.google.dev/gemini-api/docs/quickstart).
- **Key concepts:** API keys; `.env` files with `python-dotenv`; messages and roles (system, user, assistant); model ids; temperature; tokens and rate limits; HTTP errors (401 unauthorized, 429 too many requests) and retrying with back-off; OpenAI-compatible endpoints (one client, many providers).
- **Quiz seeds:** What does the system message do? What should your code do when it receives HTTP 429? Why write provider-agnostic code when using free tiers?
- **Build:** A script that sends a prompt to Groq and prints the answer and the token usage. Then change only `base_url`, `api_key` and `model` to call Gemini's [OpenAI-compatible endpoint](https://ai.google.dev/gemini-api/docs/openai).

#### P0-W2-B · Weekend
Project 0 (below), then `/submit` and `/exam`.

---

## Project 0 — "Error Explainer" CLI (`projects/pr0-error-explainer/`)
A command-line tool for your day job: give it a Python or Java stack trace or error message, and it explains in plain English (1) what went wrong, (2) the likely causes, and (3) what to check first, using a free LLM API.

**Must-haves**
- [ ] Reads the error from a file argument or from standard input: `python explain.py trace.txt` or `type trace.txt | python explain.py`.
- [ ] The API key is loaded from `.env`; `.env.example` is provided; `.env` is gitignored.
- [ ] Your system prompt lives in a separate file (`prompt.md`) so you can improve it without touching code.
- [ ] Friendly errors for a missing key, network failure and rate limit (429), with one retry after a short wait.
- [ ] A `--provider groq|gemini|ollama` flag that switches `base_url`, key and model.
- [ ] README: what it does, setup, 3 real example runs (input and output), and limitations (it can be wrong; never paste company secrets).
- [ ] You wrote the code yourself (AI-assistance policy for Phases 0–4).

**Stretch:** stream the answer token by token; `--lang hinglish`; print the token count and what the call would cost on a paid tier.

**Viva focus:** what happens between your script and the API; why `.env`; what you do when the model is wrong.

## Exam EX0 (30–45 min, lighter than later exams)
- **Part A (concepts):** AI vs ML vs DL vs LLMs; how LLMs are trained; hallucination; prompt injection; retrieval practice and spacing.
- **Part B (live coding, 15 min):** add a `--level beginner|expert` flag to your Error Explainer that changes the system prompt.
- **Part C (stakeholder):** "Your manager asks: can we just use ChatGPT to reply to customer emails automatically?"
- **Part D (judgment):** "A colleague pastes a client's database export into a free chatbot to 'analyse it quickly'. What's wrong, and what would you do?"

---

## Optional and deeper
- [Elements of AI](https://www.elementsofai.com/): the full free "Introduction to AI" course (6 chapters).
- [Karpathy — Software Is Changing (Again)](https://www.youtube.com/watch?v=LCEmiRjPEtQ): the "Software 3.0" view of programming with LLMs.
- [Harvard CS50's Introduction to AI with Python](https://cs50.harvard.edu/ai/): classic AI (search, logic, probability) with projects; [lecture playlist](https://www.youtube.com/playlist?list=PLhQjrBD2T381PopUTYtMSstgk-hsTGkVm).
- [MIT Missing Semester 2026](https://missing.csail.mit.edu/): the rest of the lectures (command line, tools, debugging).
- AI For Everyone (Andrew Ng) on [Coursera](https://www.coursera.org/learn/ai-for-everyone): only the first module is free ("Preview"); the full course needs payment or Coursera Financial Aid.
- **Regional-language options (Hindi):** [CampusX — 100 Days of Machine Learning](https://www.youtube.com/playlist?list=PLKnIA16_Rmvbr7zKYQuBfsVkjoLcJgxHH), days 1–3 (what ML is; AI vs ML vs DL).
