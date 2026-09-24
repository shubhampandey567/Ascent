# Advanced AI Learning Path: Free Resources for NLP/Transformers, LLM Internals, Prompt/Context Engineering, RAG, Agents, MCP, Evals, Fine-tuning, MLOps/LLMOps, and AI-Engineering Job Skills (verified 2026-09-24)

> Verification method (applies to every item below unless flagged): YouTube video/playlist IDs were checked live via the YouTube oEmbed endpoint on 2026-09-24 (title + channel returned). Web URLs were checked with `curl -L` (HTTP 200 + final redirect target recorded). GitHub repo stats (stars, last push, archived flag) come from the authenticated GitHub REST API on 2026-09-24. arXiv titles/dates came from arxiv.org/abs + export.arxiv.org API. DeepLearning.AI course metadata (publish date, "Free" offer flag, level, video-lesson count) was parsed from each course page's schema.org JSON-LD and visible text on 2026-09-24. "UNVERIFIED" marks anything not confirmed this way.
> Learner constraints assumed: fresh IT grad, zero budget, ~8 GB RAM laptop with no NVIDIA GPU, likely in India -> favour browser/Colab/Kaggle-runnable material and free API tiers.

## Q1. Andrej Karpathy: exact URLs, and what is new in 2025-2026

### Takeaway
All of the classic Karpathy videos are still up and their IDs check out. The new material from 2025-2026 is the nanochat repo (Oct 2025, still actively updated in Sept 2026), the microgpt single-file GPT (blog post of 12 Feb 2026), and a few talks. LLM101n has not shipped: its GitHub repo is archived, and Karpathy joined Anthropic's pre-training team on 19 May 2026. Reports describe that move as putting Eureka Labs on hold, not closing it.

### Cited Findings
**Verified video URLs (oEmbed title | channel):** Titles and channels were verified live. Upload months/years in parentheses come from background knowledge and were NOT re-verified in this session; treat them as approximate.
- "[1hr Talk] Intro to Large Language Models" (Andrej Karpathy, Nov 2023, ~1 h; general audience, no prerequisites). Best first-week overview. — [YouTube](https://www.youtube.com/watch?v=zjkBMFhNj_g)
- "Deep Dive into LLMs like ChatGPT" (Andrej Karpathy, Feb 2025, 3h31m per Karpathy's announcement). Karpathy calls it a general-audience deep dive that "covers the full training stack of how the models are developed". — [YouTube](https://www.youtube.com/watch?v=7xTGNNLPyMI); length per [Karpathy on X](https://x.com/karpathy/status/1887211193099825254)
- "How I use LLMs" (Andrej Karpathy, Feb 2025). Practical tour of LLM apps and features. — [YouTube](https://www.youtube.com/watch?v=EWvNQjAaOHw)
- "Let's build GPT: from scratch, in code, spelled out." (Andrej Karpathy, Jan 2023). Needs Python and basic PyTorch; runs on free Colab. — [YouTube](https://www.youtube.com/watch?v=kCc8FmEb1nY); code [karpathy/ng-video-lecture](https://github.com/karpathy/ng-video-lecture) (4,986 stars, last push 2024-01-31)
- "Let's build the GPT Tokenizer" (Andrej Karpathy, Feb 2024). — [YouTube](https://www.youtube.com/watch?v=zduSFxRajkE); code [karpathy/minbpe](https://github.com/karpathy/minbpe) (10,739 stars, last push 2024-07-01)
- "Let's reproduce GPT-2 (124M)" (Andrej Karpathy, Jun 2024). Full training run needs rented GPUs; the learner can watch and run small-scale pieces on Colab. — [YouTube](https://www.youtube.com/watch?v=l8pRSuU81PU); code [karpathy/build-nanogpt](https://github.com/karpathy/build-nanogpt) (5,522 stars, last push 2024-08-13)
- "State of GPT | BRK216HFS" (Microsoft Developer channel, Microsoft Build 2023). — [YouTube](https://www.youtube.com/watch?v=bZQun8Y4L2A)
- "Andrej Karpathy: Software Is Changing (Again)" (Y Combinator channel, AI Startup School, June 2025). The "Software 3.0" talk. — [YouTube](https://www.youtube.com/watch?v=LCEmiRjPEtQ)
- "The spelled-out intro to neural networks and backpropagation: building micrograd" (Andrej Karpathy). Prerequisite for the GPT videos. — [YouTube](https://www.youtube.com/watch?v=VMj-3S1tku0)
- "Neural Networks: Zero to Hero" playlist (Andrej Karpathy). — [YouTube playlist](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ)
- Dwarkesh Patel interview, "Andrej Karpathy — 'We're summoning ghosts, not building animals'" (Dwarkesh Patel channel, Oct 2025). Optional listening on the outlook for agents and AGI. — [YouTube](https://www.youtube.com/watch?v=lXUZvyajciY)

**Repos (GitHub API, 2026-09-24):**
- nanoGPT: 63,345 stars, last push 2025-11-12, not archived. — [GitHub](https://github.com/karpathy/nanoGPT)
- nanochat ("The best ChatGPT that $100 can buy"): 58,250 stars, last push 2026-09-07, not archived. — [GitHub](https://github.com/karpathy/nanochat)
- The nanochat README describes it as "the simplest experimental harness for training LLMs" on a single 8xH100 node. The speedrun now takes about 1.5 h, costs "only $48 (~2 hours of 8XH100 GPU node)" or "closer to ~$15" on spot instances, and has a CPU/MPS example script (runs/runcpu.sh) that "will not get strong results". The 2026 leaderboard cut time-to-GPT-2 from 3.04 h (29 Jan) to 1.65 h (14 Mar) and added FP8 and the NVIDIA ClimbMix dataset. For this learner it is a code-reading project, not something to train. — [GitHub nanochat README](https://github.com/karpathy/nanochat)
- llm.c (raw C/CUDA): 31,050 stars, last push 2025-06-26. — [GitHub](https://github.com/karpathy/llm.c)
- micrograd: 17,638 stars, last push 2026-08-03. — [GitHub](https://github.com/karpathy/micrograd)
- LLM101n ("Let's build a Storyteller"): **ARCHIVED**, 37,488 stars, last push 2024-08-01. — [GitHub](https://github.com/karpathy/LLM101n)

**New in 2025-2026:**
- microgpt: blog post dated 12 Feb 2026. It is "a single file of 200 lines of pure Python with no dependencies that trains and inferences a GPT", with its own tokenizer, autograd, Adam and training/inference loops, and only os/math/random imports. It runs on any laptop CPU, which makes it ideal for this learner. — [karpathy.github.io/2026/02/12/microgpt/](https://karpathy.github.io/2026/02/12/microgpt/); [gist](https://gist.github.com/karpathy/8627fe009c40f57531cb18360106ce95); [karpathy.ai/microgpt.html](https://karpathy.ai/microgpt.html)
- Karpathy published a written "Sequoia Ascent 2026 summary" on his bearblog. — [karpathy.bearblog.dev](https://karpathy.bearblog.dev/sequoia-ascent-2026/)
- Karpathy joined Anthropic's pre-training team on 19 May 2026. — [TechCrunch](https://techcrunch.com/2026/05/19/openai-co-founder-andrej-karpathy-joins-anthropics-pre-training-team/); [Quartz](https://qz.com/andrej-karpathy-joins-anthropic-pretraining-team-051926)
- The eurekalabs.ai homepage still says "Today, we are heads down building LLM101n", with no release date or pricing. — [eurekalabs.ai](https://eurekalabs.ai/)

### Inferences
- Suggested order: Intro to LLMs -> micrograd -> Let's build GPT -> Tokenizer -> microgpt (read the whole file) -> Deep Dive into LLMs -> How I use LLMs -> Software Is Changing (Again). Treat "Reproduce GPT-2" and nanochat as stretch reading. All of this is free, and apart from optional Colab runs it needs no GPU.
- LLM101n should not appear in the curriculum as an available course. Given the archived repo and Karpathy's move to Anthropic, it is unlikely to ship soon.

### Gaps
- No new long-form Karpathy teaching video from 2026 was found. YouTube hits for "Karpathy 2026" were third-party commentary (for example "Rob Shocks" and "Dr. Know-it-all" channels, verified via oEmbed), not Karpathy uploads. The Sequoia Ascent 2026 fireside-chat video URL was not verified.

## Q2. Visual explainers and university lecture series (3Blue1Brown, Jay Alammar, Umar Jamil, Stanford CS224N / CS336 / CS25 / CME295)

### Takeaway
Every core explainer is live. The newest complete university series are CS336 Spring 2026 (Language Modeling from Scratch), CME295 Autumn 2025 (Transformers & LLMs), and CS25 V6. CS224N is running Winter 2026 but still points students to the Spring 2024 YouTube playlist.

### Cited Findings
**3Blue1Brown (oEmbed-verified):**
- "Large Language Models explained briefly" (about 8 min). — [YouTube](https://www.youtube.com/watch?v=LPZh9BOjkQs)
- "Transformers, the tech behind LLMs | Deep Learning Chapter 5" (this ID was formerly titled "But what is a GPT?"). — [YouTube](https://www.youtube.com/watch?v=wjZofJX0v4M)
- "Attention in transformers, step-by-step | Deep Learning Chapter 6". — [YouTube](https://www.youtube.com/watch?v=eMlx5fFNoYc)
- "How might LLMs store facts | Deep Learning Chapter 7". — [YouTube](https://www.youtube.com/watch?v=9-Jl0dxWQs8)
- "But how do AI images and videos actually work? | Guest video by Welch Labs" (diffusion guest video). — [YouTube](https://www.youtube.com/watch?v=iv-5mZ_9CPY)
- "But what is a neural network? | Deep learning chapter 1". — [YouTube](https://www.youtube.com/watch?v=aircAruvnKk); full "Neural networks" playlist — [YouTube playlist](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)
- The 3b1b.com topic page redirects from /topics/neural-networks to /?topic=neural-networks and returns 200. — [3blue1brown.com](https://www.3blue1brown.com/?topic=neural-networks)

**Jay Alammar (HTTP 200):**
- The Illustrated Transformer. — [jalammar.github.io](https://jalammar.github.io/illustrated-transformer/)
- The Illustrated GPT-2. — [jalammar.github.io](https://jalammar.github.io/illustrated-gpt2/)
- The Illustrated DeepSeek-R1 (Language Models & Co. newsletter). — [newsletter.languagemodels.co](https://newsletter.languagemodels.co/p/the-illustrated-deepseek-r1)

**Umar Jamil (oEmbed-verified; each is a long math + PyTorch deep dive, better for weeks 2-4 of the LLM-internals block):**
- "Attention is all you need (Transformer) - Model explanation (including math), Inference and Training". — [YouTube](https://www.youtube.com/watch?v=bCz4OMemCcA)
- "Coding a Transformer from scratch on PyTorch, with full explanation, training and inference." — [YouTube](https://www.youtube.com/watch?v=ISNdQcPhsts)
- "LLaMA explained: KV-Cache, Rotary Positional Embedding, RMS Norm, Grouped Query Attention, SwiGLU". — [YouTube](https://www.youtube.com/watch?v=Mn_9W1nCFLo)
- "Coding LLaMA 2 from scratch in PyTorch - KV Cache, Grouped Query Attention, Rotary PE, RMSNorm". — [YouTube](https://www.youtube.com/watch?v=oM4VmoabDAI)
- "LoRA: Low-Rank Adaptation of Large Language Models - Explained visually + PyTorch code from scratch". — [YouTube](https://www.youtube.com/watch?v=PXWYUTMt-AU)
- "Direct Preference Optimization (DPO) explained: Bradley-Terry model, log probabilities, math". — [YouTube](https://www.youtube.com/watch?v=hvGa5Mba4c8)
- "Reinforcement Learning from Human Feedback explained with math derivations and the PyTorch code." — [YouTube](https://www.youtube.com/watch?v=qGyFrqc34yc)
- "Mistral / Mixtral Explained: Sliding Window Attention, Sparse Mixture of Experts, Rolling Buffer". — [YouTube](https://www.youtube.com/watch?v=UiX8K-xBUpE)
- "Quantization explained with PyTorch - Post-Training Quantization, Quantization-Aware Training". — [YouTube](https://www.youtube.com/watch?v=0VdNflU08yA)
- "Retrieval Augmented Generation (RAG) Explained: Embedding, Sentence BERT, Vector Database (HNSW)". — [YouTube](https://www.youtube.com/watch?v=rhZgXNdhWDY)
- "Flash Attention derived and coded from first principles with Triton (Python)". — [YouTube](https://www.youtube.com/watch?v=zy8ChVd_oTM)

**Stanford:**
- CS224N (NLP with Deep Learning): the course page is for Winter 2026. It says "Complete videos for the CS224N course are available (free!) on the CS224N 2024 YouTube playlist". Winter 2026 topics include pretraining, post-training (RLHF/SFT/DPO), PEFT, agents/tool use/RAG, evaluation, reasoning, and interpretability. — [web.stanford.edu/class/cs224n](https://web.stanford.edu/class/cs224n/)
  - Spring 2024 playlist (oEmbed: "Stanford CS224N Natural Language Processing with Deep Learning I Spring 2024 I Professor Christopher Manning"). — [YouTube playlist](https://www.youtube.com/playlist?list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D)
  - Winter 2021 playlist (older, classic). — [YouTube playlist](https://www.youtube.com/playlist?list=PLoROMvodv4rOSH4v6133s9LFPRHjEmbmJ)
- CS336 (Language Modeling from Scratch), taught by Tatsunori Hashimoto and Percy Liang. The current page is Spring 2026. Stated prerequisites are "Proficiency in Python", "Experience with deep learning and systems optimization", calculus, linear algebra, probability and ML. The five assignments (basics, systems, scaling, data, alignment) are on GitHub. — [cs336.stanford.edu](https://cs336.stanford.edu/)
  - Spring 2026 playlist (oEmbed: "Stanford CS336: Language Modeling from Scratch | Spring 2026 | Stanford Online"). — [YouTube playlist](https://www.youtube.com/playlist?list=PLoROMvodv4rMqXOcazWaTUHhq-yembLCV)
  - Spring 2025 playlist (oEmbed: "Stanford CS336 Language Modeling from Scratch I 2025"). — [YouTube playlist](https://www.youtube.com/playlist?list=PLoROMvodv4rOY23Y0BoGoBGgQ1zmU_MT_); Spring 2025 site (stanford-cs336.github.io/spring2025 redirects here) — [cs336.stanford.edu/spring2025](https://cs336.stanford.edu/spring2025/)
  - Assignment 1 repo: 2,839 stars, last push 2026-04-07. — [GitHub](https://github.com/stanford-cs336/assignment1-basics)
  - Caution: the URL `stanford-cs336.github.io/spring2026/` returns **404**. Use cs336.stanford.edu instead.
- CS25 (Transformers United) is on V6. — [web.stanford.edu/class/cs25](https://web.stanford.edu/class/cs25/); the recordings page — [cs25/recordings](https://web.stanford.edu/class/cs25/recordings/) — links the main playlist (oEmbed: "Stanford CS25 - Transformers United") — [YouTube playlist](https://www.youtube.com/playlist?list=PLoROMvodv4rNiJRchCzutFw5ItR_Z27CM)
  - "Stanford CS25: Transformers United V6 I Overview of Transformers" (oEmbed-verified). — [YouTube](https://www.youtube.com/watch?v=bHSDPgZYie0)
  - The recordings page also lists an intro lecture with Karpathy (XfpMkf4rD6E), plus talks by Jason Wei & Hyung Won Chung, Ashish Vaswani, Nathan Lambert, Douwe Kiela (RAG), Jim Fan and Geoffrey Hinton. oEmbed returns "Unauthorized" for some of these single lectures, meaning embedding is disabled, not that the video is missing. — [cs25/recordings](https://web.stanford.edu/class/cs25/recordings/)
  - One fetch summary said V6 ran "Spring Quarter 2025 (March 30 - June 3)". That conflicts with V5 being Spring 2025, so V6 is most likely Spring 2026. The year is UNVERIFIED.
- CME295 (Transformers & Large Language Models), Autumn 2025. Instructor Shervine Amidi announced the YouTube release ([X post](https://x.com/shervinea/status/1979908707879194799)); the co-instructor name "Afshine Amidi" is UNVERIFIED in this session. The Autumn 2025 playlist is oEmbed-verified ("Stanford CME295: Transformers and Large Language Models I Autumn 2025"). Topics run from tokenization and attention through MoE, decoding, SFT/RL fine-tuning, LoRA, LLM-as-judge evaluation, RoPE, quantization, reasoning, and RAG/tool calling. It is the most beginner-friendly Stanford option. — [YouTube playlist](https://www.youtube.com/playlist?list=PLoROMvodv4rOCXd21gf0CF4xr35yINeOy); [cme295.stanford.edu](https://cme295.stanford.edu/); [Stanford Online listing](https://online.stanford.edu/courses/cme295-transformers-and-large-language-models)

### Inferences
- Suggested sequence: 3B1B Ch.5-7 -> Illustrated Transformer / GPT-2 -> CME295 (lectures 1-4) -> Karpathy's build videos -> Umar Jamil deep dives -> selected CS336 lectures (for example tokenization, architecture, inference, alignment). Treat CS336 assignments as optional: they assume heavy compute and systems skills.
- CS25 V6 works as a weekly "guest-lecture" slot for staying current rather than as core material.

### Gaps
- Exact CME295 lecture count and length were not verified. Search results showed lectures 1-4 and 9 ("Recap & Current Trends"), so at least 9 exist.
- Whether CS224N Winter 2025 or Winter 2026 lectures were posted publicly: the course page points only to the 2024 playlist.

## Q3. Hugging Face Learn (LLM, Agents, MCP, smol, Cookbook, plus 2025-2026 additions)

### Takeaway
Everything on HF Learn is free, with free certificates. The Learn hub now lists a new **Context Course** (context engineering for code agents), a Robotics (LeRobot) course, and "a smol course" (post-training). The Agents and MCP courses remain available with no-deadline certificates.

### Cited Findings
- The Learn hub lists: LLM Course, Context Course (NEW: "Learn context engineering for code agents"), Robotics Course (NEW, LeRobot), a smol course (NEW, "the smollest course on post-training AI models"), Agents Course, Deep RL Course, Community Computer Vision Course, Audio Course, Open-Source AI Cookbook, ML for Games, Diffusion Course, and ML for 3D. The MCP course is not listed on the hub page but its URL still returns 200. — [huggingface.co/learn](https://huggingface.co/learn)
- **LLM Course** (formerly the "NLP/Transformers course"): the page returns 200; repo huggingface/course has 4,236 stars, last push 2026-09-23. — [huggingface.co/learn/llm-course](https://huggingface.co/learn/llm-course/chapter1/1); [GitHub](https://github.com/huggingface/course)
- **Agents Course**: Unit 0 Onboarding, Unit 1 Agent Fundamentals, Unit 2 Frameworks (smolagents, LlamaIndex, LangGraph), Unit 3 Use Cases (agentic RAG), Unit 4 Final Assignment. Bonus units cover fine-tuning an LLM for function calling, agent observability & evaluation, and agents in games (Pokemon). There are two free certificates: Fundamentals (Unit 1 only) and Completion (Unit 1 + one use-case assignment + the final challenge). The page says "There's no deadline for the certification process." Expect about 3-4 h/week, one chapter per week. Prerequisites are basic Python and basic LLM understanding. — [huggingface.co/learn/agents-course](https://huggingface.co/learn/agents-course/unit0/introduction); repo: 32,824 stars, last push 2026-09-15 — [GitHub](https://github.com/huggingface/agents-course)
- **MCP Course**: Unit 0 Onboarding, Unit 1 MCP fundamentals/architecture, Unit 2 end-to-end use case, Unit 3 deployed use case, Unit 4 bonus partner units. Two free certificates: Fundamentals (Unit 1) and Completion (Units 2 and 3). Partners are Gradio, Continue, llama.cpp and Anthropic. Needs "only a computer with internet access and a free Hugging Face account". — [huggingface.co/learn/mcp-course](https://huggingface.co/learn/mcp-course/unit0/introduction); repo: 918 stars, last push 2026-09-18 — [GitHub](https://github.com/huggingface/mcp-course)
- **a smol course** (post-training). Units: 1 Instruction Tuning, 2 Evaluation, 3 Preference Alignment, 4 Vision Language Models, 5 Reinforcement Learning, 6 Synthetic Data, 7 Award Ceremony. The page still shows Units 5-7 as "October / November / December", which is probably a stale 2025 schedule. Certificates are free (Fundamentals = Unit 1; Completion = all units + final project). The page recommends "preferably GPU access" and mentions HF Pro as optional and paid. — [huggingface.co/learn/smol-course](https://huggingface.co/learn/smol-course/unit0/1); repo: 6,756 stars, last push 2026-09-17 — [GitHub](https://github.com/huggingface/smol-course)
- **Context Course**. Units: 0 Onboarding, 1 Agent Skills, 2 MCP, 3 Plugins, 4 Sub-agents, 5 Hooks, 6 Bonus "Nano Harness". It supports Claude Code, Codex, OpenCode and Pi. Prerequisites are Python basics, the command line, an HF account, and at least one installed code agent. Certificates: "Context Fundamentals Certificate" (2-3 weeks) and "Context Engineering Certificate" (5-8 weeks). — [huggingface.co/learn/context-course](https://huggingface.co/learn/context-course)
- **Open-Source AI Cookbook** (notebooks, HTTP 200); repo: 2,737 stars, last push 2026-09-22. — [huggingface.co/learn/cookbook](https://huggingface.co/learn/cookbook/index); [GitHub](https://github.com/huggingface/cookbook)

### Inferences
- For a learner with no GPU, the Agents and MCP courses are the best HF entry points because they run on free HF Spaces/Colab and free inference credits. The smol course is the hardest to run for free, since it needs a GPU.
- The Context Course needs an installed code agent. Free options are UNVERIFIED here. Pair it with free-tier tools, or read it conceptually.

### Gaps
- Context Course launch date and whether all units are released: not stated on the page.
- Whether smol course Units 5-7 have been published, since the page still shows month labels.
- The exact monthly free inference credit on HF for 2026 was not checked.

## Q4. DeepLearning.AI (free status in 2026 and exact current URLs)

### Takeaway
DeepLearning.AI launched a paid **"DeepLearning.AI Pro"** membership. Course videos are still free to watch. Quizzes, interactive labs/notebooks, saved progress and certificates of completion are now Pro-only. All course URLs moved from `/short-courses/<slug>/` to `/courses/<slug>` (old links redirect), and some slugs changed, for example `chatgpt-prompt-eng`.

### Cited Findings
- Pro vs free: free users "watch course videos, access the community forum, and receive our newsletters". Pro adds "Quizzes and interactive labs in all courses, Certificates of completion, Ability to save your work and resume anytime, Access to professional certificate learning tracks, Projects...". — [DeepLearning.AI help center](https://info.deeplearning.ai/knowledge-base/what-do-i-get-with-the-deeplearning.ai-pro-membership-that-i-dont-get-for-free); announcement — [The Batch](https://www.deeplearning.ai/the-batch/announcing-the-deeplearning-ai-pro-membership); [membership page](https://www.deeplearning.ai/membership)
- Every course page listed below still carries a schema.org offer category of "Free" (parsed 2026-09-24), consistent with the videos staying free. Format per row: title | canonical URL | JSON-LD publish date | level | number of video lessons (the old /short-courses/ URL redirects to each):
  - Agentic AI (Andrew Ng) | [deeplearning.ai/courses/agentic-ai](https://www.deeplearning.ai/courses/agentic-ai) | 2025-09-30 | Intermediate | 31 video lessons
  - AI Python for Beginners | [/courses/ai-python-for-beginners](https://www.deeplearning.ai/courses/ai-python-for-beginners) | 2024-08-07 | Beginner | 35
  - How Transformer LLMs Work | [/courses/how-transformer-llms-work](https://www.deeplearning.ai/courses/how-transformer-llms-work) | 2025-02-05 | Beginner | 13
  - Attention in Transformers: Concepts and Code in PyTorch | [/courses/attention-in-transformers-concepts-and-code-in-pytorch](https://www.deeplearning.ai/courses/attention-in-transformers-concepts-and-code-in-pytorch) | 2025-02-12 | Beginner | 11
  - Transformers in Practice (NEW) | [/courses/transformers-in-practice](https://www.deeplearning.ai/courses/transformers-in-practice) | 2026-05-12 | Intermediate | 19
  - Claude Code: A Highly Agentic Coding Assistant | [/courses/claude-code-a-highly-agentic-coding-assistant](https://www.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant) | 2025-08-06 | Intermediate | 10
  - MCP: Build Rich-Context AI Apps with Anthropic | [/courses/mcp-build-rich-context-ai-apps-with-anthropic](https://www.deeplearning.ai/courses/mcp-build-rich-context-ai-apps-with-anthropic) | 2025-05-14 | Intermediate | 11
  - A2A: The Agent2Agent Protocol | [/courses/a2a-the-agent2agent-protocol](https://www.deeplearning.ai/courses/a2a-the-agent2agent-protocol) | 2026-02-11 | Intermediate | 14
  - Agent Skills with Anthropic (NEW) | [/courses/agent-skills-with-anthropic](https://www.deeplearning.ai/courses/agent-skills-with-anthropic) | 2026-01-28 | Beginner | 10
  - Evaluating AI Agents | [/courses/evaluating-ai-agents](https://www.deeplearning.ai/courses/evaluating-ai-agents) | 2025-02-19 | Beginner | 15
  - Reinforcement Fine-Tuning LLMs With GRPO | [/courses/reinforcement-fine-tuning-llms-grpo](https://www.deeplearning.ai/courses/reinforcement-fine-tuning-llms-grpo) | 2025-05-21 | Intermediate | 10
  - Post-training of LLMs | [/courses/post-training-of-llms](https://www.deeplearning.ai/courses/post-training-of-llms) | 2025-07-09 | Intermediate | 9
  - Fine-tuning & RL for LLMs: Intro to Post-training (longer course) | [/courses/fine-tuning-and-reinforcement-learning-for-llms-intro-to-post-training](https://www.deeplearning.ai/courses/fine-tuning-and-reinforcement-learning-for-llms-intro-to-post-training) | 2025-10-28 | Intermediate | 43
  - Finetuning Large Language Models | [/courses/finetuning-large-language-models](https://www.deeplearning.ai/courses/finetuning-large-language-models) | 2023-08-23 | Intermediate | 9
  - AI Agents in LangGraph | [/courses/ai-agents-in-langgraph](https://www.deeplearning.ai/courses/ai-agents-in-langgraph) | 2024-06-05 | Intermediate | 9
  - Long-Term Agentic Memory With LangGraph | [/courses/long-term-agentic-memory-with-langgraph](https://www.deeplearning.ai/courses/long-term-agentic-memory-with-langgraph) | 2025-03-14 | Intermediate | 7
  - Agent Memory: Building Memory-Aware Agents (NEW) | [/courses/agent-memory-building-memory-aware-agents](https://www.deeplearning.ai/courses/agent-memory-building-memory-aware-agents) | 2026-03-18 | Intermediate | 7
  - Building Code Agents with Hugging Face smolagents | [/courses/building-code-agents-with-hugging-face-smolagents](https://www.deeplearning.ai/courses/building-code-agents-with-hugging-face-smolagents) | 2025-04-23 | Intermediate | 7
  - Multi AI Agent Systems with crewAI | [/courses/multi-ai-agent-systems-with-crewai](https://www.deeplearning.ai/courses/multi-ai-agent-systems-with-crewai) | 2024-05-15 | Beginner | 18
  - Design, Develop, and Deploy Multi-Agent Systems with CrewAI (longer course) | [/courses/design-develop-and-deploy-multi-agent-systems-with-crewai](https://www.deeplearning.ai/courses/design-develop-and-deploy-multi-agent-systems-with-crewai) | 2025-11-11 | Beginner | 38
  - ChatGPT Prompt Engineering for Developers | [/courses/chatgpt-prompt-eng](https://www.deeplearning.ai/courses/chatgpt-prompt-eng) | 2023-04-27 | Beginner | 9
  - Vector Databases: from Embeddings to Applications | [/courses/vector-databases-embeddings-applications](https://www.deeplearning.ai/courses/vector-databases-embeddings-applications) | 2023-11-08 | Intermediate | 8
  - Building and Evaluating Advanced RAG | [/courses/building-evaluating-advanced-rag](https://www.deeplearning.ai/courses/building-evaluating-advanced-rag) | 2023-11-29 | Beginner | 6
  - Retrieval Augmented Generation (RAG) (longer course) | [/courses/retrieval-augmented-generation](https://www.deeplearning.ai/courses/retrieval-augmented-generation) | 2025-09-30 | Intermediate | 49. Note the old slug `retrieval-augmented-generation-rag` redirects here.
  - Advanced Retrieval for AI with Chroma | [/courses/advanced-retrieval-for-ai](https://www.deeplearning.ai/courses/advanced-retrieval-for-ai) | 2024-01-03 | Intermediate | 7
  - Building Agentic RAG with LlamaIndex | [/courses/building-agentic-rag-with-llamaindex](https://www.deeplearning.ai/courses/building-agentic-rag-with-llamaindex) | 2024-05-08 | Beginner | 6
  - Embedding Models: from Architecture to Implementation | [/courses/embedding-models-from-architecture-to-implementation](https://www.deeplearning.ai/courses/embedding-models-from-architecture-to-implementation) | 2024-07-31 | Beginner | 7
  - Function-calling and data extraction with LLMs | [/courses/function-calling-and-data-extraction-with-llms](https://www.deeplearning.ai/courses/function-calling-and-data-extraction-with-llms) | 2024-06-20 | Beginner | 8
  - Pydantic for LLM Workflows | [/courses/pydantic-for-llm-workflows](https://www.deeplearning.ai/courses/pydantic-for-llm-workflows) | 2025-07-30 | Intermediate | 8
  - DSPy: Build and Optimize Agentic Apps | [/courses/dspy-build-optimize-agentic-apps](https://www.deeplearning.ai/courses/dspy-build-optimize-agentic-apps) | 2025-06-04 | Intermediate | 6
  - Semantic Caching for AI Agents | [/courses/semantic-caching-for-ai-agents](https://www.deeplearning.ai/courses/semantic-caching-for-ai-agents) | 2025-11-19 | Intermediate | 7
  - Building Coding Agents with Tool Execution | [/courses/building-coding-agents-with-tool-execution](https://www.deeplearning.ai/courses/building-coding-agents-with-tool-execution) | 2025-12-03 | Intermediate | 9
  - Spec-Driven Development with Coding Agents (NEW) | [/courses/spec-driven-development-with-coding-agents](https://www.deeplearning.ai/courses/spec-driven-development-with-coding-agents) | 2026-04-15 | Beginner | 15
  - AI Code Review (NEW) | [/courses/ai-code-review](https://www.deeplearning.ai/courses/ai-code-review) | 2026-07-29 | Intermediate | 8
  - Building Live Voice Agents with Google's ADK | [/courses/building-live-voice-agents-with-googles-adk](https://www.deeplearning.ai/courses/building-live-voice-agents-with-googles-adk) | 2025-09-24 | Intermediate | 10
  - NVIDIA's NeMo Agent Toolkit: Making Agents Reliable | [/courses/nvidia-nat-making-agents-reliable](https://www.deeplearning.ai/courses/nvidia-nat-making-agents-reliable) | 2025-12-17 | Intermediate | 9
  - Governing AI Agents | [/courses/governing-ai-agents](https://www.deeplearning.ai/courses/governing-ai-agents) | 2025-10-22 | Beginner | 9
  - Safe and reliable AI via guardrails | [/courses/safe-and-reliable-ai-via-guardrails](https://www.deeplearning.ai/courses/safe-and-reliable-ai-via-guardrails) | 2024-11-13 | Beginner | 10
  - Red Teaming LLM Applications | [/courses/red-teaming-llm-applications](https://www.deeplearning.ai/courses/red-teaming-llm-applications) | 2024-04-03 | Beginner | 7
  - Quality and Safety for LLM Applications | [/courses/quality-safety-llm-applications](https://www.deeplearning.ai/courses/quality-safety-llm-applications) | 2023-11-15 | Beginner | 7
  - LLMOps | [/courses/llmops](https://www.deeplearning.ai/courses/llmops) | 2024-01-17 | Beginner | 6
  - Automated Testing for LLMOps | [/courses/automated-testing-llmops](https://www.deeplearning.ai/courses/automated-testing-llmops) | 2024-01-24 | Intermediate | 6
  - Efficiently Serving LLMs | [/courses/efficiently-serving-llms](https://www.deeplearning.ai/courses/efficiently-serving-llms) | 2024-03-18 | Intermediate | 8
  - Quantization Fundamentals with Hugging Face | [/courses/quantization-fundamentals](https://www.deeplearning.ai/courses/quantization-fundamentals) | 2024-04-15 | Beginner | 7
  - Pretraining LLMs | [/courses/pretraining-llms](https://www.deeplearning.ai/courses/pretraining-llms) | 2024-07-17 | Intermediate | 8
  - Generative AI with Large Language Models (longer course; JSON-LD date 2025-10-27) | [/courses/generative-ai-with-llms](https://www.deeplearning.ai/courses/generative-ai-with-llms) | Intermediate | 47
- The site sitemap lists 120 course slugs. Others not tabulated but relevant include ai-agentic-design-patterns-with-autogen, building-ai-browser-agents, microsoft-semantic-kernel, langchain-chat-with-your-data, knowledge-graphs-rag, reinforcement-learning-from-human-feedback, getting-structured-llm-output, and gemini-cli-code-and-create-with-an-open-source-agent. — [deeplearning.ai/sitemap.xml](https://www.deeplearning.ai/sitemap.xml)

### Inferences
- In 2026 DeepLearning.AI is "free to watch, pay to practice". For a zero-budget learner, pair each DLAI video course with a free notebook elsewhere (HF courses, Unsloth, Microsoft repos, or the course's public GitHub code where one exists), and do not count on DLAI certificates.
- The best DLAI picks for this path: How Transformer LLMs Work, then Attention in Transformers, Agentic AI (Ng), MCP with Anthropic, Agent Skills with Anthropic, A2A, Evaluating AI Agents, the RAG course, GRPO/Post-training, and Claude Code / Spec-Driven Development.

### Gaps
- Pro pricing (monthly/annual) and the exact Pro launch date were not captured. The help-center page does not state them.
- Course lengths in hours: the JSON-LD "courseWorkload" appears to be a placeholder (for example "PT1H" for the multi-module Agentic AI course), so hours are UNVERIFIED. Use video-lesson counts as the proxy.
- Instructor names were not captured by the parser (only "Agentic AI = Andrew Ng" comes from the page description).

## Q5. Vendor academies and free curricula: Anthropic, Google/Kaggle, Microsoft, OpenAI, plus LangChain Academy, W&B and Berkeley MOOCs

### Takeaway
Anthropic's learning hub has moved: anthropic.com/learn now redirects to **academy.claude.com**, and the developer courses sit on anthropic.skilljar.com. The old `anthropics/courses` GitHub repo is **archived**, though the prompt-engineering tutorial repo is still maintained. Kaggle/Google intensives stay available self-paced after their live runs, and there is a new June 2026 "Vibe Coding" agents edition. Microsoft's three beginner repos are actively maintained at 21 / 18 / 13 (modules 0-12) lessons. The OpenAI Cookbook moved to developers.openai.com.

### Cited Findings
**Anthropic**
- anthropic.com/learn redirects to academy.claude.com (curl, 2026-09-24). The landing page shows "AI Fluency: Framework and foundations" (14 lessons, 1 quiz, 4 hr), "AI capabilities and limitations" (13 lessons, 3.5 hr) and "Building effective human-agent teams (beta)" (5 lessons, 45 min). — [academy.claude.com](https://academy.claude.com/)
- The Skilljar catalog lists these developer courses: Claude 101, Building with the Claude API, Introduction to Model Context Protocol, Model Context Protocol: Advanced Topics ("sampling, notifications, file system access"), Claude Code in Action ("Run long, hands-off Claude Code sessions you can trust"), and Introduction to agent skills. — [anthropic.skilljar.com](https://anthropic.skilljar.com/) (course paths: [/claude-with-the-anthropic-api](https://anthropic.skilljar.com/claude-with-the-anthropic-api), [/introduction-to-model-context-protocol](https://anthropic.skilljar.com/introduction-to-model-context-protocol), [/model-context-protocol-advanced-topics](https://anthropic.skilljar.com/model-context-protocol-advanced-topics), [/claude-code-in-action](https://anthropic.skilljar.com/claude-code-in-action), [/introduction-to-agent-skills](https://anthropic.skilljar.com/introduction-to-agent-skills), [/claude-101](https://anthropic.skilljar.com/claude-101))
- Free status and certificates come from third parties only: "Every course is free, requires only an email to sign up, and issues a certificate on completion" of the final assessment. One source says the Academy "launched in March 2026 with 13 free, self-paced courses". That date conflicts with Skilljar courses existing before 2026 and is UNVERIFIED. — [Analytics Vidhya](https://www.analyticsvidhya.com/blog/2026/03/free-anthropic-ai-courses-with-certificates/); [DEV Community](https://dev.to/amareswer/anthropic-academy-free-claude-courses-and-certificates-22ki)
- `anthropics/courses` is **ARCHIVED** (GitHub API: archived=true; 22,858 stars; last push 2026-08-28). Its README lists five notebook courses: Anthropic API fundamentals, Prompt engineering interactive tutorial, Real world prompting, Prompt evaluations, and Tool use. It says the courses "favor our lowest-cost model, Claude 3 Haiku, to keep API costs down", which is an old model. — [GitHub](https://github.com/anthropics/courses)
- `anthropics/prompt-eng-interactive-tutorial` is not archived (38,277 stars; last push 2026-08-28). — [GitHub](https://github.com/anthropics/prompt-eng-interactive-tutorial)
- `anthropics/claude-cookbooks` (the renamed cookbook repo): 52,937 stars, last push 2026-09-23. — [GitHub](https://github.com/anthropics/claude-cookbooks)
- `anthropics/skills` (public Agent Skills repo): 177,849 stars. — [GitHub](https://github.com/anthropics/skills)
- Claude prompt-engineering docs now live on platform.claude.com. — [platform.claude.com](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)

**Google / Kaggle**
- 5-Day Gen AI Intensive: the learn-guide page returns 200 but renders in JavaScript, so its contents could not be read. Secondary sources say the latest live run was 31 Mar - 4 Apr 2025 and that it is now a self-paced learn guide. Each day pairs whitepapers ("sometimes over 100 pages"), a NotebookLM podcast and Kaggle codelabs. The five units cover prompt engineering, embeddings/vector databases, agents, domain-specific LLMs and MLOps. It needs a phone-verified Kaggle account. — [kaggle.com/learn-guide/5-day-genai](https://www.kaggle.com/learn-guide/5-day-genai); [KDnuggets](https://www.kdnuggets.com/kaggle-googles-free-5-day-gen-ai-course); [NYU SPS review](https://nexus.sps.nyu.edu/post/nexus-review-kaggle-5-day-gen-ai-intensive-course-with-google)
- Prompt Engineering whitepaper (Kaggle; HTTP 200). — [kaggle.com/whitepaper-prompt-engineering](https://www.kaggle.com/whitepaper-prompt-engineering)
- 5-Day AI Agents Intensive: ran live 10-14 Nov 2025 and is now self-paced. "Each day pairs a technical whitepaper with two hands-on codelabs built on Gemini and Google's Agent Development Kit." Topics are models, tools, orchestration, memory, evaluation and "Agent Ops". — [kaggle.com/learn-guide/5-day-agents](https://www.kaggle.com/learn-guide/5-day-agents); [Kaggle blog](https://www.kaggle.com/blog/5-days-of-ai-agents-intensive-course-with-google); [KDnuggets](https://www.kdnuggets.com/kaggle-googles-free-5-day-agentic-ai-course)
- NEW: "5-Day AI Agents: Intensive Vibe Coding Course With Google" ran live 15-19 June 2026 and is now self-paced (URL returns 200). A search snippet claims "over 353,000 registered participants"; that figure is UNVERIFIED. — [kaggle.com/learn-guide/5-day-agents-vibecoding](https://www.kaggle.com/learn-guide/5-day-agents-vibecoding); [Google blog recap](https://blog.google/innovation-and-ai/technology/developers-tools/ai-agents-intensive-recap-2026/)
- Google Cloud Skills Boost has been rebranded **"Google Skills"**: cloudskillsboost.google/paths/118 redirects to skills.google/paths/118, "Beginner: Introduction to Generative AI" (4 activities, "Managed by Google Cloud"). Whether it is free was not stated on the page (UNVERIFIED). — [skills.google/paths/118](https://www.skills.google/paths/118)

**Microsoft (all free on GitHub, actively updated in Sept 2026)**
- generative-ai-for-beginners: "21 Lessons" (00 setup + 01-21), 120,396 stars, last push 2026-09-24. Lessons include 04-05 prompt engineering, 08 vector search, 11 function calling, 13 securing GenAI apps, 14 GenAI lifecycle/LLMOps, 15 RAG & vector DBs, 16 open-source models/HF, 17 AI agents, 18 fine-tuning, 19 SLMs. — [GitHub](https://github.com/microsoft/generative-ai-for-beginners)
- ai-agents-for-beginners: "18 Lessons", 75,534 stars, last push 2026-09-19. Lessons: 01 intro, 02 frameworks, 03 design patterns, 04 tool use, 05 agentic RAG, 06 trustworthy agents, 07 planning, 08 multi-agent, 09 metacognition, 10 agents in production, 11 agentic protocols (MCP, A2A, NLWeb), 12 context engineering, 13 agent memory, 14 Microsoft Agent Framework, 15 computer-use agents, 16 deploying scalable agents, 17 local AI agents, 18 securing AI agents. — [GitHub](https://github.com/microsoft/ai-agents-for-beginners)
- mcp-for-beginners: 17,271 stars, last push 2026-09-22. Modules 0-12: 0 intro; 1 core concepts, including "What's Changed in MCP (2026-07-28): Stateless protocol, Extensions framework, and feature deprecations"; 2 security, including "CIMD and DCR Authorization"; 3 first server/client with 15 sub-lessons (stdio, HTTP streaming, testing, deployment, auth, Inspector, sampling, MCP Apps); 4-5 practical/advanced (pagination, OAuth2, routing, scaling, security, web search); 6-10 community, best practices, case studies, workshop; 11 a 13-lab PostgreSQL MCP-server path; 12 MCP tooling. Many labs lean on Azure. — [GitHub](https://github.com/microsoft/mcp-for-beginners)

**OpenAI**
- cookbook.openai.com redirects to developers.openai.com/cookbook; repo has 76,151 stars, last push 2026-09-23. — [developers.openai.com/cookbook](https://developers.openai.com/cookbook); [GitHub](https://github.com/openai/openai-cookbook)
- "A practical guide to building agents" PDF (HTTP 200). — [cdn.openai.com PDF](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf)
- OpenAI Academy (HTTP 200). — [academy.openai.com](https://academy.openai.com/)

**Other free sources relevant to agents and evals**
- LangChain Academy (HTTP 200) features "Foundation: Introduction to Deep Agents", "Quickstart: LangSmith Essentials" and "Foundation: Introduction to LangSmith Deployment". The classic "Introduction to LangGraph" course URL still returns 200. Free status was not stated on the landing page (UNVERIFIED). — [academy.langchain.com](https://academy.langchain.com/); [intro-to-langgraph](https://academy.langchain.com/courses/intro-to-langgraph)
- Weights & Biases courses, all labelled "Free". GenAI: AI Engineering: Agents (2 h), LLM apps: Evaluation (2 h), RAG++: From POC to production (2 h), Developer's guide to LLM prompting (2 h), LLM engineering: Structured outputs (2 h), Building LLM-powered apps (3 h), Training and fine-tuning LLMs (4 h). MLOps: Model CI/CD (2.5 h), Effective MLOps: Model development (4 h), CI/CD for ML (GitOps) (5 h), Data validation in production ML pipelines (2 h). Certificates are not stated. — [wandb.ai/site/courses](https://wandb.ai/site/courses/)
- UC Berkeley RDI Agentic AI MOOC (CS294-196, Fall 2025): 12 lectures from 15 Sep to 8 Dec 2025. Speakers include Yann Dubois (OpenAI), Yangqing Jia (NVIDIA), Noam Brown (OpenAI), Oriol Vinyals (Google DeepMind), Clay Bavor (Sierra) and Dawn Song (Berkeley). "32,000+ global participants". Certificate coursework was due 31 Jan 2026. — [agenticai-learning.org/f25](https://agenticai-learning.org/f25); first lecture oEmbed-verified: "Agentic AI MOOC | UC Berkeley CS294-196 Fall 2025 | LLM Agents Overview by Yann Dubois | Berkeley RDI" — [YouTube](https://www.youtube.com/watch?v=r1qZpYAmqmg)
- Earlier Berkeley MOOCs (both return 200): LLM Agents (Fall 2024) — [llmagents-learning.org/f24](https://llmagents-learning.org/f24); Advanced LLM Agents (Spring 2025) — [llmagents-learning.org/sp25](https://llmagents-learning.org/sp25)

### Inferences
- The Anthropic Skilljar courses (MCP intro/advanced, Claude Code in Action, Agent Skills) are the best free protocol courses to pair with the HF MCP course and the Microsoft mcp-for-beginners repo. Claude API exercises need an API key, and the free-credit situation was not verified. Microsoft's repos can use GitHub Models or other OpenAI-compatible providers (the README mentions alternatives).
- Berkeley MOOC certificates are closed (deadline 31 Jan 2026), but the lecture videos remain useful as advanced agent lectures.
- For India-based learners, Kaggle intensives are an excellent zero-cost "sprint" format: free Kaggle GPU notebooks, a whitepaper per day, and a community.

### Gaps
- Kaggle learn-guide pages render in JavaScript, so the daily whitepaper titles and livestream URLs could not be enumerated directly.
- The Anthropic Academy course list on academy.claude.com (3 courses shown) versus the Skilljar catalog (developer courses) suggests two front doors. Whether certificates are issued for every course is based on third-party claims only.
- LangChain Academy free status and certificates.

## Q6. Build-from-scratch and fine-tuning (Raschka, Labonne, Unsloth, HandsOnLLM)

### Takeaway
Raschka's repo (105k stars, updated Sept 2026) runs on an ordinary laptop, and he offers a free 7-video YouTube live-coding series; the 17 h Manning video course is paid. Unsloth's free Colab tier covers models **under about 22B parameters** (gpt-oss-20B, Qwen3-14B, Phi-4-14B, Llama-3.1-8B, Gemma 4 E2B/E4B, Qwen3.5 up to 4B), and Kaggle variants reach larger models. HandsOnLLM notebooks are built for the free Colab T4 (16 GB).

### Cited Findings
- rasbt/LLMs-from-scratch: 105,479 stars, last push 2026-09-22. The README says the main-chapter code "is designed to run on conventional laptops within a reasonable timeframe and does not require specialized hardware". The book is paid (Manning); the code is free. — [GitHub](https://github.com/rasbt/LLMs-from-scratch)
- The paid companion is "A 17-hour and 15-minute companion video course" on Manning. — [LLMs-from-scratch README](https://github.com/rasbt/LLMs-from-scratch); [Manning](https://www.manning.com/livevideo/master-and-build-large-language-models)
- The FREE YouTube playlist "Build a Large Language Model (From Scratch)" by Sebastian Raschka has 7 videos (oEmbed-verified; video count from the playlist page). His post "Coding LLMs from the Ground Up: A Complete Course" mentions about 15 hours in total. — [YouTube playlist](https://www.youtube.com/playlist?list=PLTKMiZHVd_2IIEsoJrWACkIxLRdfMlw11); [Ahead of AI post](https://magazine.sebastianraschka.com/p/coding-llms-from-the-ground-up); [companion hub](https://sebastianraschka.com/llms-from-scratch/)
- The free "Building LLMs from the Ground Up: A 3-hour Coding Workshop" is oEmbed-verified. — [YouTube](https://www.youtube.com/watch?v=quh7z1q7-uc)
- rasbt/reasoning-from-scratch: 5,280 stars, last push 2026-09-23. — [GitHub](https://github.com/rasbt/reasoning-from-scratch)
- The Ahead of AI newsletter is live (HTTP 200). — [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/)
- mlabonne/llm-course: 83,110 stars, last push 2026-02-05. It has three tracks: "LLM Fundamentals" (optional math/Python/NN), "The LLM Scientist" and "The LLM Engineer". Colab notebooks cover fine-tuning ("Fine-tune Llama 3.1 with Unsloth", ORPO, DPO, and "Supervised fine-tune Mistral-7b in a free-tier Google Colab with TRL"), quantization (GPTQ, GGUF/llama.cpp, EXL2) and merging (MergeKit, "no GPU required"). — [GitHub](https://github.com/mlabonne/llm-course)
- Unsloth: the main repo has 76,662 stars (last push 2026-09-24) and now describes itself as a "Local UI to run and train LLMs". The notebooks repo offers "250+ Fine-tuning & RL Notebooks" (5,691 stars, last push 2026-09-23). The docs moved from docs.unsloth.ai to unsloth.ai/docs. — [unsloth](https://github.com/unslothai/unsloth); [notebooks](https://github.com/unslothai/notebooks); [docs](https://unsloth.ai/docs/get-started/unsloth-notebooks)
- The Unsloth docs say the notebooks are "powered by free GPU compute". The Colab section is headed "Train and run models under 22B parameters". Standard SFT notebooks listed there include gpt-oss (20b), Qwen3 (14B), Phi-4 (14B), Llama 3.1 (8B), Llama 3.2 (1B + 3B), Qwen3-VL (8B), Gemma 3 (4B), Gemma 4 (E2B/E4B), Qwen3.5 (0.8B/2B/4B) and EmbeddingGemma (300M). Kaggle variants are listed for "Qwen3.8 27B", "Muse Glimmer (30B)" and "Gemma 4 31B". — [Unsloth docs](https://unsloth.ai/docs/get-started/unsloth-notebooks)
- Unsloth's "Large LLMs" notebooks: "These exceed Colab's free 15 GB VRAM tier ... Colab subscription or credits are required". Examples: Gemma-4-26B-A4B, Qwen3.5-35B-A3B, Qwen3.5-27B, GLM-4.7-Flash, and gpt-oss-20b with 500K context. Gemma-4-31B is flagged "FREE", presumably via Kaggle. — [Unsloth docs](https://unsloth.ai/docs/get-started/unsloth-notebooks)
- Unsloth GRPO/RL notebooks include Gemma 4 E2B (Sudoku, 2048, kernel creation), Qwen3 (4B) Advanced GRPO LoRA, gpt-oss-20b, and Llama 3.1 (8B) GSM8K + vLLM. — [unslothai/notebooks README](https://github.com/unslothai/notebooks); [Unsloth docs](https://unsloth.ai/docs/get-started/unsloth-notebooks)
- HandsOnLLM (O'Reilly "Hands-On Large Language Models", Alammar & Grootendorst): 29,261 stars, last push 2026-04-24. "We advise to run all examples through Google Colab ... Google Colab allows you to use a T4 GPU with 16GB of VRAM for free." There are 12 chapter notebooks, each with a Colab badge (Ch 3 "Looking Inside Transformer LLMs", Ch 6 prompt engineering, Ch 8 semantic search & RAG, Ch 10 embedding models, Ch 12 fine-tuning generation models) plus bonus content. The book is paid; notebooks are free. — [GitHub](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models)

### Inferences
- On the learner's laptop (8 GB RAM, no NVIDIA GPU), all of Raschka's chapters 1-5 and microgpt run on CPU. Do all fine-tuning on free Colab or Kaggle. Start with QLoRA SFT of a 1-4B model (Llama 3.2 1B/3B, Qwen3.5 2B/4B, Gemma 4 E2B), then GRPO on a small model; 8-14B models are feasible on a T4 but slow.
- The Unsloth listings show that the "state of the art on a free T4" in 2026 is roughly gpt-oss-20B and 14B-class dense models with 4-bit QLoRA.

### Gaps
- Free Colab and Kaggle GPU quotas in 2026 (weekly hours, session limits) were not checked. Colab's free VRAM is quoted as 15 GB by Unsloth and 16 GB by HandsOnLLM.
- The model names "Qwen3.8" and "Muse Glimmer" appear on the Unsloth docs page and were not independently verified.

## Q7. MLOps / LLMOps (Made With ML, DataTalksClub Zoomcamps, FSDL, Evidently, W&B, Rules of ML, Docker/FastAPI/GitHub Actions)

### Takeaway
The best free LLMOps option with a live cohort is **LLM Zoomcamp 2026**, which runs 24 Aug - 12 Oct 2026; self-paced learners get the materials but no certificate. **MLOps Zoomcamp has no 2026 live cohort** and is self-paced only. Evidently and W&B offer free LLM-eval and MLOps courses. FSDL is dated (2022/2023) but still up.

### Cited Findings
- Made With ML is live (HTTP 200); repo GokuMohandas/Made-With-ML has 49,580 stars, last push 2026-03-04. — [madewithml.com](https://madewithml.com/); [GitHub](https://github.com/GokuMohandas/Made-With-ML)
- MLOps Zoomcamp (15,324 stars): "We don't plan to run a live cohort in 2026. The course is fully available for self-paced study now." Certificates go only to people who complete the final project in a live cohort. — [GitHub README](https://github.com/DataTalksClub/mlops-zoomcamp)
- LLM Zoomcamp (7,332 stars): the 2026 cohort has `start_date: "2026-08-24"`, `end_date: "2026-10-12"`. Modules: 1 Agentic RAG, 2 Vector Search, 3 Orchestration, a dlt data-ingestion workshop, 4 Evaluation, 5 Monitoring, 6 Best Practices, 7 End-to-End Project. The entry bar: "If you can write a Python function and have heard of ChatGPT, you have enough to get started." Lectures are pre-recorded. "Self-paced learners are not eligible for certification." — [cohort.yaml](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/cohorts/2026/cohort.yaml); [README](https://github.com/DataTalksClub/llm-zoomcamp); [cohort schedule](https://courses.datatalks.club/llm-zoomcamp-2026)
- AI Dev Tools Zoomcamp 2026 (1,642 stars): starts 31 Aug 2026; "The 2026 materials are currently being finalized"; Module 1 is "AI-Native Developer Workflow". — [GitHub](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp)
- Full Stack Deep Learning 2022 course and LLM Bootcamp (2023) pages are still up (HTTP 200) but their content is dated. — [FSDL 2022](https://fullstackdeeplearning.com/course/2022/); [LLM Bootcamp](https://fullstackdeeplearning.com/llm-bootcamp/)
- Evidently AI free courses: "LLM Evaluations for AI Builders" (applied; free video course with 10 hands-on code tutorials covering LLM judges, RAG evals and adversarial testing), "LLM Evaluations for AI Product Teams" (no coding) and "Open-source ML observability course". — [evidentlyai.com/courses](https://www.evidentlyai.com/courses); [ML observability course](https://www.evidentlyai.com/ml-observability-course); [LLM evaluations course](https://www.evidentlyai.com/llm-evaluations-course)
- W&B free MLOps courses (Model CI/CD, Effective MLOps, CI/CD for ML (GitOps), Data validation) and LLM courses (Evaluation, RAG++, Agents, Training & fine-tuning LLMs). — [wandb.ai/site/courses](https://wandb.ai/site/courses/)
- DeepLearning.AI LLMOps-related videos (free to watch): LLMOps, Automated Testing for LLMOps, Efficiently Serving LLMs, Quantization Fundamentals. — see the Q4 table.
- Google "Rules of Machine Learning" (HTTP 200). — [developers.google.com](https://developers.google.com/machine-learning/guides/rules-of-ml)
- Docker "Get started" (HTTP 200). — [docs.docker.com/get-started](https://docs.docker.com/get-started/)
- FastAPI Tutorial - User Guide (HTTP 200). — [fastapi.tiangolo.com/tutorial](https://fastapi.tiangolo.com/tutorial/)
- GitHub Actions quickstart has moved to /actions/get-started/quickstart; the old /writing-workflows/quickstart URL redirects. — [docs.github.com](https://docs.github.com/en/actions/get-started/quickstart)

### Inferences
- A practical LLMOps block could be: FastAPI tutorial, then Docker get-started, then a GitHub Actions quickstart (CI running pytest and an eval script), then Evidently's LLM-evals course or W&B "LLM apps: Evaluation", with LLM Zoomcamp modules 4-5 (evaluation, monitoring) as the capstone. On an 8 GB Windows laptop, Docker Desktop may be heavy. A cloud dev environment is an alternative, but its free-tier limits were not verified here.

### Gaps
- Whether Made With ML content itself was updated after 2023: the repo shows a push on 2026-03-04, but content currency was not audited.
- Evidently course launch dates, and W&B certificates.

## Q8. Essential free readings and key papers (with verified links)

### Takeaway
All the requested essays are live. Anthropic's "Building effective agents" moved from /research/ to /engineering/, and the old URL redirects. The arXiv IDs below were verified against arXiv titles. Papers with Code shut down on 24 July 2025, and paperswithcode.com now redirects to Hugging Face's Trending Papers.

### Cited Findings
**Essays and guides (all HTTP 200 on 2026-09-24)**
- Anthropic, "Building effective agents" (Dec 2024; the /research/ URL redirects to /engineering/). — [anthropic.com](https://www.anthropic.com/engineering/building-effective-agents)
- Anthropic, "Effective context engineering for AI agents". — [anthropic.com](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Anthropic, "Writing effective tools for agents — with agents". — [anthropic.com](https://www.anthropic.com/engineering/writing-tools-for-agents)
- Lilian Weng, "LLM Powered Autonomous Agents" (2023-06-23). — [lilianweng.github.io](https://lilianweng.github.io/posts/2023-06-23-agent/)
- Chip Huyen, "Agents" (2025-01-07). — [huyenchip.com](https://huyenchip.com/2025/01/07/agents.html); "Building A Generative AI Platform" (2024-07-25). — [huyenchip.com](https://huyenchip.com/2024/07/25/genai-platform.html); free book "Introduction to Machine Learning Interviews". — [huyenchip.com/ml-interviews-book](https://huyenchip.com/ml-interviews-book/). Note that /ml-interviews-book/contents/ returns 404, so link the root.
- Eugene Yan, "Patterns for Building LLM-based Systems & Products". — [eugeneyan.com](https://eugeneyan.com/writing/llm-patterns/)
- Hamel Husain, "Your AI Product Needs Evals" — [hamel.dev](https://hamel.dev/blog/posts/evals/); "A Field Guide to Rapidly Improving AI Products" — [hamel.dev](https://hamel.dev/blog/posts/field-guide/); evals FAQ — [hamel.dev](https://hamel.dev/blog/posts/evals-faq/); LLM-as-a-judge guide — [hamel.dev](https://hamel.dev/blog/posts/llm-judge/)
- "What We've Learned From A Year of Building with LLMs" (applied-llms.org). — [applied-llms.org](https://applied-llms.org/)
- Prompting Guide (DAIR.AI). — [promptingguide.ai](https://www.promptingguide.ai/)
- OpenAI, "A practical guide to building agents" (PDF). — [cdn.openai.com](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf)

**Key papers (arXiv ID, title as on arXiv, and first-version date, all verified)**
- Attention Is All You Need (2017-06-12). — [arXiv:1706.03762](https://arxiv.org/abs/1706.03762)
- BERT (2018-10-11). — [arXiv:1810.04805](https://arxiv.org/abs/1810.04805)
- GPT-2, "Language Models are Unsupervised Multitask Learners": not on arXiv; the OpenAI PDF returns 200. — [cdn.openai.com PDF](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)
- GPT-3, "Language Models are Few-Shot Learners" (2020-05-28). — [arXiv:2005.14165](https://arxiv.org/abs/2005.14165)
- Scaling Laws for Neural Language Models (Kaplan et al., 2020-01-23). — [arXiv:2001.08361](https://arxiv.org/abs/2001.08361)
- Chinchilla, "Training Compute-Optimal Large Language Models" (2022-03-29). — [arXiv:2203.15556](https://arxiv.org/abs/2203.15556)
- InstructGPT, "Training language models to follow instructions with human feedback" (2022-03-04). — [arXiv:2203.02155](https://arxiv.org/abs/2203.02155)
- Chain-of-Thought Prompting Elicits Reasoning in LLMs (2022-01-28). — [arXiv:2201.11903](https://arxiv.org/abs/2201.11903)
- ReAct (2022-10-06). — [arXiv:2210.03629](https://arxiv.org/abs/2210.03629)
- RAG, "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" (2020-05-22). — [arXiv:2005.11401](https://arxiv.org/abs/2005.11401)
- LoRA (2021-06-17). — [arXiv:2106.09685](https://arxiv.org/abs/2106.09685)
- QLoRA (2023-05-23). — [arXiv:2305.14314](https://arxiv.org/abs/2305.14314)
- DPO (2023-05-29). — [arXiv:2305.18290](https://arxiv.org/abs/2305.18290)
- DeepSeek-R1 (2025-01-22). — [arXiv:2501.12948](https://arxiv.org/abs/2501.12948)
- Optional extras: Toolformer [arXiv:2302.04761](https://arxiv.org/abs/2302.04761); Lost in the Middle [arXiv:2307.03172](https://arxiv.org/abs/2307.03172); FlashAttention [arXiv:2205.14135](https://arxiv.org/abs/2205.14135); Constitutional AI [arXiv:2212.08073](https://arxiv.org/abs/2212.08073); The Llama 3 Herd of Models [arXiv:2407.21783](https://arxiv.org/abs/2407.21783); surveys "A Survey of Large Language Models" [arXiv:2303.18223](https://arxiv.org/abs/2303.18223) and "Large Language Models: A Survey" [arXiv:2402.06196](https://arxiv.org/abs/2402.06196)

**Paper discovery**
- paperswithcode.com now redirects to huggingface.co/papers/trending (curl-verified 2026-09-24). — [huggingface.co/papers](https://huggingface.co/papers); [HF changelog: Trending Papers](https://huggingface.co/changelog/trending-papers)
- Papers With Code "sunsetted on July 24, 2025". HF and Meta partnered on the replacement, and the historical data is kept in the paperswithcode-data repo. These are secondary sources. — [Coursera article](https://www.coursera.org/articles/papers-with-code); [HyperAI news](https://hyper.ai/en/news/42900); [GitHub issue #116](https://github.com/paperswithcode/paperswithcode-data/issues/116); [paperswithcode-data](https://github.com/paperswithcode/paperswithcode-data)

### Inferences
- A beginner reading order that follows the curriculum: Attention -> GPT-2 -> GPT-3 -> Scaling laws/Chinchilla -> InstructGPT -> LoRA/QLoRA -> RAG -> CoT -> ReAct -> DPO -> DeepSeek-R1. Pair each with an explainer (Illustrated Transformer/GPT-2, Umar Jamil's LoRA/DPO/RLHF videos, The Illustrated DeepSeek-R1).

### Gaps
- No primary Meta or Hugging Face announcement for the Papers with Code shutdown was fetched; the date comes from secondary sources.

## Q9. Job-skills demand 2025-2026, dominant agent frameworks, and protocol/standard status

### Takeaway
The best dataset found is Alexey Grigorev's analysis of **6,964 "AI Engineer" postings from Feb-Aug 2026**, which includes India. RAG and agents are baseline requirements; evals, observability and guardrails are the differentiator; MCP and LangGraph are the fastest risers. Fine-tuning is a niche: it is absent from 84.6% of roles' responsibilities. Postings also expect Python, cloud, Docker/K8s and CI/CD. LangChain+LangGraph lead the frameworks by a wide margin. MCP and AGENTS.md are now governed by the Linux Foundation's Agentic AI Foundation, A2A is v1.0 under the Linux Foundation, and Agent Skills is an open standard adopted by most coding agents.

### Cited Findings
**Job-postings dataset (primary: Grigorev, "AI Engineering Field Guide")**
- Dataset: "Generated from 6,964 job descriptions extracted from builtin.com". The search keyword was "AI Engineer" in LA (Global), New York, London, Amsterdam, Berlin and India, across "eight monthly scrapes between February 4 and August 25, 2026", with no overlapping job IDs. Skills were LLM-extracted and canonicalized, so "Treat all skill percentages as a floor". — [role/02-skills.md](https://github.com/alexeygrigorev/ai-engineering-field-guide/blob/main/role/02-skills.md)
- Role mix: AI-First 4,874 (70.0%), AI-Support 1,685 (24.2%), classic ML 340 (4.9%). Applied/production roles are 97.1% and research roles 2.9%. — [same](https://github.com/alexeygrigorev/ai-engineering-field-guide/blob/main/role/02-skills.md)
- GenAI skills as a share of all jobs: LLMs 62.2%; AI agents 41.6% (any agent skill 55.4%); RAG 39.8%; prompt engineering 34.7%; agentic workflows 30.4%; LangChain 22.0%; OpenAI API 15.2%; Anthropic API 14.4%; MCP 14.1%; LangGraph 13.8%; LlamaIndex 8.3%. — [same](https://github.com/alexeygrigorev/ai-engineering-field-guide/blob/main/role/02-skills.md)
- Within AI-First roles: agents (any) 71.6%, RAG 54.8%, prompt engineering 46.5%, fine-tuning 24.8%, Python 75.6%, AWS 45.2%, CI/CD 35.4%, Docker 24.6%, Kubernetes 22.2%. — [same](https://github.com/alexeygrigorev/ai-engineering-field-guide/blob/main/role/02-skills.md)
- Languages (all jobs): Python 70.8%, TypeScript 19.3%, Java 17.7%, SQL 14.4%, JavaScript 11.6%, Go 11.5%. Cloud: AWS 40.3%, Azure 29.6%, GCP 27.4%. Ops (counts): CI/CD 2,560, Docker 1,700, Kubernetes 1,666, observability 1,547, MLOps 1,201. Web: APIs 1,843, REST 1,120, React 1,033, FastAPI 680. Databases: vector databases 1,647, PostgreSQL 775, Pinecone 510, Weaviate 359. — [same](https://github.com/alexeygrigorev/ai-engineering-field-guide/blob/main/role/02-skills.md)
- "86.8% of AI-First roles require skills BEYOND just GenAI". GenAI + Ops is 70.6%, GenAI + Web 58.4%, and pure GenAI only 3.9%. — [same](https://github.com/alexeygrigorev/ai-engineering-field-guide/blob/main/role/02-skills.md)
- Evaluation: "59.7% of AI-First roles require evaluation-related skills". Breakdown: LLM evaluation 30.9%, observability 24.5%, guardrails 17.9%, monitoring 14.1%, model evaluation 14.1%. "This is the differentiator. RAG and agents are now baseline expectations." — [same](https://github.com/alexeygrigorev/ai-engineering-field-guide/blob/main/role/02-skills.md)
- Fine-tuning: 27.3% of AI-First roles mention it anywhere, but it is the primary responsibility in only 3.6%, secondary in 11.9%, and absent from responsibilities in 84.6%. "Fine-tuning is optional for most AI Engineers. Focus on RAG and agents first." — [same](https://github.com/alexeygrigorev/ai-engineering-field-guide/blob/main/role/02-skills.md)
- Frameworks (share of all jobs): LangChain 22.0%, LangGraph 13.8%, LlamaIndex 8.3%, CrewAI 6.7%, AutoGen 5.3%, Semantic Kernel 3.2%, DSPy 0.8%. "Frameworks travel together rather than compete"; 700 jobs ask for both LangChain and LangGraph. — [same](https://github.com/alexeygrigorev/ai-engineering-field-guide/blob/main/role/02-skills.md)
- Trends from Feb to Aug 2026: LangGraph 7.4% -> 17.2%; MCP 9.9% -> 17.6% ("the clearest steady riser"); PyTorch 20.8% -> 15.3%; fine-tuning 17.1% -> 12.7%. The integrator stack (RAG/agents/APIs) rose 80.0% -> 88.0% while the trainer stack fell 37.5% -> 30.4%. Guardrails rose 10.2% -> 15.2%, LLM-native eval tools (LangSmith, Langfuse, ...) 26.7% -> 30.1%, and AI coding tools as a listed skill 7.6% -> 12.8% ("noisy"). Among jobs using any agent framework, LangGraph's share rose 37.7% -> 61.4%. — [role/07-trends.md](https://github.com/alexeygrigorev/ai-engineering-field-guide/blob/main/role/07-trends.md)
- New titles: "Agentic AI Engineer and Generative AI Engineer are both 100% AI-First and did not exist as titles at the start of the dataset"; "AI Engineer" is 92% AI-First. — [role/02-skills.md](https://github.com/alexeygrigorev/ai-engineering-field-guide/blob/main/role/02-skills.md)
- The same repo has interview-prep material: interview process, questions, how to get hired, and take-home assignments. — [interview/](https://github.com/alexeygrigorev/ai-engineering-field-guide/tree/main/interview)
- Secondary corroboration (lower quality, edtech blog): the 11 most requested AI skills in 2026 postings are prompt engineering, Python/SQL, ML, RAG, MLOps, AI security, agentic AI, data engineering, LLM fine-tuning, multimodal AI and AI infrastructure. — [TripleTen blog](https://tripleten.com/blog/posts/ai-skills)
- India-specific claims come only from low-reliability edtech or aggregator blogs and could not be traced to primary Naukri/NASSCOM reports, so all are UNVERIFIED: "Naukri reports over 82,000 AI job postings in July 2026"; "NASSCOM-BCG ... AI engineer roles grew 67% year-on-year"; "fresher hiring in AI/ML grew 22%". — [Masai School blog](https://www.masaischool.com/blog/the-2026-ai-job-market-report-india-edition/); [Fireblaze blog](https://fireblazeaischool.in/blogs/ai-job-market-in-india-2026-what-the-data-shows/); [CareerIndia](https://www.careerindia.com/news/genai-hiring-surge-india-2026-top-skills-salary-packages-cities-011-65139.html)

**AI security**
- The OWASP Top 10 for LLM Applications (2025) runs LLM01 to LLM10: Prompt Injection, Sensitive Information Disclosure, Supply Chain, Data and Model Poisoning, Improper Output Handling, Excessive Agency, System Prompt Leakage, Vector and Embedding Weaknesses, Misinformation, Unbounded Consumption. — [genai.owasp.org/llm-top-10](https://genai.owasp.org/llm-top-10/)
- The OWASP Top 10 for Agentic Applications (for 2026) was released 9 Dec 2025. It is peer-reviewed by more than 100 experts and uses risk IDs ASI01 to ASI10. — [OWASP GenAI announcement](https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/); [resource page](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- Free learning material on this topic: DLAI "Red Teaming LLM Applications", "Safe and reliable AI via guardrails" and "Governing AI Agents" (Q4); Microsoft ai-agents-for-beginners lesson 18 "Securing AI Agents" and generative-ai-for-beginners lesson 13 (Q5).

**Agent frameworks: GitHub popularity on 2026-09-24 (stars, last push)**
- langchain-ai/langchain 146,956 ("The agent engineering platform") — [GitHub](https://github.com/langchain-ai/langchain); langchain-ai/langgraph 42,201 — [GitHub](https://github.com/langchain-ai/langgraph)
- microsoft/autogen 61,130 (last push 2026-04-15, i.e. maintenance mode) — [GitHub](https://github.com/microsoft/autogen); crewAIInc/crewAI 58,958 — [GitHub](https://github.com/crewAIInc/crewAI); run-llama/llama_index 52,306 (now "the document processing platform for AI") — [GitHub](https://github.com/run-llama/llama_index)
- openai/openai-agents-python 29,668 — [GitHub](https://github.com/openai/openai-agents-python); huggingface/smolagents 29,463 — [GitHub](https://github.com/huggingface/smolagents); google/adk-python 21,620 — [GitHub](https://github.com/google/adk-python); pydantic/pydantic-ai 20,133 — [GitHub](https://github.com/pydantic/pydantic-ai); microsoft/agent-framework 13,763 — [GitHub](https://github.com/microsoft/agent-framework); anthropics/claude-agent-sdk-python 8,153 — [GitHub](https://github.com/anthropics/claude-agent-sdk-python); AWS Strands: `strands-agents/sdk-python` now resolves to **`strands-agents/harness-sdk`** (renamed; 7,929 stars) — [GitHub](https://github.com/strands-agents/harness-sdk)
- Microsoft Agent Framework 1.0 GA shipped 3 Apr 2026 for Python and .NET. It is "the direct successor" to Semantic Kernel and AutoGen, and AutoGen now gets bug and security fixes only. — [Visual Studio Magazine](https://visualstudiomagazine.com/articles/2026/04/06/microsoft-ships-production-ready-agent-framework-1-0-for-net-and-python.aspx); [docs](https://learn.microsoft.com/en-us/agent-framework/overview/)
- Docs URL moves verified by curl: Claude Agent SDK docs moved to code.claude.com — [code.claude.com/docs/en/agent-sdk/overview](https://code.claude.com/docs/en/agent-sdk/overview); Google ADK docs moved to adk.dev — [adk.dev](https://adk.dev/); PydanticAI docs moved to pydantic.dev — [pydantic.dev/docs/ai/overview](https://pydantic.dev/docs/ai/overview/); LlamaIndex docs moved to developers.llamaindex.ai — [developers.llamaindex.ai](https://developers.llamaindex.ai/python/framework/); OpenAI Agents SDK — [openai.github.io/openai-agents-python](https://openai.github.io/openai-agents-python/); smolagents — [huggingface.co/docs/smolagents](https://huggingface.co/docs/smolagents/index); CrewAI — [docs.crewai.com](https://docs.crewai.com/); LangGraph — [langchain-ai.github.io/langgraph](https://langchain-ai.github.io/langgraph/)

**Protocols and standards**
- The Agentic AI Foundation (AAIF), under the Linux Foundation, was formed 9 Dec 2025. Its founding projects are Anthropic's MCP, Block's goose and OpenAI's AGENTS.md. — [Linux Foundation press release](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation); [OpenAI](https://openai.com/index/agentic-ai-foundation/)
- AAIF runs MCP Dev Summits in 2026, and AGNTCon + MCPCon North America is on 22-23 Oct 2026 in San Jose. — [LF Events](https://events.linuxfoundation.org/2026/04/17/agentic-ai-foundation-announces-global-2026-events-program-anchored-by-agntcon-mcpcon-north-america-and-europe/)
- AAIF has launched an "MCPA" certification to validate MCP expertise. Price and format are UNVERIFIED and probably paid. — [LF press](https://www.linuxfoundation.org/press/agentic-ai-foundation-launches-mcpa-certification-to-validate-mcp-expertise)
- The current MCP spec version is **2026-07-28**: modelcontextprotocol.io redirects to /docs/2026-07-28/. Microsoft's curriculum summarizes the release as "Stateless protocol, Extensions framework, and feature deprecations", with CIMD registration preferred over the deprecated DCR. Official docs now also cover "MCP Apps". The spec repo has 9,291 stars. — [modelcontextprotocol.io](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro); [mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners); [spec repo](https://github.com/modelcontextprotocol/modelcontextprotocol)
- A2A is at **v1.0** (the docs have a "What's New in v1.0" page). "A2A was originally developed by Google and donated to the Linux Foundation. It is maintained by a Technical Steering Committee with representatives from AWS, Cisco, Google, IBM Research, Microsoft, Salesforce, SAP, and ServiceNow." The repo has 25,912 stars. — [a2a-protocol.org/latest](https://a2a-protocol.org/latest/); [GitHub](https://github.com/a2aproject/A2A)
- **Agent Skills** is "a lightweight, open format" in which a skill is a folder with a `SKILL.md` (name + description metadata plus instructions, optionally with scripts, references and assets), loaded by progressive disclosure. It was "originally developed by Anthropic, released as an open standard". Listed clients include Claude Code, Claude, ChatGPT & Codex, Gemini CLI, GitHub Copilot, VS Code, Cursor, OpenCode, OpenHands, Goose, Junie, Kiro, Roo Code, Spring AI, Databricks and Snowflake. The spec repo has 25,641 stars. — [agentskills.io](https://agentskills.io/home); [GitHub](https://github.com/agentskills/agentskills)
- **AGENTS.md** is "a simple, open format for guiding coding agents" (repo 24,587 stars) and an AAIF founding project, reported as "adopted by more than 60,000 open source projects and agent frameworks". — [agents.md](https://agents.md/); [GitHub](https://github.com/agentsmd/agents.md); [LF press](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation)

### Inferences
- Curriculum weighting implied by the data: weight (1) Python + FastAPI + SQL/vector DBs + Docker/CI (the "full-stack" base), (2) RAG, (3) agents with tool calling, LangGraph and MCP, and (4) evals, observability and guardrails most heavily. Fine-tuning and training internals are best treated as understanding plus one portfolio project, not the core. This matches Grigorev's own suggested path: Foundation -> LLM basics -> RAG -> Frameworks -> Agents (LangGraph, MCP) -> Evaluation -> Production.
- Framework choice for teaching: LangGraph (market share plus fastest growth) as the main framework, then one lightweight SDK (OpenAI Agents SDK, PydanticAI or smolagents) to show the pattern is portable. MCP should be a required module. A2A, Agent Skills and AGENTS.md fit as one "agent protocols and context engineering" week.
- The learner's Java background is a plus, since Java appears in 17.7% of postings, and Spring AI supports Agent Skills.

### Gaps
- No primary India-only posting dataset (for example Naukri JobSpeak or a NASSCOM report PDF) was verified. Grigorev's dataset includes India, but the per-location breakdown was not extracted.
- No large posting dataset was found that names the newer SDKs (OpenAI Agents SDK, Google ADK, Claude Agent SDK, PydanticAI, smolagents). Their relative demand is inferred only from GitHub stars, which measure developer interest rather than hiring.
- Context engineering as an explicit job-posting keyword was not measured in the dataset reviewed.
