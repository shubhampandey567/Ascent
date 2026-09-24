# Zero budget AI learning path

_Research summary behind the curriculum in this repository. Researched 24 September 2026. The full notes, with every source and caveat, are in [notes/](notes/). The research assumed a typical first learner: a fresh IT graduate in India with basic Java/Python, a ~8 GB laptop without an NVIDIA GPU, and no budget. Facts date quickly; see [CONTRIBUTING.md](../../../CONTRIBUTING.md) to update them._

## Question
How should a fresh IT graduate (basic Java/Python, no AI knowledge, anxious about AI, HP 14 laptop with ~8 GB RAM, zero budget) become a strong, hard-to-replace AI engineer, with an AI agent as mentor and a learning design that fights forgetting?

## Key findings and how they shaped the design

### 1. The job market: the door narrowed for routine juniors, and widened for people who build with AI
- Employment of 22–25-year-olds in the most AI-exposed US jobs is about 19% below trend, through fewer hires rather than layoffs, while AI-*augmented* roles grow ([Stanford Digital Economy Lab, Aug 2026](https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf)).
- Indian IT still hires freshers but with a higher bar: employers want "AI fluency, applied problem-solving, and hands-on project experience", and "AI Application Developer" is the most in-demand fresher role ([TeamLease EdTech H2 2026](https://www.thehansindia.com/hans/education-careers/fresher-hiring-outlook-improves-to-75-in-hy2-2026-teamlease-edtech-report-finds-1108625)). AI/ML postings rose 31% year on year in August 2026 ([Naukri JobSpeak](https://www.latestly.com/agency-news/business-news-aiml-hiring-rises-31-pc-yoy-in-august-gcc-recruitment-grows-10-pc-naukri-jobspeak-7594785.html)).
- AI Engineer is the #1 fastest-growing job in the US and #2 in India ([LinkedIn 2026](https://www.linkedin.com/pulse/linkedin-jobs-rise-2026-25-fastest-growing-india-jrtnc)); PwC measures a 62% wage premium for AI skills.
- In ~7,000 AI-engineer postings (Feb–Aug 2026), agents and RAG are baseline, **evaluation skills (60%) are the differentiator**, MCP and LangGraph rose fastest, fine-tuning is a primary duty in under 4%, and 87% of roles want full-stack skills (APIs, Docker, CI/CD, cloud) ([AI Engineering Field Guide](https://github.com/alexeygrigorev/ai-engineering-field-guide/blob/main/role/02-skills.md)).

**Design consequences:** an early LLM-app phase (Phase 2) for job relevance and confidence; deep fundamentals (Phases 3–6) for durability; evals, security and MCP weighted heavily in Phase 7; a full production phase (Phase 8); fine-tuning kept to one strong project. A calm, sourced explainer for the learner's anxiety: `guides/why-this-path.md`.

### 2. Learning science: retrieval, spacing and hint-based AI tutoring
- Students who reread lost 52% of what they could recall within a week; students who tested themselves lost 14% ([Roediger & Karpicke 2006](https://journals.sagepub.com/doi/10.1111/j.1467-9280.2006.01693.x)). Practice testing and spaced practice are the only two "high utility" techniques in the classic review ([Dunlosky et al. 2013](https://doi.org/10.1177/1529100612453266)).
- Quizzes inside online lectures halved mind-wandering and lifted final scores from 68% to 90% ([Szpunar et al. 2013](https://www.pnas.org/doi/10.1073/pnas.1221764110)); fluent videos create an illusion of learning ([Carpenter et al. 2013](https://pubmed.ncbi.nlm.nih.gov/23645413/)).
- Recalling an item once in each of 3 spaced sessions gave more than twice the recall of 3 correct recalls in one session ([Rawson & Dunlosky 2022](https://journals.sagepub.com/doi/full/10.1177/09637214221100484)).
- Unrestricted GPT-4 raised practice scores 48% but cut exam scores 17%; a hint-based tutor avoided the harm ([Bastani et al., PNAS 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12232635/)). Junior engineers who delegated to AI scored below 40% on comprehension; those who asked conceptual questions scored 65%+ ([Anthropic, Jan 2026](https://www.anthropic.com/research/AI-assistance-coding-skills)).

**Design consequences:** closed-book `/quiz` after every lesson with prequestions and chunked viewing; a spaced-repetition scheduler (`tools/srs.py`, modified SM-2, tested); a 3-session mastery rule for weak spots; weekly AI-off checks with a 70% consolidation gate; a mentor that retrieves first and gives hints, never answers; an AI-assistance policy that loosens only after the fundamentals.

### 3. The mentor tooling in 2026
- Google Antigravity is GA with a free Individual plan (weekly quota, numbers unpublished). Its workspace config moved to `.agents/`; **workflows retire on 1 Nov 2026** in favour of Agent Skills in `.agents/skills/<name>/SKILL.md`; it reads a root `AGENTS.md`, and truncates rule files above 24,000 bytes ([Antigravity docs](https://antigravity.google/docs/rules)). The desktop app is memory-hungry on 8 GB; the `agy` CLI is lighter.
- Claude Code has no free tier (Pro ≈ ₹2,000/month in India); it reads `.claude/skills/` and imports `AGENTS.md` via `CLAUDE.md`.
- Gemini CLI's free tier for personal accounts ended on 18 June 2026 (replaced by the Antigravity CLI).

**Design consequences:** one lean `AGENTS.md` (8.5 KB) as the mentor's constitution; 12 commands as portable Agent Skills mirrored for Claude Code; deterministic bookkeeping in Python so the model spends quota on teaching; a "Plan B" that keeps the system working when the free quota runs out.

### 4. Free compute and APIs changed a lot in 2026
- Kaggle: 30 GPU hours/week (P100 or 2×T4), 30 GB RAM CPU sessions ([docs](https://www.kaggle.com/docs/efficient-gpu-usage)). Colab: no published quota, 12-hour sessions, no web hosting.
- **GitHub Models was retired on 30 July 2026.** **Hugging Face Spaces** now needs a paid plan for CPU Gradio/Docker Spaces; free accounts get 2 ZeroGPU Spaces. Gemini's free tier no longer publishes limits (reported ~20 requests/day for the newest Flash). **Groq** offers 1,000 requests/day per model free (gpt-oss, Qwen), and removed its Llama models in August 2026.
- Big-cloud free tiers all require a card.

**Design consequences:** a provider-agnostic `llm.py` pattern taught in Phases 0 and 2; Groq as the default free API; Streamlit Community Cloud and Render for hosting; Codespaces for Docker; `guides/free-compute.md` lists what works without a card.

### 5. Free courses: what's current
- All ~150 YouTube links used in the curriculum were verified on 24 Sept 2026 against their real titles and channels.
- Coursera replaced free audit with a first-module "Preview" in mid-2025; Financial Aid still exists (about 15 days, per course). DeepLearning.AI videos remain free, but quizzes, labs and certificates became paid "Pro".
- New and useful: Karpathy's microgpt (a whole GPT in 200 lines of pure Python, runs on a laptop CPU), 3Blue1Brown's 2026 entropy/cross-entropy videos, Stanford CS336 (Spring 2026) and CME295, MIT Missing Semester 2026 (with an "Agentic Coding" lecture), Hugging Face's Context Course, ML Zoomcamp 2026 (started 14 Sept 2026).

## Limits of this research
- Antigravity's free quota is unpublished; real usage limits must be observed.
- Two research threads were cut short by rate limits: the section on running local LLMs on a CPU-only 8 GB laptop was written from general knowledge (the learner measures it in Phase 6), and some Kaggle course pages could only be confirmed through search indexes because Kaggle blocks automated fetches.
- Labour-market causality is unproven; some economists find weak or no AI effect so far.
- The weekly protocol combines well-supported components, but no study has tested the full combination; its numbers (session lengths, question mix, thresholds) are sensible defaults to tune from the learner's own data.
