# Free compute, free LLM APIs, local LLMs and free deployment/supporting services for a zero-budget AI learner (state as of 2026-09-24)

Conventions used in these notes:
- "Checked 2026-09-24" = the official page was fetched on the research date (2026-09-24) and the number was read directly from it.
- "(secondary)" = number comes from a third-party blog/aggregator, not the vendor; treat as approximate.
- "CARD?" = whether a credit/debit card is needed. "No card" means the official page or a reliable source says so; "unverified" means no source found.
- Several services changed materially in 2026 (GitHub Models retired, Hugging Face Spaces paywalled Gradio/Docker creation, Groq removed Llama models, Cerebras free tier became a "Free Trial"). These are flagged inline.

## 1. Free notebooks / GPUs / cloud compute (Colab, Kaggle, Lightning, HF Spaces/ZeroGPU, Modal, Codespaces, Studio Lab, Paperspace, Deepnote, big-cloud free tiers)

### Takeaway
(in progress — see findings below)

### Cited Findings

**Google Colab (free tier)**
- Official FAQ (no "last updated" date on page; checked 2026-09-24): "notebooks can run for at most 12 hours, depending on availability and your usage patterns"; runtimes are also terminated when idle (exact idle timeout not published); "The types of GPUs and TPUs that are available in Colab vary over time"; resources and limits "fluctuate" and are not guaranteed; no fixed GPU-hour quota is published. — [Colab FAQ](https://research.google.com/colaboratory/faq.html)
- Disallowed on free Colab (FAQ): file hosting/media serving/web services, torrents/P2P, crypto mining, remote control (SSH, remote desktops), "bypassing the notebook UI to interact primarily via a web UI", distributed-computing workers, DoS, password cracking, deepfakes. Practical implication: you cannot use free Colab to host a demo server or run a UI like Gradio as a long-running web service. — [Colab FAQ](https://research.google.com/colaboratory/faq.html)
- Paid options exist (Colab Pro / Pro+ monthly compute units; Pay As You Go compute units) — PAID, flag as not needed for this plan. — [Colab FAQ](https://research.google.com/colaboratory/faq.html)

**Kaggle Notebooks** (official docs, "at time of writing", checked 2026-09-24)
- Session limits: "12 hours execution time for CPU and GPU notebook sessions and 9 hours for TPU notebook sessions". — [Kaggle Notebooks docs – Technical Specifications](https://www.kaggle.com/docs/notebooks)
- Disk: "20 Gigabytes of auto-saved disk space (/kaggle/working)" plus extra scratch disk that is not saved after the session. — [Kaggle Notebooks docs](https://www.kaggle.com/docs/notebooks)
- Hardware: CPU session = 4 CPU cores, 30 GB RAM; P100 session = 1x NVIDIA Tesla P100, 4 CPU cores, 29 GB RAM; "T4 x2" session = 2x NVIDIA Tesla T4, 4 CPU cores, 29 GB RAM; TPU 1VM = 96 CPU cores, 330 GB RAM (docs elsewhere call the TPU "TPU v3-8"). — [Kaggle Notebooks docs](https://www.kaggle.com/docs/notebooks)
- Idle: "While editing a Notebook, you are provided with 20 minutes of idle time for your interactive session." Committed runs ("Save & Run All") execute in a separate session and keep running without the browser. — [Kaggle Notebooks docs](https://www.kaggle.com/docs/notebooks)
- Weekly GPU quota: "The quota resets weekly and is 30 hours or sometimes higher depending on demand and resources." — [Kaggle Efficient GPU Usage docs](https://www.kaggle.com/docs/efficient-gpu-usage)
- Weekly TPU quota ~20 h/week (secondary; not found on the official page fetched). — [aimultiple.com free cloud GPU](https://aimultiple.com/free-cloud-gpu) (secondary)
- Experimental: Colab Pro / Pro+ subscribers who link accounts get "15 and 30 hours of extra GPU hours per week" on Kaggle (PAID route, only relevant if someone already has Colab Pro). — [Kaggle Notebooks docs](https://www.kaggle.com/docs/notebooks)
- Persistence: outputs in /kaggle/working (up to 20 GB) are saved with each notebook version and can be attached as input to later notebooks; datasets/models can be attached as inputs. — [Kaggle Notebooks docs](https://www.kaggle.com/docs/notebooks)

**Lightning AI** (pricing page rendered 2026-09-24)
- Free plan $0 ("Students, researchers, hobbyists"): "up to 30 credits"; "Get up to 80 free GPU hours to start" (asterisked: "Free GPU hrs with up to 30 free credits to start"); "Run 1 Studio free 24/7. No credit card. No commitments." but "Free Studios run 24/7 but require restart every 4 hours"; 32-core CPU Studios; single GPUs; up to 2 concurrent GPUs; "Persistent storage (50 GB limit)"; "15 req/min to our model APIs". — [Lightning AI pricing](https://lightning.ai/pricing)
- Free GPU hours implied by the 30 credits (from the pricing table's "Free hours to start" column): T4 16 GB ≈ 75 h; L4 24 GB ≈ 31 h; A100 40 GB ≈ 10 h; L40S ≈ 5 h; A100 80 GB ≈ 5 h; RTX Pro 6000 ≈ 2 h. On-demand T4 price shown: $0.55/GPU-hr (PAID beyond credits). — [Lightning AI pricing](https://lightning.ai/pricing)
- CONFLICT: third-party 2026 guides describe the free tier as "15 Lightning credits per month (~22 T4 hours)" and say phone verification (not card) is required; the official page (2026-09-24) says "up to 30 credits ... to start", which reads like a one-time starter grant rather than monthly. Treat monthly refresh as unconfirmed. — [aicreditmart Lightning guide](https://aicreditmart.com/ai-credits-providers/lightning-ai-free-plan-22-gpu-hours-month-guide-2026/) (secondary) vs [Lightning AI pricing](https://lightning.ai/pricing)

**Hugging Face Spaces hardware & ZeroGPU** (docs checked 2026-09-24) — MAJOR 2026 CHANGE
- "Static Spaces are free for everyone. Gradio and Docker Spaces run on compute and require a paid plan to create: PRO for personal accounts, Team or Enterprise for organizations. Free personal accounts in good standing can still host up to 2 Gradio Spaces running on ZeroGPU." — [HF Spaces Overview](https://huggingface.co/docs/hub/spaces-overview)
- Forum report dated 2026-07-09: on a brand-new free account "The only available runtime is ZeroGPU. Docker is marked as Paid. CPU Basic cannot be selected during creation", and downgrading a ZeroGPU Space to CPU Basic requires PRO. — [HF Forums thread, 2026-07-09](https://discuss.huggingface.co/t/new-free-accounts-cannot-create-cpu-basic-gradio-spaces-only-zerogpu-available/177629)
- CPU Basic hardware spec: 2 vCPU, 16 GB RAM, 50 GB non-persistent disk, "no hourly cost" (but creating a compute Space now needs a paid plan, see above). — [HF Spaces Overview](https://huggingface.co/docs/hub/spaces-overview); [HF Spaces GPU upgrades](https://huggingface.co/docs/hub/spaces-gpus)
- Sleep: Spaces on free hardware "go to sleep if inactive for more than a set time (currently, 48 hours)"; a visitor restarts it automatically. — [HF Spaces GPU upgrades](https://huggingface.co/docs/hub/spaces-gpus)
- ZeroGPU hardware: dynamically allocated "NVIDIA RTX Pro 6000 Blackwell" GPUs — default "large" = half GPU 48 GB VRAM (1x quota cost), "xlarge" = full GPU 96 GB (2x quota cost). PyTorch-only-ish; limited compatibility vs standard GPU Spaces. — [HF ZeroGPU docs](https://huggingface.co/docs/hub/spaces-zerogpu)
- ZeroGPU usage: "ZeroGPU Spaces are available to use for free to all users"; hosting: "Free personal accounts: accounts in good standing (verified email, account older than 30 days) can host up to 2 ZeroGPU Spaces for free"; PRO hosts up to 10. — [HF ZeroGPU docs](https://huggingface.co/docs/hub/spaces-zerogpu)
- ZeroGPU daily quota: PRO gets "8x more daily quota, including up to 40 minutes of RTX Pro 6000 Blackwell compute" → implies ~5 min/day for free users; a 2026 secondary guide states "5 minutes of ZeroGPU time a day" for free accounts. — [HF PRO page](https://huggingface.co/pro); [eesel.ai HF pricing 2026](https://www.eesel.ai/blog/hugging-face-pricing) (secondary)
- HF PRO = $9/month (PAID): 8x Spaces quota, 20x inference credits, 1 TB private storage, 10 ZeroGPU Spaces, Gradio & Docker Spaces on compute, Dev Mode. — [HF PRO page](https://huggingface.co/pro); [HF pricing](https://huggingface.co/pricing)

**Modal** (pricing page checked 2026-09-24)
- Starter plan "$0 + compute / month", "$30 / month free compute", 3 workspace seats, "100 containers + 10 GPU concurrency", limited scheduled/web functions. Academic grants: "Graduate students, labs, and researchers can get up to $10k free compute credits" (application). — [Modal pricing](https://modal.com/pricing)
- GPU per-second prices shown, e.g., A10 $0.000306/s (~$1.10/h), L40S $0.000542/s, A100 40 GB $0.000583/s, H100 $0.001097/s (PAID beyond free credit). — [Modal pricing](https://modal.com/pricing)

**GitHub Codespaces** (checked 2026-09-24)
- Personal accounts on GitHub Free: 120 core-hours/month compute + 15 GB-month storage; GitHub Pro: 180 core-hours + 20 GB-month. Usage beyond is billed to the account (so a budget of $0 blocks overage). A 2-core machine therefore gives ~60 wall-clock hours/month; 4-core ~30 h. — [GitHub Codespaces billing](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces)

**Modal — CARD REQUIRED**
- Modal billing docs: "Note that you must have a payment method on file in order to use Modal." So the $30/month Starter credit is not usable by a no-card learner. — [Modal billing docs](https://modal.com/docs/guide/billing)

**Paperspace (DigitalOcean) Gradient**
- Pricing page (checked 2026-09-24) still shows a "Free" plan ($0, "FREE GPU"): public projects only, "Auto-shutdown (12 hour limit)", 5 GB storage, "Basic instances"; instances outside free tier billed hourly. Availability of free GPUs in practice and card requirement not verified (historically free GPUs were frequently unavailable). — [Paperspace pricing](https://www.paperspace.com/pricing)

**Deepnote**
- Free plan: "Unlimited Basic machines with 5 GB RAM, 2 vCPU" (CPU only); paid tiers have a 14-day trial. — [Deepnote pricing](https://deepnote.com/pricing)

**Amazon SageMaker Studio Lab**
- The FAQ URL returned an HTTP 403 (CloudFront "request blocked") when fetched on 2026-09-24; current status not confirmed (see Gaps). — [Studio Lab FAQ](https://studiolab.sagemaker.aws/faq)

**Big-cloud free tiers — card requirements (checked 2026-09-24)**
- Google Cloud: Free Trial = $300 credit for 90 days; "During the sign up, you must provide a credit card or other payment method that is valid for the period of the Free Trial" (bank-account verification in some countries; a temporary authorization hold is placed). Notably "The $300 credit can't pay for Gemini API in AI Studio costs." — CARD REQUIRED. — [Google Cloud free features](https://cloud.google.com/free/docs/free-cloud-features)
- AWS: new-customer Free plan gives $100 credits immediately + up to $100 more earned, "up to $200 over 6 months"; the account "closes on its own 6 months after you open it or when your credits run" out unless upgraded. FAQ Q12: "AWS requires a valid payment method to verify your identity and prevent abuse" (not charged until upgrade). — CARD REQUIRED. — [AWS Free Tier](https://aws.amazon.com/free/); [AWS Free Tier FAQs](https://aws.amazon.com/free/free-tier-faqs/)
- Microsoft Azure free account: $200 credit for 30 days + 12 months of free amounts of 20+ services + always-free services; "All you need is a phone number, a credit card or a debit card (non-prepaid), and a Microsoft account or a GitHub account." — CARD REQUIRED. — [Azure account](https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account); [Azure free services](https://azure.microsoft.com/en-us/pricing/free-services)
- Azure for Students: "Free (no credit card required) with a $100 credit, which can be used within 12 months"; "Use your school email to sign up and renew yearly while you're a student." — NO CARD, but requires a valid school/student email (a graduate who has lost the student email likely cannot use it). — [Azure for Students](https://azure.microsoft.com/en-us/free/students)
- Oracle Cloud Free Tier (Always Free incl. Arm Ampere A1 compute + 30-day trial credits): Oracle's FAQ explains why "credit or debit card information" is required at signup (identity verification); "We do not accept debit cards with a PIN or virtual, single-use, or prepaid cards." Idle accounts (30+ days) "may be deemed abandoned"; "out of host capacity" errors are common for Always Free shapes. — CARD REQUIRED. — [Oracle Cloud Free Tier FAQ](https://www.oracle.com/cloud/free/faq/)

### Inferences
- (in progress)

### Gaps
- (in progress)

## 2. Free LLM APIs (Gemini/AI Studio, Groq, OpenRouter, GitHub Models, Mistral, Cerebras, HF Inference Providers, NVIDIA NIM, Cohere, others)

### Takeaway
(in progress)

### Cited Findings

**Google Gemini API / AI Studio**
- Rate-limit doc (last updated 2026-09-02) no longer prints a free-tier table: "Rate limits depend on a variety of factors (such as your usage tier) and can be viewed in Google AI Studio"; tiers: Free ("Active project or free trial"), Tier 1 ("Set up and link an active billing account"), Tier 2 ($100 paid + 3 days), Tier 3 ($1,000 paid + 30 days); limits are per project, not per key; "Specified rate limits are not guaranteed". — [Gemini API rate limits](https://ai.google.dev/gemini-api/docs/rate-limits)
- Pricing page (last updated 2026-09-23) — models with a "Free of charge" free tier: Gemini 3.8 Flash (newest, "now available"), 3.7 Flash, 3.6 Flash, 3.5 Flash, 3.5 Flash-Lite, 3.1 Flash-Lite, 3 Flash Preview, 2.5 Pro, 2.5 Flash, 2.5 Flash-Lite, Gemini Embedding 2, Gemma 4. Free tier "Not available" for Gemini 3.1 Pro and 3.1 Pro Preview (and several image/omni models). — [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing)
- Data-use caveat: free tier row "Used to improve our products: Yes"; paid tier "No". Free plan bullets: "Limited access to certain models", "Free input & output tokens", "Google AI Studio access", "Content used to improve our products". — [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing)
- Grounding with Google Search is "Not available" on the free tier for Gemini 3.8 Flash (paid: 5,000 free searches/month shared across Gemini 3.x, then $14/1,000) and for 2.5 Pro (paid: 1,500 RPD free then $35/1,000). — [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing)
- Dec 2025 change: around 6–7 Dec 2025 Google cut free-tier quotas without prior announcement — Gemini 2.5 Flash reportedly dropped from ~250 to ~20 requests/day and the Gemini 2.5 Pro free quota was pulled; a Google representative was quoted: "We dialed down the 2.5 Pro free limits which was only intended to be available for a weekend originally. Due to high demand on 3.0 Pro and other models, had to reallocate capacity." — [Yahoo Tech](https://tech.yahoo.com/ai/gemini/articles/gemini-slashed-free-api-limits-140016369.html); [aifreeapi.com Dec 2025 update](https://www.aifreeapi.com/en/posts/gemini-api-free-tier-rate-limits) (secondary)
- 2026 (secondary): "free access to Pro-tier models ending on April 1 [2026]"; Gemini 3.5 Flash ≈ 20 free RPD and 3.5 Flash-Lite ≈ 500 RPD, 10–15 RPM; Google "no longer publishes fixed request-per-day numbers". CONFLICT: the official pricing page (2026-09-23) still lists Gemini 2.5 Pro as "Free of charge" on the free tier — actual per-project quota may be 0 or tiny; check AI Studio's rate-limit page. — [QuestLoops 2026](https://questloops.com/blog/how-to-use-google-gemini-for-free-in-2026-api-limits-explained) (secondary); [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing)

**Groq (GroqCloud)** — checked 2026-09-24
- Free Plan limits (official table): openai/gpt-oss-120b, openai/gpt-oss-20b, openai/gpt-oss-safeguard-20b, qwen/qwen3.8-27b → each 30 RPM, 1K RPD, 8K TPM, 200K TPD; whisper-large-v3 and -turbo → 20 RPM, 2K RPD, 7.2K audio-sec/hour, 28.8K audio-sec/day; canopylabs orpheus TTS → 10 RPM, 100 RPD, 1.2K TPM, 3.6K TPD; llama-prompt-guard-2 (22m/86m) → 30 RPM, 14.4K RPD. Limits are per organization; cached tokens don't count. — [Groq rate limits](https://console.groq.com/docs/rate-limits)
- 2026 model removals (apply to free and developer tiers): qwen/qwen3-32b and meta-llama/llama-4-scout shut down 2026-07-17; llama-3.1-8b-instant and llama-3.3-70b-versatile shut down 2026-08-16 (replacements: gpt-oss-20b / gpt-oss-120b or qwen3.6-27b); qwen/qwen3.6-27b replaced by qwen/qwen3.8-27b on 2026-09-14; groq/compound and compound-mini decommissioned 2026-09-21. Tutorials using "llama-3.1-8b-instant"/"llama3-70b" model IDs are now broken. — [Groq deprecations](https://console.groq.com/docs/deprecations); [Groq models](https://console.groq.com/docs/models)
- NVIDIA deal: on 24 Dec 2025 Groq and NVIDIA announced a non-exclusive inference-technology licensing agreement (reported ~$20B), with founder/CEO Jonathan Ross and other leaders joining NVIDIA; Groq continues as an independent company (Simon Edwards CEO) and "GroqCloud will continue to operate without interruption". — [Groq newsroom](https://groq.com/newsroom/groq-and-nvidia-enter-non-exclusive-inference-technology-licensing-agreement-to-accelerate-ai-inference-at-global-scale); [Axios 2025-12-29](https://www.axios.com/2025/12/29/nvidia-groq-inference-chips)
- Card: free tier needs no card (secondary; Groq docs don't state it explicitly). — [CloudZero Groq pricing 2026](https://www.cloudzero.com/blog/groq-pricing/) (secondary)

**OpenRouter** — checked 2026-09-24
- Free model variants (IDs ending ":free"): 20 requests/minute; 50 requests/day if the account has purchased fewer than 10 credits (all time); 1,000 requests/day once at least 10 credits ($10) have been purchased (a one-time purchase, PAID). Negative balance → 402 errors even on free models. Daily counter resets per UTC day. — [OpenRouter limits](https://openrouter.ai/docs/api-reference/limits)
- The free-model roster rotates frequently (e.g., on 2026-09-24 the free filter showed models such as Nex AGI Nex-N2.5-Mini/Pro (free) and inclusionAI Ling 3.0 Flash variants (free)); free endpoints may log prompts for the provider. — [OpenRouter models, free filter](https://openrouter.ai/models?max_price=0)

**GitHub Models** — RETIRED
- "As of July 30, 2026, GitHub Models has been fully retired. The playground, model catalog, inference API, and bring your own key (BYOK) are no longer available to any customer." GitHub points to Azure AI Foundry or GitHub Copilot instead. Any 2025 tutorial using GitHub Models' free API is obsolete. — [GitHub Docs – GitHub Models](https://docs.github.com/en/billing/concepts/product-billing/github-models)

**Cerebras** — checked 2026-09-24 (CHANGED)
- Rate-limit doc now lists a "Free Trial" tier: gpt-oss-120b and qwen-3.8-27b → 5 RPM, 30K uncached TPM (90K total), 1M tokens/hour, 1M tokens/day. Pricing page: Developer tier = "Self-serve pay-as-you-go with free $5 credit to start"; Developer models listed: gpt-oss-120b, gemma-4-31b (and Qwen 3.8 27B in price table). — [Cerebras rate limits](https://inference-docs.cerebras.ai/support/rate-limits); [Cerebras pricing](https://www.cerebras.ai/pricing)
- CONFLICT/OUTDATED: many 2025–early-2026 guides describe a permanent free tier with "1M tokens/day", 30 RPM, 14,400 RPD, no card; the current official page shows a much tighter 5 RPM "Free Trial". — [getaiperks Cerebras guide](https://www.getaiperks.com/en/ai/cerebras-free-tier-guide) (secondary, likely outdated) vs [Cerebras rate limits](https://inference-docs.cerebras.ai/support/rate-limits)

**Hugging Face Inference Providers** — checked 2026-09-24
- Monthly credits: Free users "$0.10, subject to change" (pay-as-you-go beyond that requires buying credits); PRO $2.00/month; Team/Enterprise $2.00 per seat. — [HF Inference Providers pricing](https://huggingface.co/docs/inference-providers/pricing)

**Cohere** — checked 2026-09-24
- Trial (evaluation) keys are free: "Trial keys ... are limited to 1,000 API calls a month"; trial rate limits: Command A / R / R+ / R7B chat 20 req/min; Embed 2,000 inputs/min; Rerank 10 req/min. Trial keys are for evaluation, not production. — [Cohere rate limits](https://docs.cohere.com/docs/rate-limits)

**NVIDIA build.nvidia.com (NIM API catalog)**
- Official forum answer (Sep 2024, may be outdated): "The NVIDIA API catalog is a trial experience of NVIDIA NIM limited to 5000 free API credits. Upon sign-up, users are granted 1000 API credits"; more on request; business email unlocks 90-day NVIDIA AI Enterprise license. — [NVIDIA Developer Forums](https://forums.developer.nvidia.com/t/api-credits-for-build-nvidia-com/306633)
- 2026 secondary guides: free for prototyping via NVIDIA Developer Program, ~40 requests/minute default, no card. — [yangmao.ai NVIDIA Build](https://yangmao.ai/en/providers/nvidia-build/) (secondary)

**Mistral (La Plateforme / Studio "Experiment" plan)**
- Secondary sources (2026): free "Experiment" plan needs phone verification but no card; all models accessible at conservative limits (reported ~1 request/second, 500K TPM, 1B tokens/month); data may be used for training on the free plan. Official docs page for tiers returned 404 on 2026-09-24. — [freellms.org Mistral](https://www.freellms.org/providers/mistral-ai) (secondary)

### Inferences
- (in progress)

### Gaps
- (in progress)

## 3. Local LLMs on a CPU-only 8 GB Windows laptop (HP 14, 2021) — practical sizes, speeds, models, embeddings, dev tips

### Takeaway
(in progress)

### Cited Findings
- (in progress)

### Inferences
- (in progress)

### Gaps
- (in progress)

## 4. Free deployment for demos (HF Spaces, Streamlit Community Cloud, Render, Vercel, GitHub Pages, Koyeb/Fly/Railway)

### Takeaway
(in progress)

### Cited Findings

**Hugging Face Spaces** — see section 1: as of 2026 free accounts can create Static Spaces and up to 2 ZeroGPU Gradio Spaces; CPU-basic Gradio/Docker Spaces need PRO ($9/mo, PAID). — [HF Spaces Overview](https://huggingface.co/docs/hub/spaces-overview)

**Streamlit Community Cloud** — checked 2026-09-24
- Resource limits (may change without notice): CPU 0.078 cores min / 2 cores max; memory 690 MB min / 2.7 GB max; storage up to 50 GB. Over-limit apps show "This app has gone over its resource limits". — [Streamlit docs – manage your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app)
- "All apps without traffic for 12 hours go to sleep"; visiting wakes it. — [Streamlit docs – manage your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app)

**Render (Free instance type)** — checked 2026-09-24
- Free web services spin down after 15 minutes without inbound traffic; spin-up "takes about one minute". 750 free instance hours per workspace per month (reset monthly). Free Render Postgres: 1 GB, "expire 30 days after creation". If bandwidth/build minutes are exhausted and no payment method is on file, Render suspends free services / disables builds for the rest of the month (i.e., no card required to use free tier). — [Render free docs](https://render.com/docs/free)

**Vercel Hobby** — checked 2026-09-24
- Hobby is free but "restricts users to non-commercial, personal use only"; includes 1,000,000 function invocations/month among other caps. — [Vercel Hobby plan docs](https://vercel.com/docs/plans/hobby)

**GitHub Pages** — checked 2026-09-24
- Free for public repos on GitHub Free; published sites ≤ 1 GB; soft bandwidth limit 100 GB/month; soft limit 10 builds/hour (not applied when publishing via a custom Actions workflow); not allowed as free hosting for commercial/e-commerce sites. Static only (no Python backend). — [GitHub Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits)

**Koyeb** — no free compute plan found (checked 2026-09-24)
- Pricing page banner: "Koyeb is joining Mistral AI". Plans listed: Pro $29/mo (includes $10 compute), Scale $299/mo, Enterprise; the only $0 item seen is Serverless Postgres "Free 5h" of compute. The former free "Hobby/eco" web-service instance is not listed — treat Koyeb as PAID for web services. — [Koyeb pricing](https://www.koyeb.com/pricing)

**Railway** — checked 2026-09-24
- New accounts get a Trial with a "free one-time grant of $5" to be used within 30 days; connecting a verifiable GitHub account gives the "Full Trial" (otherwise "Limited Trial" with restricted outbound network). After the trial, a "Free" plan ($0/month) gives "$1 of free credit per month" with small per-service limits (0.5 GB RAM, 1 vCPU). Trial volumes are deleted 30 days after credits expire. — [Railway plans](https://docs.railway.com/reference/pricing/plans); [Railway free trial](https://docs.railway.com/pricing/free-trial)

**Fly.io** — no ongoing free allowance for new orgs found
- Pricing docs list only usage-based billing plus a "Free Trial" link and "Legacy plans ... Discontinued Plans" (the free-trial page 404'd on 2026-09-24). Treat as PAID after trial. — [Fly.io pricing](https://fly.io/docs/about/pricing/)

### Inferences
- (in progress)

### Gaps
- (in progress)

## 5. Free supporting services (vector DBs, experiment tracking, LLM observability/evals, CI, container registries)

### Takeaway
(in progress)

### Cited Findings

**GitHub Actions** — checked 2026-09-24
- "GitHub Actions usage is free for self-hosted runners and for public repositories that use standard GitHub-hosted runners." Private repos on GitHub Free: 2,000 minutes/month, 500 MB artifact storage, 10 GB cache per repo (GitHub Pro: 3,000 min, 1 GB). — [GitHub Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions)

**GitHub Container Registry (ghcr.io)** — checked 2026-09-24
- "Container image storage and bandwidth for the Container registry is currently free" (GitHub promises ≥1 month notice before changing). — [GitHub Packages billing](https://docs.github.com/en/billing/concepts/product-billing/github-packages)

**Docker Hub** — checked 2026-09-24
- Personal (authenticated, free): 200 pulls per 6 hours, unlimited public repos, up to 1 private repo; unauthenticated: 100 pulls per 6 hours per IPv4 address (or IPv6 /64). — [Docker Hub usage & limits](https://docs.docker.com/docker-hub/usage/)

**Vector databases**
- Local/OSS (no account): Chroma and FAISS run in-process on the laptop (no quotas). (General knowledge; not separately sourced.)
- Qdrant Cloud Free Tier: "Free forever", 1 node with 0.5 vCPU / 1 GB RAM / 4 GB disk; "You don't need a credit card to join"; "free tier clusters are automatically suspended after 1 week, and deleted after 4 weeks of inactivity if not reactivated." — NO CARD. — [Qdrant pricing](https://qdrant.tech/pricing/); [Qdrant create-cluster docs](https://qdrant.tech/documentation/cloud/create-cluster/)
- Pinecone Starter (Free): AWS us-east-1 only; storage up to 2 GB; up to 2M write units/month and 1M read units/month; up to 5 indexes, 100 namespaces per index; 1 project; up to 2 users. Next tier "Builder" $20/month flat (PAID). Card requirement not stated on the page. — [Pinecone pricing](https://www.pinecone.io/pricing/)
- Chroma Cloud: Starter "$0 ... + $5 in free credits", then usage-based; "Currently Chroma accepts credit card for Starter and Team plans" (card likely needed to go beyond credits). — [Chroma pricing](https://www.trychroma.com/pricing)
- Supabase Free: 500 MB database per project, shared CPU / 500 MB RAM, 5 GB egress, 1 GB file storage, 50,000 MAU; "Free projects are paused after 1 week of inactivity. Limit of 2 active projects." pgvector is a supported Postgres extension. — [Supabase pricing](https://supabase.com/pricing); [Supabase pgvector docs](https://supabase.com/docs/guides/database/extensions/pgvector)
- Neon Free: "Build and learn free with no time limits and no credit card required"; 100 projects, 0.5 GB storage per project, 100 CU-hours per project per month, scale-to-zero after 5 minutes inactive. — NO CARD. — [Neon pricing](https://neon.com/pricing)

**Experiment tracking**
- Weights & Biases Free ($0/mo, "personal development"): experiment tracking, tracing/evaluations (Weave), registry; storage 5 GB/month; Weave data ingestion 1 GB/month; Pro starts at $60/month (PAID); "Free forever for academic research" track exists. — [W&B pricing](https://wandb.ai/site/pricing/)
- MLflow: open-source, runs locally (e.g., `mlflow ui` with local file/SQLite store) at $0. (General knowledge.)
- Comet: now centred on Opik (LLM observability). Opik open-source = free self-host; Opik "Free Cloud": up to 10 team members, 25k spans/month, 60-day data retention. Classic Comet experiment management is shown as an "Optional Add-On: MLOps Platform" — free status for individuals unclear. — [Comet pricing](https://www.comet.com/site/pricing/)

**LLM observability / evals**
- Langfuse Cloud Hobby: Free, "no credit card required", all platform features with limits, 50k units/month, 30 days data access, 2 users; also self-hostable (Docker Compose). — NO CARD. — [Langfuse pricing](https://langfuse.com/pricing)
- Arize: Phoenix OSS (open-source observability & evals, self-host/local, free); Arize AX Free (managed): 25k spans/month, 1 GB ingestion/month, 15-day retention. — [Arize pricing](https://arize.com/pricing/)

**Other free inference worth knowing**
- Cloudflare Workers AI: "10,000 Neurons per day at no charge" on the Workers Free plan; more requires Workers Paid; some large models (e.g., Kimi K2.6/K2.7-code, GLM-5.x, some DeepSeek) "require a paid billing method". — [Cloudflare Workers AI pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/)

### Inferences
- (in progress)

### Gaps
- (in progress)
