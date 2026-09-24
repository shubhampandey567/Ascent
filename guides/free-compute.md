# Free compute: what runs where

_Checked September 2026. Free tiers change often: if something here stops working, tell the Mentor and it will look up the current limits. Anything that needs a credit card is marked **CARD**; don't use those._

## The rule
**Your laptop edits, thinks and runs light code. The cloud does the heavy lifting.**

| Job | Where |
|---|---|
| Editing, Git, the Mentor, `tools/tracker.py` | your laptop |
| Python scripts, Pandas on small data (< ~1 GB), scikit-learn | your laptop |
| Big data (> 1 GB), anything that needs a GPU, long training runs | **Kaggle** (first choice) or **Colab** |
| Calling LLMs | free APIs (**Groq**, **Gemini**) or small local models with **Ollama** |
| Hosting a demo | **Streamlit Community Cloud**, **Render**, or a **Hugging Face ZeroGPU Space** |
| Docker (Phase 8) | **GitHub Codespaces** (Docker Desktop is too heavy for 8 GB RAM) |

## Your laptop (the course baseline)
The course assumes a modest laptop: about 8 GB RAM and integrated graphics, with no NVIDIA GPU. That's typical of budget laptops from 2020–2022, such as the HP 14 (2021) with an Intel 11th-gen i3/i5 or AMD Ryzen 5000U the course was first designed on. If yours is stronger, great; nothing here needs more. The Mentor records your exact specs during `/start`.

Keep it fast:
- Close browser tabs while studying. Each Chrome tab can eat hundreds of MB.
- Avoid WSL2 and Docker Desktop: they reserve gigabytes of RAM. Use Codespaces for Docker.
- If the Antigravity desktop app feels slow, use the Antigravity CLI (`agy`) in a terminal with a light editor.
- Use one virtual environment per project (`python -m venv .venv`) so installs stay small.

**Local LLMs on this laptop:** with 8 GB RAM and no GPU, small models of about 1–4 billion parameters in 4-bit quantization are practical with [Ollama](https://ollama.com). Expect a few to perhaps 15–20 tokens per second depending on model size; you'll measure it yourself in Phase 6. 7–8B models technically fit but are slow and leave little memory for anything else. Check [ollama.com/library](https://ollama.com/library) for current small models. For embeddings, `sentence-transformers` models like `all-MiniLM-L6-v2` run fine on a CPU.

## Notebooks with free GPUs

### Kaggle Notebooks (first choice)
- **30 GPU hours per week** (sometimes more), resetting weekly. GPU options: one Tesla P100 or two Tesla T4s.
- Sessions up to 12 hours (TPU 9 hours). 20 minutes of idle time while you edit; "Save & Run All" keeps running with the browser closed.
- CPU sessions have 4 cores and **30 GB RAM**, far more than your laptop, which makes them great for big-data Pandas work too.
- 20 GB of saved output per notebook; attach datasets and models as inputs.
- **Verify your phone number** in Kaggle settings to unlock GPUs and internet access.
- Docs: [Kaggle notebooks](https://www.kaggle.com/docs/notebooks), [efficient GPU usage](https://www.kaggle.com/docs/efficient-gpu-usage)

**Save your GPU hours:** write and debug on CPU with a tiny data sample, then switch the accelerator on for the real run. Turn the GPU off when you're reading or thinking.

### Google Colab (free tier)
- Sessions up to 12 hours "depending on availability and your usage patterns"; idle sessions get disconnected; no published GPU quota (usually a T4 when available).
- Not allowed on the free tier: hosting web apps or UIs, SSH or remote desktops, crypto mining. It's for notebooks.
- Save work to Google Drive or GitHub; the machine is wiped when the session ends.
- FAQ: [research.google.com/colaboratory/faq.html](https://research.google.com/colaboratory/faq.html)

### Lightning AI (backup)
- Free plan: up to 30 credits to start (about 75 T4 GPU hours), one free CPU Studio that runs 24/7 (restart every 4 hours), 50 GB storage, no credit card. Whether credits refresh monthly is unclear. [Pricing](https://lightning.ai/pricing)

### GitHub Codespaces
- 120 core-hours per month free on a personal account (about 60 hours on a 2-core machine), 15 GB storage. A full Linux machine in the browser with Docker available: ideal for Phase 8. [Billing docs](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces)
- Stop your codespace when you're done; idle time counts.

## Free LLM APIs
Get these keys in Phase 0 and keep them in `.env` (never in code).

| Provider | Free allowance (Sept 2026) | Card? | Use it for |
|---|---|---|---|
| **[Groq](https://console.groq.com)** | per model: 30 requests/min, 1,000 requests/day, 200K tokens/day. Models include `openai/gpt-oss-20b`, `openai/gpt-oss-120b`, `qwen/qwen3.8-27b`, and Whisper for speech | no | **your default** for development: fast, and OpenAI-compatible |
| **[Google AI Studio (Gemini API)](https://aistudio.google.com)** | Flash and Flash-Lite models plus Gemini embeddings are free; limits are shown only inside AI Studio (reports: about 20 requests/day for the newest Flash, about 500/day for Flash-Lite) | no | Flash-Lite for volume, embeddings, and trying Gemini |
| **[OpenRouter](https://openrouter.ai)** | models ending in `:free`: 20/min, 50/day | no | trying many different models |
| **[Cerebras](https://cloud.cerebras.ai)** | free trial: 5 requests/min, 1M tokens/day | no | backup |
| **[Cohere](https://dashboard.cohere.com)** | trial key: 1,000 calls/month; Rerank 10/min | no | rerankers in Phase 7 |
| **Ollama** (local) | unlimited, on your laptop | — | privacy, offline, experiments with small models |

**Important caveats**
- **Free tiers may use your prompts to improve their products** (Google says so explicitly for the Gemini free tier). Never send personal data, and never send your employer's code or data.
- **Model names change.** Groq removed its Llama models in August 2026, so many older tutorials are broken. If a model id fails, check the provider's model list.
- **Retired:** GitHub Models (July 30, 2026). Ignore tutorials that use it.
- **Write provider-agnostic code.** Groq, OpenRouter, Cerebras, Ollama and Gemini all offer OpenAI-compatible endpoints, so one client works with all of them by changing `base_url`, `api_key` and `model`. When one free tier runs out, switch providers, not code.

```python
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=os.environ["GROQ_API_KEY"])
reply = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[{"role": "user", "content": "Explain a Python KeyError in one sentence."}],
)
print(reply.choices[0].message.content)
```

(`pip install openai python-dotenv`. The same code works with Ollama using `base_url="http://localhost:11434/v1"` and `api_key="ollama"`.)

## Hosting demos for free

| Where | Free allowance | Card? | Best for |
|---|---|---|---|
| **[Streamlit Community Cloud](https://streamlit.io/cloud)** | up to ~2.7 GB RAM; sleeps after 12 h without visitors (wakes on visit) | no | Streamlit apps: your default for Phases 2 and 4 |
| **[Render](https://render.com/docs/free)** | 750 instance-hours/month; spins down after 15 min idle (about 1 min to wake); free Postgres expires after 30 days | no | FastAPI services and Docker (Phase 8) |
| **[Hugging Face Spaces](https://huggingface.co/docs/hub/spaces-overview)** | Static Spaces free; free accounts (verified email, 30+ days old) can host up to **2 ZeroGPU Gradio Spaces**. CPU Gradio and Docker Spaces now need the paid PRO plan | no | Gradio demos of your models (Phases 4–6) |
| **[GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits)** | static sites from public repos | no | portfolio site, project pages |

Not free in 2026 without a card or payment: Koyeb, Fly.io, Railway (tiny trial only), Modal (needs a card on file).

## Free supporting services

| Need | Free option | Card? |
|---|---|---|
| Vector database | Chroma or FAISS on your laptop (no account); [Qdrant Cloud](https://qdrant.tech/pricing/) free cluster (suspended after a week of inactivity) | no |
| Postgres (+ pgvector) | [Neon](https://neon.com/pricing) free (0.5 GB per project); [Supabase](https://supabase.com/pricing) free (pauses after a week idle) | no |
| Experiment tracking | MLflow on your laptop; [Weights & Biases](https://wandb.ai/site/pricing/) free personal plan | no |
| LLM tracing and evals | [Langfuse Cloud Hobby](https://langfuse.com/pricing) (50k units/month); [Arize Phoenix](https://arize.com/pricing/) open source | no |
| CI | [GitHub Actions](https://docs.github.com/en/billing/concepts/product-billing/github-actions): free for public repos; 2,000 min/month for private | no |
| Container registry | [GitHub Container Registry](https://docs.github.com/en/billing/concepts/product-billing/github-packages) (free) | no |

## Big clouds: look, don't sign up
Google Cloud, AWS, Azure and Oracle free tiers all require a credit or debit card. You'll learn cloud *concepts* in Phase 8 and use Codespaces, Render and Kaggle instead. If your employer gives you a cloud sandbox, that's the place to practise real cloud services (follow your company's rules).

## When a free tier runs out
1. Switch provider (that's why the code is provider-agnostic).
2. Use a smaller or local model for development; use the good model only for final runs.
3. Cache responses while you develop so you don't pay the same request twice.
4. Wait for the reset: Kaggle weekly, most APIs daily.
