#!/usr/bin/env python3
"""Fail if the upstream repository contains someone's personal learning data.

Learners work in their own private copy, where tracker/, notes/, projects/ and flashcards/ fill
up. The upstream template must stay blank so every new learner starts clean. CI runs this on
every pull request.

  python scripts/check_template.py
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))


def main() -> None:
    problems: list[str] = []
    tracker = ROOT / "tracker"

    for name in ("events.jsonl",):
        if (tracker / name).exists() and (tracker / name).read_text(encoding="utf-8").strip():
            problems.append(f"tracker/{name} must not be committed with events")
    queue = (tracker / "review-queue.csv").read_text(encoding="utf-8").strip().splitlines()
    if len(queue) != 1:
        problems.append("tracker/review-queue.csv must contain only the header row")
    if (tracker / "reports").exists() and any((tracker / "reports").iterdir()):
        problems.append("tracker/reports/ must be empty")
    journal = (tracker / "journal.md").read_text(encoding="utf-8")
    if journal.rstrip().split("\n---", 1)[-1].strip():
        problems.append("tracker/journal.md must have no entries after the '---' line")
    for line in (tracker / "profile.md").read_text(encoding="utf-8").splitlines():
        if line.startswith("- Name:") and line.strip() != "- Name:":
            problems.append("tracker/profile.md must be the blank template (Name is filled in)")

    import tracker as tr  # the generated views must match an empty event log
    tr.use_root(ROOT)
    items, phases = tr.load_curriculum()
    empty = tr.State(tr.date.today(), items, phases, [])
    progress = (tracker / "progress.md").read_text(encoding="utf-8")
    if "Not started yet" not in progress:
        problems.append("tracker/progress.md must be the empty dashboard (run: python tools/tracker.py report on a clean copy)")
    if (tracker / "weak-spots.md").read_text(encoding="utf-8") != tr.weak_view(empty):
        problems.append("tracker/weak-spots.md must be the empty generated view")

    for folder in ("notes", "projects", "flashcards"):
        extra = [p.relative_to(ROOT).as_posix() for p in (ROOT / folder).rglob("*")
                 if p.is_file() and p.name != "README.md"]
        if extra:
            problems.append(f"{folder}/ must only contain README.md in the template (found: {', '.join(extra[:5])})")
    if (ROOT / ".env").exists():
        problems.append(".env must never be committed")

    if problems:
        print("The template contains personal learning data:\n- " + "\n- ".join(problems), file=sys.stderr)
        print("Contribute from a fresh clone of the upstream repo, not from your learning copy.", file=sys.stderr)
        sys.exit(1)
    print("OK: template is clean")


if __name__ == "__main__":
    main()
