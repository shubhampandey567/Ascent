@AGENTS.md

## Claude Code notes
- This workspace's slash commands are skills in `.claude/skills/`, generated from `.agents/skills/` (the shared source other agents read). To change a command, edit `.agents/skills/<name>/SKILL.md` and run `python scripts/sync_agents.py`.
- On Windows, if `python` is not on PATH, run the helpers with `py` (for example `py tools/tracker.py status`).
