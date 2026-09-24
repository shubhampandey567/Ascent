# Phase 6 — Transformers & LLM Internals

**Plan weeks 37–43 · 7 weeks · Difficulty ★★★★★ · Badge: LLM Internals Engineer**

## Why this phase matters
In Phase 2 you *used* LLMs. Now you open the box: attention, tokenization, training, inference and fine-tuning. Most people who build with LLMs can't explain why a model hallucinates, why non-English text often costs more tokens, why a 4-bit model fits in 2 GB, or when fine-tuning beats RAG. You will. That understanding is what lets you debug, choose models, estimate costs and answer the hard interview questions.

A reality check from 2026 job postings: fine-tuning is the *main* job in only about 4% of AI-engineer roles. So this phase is about deep understanding plus one strong portfolio project, not about becoming a model trainer.

## Before you start
- Phase 5 passed: you've built micrograd, trained networks in PyTorch, and watched makemore.
- Kaggle account phone-verified (GPU notebooks). See [guides/free-compute.md](../guides/free-compute.md).

## You will be able to
- Explain self-attention (queries, keys, values, masking, heads) with a diagram and in code.
- Build and train a small GPT from scratch and sample from it with temperature, top-k and top-p.
- Explain tokenization (BPE) and its side effects.
- Describe how LLMs are trained: pretraining, supervised fine-tuning, preference tuning (RLHF, DPO), and reasoning via reinforcement learning.
- Explain inference costs: KV cache, quantization, batching.
- Fine-tune a small open model with QLoRA on a free GPU, evaluate it honestly, and run it locally.

> **About DeepLearning.AI courses:** videos are free to watch. Quizzes, labs and certificates now need a paid "Pro" membership, so skip those parts and do this curriculum's build tasks instead.

---

## Week 1 (plan week 37) — Attention, visually

#### P6-W1-L1 · Transformers: the big picture (~60 min)
- **Learn:** [3Blue1Brown — Transformers, the tech behind LLMs (Deep Learning Ch. 5)](https://www.youtube.com/watch?v=wjZofJX0v4M) (~27 min).
- **Alt:** [Jay Alammar — The Illustrated GPT-2](https://jalammar.github.io/illustrated-gpt2/)
- **Key concepts:** text → tokens → embedding vectors → a stack of (attention + MLP) blocks → unembedding → softmax → a probability for every possible next token; generation = predict, sample, append, repeat; temperature reshapes the distribution; the embedding matrix and context size as the model's limits.
- **Quiz seeds:** Why does the model output a *distribution* rather than one word? What does temperature 0 vs 2 do? Where do the model's "parameters" live in this picture?
- **Build:** In NumPy, write `softmax(logits, temperature)` and show how the distribution for `[2.0, 1.0, 0.1]` changes at T = 0.5, 1, 2.

#### P6-W1-L2 · Attention step by step (~60 min)
- **Learn:** [3Blue1Brown — Attention in transformers, step-by-step (Ch. 6)](https://www.youtube.com/watch?v=eMlx5fFNoYc) (~26 min).
- **Alt:** [DeepLearning.AI — Attention in Transformers: Concepts and Code in PyTorch](https://www.deeplearning.ai/courses/attention-in-transformers-concepts-and-code-in-pytorch) (StatQuest's Josh Starmer; 11 short videos).
- **Key concepts:** query, key and value vectors; dot product as relevance; softmax over scores → attention pattern; causal masking (no peeking at future tokens); dividing by √d; multi-head attention (several patterns in parallel); cost grows with the square of context length.
- **Quiz seeds:** Why must a GPT mask future positions during training? What would go wrong without dividing by √d? Explain multi-head attention using a code-review analogy.
- **Build:** Scaled dot-product attention in NumPy for 3 tokens with d = 4, with a causal mask. Check that each row of the attention matrix sums to 1.

#### P6-W1-L3 · Where knowledge lives (~60 min)
- **Learn:** [3Blue1Brown — How might LLMs store facts (Ch. 7)](https://www.youtube.com/watch?v=9-Jl0dxWQs8) (~23 min), then read [Jay Alammar — The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/).
- **Key concepts:** MLP blocks as a kind of key–value memory; superposition (more features than dimensions); residual stream; encoder vs decoder vs encoder–decoder transformers (BERT vs GPT vs T5).
- **Quiz seeds:** What is the residual stream? Why are GPT-style models "decoder-only"? What's a task where an encoder (BERT) fits better than a decoder?
- **Build:** Draw (on paper or in a diagram tool) one full transformer block with shapes for batch B, sequence T and width C. Photo or file into `notes/P6/`.

#### P6-W1-L4 · How transformer LLMs work, end to end (~75 min)
- **Learn:** [DeepLearning.AI — How Transformer LLMs Work](https://www.deeplearning.ai/courses/how-transformer-llms-work) (Jay Alammar and Maarten Grootendorst; 13 short videos; watch lessons 1–7 today).
- **Alt / deeper:** [Stanford CME295 — Transformers & LLMs (Autumn 2025)](https://www.youtube.com/playlist?list=PLoROMvodv4rOCXd21gf0CF4xr35yINeOy), lecture 1. The most beginner-friendly Stanford LLM course.
- **Key concepts:** tokenizer → embeddings → positional information → transformer blocks → LM head; KV cache preview; mixture-of-experts preview; how recent architectures differ from the 2017 transformer.
- **Quiz seeds:** Why do transformers need positional information at all? What is cached in the KV cache, and why does that speed up generation?
- **Build:** Finish the course's remaining lessons over the weekend if time allows.

#### P6-W1-B · Weekend build
Implement a single causal self-attention head in PyTorch (`nn.Linear` for Q, K, V; mask with `torch.tril`). Compare your output with `torch.nn.functional.scaled_dot_product_attention(..., is_causal=True)` on random input; they should match to about 1e-6.

---

## Week 2 (plan week 38) — Build a GPT from scratch
One video, four sittings, on a **Kaggle or Colab GPU notebook**. Code along; don't just watch. Minute ranges are approximate, so use the chapter list under the video. The Mentor can quiz exactly the part you watched: `/quiz https://www.youtube.com/watch?v=kCc8FmEb1nY` with the minutes.

#### P6-W2-L1 · Data, batches and a bigram baseline (~75 min)
- **Learn:** [Karpathy — Let's build GPT: from scratch, in code, spelled out](https://www.youtube.com/watch?v=kCc8FmEb1nY), **0:00–0:42**. Code: [karpathy/ng-video-lecture](https://github.com/karpathy/ng-video-lecture).
- **Key concepts:** character-level tokenization; train/validation split; random chunks of `block_size` in batches; the bigram model as a baseline; cross-entropy loss ≈ −ln(1/65) ≈ 4.17 at random initialisation.
- **Quiz seeds:** Why is the starting loss about 4.17 for 65 characters? What are the shapes of `x` and `y` in a batch, and how does `y` relate to `x`?

#### P6-W2-L2 · The self-attention trick (~75 min)
- **Learn:** same video, **0:42–1:19**.
- **Key concepts:** averaging past tokens with a lower-triangular matrix; weighted aggregation as matrix multiplication; softmax with `-inf` masking; a single self-attention head; positional embeddings; attention as "communication" between tokens; why attention operates over sets.
- **Quiz seeds:** Why does masking with `-inf` before softmax give zero weight? What do the notes about "no communication across the batch dimension" mean?

#### P6-W2-L3 · Multi-head attention, feed-forward, residuals, LayerNorm (~75 min)
- **Learn:** same video, **1:19–1:38**.
- **Key concepts:** multi-head attention; the feed-forward layer ("thinking" on each token); residual connections keep gradients flowing; LayerNorm vs BatchNorm (you met BatchNorm in makemore).
- **Quiz seeds:** What problem do residual connections solve in deep networks? Why does LayerNorm suit transformers better than BatchNorm?

#### P6-W2-L4 · Scaling up and the road to ChatGPT (~75 min)
- **Learn:** same video, **1:38–end**.
- **Key concepts:** scaling width, depth, heads and context; dropout; train vs validation loss while scaling; encoder vs decoder; pretraining vs fine-tuning vs RLHF (how a base model becomes an assistant).
- **Quiz seeds:** Your validation loss rises while training loss keeps falling. What is happening and what are 3 fixes? What turns a base model into ChatGPT?

#### P6-W2-B · Weekend build
Train your GPT on a different corpus of your choice (for example a public-domain book from [Project Gutenberg](https://www.gutenberg.org), or text in your own language and script). Plot train and validation loss, save 3 samples at different temperatures, and write down what changed and why. This becomes part A of the phase project.

---

## Week 3 (plan week 39) — Tokenization and the Hugging Face ecosystem

#### P6-W3-L1 · Tokenization, part 1 (~75 min)
- **Learn:** [Karpathy — Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE), **first ~65 minutes**. Code: [karpathy/minbpe](https://github.com/karpathy/minbpe).
- **Key concepts:** Unicode code points vs UTF-8 bytes; byte-pair encoding (merge the most frequent pair, repeat); vocabulary size trade-offs; encode and decode.
- **Quiz seeds:** Why not just use raw bytes as tokens? Walk through one BPE merge on the string "aaabdaaabac".

#### P6-W3-L2 · Tokenization, part 2 (~75 min)
- **Learn:** same video, **~65 min to the end**. Try tokenizers live at [tiktokenizer](https://tiktokenizer.vercel.app).
- **Key concepts:** regex pre-splitting (GPT-2/GPT-4 tokenizers); special tokens; SentencePiece; why LLMs struggle with spelling, arithmetic and some non-English languages; tokens as the unit of cost and context.
- **Quiz seeds:** Why can a model fail to count the letters in "strawberry"? Why may the same sentence in Hindi (or another non-English language) cost several times more tokens than in English?

#### P6-W3-L3 · Hugging Face transformers (~75 min)
- **Learn:** [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1), chapters 1–2 (transformer models, `pipeline()`, tokenizers, models). Run the examples in Colab.
- **Key concepts:** the Hub; model cards; `AutoTokenizer` and `AutoModel`; padding, truncation and attention masks; logits → probabilities.
- **Quiz seeds:** What does the attention mask do in a padded batch? What should you read in a model card before using a model?

#### P6-W3-L4 · Fine-tuning a pretrained encoder (~75 min)
- **Learn:** Hugging Face LLM Course, chapter 3 (fine-tuning with `Trainer`), on a Kaggle or Colab GPU.
- **Key concepts:** datasets library; tokenizing a dataset with `map`; dynamic padding; `Trainer` and `TrainingArguments`; evaluation metrics.
- **Quiz seeds:** Why fine-tune a pretrained model instead of training from scratch? What is transfer learning here?
- **Build:** Fine-tune a small BERT-style model on a sentiment or topic dataset; report accuracy and F1.

#### P6-W3-B · Weekend build
Train a small BPE tokenizer on 1–2 MB of text you choose (your own code, or `minbpe` as reference). Then compare token counts for the same 10 sentences in English and another language you know using [tiktoken](https://github.com/openai/tiktoken) and your tokenizer. Write a short "why my language costs more tokens" note with numbers. A good blog post.

---

## Week 4 (plan week 40) — How LLMs are trained

#### P6-W4-L1 · Pretraining and scaling laws (~75 min)
- **Learn:** [DeepLearning.AI — Pretraining LLMs](https://www.deeplearning.ai/courses/pretraining-llms) (8 short videos), then read the abstract and main figure of [Chinchilla: Training Compute-Optimal LLMs](https://arxiv.org/abs/2203.15556).
- **Key concepts:** next-token prediction on trillions of tokens; data quality and deduplication; compute budget; scaling laws (loss falls predictably with more parameters, data and compute); the compute-optimal ratio of tokens to parameters.
- **Quiz seeds:** What did Chinchilla show about models like GPT-3? Why does data quality matter as much as model size?

#### P6-W4-L2 · Post-training: SFT, RLHF, DPO (~75 min)
- **Learn:** [DeepLearning.AI — Post-training of LLMs](https://www.deeplearning.ai/courses/post-training-of-llms) (9 short videos). Read the abstract and Figure 2 of [InstructGPT](https://arxiv.org/abs/2203.02155).
- **Alt / deeper:** [Umar Jamil — DPO explained](https://www.youtube.com/watch?v=hvGa5Mba4c8)
- **Key concepts:** supervised fine-tuning on instruction–response pairs; reward model from human preferences; RLHF; DPO as a simpler alternative that needs no separate reward model; why chat models refuse, follow formats and sometimes flatter.
- **Quiz seeds:** Explain the 3 steps in InstructGPT's Figure 2. What does DPO remove from the RLHF pipeline?

#### P6-W4-L3 · Reasoning models (~75 min)
- **Learn:** read [The Illustrated DeepSeek-R1](https://newsletter.languagemodels.co/p/the-illustrated-deepseek-r1) and the abstract of [DeepSeek-R1](https://arxiv.org/abs/2501.12948).
- **Optional:** [DeepLearning.AI — Reinforcement Fine-Tuning LLMs With GRPO](https://www.deeplearning.ai/courses/reinforcement-fine-tuning-llms-grpo)
- **Key concepts:** chain-of-thought; reinforcement learning with verifiable rewards (math, code); GRPO; "thinking tokens" and test-time compute; distilling reasoning into small models.
- **Quiz seeds:** Why do rewards for math and code tasks work well for RL? Why do reasoning models cost more per answer?

#### P6-W4-L4 · How to read a paper (~60 min)
- **Learn:** [S. Keshav — How to Read a Paper](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf) (3 pages). Then do a *first pass* (title, abstract, headings, figures, conclusion) of [Attention Is All You Need](https://arxiv.org/abs/1706.03762).
- **Key concepts:** the three-pass method; reading figures first; what problem a paper solves and what it claims.
- **Quiz seeds:** After your first pass, what problem did the transformer paper solve, and what did it replace?

#### P6-W4-B · Weekend build: microgpt on your own laptop
Read and run Karpathy's [microgpt](https://karpathy.github.io/2026/02/12/microgpt/): a complete GPT in about 200 lines of pure Python with no dependencies (tokenizer, autograd, Adam optimizer, training and sampling). It runs on your laptop's CPU. Annotate every section in `notes/P6/microgpt.md`, mapping each part to what you learned in Phases 5 and 6. When you can explain every line, you understand LLMs better than most people who use them daily.

---

## Week 5 (plan week 41) — Inference and efficiency

#### P6-W5-L1 · Decoding and the KV cache (~75 min)
- **Learn:** [Umar Jamil — LLaMA explained: KV-Cache, Rotary Positional Embedding, RMS Norm, Grouped Query Attention, SwiGLU](https://www.youtube.com/watch?v=Mn_9W1nCFLo), the KV-cache section (use the chapter list).
- **Key concepts:** greedy vs sampling; temperature, top-k and top-p; repetition; the KV cache (reuse past keys and values instead of recomputing them); why the first token is slow and the rest are faster.
- **Quiz seeds:** What exactly is stored in the KV cache? Why does top-p adapt better than top-k?
- **Build:** Add temperature, top-k and top-p sampling to your Week 2 GPT and compare outputs.

#### P6-W5-L2 · Quantization (~60 min)
- **Learn:** [DeepLearning.AI — Quantization Fundamentals with Hugging Face](https://www.deeplearning.ai/courses/quantization-fundamentals) (7 short videos).
- **Alt / deeper:** [Umar Jamil — Quantization explained with PyTorch](https://www.youtube.com/watch?v=0VdNflU08yA)
- **Key concepts:** fp32, fp16, bf16, int8, int4; memory ≈ parameters × bytes per parameter; GGUF files for llama.cpp and Ollama; the accuracy vs memory trade-off.
- **Quiz seeds:** Roughly how much RAM do a 3B model's weights need in fp16 and in 4-bit? Why can your 8 GB laptop run a 3B model in 4-bit but not in fp16?

#### P6-W5-L3 · Serving LLMs (~60 min)
- **Learn:** [DeepLearning.AI — Efficiently Serving LLMs](https://www.deeplearning.ai/courses/efficiently-serving-llms) (8 short videos).
- **Key concepts:** batching and continuous batching; throughput vs latency; serving many LoRA adapters on one base model; what vLLM and llama.cpp do.
- **Quiz seeds:** Why does batching raise throughput but can raise latency? When would you serve one base model with many LoRA adapters?

#### P6-W5-L4 · Architecture tour: MoE, long context, images (~60 min)
- **Learn:** [Umar Jamil — Mistral / Mixtral explained](https://www.youtube.com/watch?v=UiX8K-xBUpE) (mixture-of-experts section), then [3Blue1Brown × Welch Labs — But how do AI images and videos actually work?](https://www.youtube.com/watch?v=iv-5mZ_9CPY)
- **Key concepts:** mixture of experts (only some parameters active per token); sliding-window attention; rotary position embeddings for long context; diffusion models for images; vision-language models turn images into tokens.
- **Quiz seeds:** Why can a mixture-of-experts model be big but cheap per token? How does a diffusion model generate an image, in 3 sentences?

#### P6-W5-B · Weekend build: benchmark your laptop
With [Ollama](https://ollama.com), run 2 small models (1–4B) in 2 quantizations each. For each, measure tokens per second, RAM used (Task Manager) and quality on the same 10 prompts (your own 1–5 score). Put the results in a table with a recommendation. You now know exactly what your hardware can do.

---

## Week 6 (plan week 42) — Fine-tuning

#### P6-W6-L1 · When to fine-tune, and LoRA (~75 min)
- **Learn:** [Umar Jamil — LoRA explained visually + PyTorch code from scratch](https://www.youtube.com/watch?v=PXWYUTMt-AU), then the abstracts of [LoRA](https://arxiv.org/abs/2106.09685) and [QLoRA](https://arxiv.org/abs/2305.14314).
- **Key concepts:** prompt vs RAG vs fine-tune (fine-tuning changes *behaviour and format*, RAG adds *knowledge*); LoRA trains small low-rank matrices next to frozen weights; QLoRA = 4-bit base model + LoRA; adapters are small files.
- **Quiz seeds:** Your company wants the model to know this month's HR policy. Fine-tune or RAG? Why? Why does LoRA need so much less memory than full fine-tuning?

#### P6-W6-L2 · QLoRA on a free GPU (~90 min)
- **Learn:** pick a small-model notebook from [Unsloth's free notebooks](https://unsloth.ai/docs/get-started/unsloth-notebooks) (Llama 3.2 1B/3B, Qwen3.5 2B/4B or Gemma 4 E2B) and run it on Colab or Kaggle.
- **Key concepts:** chat templates; formatting a dataset; LoRA rank and alpha; learning rate and epochs; watching the loss; GPU memory limits of a free T4.
- **Quiz seeds:** Why must training data use the model's chat template? What happens if you train too many epochs on 200 examples?

#### P6-W6-L3 · Evaluate the fine-tune honestly (~75 min)
- **Learn:** [Hamel Husain — Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/) (first half) and apply it to your model.
- **Key concepts:** a held-out test set that never touched training; comparing base vs fine-tuned vs a strong prompted model; overfitting and catastrophic forgetting; exact-match vs rubric-based scoring.
- **Quiz seeds:** Your fine-tuned model scores 95% on test data generated by the same script as the training data. Why might that be misleading?

#### P6-W6-L4 · Publish and run locally (~60 min)
- **Learn:** the export sections of your Unsloth notebook (save adapter, merge, GGUF).
- **Key concepts:** pushing to the Hugging Face Hub; writing a model card (intended use, data, evaluation, limits); GGUF export; running your own model with Ollama on your laptop.
- **Quiz seeds:** What belongs in a model card, and why does it matter for users?

#### P6-W6-B · Weekend build
Project work (below).

---

## Week 7 (plan week 43) — Project 6 and exam
#### P6-W7-L1 to L4 · Project 6 work
#### P6-W7-B · Weekend: `/submit`, then `/exam`

### Project 6 — "Inside the LLM" (`projects/pr6-inside-the-llm/`)
**Part A — TinyGPT (from scratch).** Your Week 2 GPT trained on a corpus you chose.
**Part B — Specialist small model (fine-tuned).** QLoRA fine-tune of a 1–4B open model for one narrow task. Ideas: English questions → SQL for a sample schema; classify IT support tickets into categories; extract fields from (synthetic) invoices in your country's format into JSON.

**Must-haves**
- [ ] Part A: training and validation loss curves; samples at 3 temperatures; top-k/top-p sampling implemented by you; one ablation (for example heads, context length or depth) with a results table.
- [ ] Part A: README section explaining self-attention in your own words, with a diagram.
- [ ] Part B: dataset of 300+ examples (public or synthetic, never employer data) with a held-out test set of 50+ examples.
- [ ] Part B: comparison table of base model, fine-tuned model, and a strong model via a free API with a good prompt, using the same metric.
- [ ] Part B: adapter or merged model on the Hugging Face Hub with a model card; GGUF version running locally in Ollama (screenshot or log).
- [ ] Notebooks saved with outputs; Kaggle or Colab links in the README.

**Stretch:** GRPO on a tiny task with a verifiable reward; add rotary embeddings to TinyGPT; report cost and time per training run.

**Viva focus:** attention shapes; why your loss curves look the way they do; why you chose LoRA rank and learning rate; whether fine-tuning was even the right call vs prompting or RAG.

### Exam EX6
- **Part A (concepts):** attention, tokenization, training stages, KV cache, quantization, LoRA, evaluation traps.
- **Part B (live coding):** implement a causal self-attention head's forward pass in PyTorch from memory, with a test against `scaled_dot_product_attention`.
- **Part C (stakeholder):** "Our CTO asks: should we fine-tune our own model or use RAG with an API model for our internal documents chatbot?"
- **Part D (judgment):** "A vendor claims their fine-tuned 3B model beats a frontier model on your task. What do you ask for before believing it?"

---

## Optional and deeper
- [Karpathy — Let's reproduce GPT-2 (124M)](https://www.youtube.com/watch?v=l8pRSuU81PU): watch for the engineering; the full run needs rented GPUs.
- [karpathy/nanochat](https://github.com/karpathy/nanochat): read the code of a complete ChatGPT-style pipeline (not for training on a free tier).
- [Stanford CME295 — Transformers & LLMs](https://www.youtube.com/playlist?list=PLoROMvodv4rOCXd21gf0CF4xr35yINeOy): the whole course.
- [Stanford CS336 — Language Modeling from Scratch (Spring 2026)](https://www.youtube.com/playlist?list=PLoROMvodv4rMqXOcazWaTUHhq-yembLCV), with its [course site](https://cs336.stanford.edu/). Advanced; assignments need serious compute.
- [Sebastian Raschka — Build a Large Language Model (From Scratch), free video series](https://www.youtube.com/playlist?list=PLTKMiZHVd_2IIEsoJrWACkIxLRdfMlw11) and [code](https://github.com/rasbt/LLMs-from-scratch). Chapters 1–5 run on a normal laptop.
- [Umar Jamil — Coding LLaMA 2 from scratch](https://www.youtube.com/watch?v=oM4VmoabDAI) and [RLHF explained](https://www.youtube.com/watch?v=qGyFrqc34yc)
- [Stanford CS224N (Spring 2024)](https://www.youtube.com/playlist?list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D) and [CS25 Transformers United](https://www.youtube.com/playlist?list=PLoROMvodv4rNiJRchCzutFw5ItR_Z27CM) guest lectures.
- [Maxime Labonne — LLM Course](https://github.com/mlabonne/llm-course): a roadmap with Colab notebooks for fine-tuning, quantization and merging.
- [Hands-On Large Language Models notebooks](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models): built for the free Colab T4.
- [Hugging Face — a smol course](https://huggingface.co/learn/smol-course/unit0/1) on post-training (needs GPU access).
