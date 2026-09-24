# Using the course with your AI agent

The Mentor is plain files, so almost any AI coding agent can play it:

- **`AGENTS.md`**: the Mentor's rules. Read automatically by nearly every agent.
- **`.agents/skills/<command>/SKILL.md`**: one file per command (`/start`, `/today`, `/quiz`, ...), in the open [Agent Skills](https://agentskills.io/) format.
- **`tools/tracker.py`**, **`tools/srs.py`**, **`tools/transcript.py`**: small Python scripts the agent runs to record progress, schedule reviews and read video transcripts.

Whatever agent you use, the agent must be able to **read files, edit files in this folder, and run `python` commands**. Allow these three commands without asking every time; keep approval prompts on for everything else:

```
python tools/tracker.py
python tools/srs.py
python tools/transcript.py
```

## Which agent should I use?

| Agent | Cost (Sept 2026) | Reads `AGENTS.md` | Commands appear as | Notes |
|---|---|---|---|---|
| [Google Antigravity](https://antigravity.google/download) | free Individual plan (weekly quota, numbers unpublished) | yes | `/today` | the recommended free option |
| [Claude Code](https://code.claude.com/docs/en/setup) | paid (Claude Pro or higher) | via `CLAUDE.md` | `/today` | uses the generated `.claude/skills/` |
| [GitHub Copilot in VS Code](https://code.visualstudio.com/docs/agent-customization/agent-skills) | Copilot Free (small monthly allowance) or paid | yes | `/today` in agent mode | reads `.agents/skills/` |
| [Cursor](https://cursor.com/docs/skills) | free Hobby plan (limited) or paid | yes | `/today` | reads `.agents/skills/` |
| [OpenAI Codex](https://developers.openai.com/codex/skills) | limited use on free ChatGPT, more on paid | yes | type `today` | reads `.agents/skills/` |
| [OpenCode](https://opencode.ai/docs/skills/) | free, with free models (OpenCode Zen or OpenRouter `:free`) | yes | `/today` | uses the generated `.opencode/commands/` |
| [Gemini CLI](https://geminicli.com/docs/cli/skills/) | needs a Gemini API key (free tier is small) | via `.gemini/settings.json` | type `today` | personal free tier ended June 2026; the Antigravity CLI replaced it |
| [Windsurf](https://docs.devin.ai/desktop/cascade/skills) | free or paid plans | yes | `@today` | reads `.agents/skills/` |
| Any other agent (Zed, Aider, Cline, Roo, Kilo, Goose, Junie, Amp, ...) | varies | usually | type `today` | if needed, say "read AGENTS.md and follow it" |

Free quotas are small everywhere. The course is designed to be thrifty: a short `AGENTS.md`, skills loaded only when used, and Python doing the bookkeeping. If you run out, see "Plan B" in the README.

## Setup notes per agent

### Google Antigravity
1. Install from [antigravity.google/download](https://antigravity.google/download) and sign in with a personal Google account.
2. **Open Folder** → your copy of this repository. `AGENTS.md` and the skills load automatically.
3. In settings, add `python tools/tracker.py`, `python tools/srs.py` and `python tools/transcript.py` to the terminal command **Allow list**. Keep "Request Review" for other commands; don't switch on "Always Proceed" or "Turbo" on a personal machine.
4. Use a **Flash** model for daily sessions (it saves your weekly quota), and a **Pro** model for `/submit` and `/exam`.
5. On a laptop with 8 GB RAM the desktop app can be heavy. The lighter **Antigravity CLI** works the same way: install it with `irm https://antigravity.google/cli/install.ps1 | iex` in PowerShell (Windows) or `curl -fsSL https://antigravity.google/cli/install.sh | bash` (macOS/Linux), then run `agy` inside the folder.

### Claude Code
1. [Install](https://code.claude.com/docs/en/setup) and run `claude` inside the folder. `CLAUDE.md` imports `AGENTS.md`; the commands come from `.claude/skills/`.
2. When asked to run `python tools/tracker.py ...`, choose the option that always allows it.
3. On Windows without Git Bash, Claude Code uses PowerShell; if `python` isn't found, the Mentor will use `py`.

### GitHub Copilot in VS Code
1. Open the folder in VS Code, open Copilot Chat and switch to **Agent** mode.
2. Type `/` to see the course commands (VS Code reads `.agents/skills/`). If they don't appear, update VS Code, or type "follow the today skill".
3. Approve the tracker commands when asked.

### Cursor
Open the folder; Cursor reads `AGENTS.md` and `.agents/skills/`. Type `/today` in the agent chat.

### OpenAI Codex (CLI, IDE extension or app)
Run Codex in the folder. It reads `AGENTS.md` and discovers `.agents/skills/`. Type `today`, `quiz`, `recall` and so on; Codex loads the matching skill.

### OpenCode
Run `opencode` in the folder and pick a free model. `/today` and the other commands come from `.opencode/commands/`, which point to the skills.

### Gemini CLI
The repository's `.gemini/settings.json` makes Gemini CLI read `AGENTS.md`, and Gemini CLI also reads `.agents/skills/`. It needs a Gemini API key; the free personal Google-login tier ended in June 2026.

### Windsurf
Open the folder. Skills from `.agents/skills/` are used automatically, or mention them with `@today`.

### Any other agent
If your agent doesn't read `AGENTS.md` on its own, start the chat with: "Read AGENTS.md and act as the Mentor it describes." Then type the command words (`start`, `today`, `quiz`, ...).

## No agent at all
You can still follow the course with a free chat app (Gemini, ChatGPT, Claude) and the tracker on your own computer. See "Plan B" in the README.

## Keeping this page current
Agents change their conventions often. If something here stops working, please open an "AI agent problem" issue or a pull request ([CONTRIBUTING.md](../CONTRIBUTING.md)). Maintainers regenerate adapters with `python scripts/sync_agents.py`.
