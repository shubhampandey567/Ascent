#!/usr/bin/env python3
"""Keep every AI agent's command files in sync with the one source of truth: .agents/skills/.

Most agents read .agents/skills/<name>/SKILL.md directly (Antigravity, GitHub Copilot in VS Code,
Cursor, Codex, Gemini CLI, OpenCode, Windsurf). This script generates the rest:
  .claude/skills/<name>/SKILL.md   exact copies (Claude Code reads only .claude/skills)
  .opencode/commands/<name>.md     thin wrappers so /name works as a slash command in OpenCode
It also validates each skill's frontmatter against the Agent Skills spec.

  python scripts/sync_agents.py          regenerate
  python scripts/sync_agents.py --check  fail (exit 1) if anything is out of date or invalid (CI)
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / ".agents" / "skills"
CLAUDE = ROOT / ".claude" / "skills"
OPENCODE = ROOT / ".opencode" / "commands"
NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def frontmatter(text: str) -> dict[str, str]:
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    return dict(line.split(": ", 1) for line in m.group(1).splitlines() if ": " in line)


def problems(skill: Path) -> list[str]:
    meta = frontmatter(skill.read_text(encoding="utf-8"))
    name, desc = meta.get("name", ""), meta.get("description", "")
    out = []
    if name != skill.parent.name:
        out.append(f"name '{name}' must match its folder '{skill.parent.name}'")
    if not NAME.match(name) or len(name) > 64:
        out.append("name must be 1-64 chars of lowercase letters, digits and single hyphens")
    if not 0 < len(desc) <= 1024:
        out.append("description must be 1-1024 chars")
    if ": " in desc or " #" in desc:
        out.append("description must not contain ': ' or ' #' (breaks strict YAML parsers); rephrase")
    if skill.read_text(encoding="utf-8").count("\n") > 500:
        out.append("keep SKILL.md under 500 lines")
    return out


def opencode_wrapper(name: str, description: str) -> str:
    return (f"---\ndescription: {description}\n---\n"
            f"Load the `{name}` skill and follow it exactly: `.agents/skills/{name}/SKILL.md`.\n"
            "Treat this as the learner's argument, if any: $ARGUMENTS\n")


def expected() -> dict[Path, str]:
    files: dict[Path, str] = {}
    for skill in sorted(SOURCE.glob("*/SKILL.md")):
        text = skill.read_text(encoding="utf-8")
        name = skill.parent.name
        files[CLAUDE / name / "SKILL.md"] = text
        files[OPENCODE / f"{name}.md"] = opencode_wrapper(name, frontmatter(text).get("description", ""))
    return files


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="verify only; exit 1 on any difference")
    args = parser.parse_args()

    errors = [f"{s.relative_to(ROOT)}: {p}" for s in sorted(SOURCE.glob("*/SKILL.md")) for p in problems(s)]
    want = expected()
    stale = [p for p, text in want.items() if not p.exists() or p.read_text(encoding="utf-8") != text]
    extra = [p for folder in (CLAUDE, OPENCODE) if folder.exists()
             for p in folder.rglob("*") if p.is_file() and p not in want]

    if args.check:
        errors += [f"out of date: {p.relative_to(ROOT)}" for p in stale]
        errors += [f"not generated from .agents/skills (delete it or add a skill): {p.relative_to(ROOT)}" for p in extra]
        if errors:
            print("\n".join(errors) + "\nRun: python scripts/sync_agents.py", file=sys.stderr)
            sys.exit(1)
        print(f"OK: {len(want) // 2} skills, adapters in sync")
        return

    if errors:
        sys.exit("\n".join(errors))
    for p in extra:
        p.unlink()
    for folder in (CLAUDE, OPENCODE):
        for d in sorted(folder.rglob("*"), reverse=True) if folder.exists() else []:
            if d.is_dir() and not any(d.iterdir()):
                d.rmdir()
    for path, text in want.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")
    print(f"Synced {len(want) // 2} skills -> .claude/skills and .opencode/commands"
          + (f" (removed {len(extra)} stale files)" if extra else ""))


if __name__ == "__main__":
    main()
