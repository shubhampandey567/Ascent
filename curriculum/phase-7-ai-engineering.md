# Phase 7 — AI Engineering II: RAG, Agents, MCP, Evals

**Plan weeks 45–53 · 9 weeks · Difficulty ★★★★☆ · Badge: AI Engineer**

## Why this phase matters
This is the job. An analysis of about 7,000 "AI Engineer" job postings from February to August 2026 (US, Europe and India) found:
- **Agents** appear in 72% of AI-first roles and **RAG** in 55%; both are now baseline expectations.
- **Evaluation skills** (LLM evals, observability, guardrails) appear in **60%** and are called "the differentiator".
- **MCP** (9.9% → 17.6%) and **LangGraph** (7.4% → 17.2%) were the fastest-rising skills over those six months.
- 87% of roles also want skills beyond GenAI: APIs, cloud, Docker, CI/CD. (That's Phase 8.)

Source: [Alexey Grigorev, AI Engineering Field Guide](https://github.com/alexeygrigorev/ai-engineering-field-guide/blob/main/role/02-skills.md).

So this phase builds serious RAG, agents with tools, your own MCP server, and above all **evaluation and security**: proving a system works, finding where it fails, and keeping it safe.

## Before you start
- Phases 2 and 6 passed (you built RAG v1, and you understand how LLMs work inside).
- Your provider-agnostic `llm.py` from Phase 2, and free API keys (Groq, Gemini; a Cohere trial key for reranking).

## You will be able to
- Build advanced RAG: hybrid search, reranking, query rewriting, contextual chunking, with measured improvements.
- Build agents from scratch (tool-calling loop) and with LangGraph, including human approval steps.
- Build and secure an MCP server, and explain A2A and Agent Skills.
- Engineer context for agents (what goes into the model's window, and when).
- Evaluate LLM systems: error analysis, golden sets, calibrated LLM-as-judge, agent trajectory evals.
- Trace, monitor and cost your system; defend it against prompt injection; add guardrails.
- Direct coding agents professionally: specs, context files, review.

> **AI-assistance policy from here:** coding agents are encouraged. Directing them well is a skill this phase teaches. You must still explain every line in the viva.
>
> **About DeepLearning.AI courses:** videos are free to watch; quizzes, labs and certificates need the paid Pro membership. Build with your free keys instead.

---

## Week 1 (plan week 45) — Advanced RAG

#### P7-W1-L1 · Retrieval that actually works (~75 min)
- **Learn:** [DeepLearning.AI — Retrieval Augmented Generation (RAG)](https://www.deeplearning.ai/courses/retrieval-augmented-generation), the modules on retrieval (keyword search, semantic search, hybrid search).
- **Key concepts:** BM25 keyword search; dense (vector) search; why hybrid search wins on names, codes and acronyms; reciprocal rank fusion.
- **Quiz seeds:** Why does pure vector search miss a query like "error code ORA-00942"? How does reciprocal rank fusion combine two ranked lists?

#### P7-W1-L2 · Chunking and context (~75 min)
- **Learn:** Anthropic's [Introducing Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval), then the abstract and main figure of [Lost in the Middle](https://arxiv.org/abs/2307.03172).
- **Key concepts:** chunk boundaries; adding document context to each chunk; parent–child retrieval; models use the start and end of long contexts better than the middle.
- **Quiz seeds:** Why can a chunk that says "the revenue grew 3%" be useless on its own? What does "lost in the middle" imply for how you order retrieved chunks?

#### P7-W1-L3 · Reranking and query rewriting (~60 min)
- **Learn:** [DeepLearning.AI — Advanced Retrieval for AI with Chroma](https://www.deeplearning.ai/courses/advanced-retrieval-for-ai) (7 short videos).
- **Key concepts:** cross-encoder rerankers (a slower, more accurate second pass); query expansion; multi-query; HyDE (search with a hypothetical answer).
- **Quiz seeds:** Why not use a cross-encoder for the whole search instead of only reranking?

#### P7-W1-L4 · Measuring RAG (~75 min)
- **Learn:** [DeepLearning.AI — Building and Evaluating Advanced RAG](https://www.deeplearning.ai/courses/building-evaluating-advanced-rag) (6 short videos).
- **Key concepts:** retrieval metrics (hit rate, recall@k, MRR); generation metrics (faithfulness or groundedness, answer relevance); the "RAG triad"; comparing variants on the same golden set.
- **Quiz seeds:** Recall@5 went up but answer quality didn't. Where do you look?

#### P7-W1-B · Weekend build
Upgrade your Project 2 RAG: hybrid search + a reranker (local cross-encoder or Cohere's free trial) + your golden set. A before/after table for every change.

---

## Week 2 (plan week 46) — Tool calling and agents from scratch

#### P7-W2-L1 · Workflows vs agents (~60 min)
- **Learn:** Anthropic, [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents).
- **Key concepts:** workflows (fixed code paths) vs agents (the model chooses the steps); prompt chaining, routing, parallelisation, orchestrator–workers, evaluator–optimiser; start simple and add autonomy only when it earns its cost.
- **Quiz seeds:** Give a task where a workflow beats an agent, and one where an agent is needed.

#### P7-W2-L2 · Function calling in depth (~75 min)
- **Learn:** your provider's tool-calling docs (for example [Groq tool use](https://console.groq.com/docs/tool-use)), then [DeepLearning.AI — Function-calling and data extraction with LLMs](https://www.deeplearning.ai/courses/function-calling-and-data-extraction-with-llms) if you skipped it in Phase 2.
- **Key concepts:** tool schemas; the model returns a call, your code runs it and sends back the result; parallel calls; validating arguments; tool errors as information for the model.
- **Quiz seeds:** Why should tool results that contain errors go back to the model instead of crashing?

#### P7-W2-L3 · The agent loop, by hand (~90 min)
- **Learn:** read [Lilian Weng — LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) and the abstract of [ReAct](https://arxiv.org/abs/2210.03629), then write your own loop: think → call tool → observe → repeat → answer.
- **Key concepts:** planning, memory and tool use; ReAct; a maximum number of steps; logging every step (a trace).
- **Build:** An agent in plain Python with 3 tools (for example calculator, file search over your notes, and a weather API), a step limit, and a printed trace.

#### P7-W2-L4 · Designing tools for agents (~60 min)
- **Learn:** Anthropic, [Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents), and Chip Huyen, [Agents](https://huyenchip.com/2025/01/07/agents.html).
- **Key concepts:** tool names and descriptions as prompts; returning concise, meaningful results; error messages that help the model recover; fewer, better tools.
- **Quiz seeds:** Your agent keeps calling the wrong tool. What do you change first?

#### P7-W2-B · Weekend
Harden your from-scratch agent: argument validation, tool errors, a step limit, and a JSON trace log per run.

---

## Week 3 (plan week 47) — Agent frameworks

#### P7-W3-L1 · Agent fundamentals (~75 min)
- **Learn:** [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/unit0/introduction), Unit 1 (free certificate for this unit).
- **Key concepts:** thought–action–observation; tools; messages and special tokens; the agent's system prompt.

#### P7-W3-L2 · Frameworks compared (~75 min)
- **Learn:** Agents Course, Unit 2: the LangGraph section (skim smolagents and LlamaIndex).
- **Key concepts:** what frameworks give you (state, retries, persistence, tracing) and what they cost (abstraction, lock-in); LangGraph's graph of nodes and edges.

#### P7-W3-L3 · LangGraph in depth (~75 min)
- **Learn:** [DeepLearning.AI — AI Agents in LangGraph](https://www.deeplearning.ai/courses/ai-agents-in-langgraph) (9 short videos) or LangChain Academy's free [Introduction to LangGraph](https://academy.langchain.com/courses/intro-to-langgraph); reference: [LangGraph docs](https://langchain-ai.github.io/langgraph/).
- **Key concepts:** state; nodes and edges; conditional routing; checkpoints and persistence; human-in-the-loop interrupts.
- **Quiz seeds:** Why does an agent that takes real actions need persistence and interrupts?

#### P7-W3-L4 · One more SDK, to see the pattern (~60 min)
- **Learn:** the quickstart of one lightweight SDK: [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/), [PydanticAI](https://pydantic.dev/docs/ai/overview/), [smolagents](https://huggingface.co/docs/smolagents/index) or [Google ADK](https://adk.dev/).
- **Key concepts:** the same ideas under different names (agent, tool, handoff, runner); choosing by team and stack, not hype.

#### P7-W3-B · Weekend build
Rebuild your Week 2 agent in LangGraph with a human-approval step before any "write" action. Compare the two versions in 5 lines.

---

## Week 4 (plan week 48) — MCP, protocols and context engineering

#### P7-W4-L1 · MCP fundamentals (~75 min)
- **Learn:** [Hugging Face MCP Course](https://huggingface.co/learn/mcp-course/unit0/introduction), Unit 1 (free certificate), and the [official MCP introduction](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro) (spec version 2026-07-28).
- **Key concepts:** hosts, clients and servers; tools, resources and prompts; stdio vs HTTP transports; why a standard protocol beats one-off integrations.
- **Quiz seeds:** What problem does MCP solve that function calling alone doesn't?

#### P7-W4-L2 · Build an MCP server (~90 min)
- **Learn:** [DeepLearning.AI — MCP: Build Rich-Context AI Apps with Anthropic](https://www.deeplearning.ai/courses/mcp-build-rich-context-ai-apps-with-anthropic) (11 short videos) or Anthropic's free [Introduction to Model Context Protocol](https://anthropic.skilljar.com/introduction-to-model-context-protocol); build with the official [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk).
- **Build:** An MCP server over your own learning tracker: tools like `due_reviews()` and `progress_summary()` (wrapping `tools/tracker.py` and `tools/srs.py`) and `search_notes(query)`. Connect it to your agent client (Antigravity, VS Code or Claude Code) and use it.

#### P7-W4-L3 · Protocol security, A2A and Agent Skills (~75 min)
- **Learn:** the security module of [Microsoft MCP for Beginners](https://github.com/microsoft/mcp-for-beginners); skim [DeepLearning.AI — A2A: The Agent2Agent Protocol](https://www.deeplearning.ai/courses/a2a-the-agent2agent-protocol) and [Agent Skills with Anthropic](https://www.deeplearning.ai/courses/agent-skills-with-anthropic).
- **Key concepts:** tool poisoning and malicious servers; least privilege; authentication; A2A for agent-to-agent communication; Agent Skills as loadable instructions (your mentor's `.agents/skills/` folder is exactly this).
- **Quiz seeds:** Why is installing an unknown MCP server like installing unknown software?

#### P7-W4-L4 · Context engineering (~60 min)
- **Learn:** Anthropic, [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents). Optional: the Hugging Face [Context Course](https://huggingface.co/learn/context-course).
- **Key concepts:** context as a limited budget; just-in-time retrieval vs pre-loading; compaction; structured notes; sub-agents. Then study how your own mentor is built (`AGENTS.md` always loaded, skills on demand, a Python helper for bookkeeping) and critique it.
- **Quiz seeds:** Why does this folder keep `AGENTS.md` short and push detail into skills?

#### P7-W4-B · Weekend
Finish the tracker MCP server: read-only tools plus one write tool behind a confirmation, with tests.

---

## Week 5 (plan week 49) — Evals: the differentiator

#### P7-W5-L1 · Why evals, and error analysis first (~75 min)
- **Learn:** Hamel Husain, [Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/) (all of it) and [A Field Guide to Rapidly Improving AI Products](https://hamel.dev/blog/posts/field-guide/).
- **Key concepts:** look at real traces before writing metrics; categorise failures; unit-test-style assertions for LLM output; evals as the engine of improvement.

#### P7-W5-L2 · LLM-as-judge, done properly (~75 min)
- **Learn:** Hamel Husain, [Using LLM-as-a-Judge](https://hamel.dev/blog/posts/llm-judge/) and his [evals FAQ](https://hamel.dev/blog/posts/evals-faq/).
- **Key concepts:** binary pass/fail criteria beat 1–10 subjective scales; writing a clear judge rubric with few-shot positive and negative edge cases; measuring Cohen's Kappa / agreement rate between the LLM judge and your human labels before trusting it; mitigating judge biases (position bias, verbosity bias, self-enhancement bias, and sycophancy).
- **Quiz seeds:** Your judge agrees with human labels only 60% of the time. What are 3 concrete fixes to calibrate it? Why is binary criteria superior to 1–5 scoring for automated regression gates?

#### P7-W5-L3 · Evaluating agents and trajectories (~75 min)
- **Learn:** [DeepLearning.AI — Evaluating AI Agents](https://www.deeplearning.ai/courses/evaluating-ai-agents) (15 short videos).
- **Key concepts:** final-outcome evals vs trajectory evals (inspecting intermediate tool calls, argument validity, and sequence efficiency); tool-selection precision and recall; loop detection and runaway prevention; reasoning trace audits (did the agent arrive at the right answer via an unsafe or hallucinated shortcut?); tracking task latency, token consumption, and dollar cost per completed mission.
- **Quiz seeds:** Why is final-answer accuracy alone insufficient for evaluating multi-step autonomous agents? What is a trajectory eval, and how do you score whether an agent's tool calls were optimal?

#### P7-W5-L4 · Hands-on eval tooling (~75 min)
- **Learn:** Evidently's free [LLM Evaluations for AI Builders](https://www.evidentlyai.com/llm-evaluations-course) (choose 2–3 code tutorials), or W&B's free "LLM apps: Evaluation" from [wandb.ai/site/courses](https://wandb.ai/site/courses/).
- **Key concepts:** eval datasets as versioned files; running evals in one command; comparing runs; adversarial test cases.

#### P7-W5-B · Weekend build
An eval harness for your RAG + agent: 30+ cases (including adversarial and unanswerable ones), deterministic checks plus a calibrated LLM judge, one command to run, a results table.

---

## Week 6 (plan week 50) — Security, guardrails and observability

#### P7-W6-L1 · The threat model (~75 min)
- **Learn:** [OWASP Top 10 for LLM Applications (2025)](https://genai.owasp.org/llm-top-10/) in full, and skim the [OWASP Top 10 for Agentic Applications](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/).
- **Key concepts:** prompt injection (direct and indirect); sensitive-information disclosure; excessive agency; improper output handling; system-prompt leakage; vector-store weaknesses; unbounded consumption (cost attacks).
- **Quiz seeds:** Your agent reads emails and can send emails. Describe an indirect prompt-injection attack and 3 defences.

#### P7-W6-L2 · Red-team your own app (~75 min)
- **Learn:** [DeepLearning.AI — Red Teaming LLM Applications](https://www.deeplearning.ai/courses/red-teaming-llm-applications) (7 short videos).
- **Build:** Write 15 attack prompts against your Project 7 idea or your RAG app, run them, and record which succeed.

#### P7-W6-L3 · Guardrails (~60 min)
- **Learn:** [DeepLearning.AI — Safe and reliable AI via guardrails](https://www.deeplearning.ai/courses/safe-and-reliable-ai-via-guardrails) (10 short videos).
- **Key concepts:** input and output validation; allow-lists for tools and domains; least privilege; human approval for irreversible actions; defence in depth, because no single guardrail is enough.

#### P7-W6-L4 · Observability and cost (~75 min)
- **Learn:** the [Langfuse docs](https://langfuse.com/docs) (free Hobby cloud, no card) or [Arize Phoenix](https://github.com/Arize-ai/phoenix) (open source, runs locally).
- **Key concepts:** traces and spans; logging prompts, outputs, latency, tokens and cost; dashboards; sampling production traces into your eval set; caching and model routing (a small model first, a big one when needed).
- **Quiz seeds:** Your bill doubled overnight. Which traces do you look at first?

#### P7-W6-B · Weekend
Add tracing, guardrails and your red-team results to your agent.

---

## Week 7 (plan week 51) — Memory, multi-agent systems, and working with coding agents

#### P7-W7-L1 · Agent memory (~60 min)
- **Learn:** [DeepLearning.AI — Agent Memory: Building Memory-Aware Agents](https://www.deeplearning.ai/courses/agent-memory-building-memory-aware-agents) (7 short videos).
- **Key concepts:** short-term (conversation) vs long-term memory; what to store, summarise or forget; privacy of stored memories.

#### P7-W7-L2 · Multi-agent systems (~60 min)
- **Learn:** [Microsoft AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners), lessons 03 (design patterns) and 08 (multi-agent).
- **Key concepts:** orchestrator–worker and hand-off patterns; when multiple agents help (parallel, specialised work) and when they only add cost and failure points.

#### P7-W7-L3 · Directing coding agents professionally (~75 min)
- **Learn:** [DeepLearning.AI — Spec-Driven Development with Coding Agents](https://www.deeplearning.ai/courses/spec-driven-development-with-coding-agents) or [Claude Code: A Highly Agentic Coding Assistant](https://www.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant); skim [AI Code Review](https://www.deeplearning.ai/courses/ai-code-review).
- **Key concepts:** write the spec first; give agents context files (`AGENTS.md`); small, reviewable steps; tests as guardrails; reviewing AI pull requests like a senior engineer.

#### P7-W7-L4 · Project 7 design doc (~75 min)
- **Build:** A 1–2 page design doc: problem and users, architecture diagram, tools and their permissions, data, eval plan, threat model, cost estimate, what's out of scope. The Mentor reviews it before you build.

#### P7-W7-B · Weekend: start building Project 7

---

## Weeks 8–9 (plan weeks 52–53) — Project 7 and exam
#### P7-W8-L1 to L4 · Project 7: build and evaluate
#### P7-W8-B · Weekend: Project 7 work
#### P7-W9-L1 to L4 · Project 7: harden and document
#### P7-W9-B · Weekend: `/submit`, then `/exam`

## Project 7 — "An agentic assistant for a real workflow" (`projects/pr7-agent/`)
Pick a workflow you understand. Ideas:
- **IT Support Copilot:** answers from runbooks (advanced RAG with citations), looks up tickets through your MCP server over a SQLite database of *synthetic* tickets, drafts a resolution, and needs human approval before "closing" a ticket.
- **Job-hunt agent:** matches your profile to public job posts and drafts tailored notes, with human approval before anything is sent.
- **Personal finance agent:** analyses a synthetic bank-statement CSV and answers questions, with strict tool permissions.

**Must-haves**
- [ ] An agent (LangGraph, or another framework with a written justification) with at least 3 tools, at least one served by **your own MCP server**.
- [ ] Human approval for every action that writes or sends anything.
- [ ] An eval suite of 30+ cases, including adversarial and prompt-injection cases, with deterministic checks and a calibrated LLM judge (agreement with your labels reported); one command runs it.
- [ ] Tracing (Langfuse or Phoenix), plus cost and latency per task reported.
- [ ] Guardrails and a short threat model based on the OWASP lists; red-team results included.
- [ ] README: architecture diagram, how to run, eval results, known failure modes, cost estimate.
- [ ] A deployed demo, or a recorded demo video if hosting is blocked.
- [ ] Only public or synthetic data. Never employer data.

**Stretch:** memory across sessions; a second agent for review (evaluator–optimiser); an A2A endpoint; semantic caching.

**Viva focus:** walk through one real trace; defend one design decision with eval numbers; explain how an attacker would try to break it.

## Exam EX7
- **Part A (concepts):** hybrid search, reranking, chunking, agent patterns, tool design, MCP, context engineering, LLM-as-judge, agent evals, OWASP risks, observability.
- **Part B (live coding, 25 min):** add a new tool to your agent (or MCP server) with argument validation and a test, then add 3 eval cases for it.
- **Part C (stakeholder):** "The business wants the support agent to close tickets automatically. How do you respond, and what would you need to see first?"
- **Part D (judgment):** "Your LLM judge says answer quality improved from 78% to 91% after a prompt change. Do you believe it?"

---

## Optional and deeper
- [DeepLearning.AI — Agentic AI (Andrew Ng)](https://www.deeplearning.ai/courses/agentic-ai): 31 video lessons on agent design patterns.
- [UC Berkeley Agentic AI MOOC (Fall 2025)](https://agenticai-learning.org/f25): advanced lectures from industry leaders.
- [Kaggle/Google — 5-Day AI Agents Intensive](https://www.kaggle.com/learn-guide/5-day-agents) and the [Vibe Coding edition](https://www.kaggle.com/learn-guide/5-day-agents-vibecoding): whitepapers and codelabs, self-paced.
- [Microsoft AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners) (all 18 lessons) and [MCP for Beginners](https://github.com/microsoft/mcp-for-beginners).
- [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/unit0/introduction): Units 3–4 and the bonus units for the completion certificate.
- [DataTalksClub — LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp): agentic RAG, evaluation and monitoring modules.
- Readings: [Eugene Yan — Patterns for Building LLM-based Systems](https://eugeneyan.com/writing/llm-patterns/), [What We've Learned From A Year of Building with LLMs](https://applied-llms.org/), [OpenAI — A practical guide to building agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf), Chip Huyen's [Building A Generative AI Platform](https://huyenchip.com/2024/07/25/genai-platform.html).
- Other SDKs worth knowing: [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview), [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/) (successor to AutoGen and Semantic Kernel), [CrewAI](https://docs.crewai.com/).
