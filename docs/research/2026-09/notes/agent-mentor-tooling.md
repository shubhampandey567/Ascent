# AI coding-agent tools as a free, folder-based "mentor" (Google Antigravity, Claude Code, Gemini CLI + free fallbacks), state as of 2026-09-24

_All URLs were accessed on 2026-09-24 unless a date is given. Most official doc pages carry no "last updated" date, so "as fetched 2026-09-24" is the best available timestamp. Tags: **[SECONDARY]** = third-party or press source, not confirmed on an official page. **[UNVERIFIED]** = could not be confirmed. **[CONFLICT]** = sources disagree. **[OUTDATED?]** = may be stale._

---

## 1. Google Antigravity: status, free tier, quotas, paid tiers (incl. India), models, system requirements (Windows 11 / 8 GB RAM / no GPU)

### Takeaway
As of Sept 2026, Antigravity is Generally Available. It ships as three surfaces: the Antigravity 2.0 desktop app (launched at I/O on May 19, 2026), the Antigravity IDE, and the `agy` CLI. There is a $0 "Individual" plan for personal Google accounts (18+, approved countries) that includes Gemini 3.x Flash and Pro, Claude Sonnet/Opus 4.6 and gpt-oss-120b. Its quota refreshes only **weekly**, and Google publishes no numeric limits. Windows 10/11 x64 is officially supported and no GPU is needed because the models run in the cloud. No RAM minimum is published, and community reports of multi-GB memory use make 8 GB tight for the full GUI. The Go-based CLI is the lighter option.

### Cited Findings
**Status and product surfaces**
- The pricing page labels the Individual and Google AI Pro tiers "Generally Available", marks Ultra "New!", and marks the Organization plan "Now Available". — [Antigravity pricing](https://antigravity.google/pricing)
- I/O post dated **May 19, 2026**: Antigravity 2.0 is "a standalone desktop application that delivers the first major step towards our vision of an independent agent-focused surface". The same post announces the Antigravity CLI, the "Antigravity agent via the Gemini API", and the Antigravity SDK ("available today in preview"). — [Antigravity blog, I/O 2026](https://antigravity.google/blog/google-io-2026); corroborated by [Google blog, I/O 2026 developer highlights (May 19, 2026)](https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/)
- Earlier (2025) coverage described Antigravity as a "Public Preview". — [DEV Community](https://dev.to/blamsa0mine/google-antigravity-public-preview-what-it-is-how-it-works-and-what-the-limits-really-mean-4pe) [SECONDARY; historical context only]
- Versions on the download page as fetched 2026-09-24: Antigravity 2.0 **v2.17.0**, Antigravity CLI **v1.2.9**, Antigravity IDE **v2.5.5**, Antigravity SDK **v0.1.18** (Python). IDE extensions are listed for VS Code, Visual Studio, JetBrains, Zed and Xcode. — [Antigravity download](https://antigravity.google/download)
- The Antigravity CLI is "Built in Go" and described as "snappier and more responsive". — [Google Developers Blog, May 19, 2026](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)

**Free tier and eligibility**
- Individual plan: "$0/month". Features, quoted verbatim: "Agent model: access to Gemini 3.8 Flash, Gemini 3.7 Flash, Gemini 3.6 Flash, Gemini 3.1 Pro, Claude Sonnet & Opus 4.6, gpt-oss-120b"; "Unlimited Tab completions"; "Unlimited Command requests"; "Basic weekly rate limits". — [Antigravity pricing](https://antigravity.google/pricing)
- All plans get "Unlimited Tab completions" and "Access to all product features, such as the Scheduled Tasks and the CLI". — [Antigravity docs: Plans](https://antigravity.google/docs/plans)
- "At the moment, Antigravity is unavailable to under-18 users." "Google Antigravity is currently available for personal Google accounts in approved geographies." The FAQ lists 224 countries and territories. — [Antigravity FAQ](https://antigravity.google/docs/faq)
- "You may opt out of data collection at any point from the Settings panel." — [Antigravity FAQ](https://antigravity.google/docs/faq)
- The pricing, plans and FAQ pages as fetched do not mention a credit-card requirement for the Individual plan. — [pricing](https://antigravity.google/pricing), [plans](https://antigravity.google/docs/plans)

**Quotas and rate limits (no numbers are published)**
- Free/baseline: "Meaningful quota, refreshed weekly"; "Weekly rate limit". — [Plans](https://antigravity.google/docs/plans)
- Google AI Pro: "High, generous quota, refreshed every five hours until weekly limit reached"; "Higher weekly rate limit". — [Plans](https://antigravity.google/docs/plans)
- Google AI Ultra: "highest, most generous quota, refreshed every five hours"; "Highest weekly rate limits"; "Access to third-party models". — [Plans](https://antigravity.google/docs/plans)
- Limits are "correlated with the amount of work done by the agent" rather than simple prompt counts. — [Plans](https://antigravity.google/docs/plans)
- AI credits: Pro and Ultra users can "utilize purchased AI credits (or any one-time promotional credits) for additional overage usage". Credits are bought via one.google.com/ai/credits, consumed "at standard Gemini Enterprise consumption pricing", and controlled by an "AI Credit Overages" setting ("Never" / "Always"). The page does not say whether free users can buy credits. — [Plans](https://antigravity.google/docs/plans)
- Third-party analyses agree that Google publishes no absolute quota figures for any tier. — [datastudios.org](https://www.datastudios.org/post/is-google-antigravity-free-to-use-pricing-limits-and-what-developers-should-expect), [cloudzero](https://www.cloudzero.com/blog/google-antigravity-pricing/) [SECONDARY]
- One blog estimates the Antigravity CLI free ceiling at "low tens of requests per day". — [yaw.sh](https://yaw.sh/blog/gemini-cli-not-free-alternatives/) [SECONDARY, UNVERIFIED]

**Paid tiers and prices (incl. India)**
- The pricing page lists Individual ($0), Google AI Pro, Google AI Ultra and "Organization plan via Google Cloud", but shows no prices for Pro or Ultra and **no INR prices**. — [pricing](https://antigravity.google/pricing)
- At I/O (May 19, 2026) Google launched a "new $100 per month Google AI Ultra plan" with "five times the capacity of the Google AI Pro plan". A $100 bonus-credit promo expired May 25, 2026. — [Antigravity blog](https://antigravity.google/blog/google-io-2026), [Google blog](https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/)
- India offer: Jio SIM users aged 18+ on an active unlimited 5G plan of ₹349 or above can get **18 months of Google AI Pro free** (valued at ~₹35,100), claimed via the MyJio app with a Gmail ID. — [Jio Google Gemini offer page](https://www.jio.com/google-gemini-offer/) (from search result, page not fetched); [Gulf News](https://gulfnews.com/technology/companies/google-and-jio-launch-free-18-month-ai-pro-access-for-millions-in-india-1.500328266) [SECONDARY]
- A separate one-year free Google AI Pro promotion for Indian college students reportedly ran "until September 15". The year and whether it is still open are unclear. — search-result summaries of [Medium](https://colinritman.medium.com/how-to-get-google-ai-pro-5tb-for-18-months-free-or-for-50-if-you-are-not-eligible-492963a96f00) and others [SECONDARY, UNVERIFIED]

**Models**
- Docs model list: "Gemini 3.8 Flash", "Gemini 3.7 Flash", "Gemini 3.6 Flash" (tier "Fast"), "Gemini 3.1 Pro" (tier "High"), "Claude Sonnet 4.6 (thinking)", "Claude Opus 4.6 (thinking)", "GPT-OSS-120b". The Gemini models offer Low, Medium or High thinking levels. "Nano Banana 2" is used for image generation, e.g. UI mockups. The model choice "is sticky between user messages within a conversation". The section heading references "Free & Google AI Plus Plan". — [Antigravity docs: Models](https://antigravity.google/docs/models)
- At I/O 2026, "Gemini 3.5 Flash, is now the default Gemini Flash model on Google Antigravity". Newer Flash versions have since superseded it (see above). — [Antigravity blog](https://antigravity.google/blog/google-io-2026)
- **[CONFLICT]** The pricing page lists Claude Sonnet/Opus 4.6 under the free Individual plan, but the Plans doc lists "Access to third-party models" as an Ultra benefit. — [pricing](https://antigravity.google/pricing) vs [plans](https://antigravity.google/docs/plans)

**System requirements**
- Windows: "Windows 10 (64 bit)" (download page: "Windows 10 (64-bit) or later"), x64 and ARM64. macOS: "Min Version 12 (Monterey)", Apple Silicon or Intel. Linux: "glibc >= 2.28, glibcxx >= 3.4.25 (e.g. Ubuntu 20, Debian 10, Fedora 36, RHEL 8)". **No RAM, CPU-speed, disk or GPU requirement is listed.** — [Getting started](https://antigravity.google/docs/getting-started), [Download](https://antigravity.google/download)
- Community reports of heavy memory use:
  - one user saw Antigravity reach 12.8 GB (80%) on a 16 GB laptop;
  - "Antigravity Helper (Renderer)" and "Helper (Plugin)" processes used >120% CPU with ~4.8 GB resident memory;
  - memory can pass 75% within minutes even with one agent.
  - Sources: [Google AI Developers Forum thread](https://discuss.ai.google.dev/t/antigravity-memory-consumption/122512), [Antigravity Lab](https://antigravitylab.net/en/articles/tips/antigravity-high-cpu-memory-usage-fix), [Medium](https://aakash4dev.medium.com/stop-antigravity-from-eating-your-ram-a-simple-linux-fix-9e548d3a4481) [SECONDARY, anecdotal, via search summaries]

### Inferences
- **HP 14 (2021), Windows 11, 8 GB RAM, no NVIDIA GPU:**
  - Officially supported: Windows 10+ x64, and a GPU is irrelevant because inference is cloud-side.
  - In practice the full desktop app or IDE (Electron-style multi-process, plus a Chrome instance for browser tasks) may swap heavily on 8 GB. The anecdotes above are from 16 GB machines.
  - Recommendation: use the **`agy` CLI** (Go binary) in Windows Terminal plus a light editor. If you use the GUI, close other apps and avoid browser-agent tasks.
- The free weekly quota fits a "few mentor sessions per week" pattern, not all-day use. Design the mentor to be token-thrifty: short AGENTS.md, skills loaded on demand, and the Python helper doing the bookkeeping instead of the model.
- "Unlimited Command requests" most likely refers to the editor's inline command feature, not agent turns. The agent is what consumes the weekly quota. [inference]
- The Jio offer's ₹35,100 for 18 months implies a Google AI Pro list price of about ₹1,950/month in India. [derived arithmetic, not an official price quote]

### Gaps
- No official numeric quota for any tier (requests, tokens or "work units"). Google does not publish them.
- Google AI Pro and Ultra prices (USD or INR) are not shown on Antigravity pages. The only official price is the new $100/month Ultra plan from the I/O post. The "Google AI Plus" plan named on the Models page has no price or quota details there.
- India is presumably among the 224 approved countries, but the fetched FAQ text did not explicitly confirm it.
- No official RAM or CPU minimum. The 8 GB assessment rests on anecdotes.
- The Claude-on-free-plan conflict (pricing page vs Plans doc) is unresolved.

---

## 2. Antigravity customization, exactly: rules, workflows (deprecated), skills, AGENTS.md/GEMINI.md, terminal/file permissions, @-mentions, CLI

### Takeaway
Antigravity 2.0 moved its config from `.agent/` (singular, now legacy) to **`.agents/`**:
- Rules live in `.agents/rules/*.md` with a `trigger:` frontmatter field.
- Skills live in `.agents/skills/<name>/SKILL.md` and are invoked as `/<name>`.
- Root `AGENTS.md` and `GEMINI.md` are read automatically.

**Workflows are deprecated and will be retired on Nov 1, 2026.** Build new "slash commands" as Agent Skills; `/migrate-workflows` converts old ones. The agent can read and write workspace files and run terminal commands. On **Windows**, commands default to "Request Review/Ask" unless allow-listed, and the terminal sandbox is only a preview there.

### Cited Findings
**Rules: locations and precedence**
- Directory-scoped rules are discovered by walking up the tree: `<dir>/AGENTS.md` or `<dir>/GEMINI.md`; `<dir>/.agents/AGENTS.md` or `<dir>/.agents/GEMINI.md`; `<dir>/.agents/rules/*.md`. The legacy `.agent/rules/*.md` is still recognized. — [Antigravity docs: Rules](https://antigravity.google/docs/rules)
- Global rules: `~/.gemini/AGENTS.md`, `~/.gemini/GEMINI.md`, `~/.gemini/config/AGENTS.md`, `~/.gemini/config/GEMINI.md`, `~/.gemini/config/rules/*.md` (modular, frontmatter required). CLI-specific global rules: `~/.gemini/antigravity-cli/rules/*.md`. — [Rules](https://antigravity.google/docs/rules)
- Rules from all scopes combine cumulatively, and directory-scoped rules take priority over global ones. — [Rules](https://antigravity.google/docs/rules)

**Rules: format, triggers and limits**
- Files in `.agents/rules/` **require** YAML frontmatter with `trigger`. `AGENTS.md` and `GEMINI.md` do **not**. — [Rules](https://antigravity.google/docs/rules)
- The four `trigger` values:
  - `always_on`: "full content into the system prompt on every turn".
  - `model_decision`: "injects only the rule's path and description upfront". `description` is required.
  - `glob`: activates when the agent touches files matching `globs:`. The doc's pattern example is `"*.proto, **/*.pb.go"`, and the field is given as "`globs` or `glob`".
  - `manual`: "loaded...only when you explicitly `@`-mention it in chat".
  - Source: [Rules](https://antigravity.google/docs/rules)
- Limits: "Antigravity truncates any single rule file that exceeds 24,000 bytes (after expanding @[label](path) includes)". All active global and `always_on` rules share "a 20,000-token aggregate rules budget separate from the customization budget". Over budget, larger files are demoted to pointers that load on demand. — [Rules](https://antigravity.google/docs/rules)
- @ syntax inside rules: `@[label](path)` **inlines** the file's contents; `@filename` resolves the path **without** inlining. — [Rules](https://antigravity.google/docs/rules)

Minimal rule files, built from the documented fields (adapted, not copied from a doc code block):
```markdown
<!-- .agents/rules/mentor-persona.md -->
---
trigger: always_on
---
You are a patient programming mentor for a beginner. Ask before giving full solutions.
```
```markdown
<!-- .agents/rules/python-style.md -->
---
trigger: glob
globs: "**/*.py"
---
Explain every new Python concept in one sentence before using it.
```
```markdown
<!-- .agents/rules/quiz-mode.md -->
---
trigger: model_decision
description: Use when the learner asks to be quizzed or tested.
---
Ask one question at a time; wait for the answer; grade it; record via tools/mentor.py.
```

**Workflows (DEPRECATED: retired Nov 1, 2026)**
- "Workflows are being deprecated in favor of Agent Skills by November 1, 2026." A migration guide and a `/migrate-workflows` command are provided. — [Antigravity docs: IDE Workflows](https://antigravity.google/docs/ide/workflows/); "Workflows are deprecated and will be retired on November 1, 2026" — [Workflows to Skills Migration](https://antigravity.google/docs/migration/workflows-to-skills/)
- Workflows are "saved as markdown files", limited to "12,000 characters each", and invoked as `/workflow-name`. Nesting works: "/workflow-1 can include instructions like 'Call /workflow-2' and 'Call /workflow-3'". They are created in the Customizations panel (Global or Workspace), or the agent can generate them. — [IDE Workflows](https://antigravity.google/docs/ide/workflows/)
- 2.0-era workflow paths: workspace `.agents/workflows/<name>.md`, global `~/.gemini/config/workflows/<name>.md`. Frontmatter is `name` + `description`. — [Migration guide](https://antigravity.google/docs/migration/workflows-to-skills/)
- Legacy (2025 launch era) layout: `.agent/workflows/*.md` with `description:` frontmatter, a separate global workflows folder, a `// turbo` annotation above a step to auto-run its command, and `// turbo-all` to auto-run every command. — [DEV Community](https://dev.to/malloc72p/antigravity-getting-the-most-out-of-agentic-coding-with-rules-skills-and-workflows-54pb), [agentpedia.codes](https://agentpedia.codes/rules/antigravity-workflows/antigravity-workflow-fundamentals) [SECONDARY, OUTDATED?]
- Verbatim "Before" workflow from the migration guide:
```markdown
---
name: build-and-test
description: Run test suites and verify build
---

Run the following checks sequentially:
1. First run `npm run check` to verify TypeScript and template integrity.
2. Next execute `npm run test` for unit tests.
3. If tests pass, run `npm run build` and report the generated bundle size.
```
- What `/migrate-workflows` does, step by step:
  1. Scans the global and workspace workflow directories.
  2. Parses each workflow's frontmatter and body.
  3. Creates `.agents/skills/<workflow-name>/SKILL.md`.
  4. Renames the originals with a `.bak` suffix.
  5. Activates the new skills immediately for slash commands.
  - Source: [Migration guide](https://antigravity.google/docs/migration/workflows-to-skills/)

**Agent Skills (the replacement for workflows and custom slash commands)**
- Paths by surface:
  - Antigravity 2.0: workspace `<workspace-root>/.agents/skills/<skill-folder>/`, global `~/.gemini/config/skills/<skill-folder>/`.
  - CLI: workspace `.agents/skills/`, global `~/.gemini/antigravity-cli/skills/`, plugins `~/.gemini/antigravity-cli/plugins/<name>/skills/`.
  - IDE: workspace `.agents/skills/`, global `~/.gemini/config/skills/` (legacy `~/.gemini/antigravity/skills/` still supported).
  - "backward compatibility maintained for `.agent/skills`".
  - Source: [Antigravity docs: Skills](https://antigravity.google/docs/skills)
- SKILL.md frontmatter: `name` is optional and defaults to the folder name; `description` is required ("what the skill does and when to use it"). Optional folders: `scripts/`, `examples/`, `resources/`. The Google codelab instead shows `scripts/`, `references/`, `assets/`. — [Skills](https://antigravity.google/docs/skills), [Codelab](https://codelabs.developers.google.com/getting-started-google-antigravity)
- Skills load in three phases (Discovery → Activation → Execution). They "activate autonomously or via manual slash commands (`/<skill-name>`)". — [Skills](https://antigravity.google/docs/skills)
- Verbatim "After" skill from the migration guide. The directory is `.agents/skills/build-and-test/` containing `SKILL.md` and `scripts/verify-bundle.js`.
````markdown
---
name: build-and-test
description: Runs full validation suite including TypeScript checks, unit tests, and production build verification. Use before submitting changes.
---

# Build and Test Suite

Execute the project verification pipeline:

1. **Type & Template Diagnostics**:
   ```bash
   npm run check
   ```

2. **Unit Tests**:
   ```bash
   npm run test
   ```

3. **Production Build & Bundle Size Analysis**:
   ```bash
   npm run build
   node scripts/verify-bundle.js
   ```
````
(Source: [Migration guide](https://antigravity.google/docs/migration/workflows-to-skills/))

**Built-in slash commands (2.0 / CLI)**
- Built-ins:
  - `/boost`, `/teamwork-preview`, `/goal`, `/plan` ("Structured planning with requirement discovery");
  - `/grill-me` ("Interactive design alignment interview");
  - `/learn` ("Distills session feedback and corrections into persistent Rules or Skills");
  - `/schedule` (cron-based background automation), `/browser`, `/btw`.
- "Public slash commands are supported across Antigravity developer surfaces." Arguments are given as free text after the command, e.g. `/plan Refactor our authentication middleware...`.
- The page does not document a separate custom-command file format. Custom slash commands come from Skills.
- Source: [Antigravity docs: Slash commands](https://antigravity.google/docs/slash-commands/)

**Terminal and file permissions / auto-execution**
- Antigravity 2.0 on macOS/Linux has three presets under Settings → General → Permission Settings, overridable per project under Settings → Projects:
  - "Default": commands run without prompting inside the Terminal Sandbox; running outside it needs approval.
  - "Request Review": sandbox disabled; every command needs approval.
  - "Turbo": "All commands run without prompting with no isolation or restrictions".
  - Source: [Agent settings](https://antigravity.google/docs/agent-settings/), [Permissions](https://antigravity.google/docs/permissions)
- **Windows** "Terminal Command Auto Execution" options:
  - "Request Review": the agent never runs commands without prompting, except Allow-list items.
  - "Proceed in Sandbox": commands auto-run in the sandbox; anything outside needs review.
  - "Always Proceed": runs without prompting, except Deny-list items.
  - "Agent Non-Workspace File Access" is disabled by default. Windows commands "default to Ask", and "sandboxing [is] available as preview feature".
  - Source: [Agent settings](https://antigravity.google/docs/agent-settings/), [Permissions](https://antigravity.google/docs/permissions)
- Rule grammar is `action(target)`, evaluated "Deny > Ask > Allow". Actions and workspace defaults:

  | Action | Target | Workspace default |
  |---|---|---|
  | `read_file` | path | auto-allowed |
  | `write_file` | path | auto-allowed |
  | `read_url`, `execute_url` | domain | Ask |
  | `command` | `prefix`, `regex:pattern` or `*` | Ask (allowed in-sandbox under Default) |
  | `mcp` | `server/tool` | Ask |
  | `unsandboxed` | (Windows/CLI only) | Ask |

  "Allowing `write_file` on a path automatically grants `read_file` on that path." — [Permissions](https://antigravity.google/docs/permissions)
- CLI permissions live in `~/.gemini/antigravity-cli/settings.json`. Verbatim example:
```json
{
    "permissions": {
        "allow": [
            "command(git)",
            "command(regex:npm run (build|lint|test))",
            "read_file(/var/log/app)",
            "write_file(src/)",
            "read_url(google.com)",
            "mcp(linter/*)"
        ],
        "deny": [
            "command(rm -rf)",
            "command(sudo)",
            "write_file(.git/)"
        ],
        "ask": ["command(*)", "execute_url(aws.amazon.com)"]
    }
}
```
(Source: [Permissions](https://antigravity.google/docs/permissions))

**Antigravity CLI (`agy`): install, auth, Gemini CLI migration**
- Install commands (no Node.js prerequisite is mentioned):
  - Windows PowerShell: `irm https://antigravity.google/cli/install.ps1 | iex`
  - Windows CMD: `curl -fsSL https://antigravity.google/cli/install.cmd -o install.cmd && install.cmd && del install.cmd`
  - macOS/Linux: `curl -fsSL https://antigravity.google/cli/install.sh | bash`
  - Source: [CLI install](https://antigravity.google/docs/cli/install), [Download](https://antigravity.google/download)
- Binary location: Windows `C:\Users\<username>\AppData\Local\agy\bin`; macOS/Linux `~/.local/bin/agy`. — [CLI install](https://antigravity.google/docs/cli/install)
- Auth options:
  - OS-keyring / browser sign-in.
  - An SSH OAuth flow.
  - A Gemini API key: set `modelProvider` to `gemini` and export `GEMINI_API_KEY`.
  - `/logout` clears credentials.
  - Source: [CLI install](https://antigravity.google/docs/cli/install)
- Migration from Gemini CLI:
  - `agy plugin import gemini` imports configuration; "legacy commands converted to skills".
  - Skills move from `~/.gemini/skills/` → `~/.gemini/antigravity-cli/skills/` and `.gemini/skills/` → `.agents/skills/`.
  - MCP config moves from `~/.gemini/settings.json` → `~/.gemini/config/mcp_config.json` (global) or `.agents/mcp_config.json` (workspace).
  - "The agent continues to parse and enforce rule constraints defined inside your active directory's `GEMINI.md` and `AGENTS.md` files."
  - Source: [GCLI migration](https://antigravity.google/docs/cli/gcli-migration)
- Also carried over: "Agent Skills, Hooks, Subagents, and Extensions (now as Antigravity plugins)". — [Google Developers Blog](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)

### Inferences
- **For the mentor ecosystem, do not build new Antigravity workflows** (retiring Nov 1, 2026). Build each command as an Agent Skill in `.agents/skills/<name>/SKILL.md` and invoke it as `/<name>`. Workflows could chain (`Call /workflow-2`); skills have no documented chaining, so write "then follow the steps in the `/quiz` skill" as plain instruction text. That is unverified behaviour.
- Put the mentor persona in root `AGENTS.md`. Antigravity reads it with no frontmatter, and so do Claude Code and others (see Q3/Q5). Use `.agents/rules/*.md` only for Antigravity-specific or conditional (glob / model_decision) rules.
- Allow-list the helper so the mentor can run it without a prompt every time. In the CLI, add `"allow": ["command(python tools/mentor.py)"]`, adapted from the documented `command(prefix)` form. In the Windows GUI, keep "Request Review" and add the same prefix to the Allow list. This avoids "Always Proceed/Turbo" on a personal laptop.
- `@[label](path)` in an Antigravity rule inlines the file, but a bare `@file` only resolves the path. Claude Code's `@path` always inlines (Q3). A shared AGENTS.md using `@docs/x.md` will therefore behave differently in the two tools. Keep AGENTS.md self-contained or tell the agent explicitly to read the file.
- The built-in `/learn`, `/grill-me` and `/schedule` commands are relevant to a mentor: saving corrections as rules, Socratic interviews, and scheduled reminders.

### Gaps
- Whether a skill can receive structured arguments (an equivalent of `$ARGUMENTS`) is undocumented. Only free-text-after-command is shown for built-ins.
- Whether one skill can invoke another skill is not documented.
- Exact @-mention syntax for files and folders in the chat box was not captured. Only `@`-mentioning manual rules in chat and the in-rule syntax are documented.
- Whether Antigravity tolerates Claude-Code-only frontmatter keys (e.g. `disable-model-invocation`) in `.agents/skills` was not verified.
- The exact YAML shape of `globs` (string vs list) is shown only as a comma-separated string example.

---

## 3. Claude Code (2026): commands vs skills, frontmatter, arguments, CLAUDE.md imports, native AGENTS.md, cheapest access (incl. India), free access, Windows requirements

### Takeaway
- Custom commands and skills are merged: `.claude/commands/<name>.md` and `.claude/skills/<name>/SKILL.md` both create `/<name>`. Skills are the recommended form and add supporting files plus many frontmatter options.
- `$ARGUMENTS` and **0-based** `$0`, `$1`… substitutions work.
- CLAUDE.md supports `@path` imports (max depth 4).
- Since **v2.1.277**, Claude Code reads `AGENTS.md` natively, but by default only when no `CLAUDE.md` or `CLAUDE.local.md` exists.
- There is **no free access**: the Free claude.ai plan excludes Claude Code. The cheapest route is Pro at $17/mo billed annually ($20 monthly); in India, Pro is ₹2,000/mo billed annually, payable by card or app-store billing only (no UPI).

### Cited Findings
**Commands vs skills**
- "Custom commands have been merged into skills. A file at `.claude/commands/deploy.md` and a skill at `.claude/skills/deploy/SKILL.md` both create `/deploy` and work the same way. Your existing `.claude/commands/` files keep working." — [Claude Code docs: Skills](https://code.claude.com/docs/en/skills)
- Storage and precedence:
  - Enterprise (managed) > Personal `~/.claude/skills/<name>/SKILL.md` > Project `.claude/skills/<name>/SKILL.md`.
  - Nested `<subdir>/.claude/skills/` and `--add-dir` directories load at project level.
  - Plugin skills are namespaced `/plugin-name:skill-name`.
  - Your skill replaces a bundled skill with the same name.
  - Source: [Skills](https://code.claude.com/docs/en/skills)
- Claude Code skills "follow the Agent Skills open standard". — [Skills](https://code.claude.com/docs/en/skills)

**Frontmatter fields (current)**
| Field | Purpose |
|---|---|
| `name` | Defaults to the directory name. |
| `description` | Recommended. Combined with `when_to_use`, truncated at **1,536 chars**. |
| `when_to_use` | Extra trigger context, appended to `description`. |
| `argument-hint` | Hint shown in autocomplete, e.g. `[issue-number]`. |
| `arguments` | Named positional args for `$name`. |
| `disable-model-invocation` | `true` means only you can invoke it. Default `false`. |
| `user-invocable` | `false` hides it from the `/` menu. |
| `allowed-tools` | Tools usable without prompting during that turn. |
| `disallowed-tools` | Tools removed while the skill is active. |
| `model` | Model override, or `inherit`. |
| `effort` | `low` / `medium` / `high` / `xhigh` / `max`. |
| `context: fork` | Run as a forked subagent. |
| `agent` | Subagent type for `context: fork`. |
| `background` | For `context: fork`; needs v2.1.218+. |
| `hooks` | Hooks registered while the skill runs. |
| `paths` | Globs that limit auto-activation. |
| `shell` | `bash` (default) or **`powershell`**; used by `` !`cmd` `` injection. |
| `metadata`, `license`, `compatibility` | Accepted, not acted on. |

(Source: [Skills](https://code.claude.com/docs/en/skills))
- Fields in the Agent Skills spec (portable): `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`. The other fields are Claude Code-only, and uploading a skill with them to claude.ai or the Skills API is a "hard error". — [Skills](https://code.claude.com/docs/en/skills)

**Arguments and substitutions**
| Placeholder | Meaning |
|---|---|
| `$ARGUMENTS` | All arguments. |
| `$ARGUMENTS[N]` | Argument by **0-based** index. |
| `$N` | Shorthand for `$ARGUMENTS[N]`, e.g. `$0`, `$1`. |
| `$name` | Named argument from the `arguments` field. |
| `${CLAUDE_SESSION_ID}`, `${CLAUDE_EFFORT}` | Session ID, current effort level. |
| `${CLAUDE_SKILL_DIR}` | The skill's own folder. |
| `${CLAUDE_PROJECT_DIR}` | Project root; v2.1.196+. |

(Source: [Skills](https://code.claude.com/docs/en/skills))
- Dynamic context:
  - `` !`<command>` `` runs a shell command before the skill is sent, and its output replaces the placeholder. A fenced block starting with ` ```! ` does the same for multiple lines.
  - Any non-zero exit aborts the invocation, except exit 1 from grep/find/diff.
  - `{"disableSkillShellExecution": true}` disables it.
  - It never runs for skills synced from claude.ai (v2.1.228+).
  - Source: [Skills](https://code.claude.com/docs/en/skills)
- Keep SKILL.md under 500 lines. Invoked skill content stays in context. After compaction, each skill is re-attached with its first 5,000 tokens, within a shared 25,000-token budget. — [Skills](https://code.claude.com/docs/en/skills)
- Verbatim minimal SKILL.md from the docs:
```markdown
---
description: Summarizes uncommitted changes and flags anything risky. Use when the user asks what changed.
---

## Current changes

!`git diff HEAD`

## Instructions

Summarize the changes above in two or three bullet points, then list any risks you notice such as missing error handling, hardcoded values, or tests that need updating.
```

**CLAUDE.md, imports and AGENTS.md**
- Syntax is `@path/to/import`. Relative paths resolve from the importing file, absolute paths are allowed, and nesting is limited to "a maximum depth of four hops". Imports inside code spans and fenced blocks are skipped. External imports (outside the working directory) trigger a one-time approval dialog. — [Claude Code docs: Memory](https://code.claude.com/docs/en/memory)
- Locations:
  - Project: `./CLAUDE.md` or `./.claude/CLAUDE.md`.
  - Local: `./CLAUDE.local.md` (gitignore it).
  - User: `~/.claude/CLAUDE.md`.
  - Rules: `.claude/rules/*.md`.
  - Files are concatenated from filesystem root down to the working directory; subdirectory CLAUDE.md files load lazily.
  - Block-level HTML comments are stripped.
  - Source: [Memory](https://code.claude.com/docs/en/memory)
- **Native AGENTS.md:** "Claude Code can read AGENTS.md as your project instructions… Reading AGENTS.md directly requires Claude Code v2.1.277 or later." Default behaviour:
  - Claude reads AGENTS.md only if there is no `CLAUDE.md`, `.claude/CLAUDE.md` or `CLAUDE.local.md` in the working directory or above it.
  - `~/.claude/CLAUDE.md` and `.claude/rules/` do not count, and keep loading alongside.
  - It also reads `.claude/AGENTS.md`.
  - It does **not** read `AGENTS.local.md`, `AGENTS.override.md`, "or anything under a `.agents/` directory".
  - Source: [Memory](https://code.claude.com/docs/en/memory)
- `/config` → **Project instructions** can be `claude-md-or-agents-md` (default), `claude-md-and-agents-md`, `claude-md` or `managed-only`. Equivalent JSON, valid only in user, `--settings` or managed settings files:
```json
{
  "pluginConfigs": {
    "agents-md@builtin": {
      "options": { "instructionFiles": "claude-md-and-agents-md" }
    }
  }
}
```
(Source: [Memory](https://code.claude.com/docs/en/memory))
- Import pattern, verbatim ("Claude reads the imported file first, then the rest"):
```markdown
@AGENTS.md

## Claude Code

Use plan mode for changes under `src/billing/`.
```
  Keeping the import "never makes Claude read AGENTS.md twice". On **Windows**, prefer the import over a symlink: "Creating a symlink there needs Administrator privileges or Developer Mode, and Git checks a committed symlink out as a plain text file unless `core.symlinks` is enabled". — [Memory](https://code.claude.com/docs/en/memory)
- `/import` (v2.1.213+) copies another agent's config into Claude Code, including AGENTS.md, MCP servers, commands, subagents and skills. — [Memory](https://code.claude.com/docs/en/memory)

**Plans, prices, free access**
- The Free plan does **not** include Claude Code: "No" in the comparison table. — [claude.com/pricing](https://claude.com/pricing). Setup docs: "Claude Code requires a Pro, Max, Team, Enterprise, or Console account. The free claude.ai plan does not include Claude Code access." — [Claude Code docs: Setup](https://code.claude.com/docs/en/setup)
- Pro: $17/month billed annually ($200 up front) or $20/month billed monthly. Max from $100/month. "Every plan has usage limits that reset on a rolling five-hour session window, and paid plans add weekly limits on top." — [claude.com/pricing](https://claude.com/pricing)
- India (TechCrunch, **July 13, 2026**): Pro "₹2,000 (about $21) a month when billed annually"; Max "₹11,999"; Team "₹2,399… per seat a month". India prices include local taxes. No UPI: "Users still need to pay by card or through Apple's and Google's app store billing systems." — [TechCrunch](https://techcrunch.com/2026/07/13/anthropic-starts-localizing-claude-pricing-for-india-its-biggest-market-after-the-us/)
- Secondary reports give Pro monthly billing at ₹2,399 and the top Max tier at ₹23,999. — search summaries citing [AIM](https://analyticsindiamag.com/ai-news/anthropic-introduces-india-specific-pricing-for-claude-ai-subscriptions) and [Croma](https://www.croma.com/unboxed/anthropic-claude-ai-india-local-pricing-plans-confirmed) [SECONDARY, UNVERIFIED on claude.com]
- The pricing page mentions an institution-wide Education plan only; no individual student discount was found. — [claude.com/pricing](https://claude.com/pricing)
- Non-Anthropic backend via Ollama:
  - `ollama launch claude`, or manually `ANTHROPIC_AUTH_TOKEN=ollama` + `ANTHROPIC_BASE_URL=http://localhost:11434` followed by `claude --model qwen3.5`.
  - Local models need a context length of "64k or higher".
  - Cloud models work via `OLLAMA_API_KEY`.
  - "Basic chat and file edits work with compatible models. Hosted WebSearch and advanced tool controls are not fully supported."
  - Source: [Ollama docs: Claude Code](https://docs.ollama.com/integrations/claude-code)

**System requirements and Windows install**
- Requirements: Windows 10 1809+ (or Server 2019+), macOS 13+, Ubuntu 20.04+, Debian 10+, Alpine 3.19+. "4 GB+ RAM, x64 or ARM64 processor". Internet is required. Shell: Bash, Zsh, PowerShell or CMD. Must be in an Anthropic-supported country. — [Setup](https://code.claude.com/docs/en/setup)
- Windows install:
  - PowerShell `irm https://claude.ai/install.ps1 | iex`, CMD `curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd`, or `winget install Anthropic.ClaudeCode`.
  - No Administrator rights needed. Git for Windows is optional: it enables the Bash tool, otherwise Claude uses the PowerShell tool.
  - Sandboxing is "Not supported" on native Windows but is supported under WSL 2.
  - The npm package needs Node.js 22+ as of v2.1.198; the native install needs no Node.
  - Source: [Setup](https://code.claude.com/docs/en/setup)

### Inferences
- **Shared mentor file for both tools:** keep the persona in root `AGENTS.md`. For Claude Code, either have no CLAUDE.md (v2.1.277+ reads AGENTS.md), or add a `CLAUDE.md` whose first line is `@AGENTS.md` if you need Claude-only notes or a `CLAUDE.local.md`. The import is the Windows-safe choice.
- **Skills must live in two places:** Claude Code does not read `.agents/` and its skills table has no `.agents/skills`. Antigravity reads `.agents/skills` (and legacy `.agent/skills`) but not `.claude/skills`. Keep `.agents/skills/` as the source of truth and have the Python helper copy it into `.claude/skills/`, since Windows symlinks need Admin or Developer Mode. For the Claude copy, the helper can inject Claude-only keys such as `disable-model-invocation: true` and `argument-hint`.
- Use `$ARGUMENTS` (not `$1`) in Claude copies. `$N` is now 0-based, so older examples that use `$1` for the first argument may be off by one. In the cross-tool body text, also say "use any text typed after the command as the topic" for Antigravity, which has no documented placeholder.
- On a Windows laptop without Git Bash, add `shell: powershell` to Claude skills that use `` !`python tools/mentor.py status` `` injection.
- With zero budget and no card, Claude Code is **not** a realistic primary tool. The Ollama route technically runs the Claude Code CLI for free, but local models need 64k+ context, which is impractical on 8 GB RAM without a GPU, and cloud free limits are undocumented.

### Gaps
- Exact permission-rule syntax for pre-approving `python tools/mentor.py` in Claude Code on Windows (Bash vs PowerShell tool names in `allowed-tools` or settings `permissions.allow`) was not fetched. The Agent Skills spec example `Bash(git:*)` is the only syntax captured.
- What Claude Code does when a skill has no `$ARGUMENTS` but the user passes arguments (e.g. whether they are appended) was not verified this session.
- Official INR prices for monthly Pro and Max 20x were not confirmed on claude.com; the pricing fetch showed USD only.
- Ollama Cloud free-tier limits are not stated on the Ollama page.

---

## 4. Gemini CLI (2026): free-tier status and limits, context files, custom commands, install requirements, Windows

### Takeaway
**The famous free Gemini CLI tier is gone.** On **June 18, 2026**, Gemini CLI "stop[ped] serving requests for Google AI Pro, Google AI Ultra, and free tier individual accounts". Google moved consumers to the Antigravity CLI (`agy`). Gemini CLI remains open source (Apache-2.0) and still works with a Gemini API key, Vertex AI, or Code Assist Standard/Enterprise. It is now at best a secondary free fallback via a free AI Studio API key, and those free API limits are uncertain and conflicting. Its file formats (GEMINI.md, TOML commands) remain documented.

### Cited Findings
**Shutdown / change history**
- Google Developers Blog, **May 19, 2026**: "On June 18, 2026, Gemini CLI and Gemini Code Assist IDE extensions will stop serving requests for Google AI Pro and Ultra". Code Assist Standard/Enterprise access "remains unchanged". Users are pointed to the migration docs. — [Google Developers Blog](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)
- GitHub announcement posted **June 18, 2026**: "Gemini CLI will stop serving requests for Google AI Pro, Google AI Ultra, and free tier individual accounts". "Enterprise users with Gemini Code Assist licenses and API key authentication remain completely unaffected." It says "Your custom and installed skills will be automatically imported" into the Antigravity CLI. — [gemini-cli Discussion #28017](https://github.com/google-gemini/gemini-cli/discussions/28017)
- The docs site banner reads: "Unpaid tier and Google One users: Gemini CLI was replaced by Antigravity CLI on June 18th, 2026." — [geminicli.com custom commands](https://geminicli.com/docs/cli/custom-commands/), [installation](https://geminicli.com/docs/get-started/installation/)
- Quota page ("Last updated Jun 18, 2026") still lists the pre-shutdown tiers:
  - Log in with Google: Gemini Code Assist (Individual) "1,000 requests" per day; Google AI Pro "1,500"; Ultra "2,000".
  - **Gemini API key, unpaid: "250 maximum model requests / user / day", "Flash model only"**.
  - Vertex AI Express Mode: free for "90 days before you need to enable billing".
  - Code Assist Standard 1,500/day; Enterprise 2,000/day.
  - Source: [geminicli.com quota & pricing](https://geminicli.com/docs/resources/quota-and-pricing/)
- **[CONFLICT/OUTDATED?]** The GitHub README still advertises Google sign-in at "60 requests/min and 1,000 requests/day" and an API key at "1000 requests/day with Gemini 3", with no deprecation banner. It appears stale. — [gemini-cli README](https://github.com/google-gemini/gemini-cli)
- **[CONFLICT, SECONDARY]** The Gemini API free tier (AI Studio key) in Sept 2026 is reported at about 20 requests/day for Gemini 3.5–3.8 Flash and 500/day for Flash-Lite models. Another source claims 1,500/day, but that is April-2026 data for 2.5 Flash. The official rate-limit page defers to AI Studio instead of listing numbers. — [aipromptshub](https://aipromptshub.co/blog/gemini-api-free-tier-rate-limits), [tokenmix](https://tokenmix.ai/blog/gemini-api-free-tier-limits), [ai.google.dev rate limits](https://ai.google.dev/gemini-api/docs/rate-limits)

**Context files (GEMINI.md)**
- Hierarchy:
  1. Global `~/.gemini/GEMINI.md`.
  2. GEMINI.md files in workspace directories and their parents.
  3. Just-in-time: "When a tool accesses a file or directory, the CLI automatically scans for GEMINI.md files in that directory and its ancestors up to a trusted root."
  - Source: [geminicli.com GEMINI.md](https://geminicli.com/docs/cli/gemini-md/)
- Imports use `@file.md` and support "both relative and absolute paths", e.g. `@./components/instructions.md`. — [GEMINI.md docs](https://geminicli.com/docs/cli/gemini-md/)
- To read AGENTS.md too, add to settings.json (verbatim): `{ "context": { "fileName": ["AGENTS.md", "CONTEXT.md", "GEMINI.md"] } }`. agents.md shows a single-string form in `.gemini/settings.json`: `{ "context": { "fileName": "AGENTS.md" } }`. — [GEMINI.md docs](https://geminicli.com/docs/cli/gemini-md/), [agents.md](https://agents.md/)
- `/memory show` displays the concatenated memory; `/memory reload` re-scans. — [GEMINI.md docs](https://geminicli.com/docs/cli/gemini-md/)

**Custom commands (TOML)**
- Locations: global `~/.gemini/commands/`, project `<project>/.gemini/commands/`. Project overrides global for the same name. Subfolders namespace with a colon, e.g. `.gemini/commands/git/commit.toml` → `/git:commit`. `/commands reload` and `/commands list` manage them. — [Custom commands](https://geminicli.com/docs/cli/custom-commands/)
- Fields: `prompt` (required string), `description` (optional, shown in `/help`). — [Custom commands](https://geminicli.com/docs/cli/custom-commands/)
- `{{args}}` is replaced by user input: shell-escaped inside `!{...}`, raw outside. If `{{args}}` is absent and arguments are given, "the full typed command appends to the prompt after two newlines". — [Custom commands](https://geminicli.com/docs/cli/custom-commands/)
- `!{...}` runs a shell command after a confirmation dialog. On failure it injects stderr plus `[Shell command exited with code 1]`. `@{...}` injects file contents or directory listings (respecting .gitignore and .geminiignore); it is processed before shell and argument substitution. — [Custom commands](https://geminicli.com/docs/cli/custom-commands/)
- Verbatim example, invoked as `/refactor:pure`:
```toml
# ~/.gemini/commands/refactor/pure.toml
description = "Asks the model to refactor the current context into a pure function."
prompt = """Please analyze the code I've provided in the current context.
Refactor it into a pure function.
Your response should include:
1. The refactored, pure function code block.
2. A brief explanation of the key changes you made and why they contribute to purity."""
```

**Install requirements**
- "Node.js 20.0.0+". OS: macOS 15+, **Windows 11 24H2+**, Ubuntu 20.04+. RAM: 4 GB+ for casual use, 16 GB+ for power users. Shell: Bash, Zsh or PowerShell. Install with `npm install -g @google/gemini-cli` (or brew, MacPorts, conda). Stable, preview and nightly channels are available. — [geminicli.com installation](https://geminicli.com/docs/get-started/installation/); `npx @google/gemini-cli`, Apache License 2.0 — [README](https://github.com/google-gemini/gemini-cli)

### Inferences
- Do not build the mentor around Gemini CLI. Its role is now "same files, optional API-key fallback".
- The Antigravity CLI imports Gemini CLI skills, and "legacy commands [are] converted to skills". It reads GEMINI.md and AGENTS.md, so GEMINI.md-based setups carry over.
- A free AI Studio API key can feed either Gemini CLI or the Antigravity CLI (`modelProvider: gemini`). At the reported ~20 RPD for current Flash models it is only an emergency fallback. Verify in AI Studio.
- Check the laptop's Windows build: Gemini CLI now lists Windows 11 **24H2+**, whereas Antigravity and Claude Code accept Windows 10.

### Gaps
- Official current free-tier RPM/RPD per model for the Gemini API. Visible only after logging in at aistudio.google.com/rate-limit.
- Whether Gemini CLI now also reads `.agents/skills` (not checked; its skills doc at geminicli.com/docs/cli/skills/ was not fetched).
- Long-term maintenance status of the open-source Gemini CLI repo beyond enterprise use is not stated.

---

## 5. AGENTS.md and Agent Skills open standards: governance and which tools read them (with the cross-tool folder layout)

### Takeaway
AGENTS.md is "now stewarded by the Agentic AI Foundation under the Linux Foundation". It is read natively by Codex, Cursor, Jules, Amp, Factory, Zed, Warp, VS Code/Copilot coding agent, Devin, Windsurf, Junie, RooCode, Kilo Code, OpenCode, Goose and Aider (via config). Primary docs confirm it is now also read by **Antigravity** and by **Claude Code (v2.1.277+)**; Gemini CLI reads it via `context.fileName`. The companion **Agent Skills** standard (SKILL.md) originated at Anthropic and is supported by Claude Code, Antigravity, Codex, Copilot/VS Code, Cursor, OpenCode, Gemini CLI, Roo Code and others. Because the two tools use different skill folders, one AGENTS.md can serve both, but skills need two copies.

### Cited Findings
- AGENTS.md is "A simple, open format for guiding coding agents". It is "now stewarded by the Agentic AI Foundation under the Linux Foundation", and it came out of work by OpenAI Codex, Amp, Jules, Cursor and Factory. — [agents.md](https://agents.md/)
- Tools listed on agents.md: Codex, Jules, Factory, Aider, Goose, Opencode, Zed, Warp, VS Code, Devin, UiPath, Junie, Amp, Cursor, RooCode, Gemini CLI, Kilo Code, Phoenix, Semgrep, GitHub Copilot Coding Agent, Ona, Windsurf, Augment Code. The list as fetched does not name Claude Code or Antigravity, which both read it now (next bullets). — [agents.md](https://agents.md/)
- Nesting: "Agents automatically read the nearest file in the directory tree, so the closest one takes precedence." Aider uses `read: AGENTS.md` in `.aider.conf.yml`; Gemini CLI uses `{ "context": { "fileName": "AGENTS.md" } }`. — [agents.md](https://agents.md/)
- Antigravity reads `AGENTS.md` and `GEMINI.md` in the workspace root and subdirectories, and `~/.gemini/AGENTS.md` globally. — [Antigravity Rules](https://antigravity.google/docs/rules)
- Claude Code reads AGENTS.md natively from v2.1.277, with the default and settings behaviour described in Q3. — [Claude Code Memory](https://code.claude.com/docs/en/memory)
- Codex: "AGENTS.md support" is available across all plan tiers. — [ChatGPT/Codex pricing](https://learn.chatgpt.com/docs/pricing)
- Agent Skills: "originally developed by Anthropic, released as an open standard". The client showcase includes Claude Code, Claude, Gemini CLI, OpenCode, Cursor, Amp, Goose, GitHub Copilot, VS Code, ChatGPT & Codex, Roo Code, Junie, Factory, Kiro, TRAE, OpenHands, Letta and others. — [agentskills.io](https://agentskills.io/)
- Spec constraints:
  - `name`: required, 1–64 chars, lowercase `a-z0-9` and hyphens, no leading, trailing or consecutive hyphens, "Must match the parent directory name".
  - `description`: required, 1–1024 chars, says what the skill does and when to use it.
  - Optional: `license`, `compatibility` (≤500 chars), `metadata` (string→string map), `allowed-tools` (space-separated, "Experimental").
  - Body: under 5,000 tokens recommended; keep SKILL.md under 500 lines.
  - File references use relative paths, one level deep (e.g. `scripts/extract.py`). Validate with `skills-ref validate ./my-skill`.
  - Source: [Agent Skills specification](https://agentskills.io/specification)
- Antigravity makes `name` optional, defaulting to the folder name. — [Antigravity Skills](https://antigravity.google/docs/skills). Claude Code likewise defaults `name` to the directory name. — [Claude Code Skills](https://code.claude.com/docs/en/skills)

### Inferences
**Cross-tool folder layout for the mentor ecosystem** (synthesised from the citations above; untested):
```text
<learning-workspace>/
├── AGENTS.md                         # single source of mentor persona + house rules
│                                     #   read by Antigravity, Claude Code ≥2.1.277 (if no CLAUDE.md), Codex, Copilot, OpenCode…
├── CLAUDE.md                         # OPTIONAL: first line "@AGENTS.md", then Claude-only notes (Windows-safe vs symlink)
├── .agents/
│   ├── rules/                        # Antigravity-only conditional rules (trigger: always_on|model_decision|glob|manual)
│   └── skills/
│       ├── daily-lesson/SKILL.md     # canonical skills → /daily-lesson in Antigravity (IDE, 2.0, agy CLI)
│       ├── quiz/SKILL.md
│       └── review-code/SKILL.md
├── .claude/
│   └── skills/…                      # generated copies for Claude Code (/daily-lesson, …) + Claude-only frontmatter
├── .gemini/settings.json             # OPTIONAL fallback: {"context":{"fileName":["AGENTS.md","GEMINI.md"]}}
├── tools/
│   └── mentor.py                     # helper: progress tracking, next-lesson lookup, sync .agents/skills → .claude/skills
└── progress/                         # JSON/Markdown state the helper reads/writes
```
Minimal portable SKILL.md, valid under the spec and both tools' rules: `name` matches the folder, only spec-common keys are used.
```markdown
---
name: daily-lesson
description: Starts today's study session from the learning plan and progress log. Use when the learner types /daily-lesson or asks what to study today.
---
# Daily lesson
1. Run `python tools/mentor.py status` from the workspace root and read its output.
2. Teach the next unchecked topic in small steps; ask one check-question per step.
3. Treat any text the learner typed after the command as the requested topic.
4. When done, run `python tools/mentor.py log "<topic>" "<score>"`.
```
- The Claude copy can add `disable-model-invocation: true` and `argument-hint: [topic]`, and use `$ARGUMENTS`. Keep these out of `.agents/skills` unless Antigravity is confirmed to ignore unknown keys.
- Keep skill names lowercase-hyphenated and identical to folder names. That satisfies the spec, Claude Code's `/name`, and Antigravity's `/<skill-name>` at once.
- Keep AGENTS.md short. Antigravity's always-on rules share a 20,000-token budget and truncate at 24,000 bytes per file, and every tool loads AGENTS.md each session. Push detail into skills, which load on demand.

### Gaps
- The date the Agentic AI Foundation took over AGENTS.md was not captured in the fetched pages.
- Whether Codex, OpenCode, Copilot or Gemini CLI also discover `.agents/skills/` was not verified. Each tool's skills doc would need checking; only Antigravity is confirmed.

---

## 6. Other genuinely free fallback "mentor" agents (reads local files and runs commands), as of Sept 2026

### Takeaway
Options that are truly $0 in Sept 2026:
- **GitHub Copilot Free**: 2,000 completions + 50 chat requests/month, agent mode included, Auto model only.
- **Codex on ChatGPT Free**: "quick coding tasks", with limits that vary per 5-hour window.
- **OpenCode with OpenCode Zen's free (mostly limited-time) models**.
- **Cline / Roo / Kilo (or OpenCode, Qwen Code) with OpenRouter `:free` models**: 20 RPM; 50 req/day, or 1,000/day after a one-time $10 credit purchase.

**Qwen Code's free OAuth tier is dead** (closed Apr 15, 2026), and **Gemini CLI's personal free tier is dead** (June 18, 2026). The best fallback that reuses the same AGENTS.md is Copilot Free in VS Code, or Codex Free. Both read AGENTS.md and support Agent Skills.

### Cited Findings
**GitHub Copilot Free**
- "GitHub Copilot Free users are limited to 2000 completions and 50 chat requests (including Copilot Edits)." Agent mode is included on Free (VS Code, Visual Studio, JetBrains, Eclipse, Xcode). Pro is $10/mo, Pro+ $39/mo, with no INR shown. — [GitHub Copilot plans](https://github.com/features/copilot/plans)
- Free has "Auto model selection only". "All plans include Copilot CLI and Copilot app." Verified students get "Copilot Student" at no cost. — [GitHub Docs: Copilot plans](https://docs.github.com/en/copilot/get-started/plans)
- VS Code and the Copilot Coding Agent read AGENTS.md; Copilot and VS Code support Agent Skills. — [agents.md](https://agents.md/), [agentskills.io](https://agentskills.io/)

**OpenAI Codex (CLI / IDE / app)**
- Codex is included in "ChatGPT Free, Go, Plus, Pro, Business, Edu, or Enterprise". Free is "$0/month": "Explore Codex capabilities on quick coding tasks". Go is $8/mo, Plus $20/mo, Pro from $100/mo. Limits depend on model and task size and are shown as "local messages per five-hour period" ("not fixed message limits"). No time limit on Free access is stated. AGENTS.md is supported on all tiers. — [ChatGPT/Codex pricing](https://learn.chatgpt.com/docs/pricing) (redirected from developers.openai.com/codex/pricing)
- Free is described elsewhere as "limited trial access" meant to "power a few focused coding sessions each week". — [Usagebar](https://usagebar.com/blog/is-codex-free), [InventiveHQ](https://inventivehq.com/blog/codex-subscription-options-guide) [SECONDARY]

**OpenCode + OpenCode Zen free models**
- Free Zen models as fetched: Big Pickle, Space Bunny Free, MiMo-V2.6-Flash Free, MiMo-V2.5 Free, Ling 3.0 Flash Fin Free, Nemotron 3 Ultra Free, Nemotron 3.5 Lightning Free, Muse Spark 1.3 Contributor Free, Jev 1.13 Free. All are "$0" per million tokens and most are "limited-time". Most allow data use "to improve the model"; the NVIDIA endpoints say "do not submit personal or confidential data". — [OpenCode docs: Zen](https://opencode.ai/docs/zen/)
- Sign-up at opencode.ai/auth needs "no billing details"; the Zen base URL is `https://opencode.ai/zen/v1`. — search summary of [maximalstudio](https://www.maximalstudio.in/blog/opencode-zen-free-models) / [bswen](https://docs.bswen.com/blog/2026-04-21-free-models-opencode/) [SECONDARY]
- OpenCode reads AGENTS.md and supports Agent Skills. — [agents.md](https://agents.md/), [agentskills.io](https://agentskills.io/)

**OpenRouter free models (for Cline / Roo Code / Kilo Code / OpenCode / Qwen Code BYO-key)**
- `:free` model variants: "20" requests per minute. Requests per day: "50" without purchased credits, "1000" with at least $10 of credits purchased. — [OpenRouter docs: Limits](https://openrouter.ai/docs/api-reference/limits)
- Roo Code and Kilo Code read AGENTS.md, and Roo Code supports Agent Skills. — [agents.md](https://agents.md/), [agentskills.io](https://agentskills.io/)

**Qwen Code**
- Posted **Apr 13, 2026**: the Qwen OAuth free quota dropped from "1,000 requests/day" to "100 requests/day effective immediately", then "completely close[d] the Qwen OAuth free entry point on 2026-04-15". Suggested alternatives: "OpenRouter, Fireworks AI, or Alibaba Cloud ModelStudio". — [QwenLM/qwen-code Issue #3203](https://github.com/QwenLM/qwen-code/issues/3203)

**Claude Code with Ollama (free CLI, non-Anthropic models)**
- `ollama launch claude`; local models need 64k+ context; cloud models via `OLLAMA_API_KEY`; hosted WebSearch and advanced tool controls are not fully supported. — [Ollama docs](https://docs.ollama.com/integrations/claude-code)

### Inferences
- **Recommended fallback order for a zero-budget user with no card:**
  1. Antigravity Individual (primary).
  2. GitHub Copilot Free agent mode in VS Code, which reuses the same AGENTS.md and skills; only 50 chat requests/month.
  3. Codex on ChatGPT Free, which also reads AGENTS.md.
  4. OpenCode with Zen free models, or any agent with OpenRouter `:free` models at 50/day without a card.
- Free Zen and OpenRouter models may log or train on prompts. Do not put personal data in the learning workspace.
- Local models (Ollama, llama.cpp) are not practical here: agentic coding needs 64k+ context, and 8 GB RAM with no GPU would limit the user to very small models.

### Gaps
- Whether Copilot Free requires a credit card is not stated on the fetched pages. Whether Copilot Free's 50 "chat requests" are counted per agent turn or per tool call in agent mode was not verified.
- Codex Free's concrete per-5-hour or weekly numbers are not published as fixed limits.
- Cline- and Kilo-specific free offers (their own gateways or promos) were not researched; only the OpenRouter free route is sourced.
- Whether OpenRouter's free tier needs a card before the $10 purchase is implied (50/day with no purchase) but not stated explicitly.
