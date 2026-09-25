---
name: start
description: First-time onboarding for the AI learning path. Runs the interview, a placement diagnostic and the setup checklist, records the pace with tools/tracker.py, and fills tracker/profile.md. Use when the learner types /start or when tracker/profile.md has no name yet.
---
# /start — Onboarding (about 45 minutes; fine to split over two sittings)

Goal: know the learner, place them correctly, get their tools working, start the tracker, and leave them convinced this is doable.

1. **Welcome (at most 8 lines).** Explain the loop: learn (a video or reading) → `/quiz` → build → reviews come back on a schedule (`/recall`) → projects are verified with `/submit` → `/weekly` every Sunday → `/exam` ends each phase. Everything is tracked automatically in `tracker/progress.md`. State the deal: "I will never do your work for you. I will make you able to do it."

2. **Interview, one question at a time.** Write each answer into `tracker/profile.md` as you go.
   - Name; current job or studies; tech stack; the business domain they work in (if any).
   - Real-world problems or curiosities in their field or daily work that bug them or that they find fascinating (these become personal curiosity hooks throughout the course).
   - Time: minutes per weekday and preferred time; weekend hours. Propose a pace: Light (~6 h/week), Standard (~10 h), Intense (~15 h), and a weekly goal of study days.
   - Computer: ask permission, then read RAM, CPU and free disk. Windows: `Get-CimInstance Win32_ComputerSystem | Select-Object TotalPhysicalMemory` and `Get-CimInstance Win32_Processor | Select-Object Name`. macOS: `sysctl hw.memsize machdep.cpu.brand_string`. Linux: `free -h` and `lscpu`.
   - Budget: free only (the default), or some money for tools? The course never requires paying.
   - Phone (Android or iPhone) for Anki.
   - Preferred language for explanations; are videos in another language welcome as alternates? Country or region (for local examples, prices and resources).
   - Comfort from 1 to 5 with Python, math, SQL and Git; any AI/ML exposure.
   - Why they are doing this; what they want to build; their 12-month goal.
   - Their biggest worry about AI and their career. Acknowledge it and mention `guides/why-this-path.md`.
   - Does anyone else follow their progress (a mentor, manager, parent)? If yes, point them to "For mentors and parents" in `README.md`.

3. **Diagnostic: 10 questions, one at a time, no notes, about 15 minutes.** Say that it is for placement only, not pass/fail.
   - Python ×5: predict the output of a list comprehension; count words with a dict; a function with a default argument; a small class; read a CSV and compute an average column.
   - Math ×3: what a dot product measures (intuition); what a derivative tells you; the probability of rolling a total of 7 with two dice.
   - AI ×2: what "machine learning" means in one sentence; what an LLM does when it answers a question.

   Record the score and notes in the profile. Python 4/5 or better → Phase 1 week 1 test-outs are allowed. Math 1/3 or worse → note "go slower in Phase 3; use the Khan Academy alternates".

4. **Implementation intention.** Ask them to complete this sentence: "After ______ (an existing daily habit), I will open the mentor and type /today." Record it in the profile. Plans tied to a cue like this are followed far more often than vague intentions.

5. **Setup checklist.** Walk through `README.md` → "Quick start" items not done yet: GitHub, Google (Colab, AI Studio), Kaggle with phone verification, Hugging Face, Python, Git, Anki (optional), and permission for the agent to run `python tools/tracker.py` and `python tools/transcript.py`. Setup problems are not the learning goal, so you may fix them directly.

6. **Explain the AI-assistance policy** from `AGENTS.md` in 3 lines.

7. **Start the tracker:** `python tools/tracker.py setup --pace <light|standard|intense> --goal-days <N> --minutes <N>` (add `--start YYYY-MM-DD` only if they want to start on a later day). Then `python tools/tracker.py session --minutes <time spent>`. Write the first entry in `tracker/journal.md`.

8. **Close.** Show the map in 5 lines (from `curriculum/00-overview.md`), name the first lesson (`python tools/tracker.py next`), show where the dashboard lives (`tracker/progress.md`), and say: "Type /today whenever you sit down to study."
