# Security policy

This repository is a learning course: Markdown content, instructions for AI coding agents, and small Python scripts that read and write files inside the repository. Security still matters, because AI agents execute instructions from these files on learners' computers.

## What counts as a security issue
- Instructions in `AGENTS.md`, `.agents/skills/` or the curriculum that could make an agent run harmful commands, leak secrets, or act outside the repository.
- Hidden or injected instructions in content (for example text designed to manipulate an AI agent reading a lesson).
- Scripts in `tools/` or `scripts/` that could damage files, execute untrusted input, or send data anywhere.
- Links that now lead to malware, phishing or credential-harvesting pages.
- Anything that encourages learners to share API keys, passwords or employer data.

## How to report
Please **don't open a public issue** for security problems. Use GitHub's private vulnerability reporting instead: the repository's **Security** tab → **Report a vulnerability**. If that isn't available, open a short public issue asking the maintainers for a private channel, without any details of the problem.

You'll get an acknowledgement within 7 days. Dead links and outdated resources are not security issues; use the normal issue templates for those.

## For learners
- Keep your copy of this course **private**: it contains your progress, notes and journal.
- API keys live only in `.env`, which is gitignored. Never paste them into chat, code, notebooks or issues.
- Never paste your employer's code or confidential data into free AI tools, including your mentor.
- Review what your AI agent asks to run. The course only needs `python tools/tracker.py`, `python tools/srs.py` and `python tools/transcript.py` pre-approved; keep approval prompts on for everything else.
