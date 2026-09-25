# How to learn (and remember) — the science behind this system

You will spend hundreds of hours on this course. How you study decides whether those hours stick. This page explains what the research says, in plain words, and exactly how this folder uses it. Sources are at the bottom.

## 1. You forget fast, unless you pull things back out of memory
- Forgetting is steepest in the first hours and days, then it levels off. Ebbinghaus measured this in the 1880s and a 2015 replication found the same curve.
- In a classic experiment, students who only **reread** a text lost **52%** of what they could recall within a week. Students who **tested themselves** lost only **14%**. The rereaders felt *more* confident, and they did worst.

**What this system does:** every lesson ends with a closed-book `/quiz`, and every topic comes back for review (`/recall`) about 1, 3, 8, 21 and 55 days later, scheduled by `tools/srs.py` and recorded by `tools/tracker.py`, which also shows your progress in `tracker/progress.md`.

## 2. Testing yourself beats rereading, highlighting and re-watching
A famous 2013 review rated ten study techniques:

| Utility | Techniques |
|---|---|
| **High** | practice testing (quizzing yourself); spaced practice |
| Moderate | asking "why is this true?"; explaining steps to yourself; mixing topics (interleaving) |
| Low | summarising, highlighting, rereading, mnemonics, imagery |

The low-utility ones are the techniques most students use. Quizzing with feedback works especially well (meta-analyses find about twice the effect of quizzing without feedback), which is why the Mentor corrects every answer right away.

## 3. Spread it out
Spaced practice reliably beats cramming, and the best gap between reviews grows with how long you want to remember. For long-term memory, a review about 1 day later, then a few days, then a week or two, then a month or more, works well. Reviewing a bit too late costs less than reviewing too early.

**Mastery rule used here:** you've truly got an idea when you recall it correctly, without help, in **three separate sessions on different days**. Getting it right three times in one sitting counts much less; one study found the spaced version gave more than twice the recall.

## 4. Watching a video is not learning (yet)
- A smooth, confident speaker makes you *feel* you learned more, without you actually learning more. "That was clear" is not evidence. Only the quiz is.
- Short quizzes during an online lecture cut mind-wandering roughly in half and raised final test scores from 68% to 90% in one study.
- Questions asked *before* watching improve learning of exactly what they ask about.

### Curiosity before content (the information-gap effect)
When someone explains an answer to a question you never asked, your brain discards it as background noise. But when you face an intuitive puzzle or dilemma *first*—especially one connected to your job or tech stack—your brain creates an open loop (an "information gap", Loewenstein 1994). That open loop triggers dopamine, raises alertness, and turns passive watching into an active search for the missing piece.

That is why your AI Mentor will always ask you a quick question, teaser, or puzzle connecting the topic to your world *before* sending you off to watch or read. Take 15 seconds to guess! Even a completely wrong guess primes your neural pathways to absorb the true explanation when you encounter it.

**How to watch every video in this course:**
1. Engage with the **Curiosity Hook** and read the 2–3 **focus questions** the Mentor gives you before you press play. Guess the answers.
2. Watch in chunks of about **5–10 minutes**. At each natural break, pause and write 2–3 bullet points **from memory** before continuing. Don't rewind before you've tried to recall.
3. Speed 1.25–1.75× is fine (research shows little loss up to 2×). Spend the saved time on recall, not on re-watching.
4. Code along whenever there's code. Typing it yourself beats watching it.
5. When the video ends, close it, write your note from memory (`notes/README.md`), then type `/quiz`.

Handwriting vs typing notes matters less than *processing*: paraphrase in your own words, never copy the transcript.

## 5. Mix topics, explain, and teach
- **Interleaving:** mixing related topics (for example, three different loss functions in one practice set) helps you learn *when* to use which. The "from earlier" question in each quiz and the mixed `/weekly` test do this.
- **Self-explanation:** explaining *why* each step works improves understanding. That's why the Mentor asks "why" so often.
- **Teaching:** explaining to someone else (the Feynman question in every quiz, blog posts, demos at work) deepens your own understanding.

## 6. Build things
Projects force you to combine ideas, meet real errors and make decisions, which is exactly what jobs require. From Phase 1 onwards at least 40% of your time is hands-on. Useful progression inside a lesson: **predict** what code does → **run** it → **modify** it → **write** your own.

## 7. Use AI to learn, not to skip learning
This is the most important section for your future.
- In a 2025 study (PNAS) with about 1,000 students, those who used plain GPT-4 during practice scored **48% higher** on practice problems, then **17% lower** on the exam without AI. A version that gave **hints instead of answers** raised practice scores even more and caused no exam harm. Students didn't notice they had learned less.
- In a 2025 Harvard study, a carefully designed AI tutor that made students do the thinking produced learning gains more than double those of an active-learning class.
- In a January 2026 Anthropic study, junior engineers who learned a new library by delegating to AI scored **below 40%** on a comprehension quiz. Those who used AI to ask **conceptual questions** scored **65% or more**. The biggest gap was in debugging.

**So the Mentor gives hints, not answers, and you write the code in the foundation phases.** It isn't being stingy; it's protecting the skills that make you valuable. At work, using AI to go faster is fine. In learning mode, you write first and the AI reviews.

## 8. Your weekly rhythm (~10 hours)

| Block | When | Time |
|---|---|---|
| Anki flashcards | daily, e.g. commute or morning | 5–10 min |
| Learn sessions (`/today`) | 4 weekdays | 60–75 min each |
| Build session | Saturday | 2–3 h |
| `/weekly` check and plan (no AI help, closed book) | Sunday | 60–90 min |
| Reserve days | 1–2 per week | flashcards only, or rest |

Inside a long session, work in blocks of 25 minutes with a 5-minute break, or 50 with 10. Stand up, walk, look away from the screen.

**Sleep is part of studying.** Memories consolidate during sleep. A short review in the evening plus a quick recall the next morning works well. Pulling all-nighters before an exam does the opposite.

## 9. Habits for a working adult
- **Attach studying to a fixed cue:** "After dinner at 9 pm, I open the mentor and type `/today`." Plans in this "after X, I do Y" form are followed much more often than vague intentions.
- **It takes months, not weeks, for a routine to feel automatic** (studies found around 2 months on average, with a wide range). The first 8 weeks are the hardest.
- **Never miss twice.** Missing one day is normal. Missing two in a row starts a new habit: the habit of not studying.
- **Reserve days are allowed.** Plan 1–2 per week. On a bad day do the minimum session: 10 minutes of reviews plus one short video.
- **Track weeks, not streaks.** A broken streak feels like failure and makes people quit. The goal is "4 study days this week", not "300 days in a row".

## 10. When you've been away
| Gap | What to do |
|---|---|
| 1 day | Nothing special. Do the due reviews first. |
| 2–6 days | No new flashcards for a few days. Reviews first (max 8 topics per day). New lessons again once the backlog is small. |
| A week or more | A 30–45 minute re-entry session: `/recall` on the last two weeks, reteach whatever failed, then one week at about 70% of normal pace. |
| More than 2 weeks | `/replan`. No guilt. The files remember where you were. |

## 11. Anki setup (5 minutes, once)
1. Install Anki (free on Windows and Android; see `flashcards/README.md`).
2. In the deck options, turn on **FSRS** (the modern scheduler). Set **desired retention to 0.90**; lower it to 0.85 if daily reviews take more than about 20 minutes.
3. **New cards per day: 10** at most.
4. Rate honestly. "Again" is information, not failure.

## 12. Confidence check
Before answering a quiz question, you can say how sure you are (1–5). Errors you were *confident* about are the most valuable ones to find: once corrected, they tend to stick. The Mentor will point them out.

---

## Sources
- Murre & Dros (2015), replication of Ebbinghaus's forgetting curve — [PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0120644)
- Roediger & Karpicke (2006), test-enhanced learning — [Psychological Science](https://journals.sagepub.com/doi/10.1111/j.1467-9280.2006.01693.x)
- Dunlosky et al. (2013), effective learning techniques — [PSPI](https://doi.org/10.1177/1529100612453266)
- Rowland (2014), testing-effect meta-analysis — [Psychological Bulletin](https://pubmed.ncbi.nlm.nih.gov/25150680/)
- Cepeda et al. (2008), optimal spacing — [Psychological Science](https://journals.sagepub.com/doi/10.1111/j.1467-9280.2008.02209.x)
- Rawson & Dunlosky (2022), successive relearning — [Current Directions in Psychological Science](https://journals.sagepub.com/doi/full/10.1177/09637214221100484)
- Carpenter et al. (2013), the fluent-lecturer illusion — [PubMed](https://pubmed.ncbi.nlm.nih.gov/23645413/)
- Szpunar, Khan & Schacter (2013), quizzes inside online lectures — [PNAS](https://www.pnas.org/doi/10.1073/pnas.1221764110)
- King-Shepard et al. (2025), prequestions meta-analysis — [Educational Psychology Review](https://link.springer.com/article/10.1007/s10648-025-10075-7)
- Loewenstein (1994), "The psychology of curiosity: A review and reinterpretation" — [Psychological Bulletin](https://doi.org/10.1037/0033-2909.116.1.75)
- Murphy et al. (2022), video playback speed — [Applied Cognitive Psychology](https://onlinelibrary.wiley.com/doi/abs/10.1002/acp.3899)
- Flanigan et al. (2024), handwritten vs typed notes meta-analysis — [Educational Psychology Review](https://link.springer.com/article/10.1007/s10648-024-09914-w)
- Bastani et al. (2025), "Generative AI without guardrails can harm learning" — [PNAS (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12232635/)
- Kestin et al. (2025), AI tutoring outperforms active learning — [Scientific Reports (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12179260/)
- Anthropic (2026), how AI assistance affects coding skill formation — [Anthropic](https://www.anthropic.com/research/AI-assistance-coding-skills)
- Lally et al. (2010), how habits form — [European Journal of Social Psychology](https://onlinelibrary.wiley.com/doi/10.1002/ejsp.674)
- Mazza et al. (2016), sleep between learning sessions — [Psychological Science](https://journals.sagepub.com/doi/abs/10.1177/0956797616659930)
- Biwer et al. (2023), systematic breaks while studying — [British Journal of Educational Psychology](https://bpspsychub.onlinelibrary.wiley.com/doi/abs/10.1111/bjep.12593)
- Anki manual, FSRS deck options — [docs.ankiweb.net](https://docs.ankiweb.net/deck-options.html)

The full research notes, with every number and caveat, are in [docs/research/2026-09/notes/learning-science.md](../docs/research/2026-09/notes/learning-science.md).
