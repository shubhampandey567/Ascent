#!/usr/bin/env python3
"""Print a YouTube video's transcript so the Mentor can quiz you on exactly what it said.

  python tools/transcript.py <youtube-url-or-id> [--from MIN] [--to MIN] [--lang hi]

One-time setup:  pip install youtube-transcript-api

Output is grouped into ~1-minute paragraphs with [mm:ss] stamps. Use --from/--to
(minutes) to quiz only the part you watched today, e.g. a 2-hour Karpathy video
watched in four sittings.

If captions are disabled or YouTube blocks the request, the script says so and
exits with code 2; the Mentor then uses the lesson's key concepts from the
curriculum instead.
"""

from __future__ import annotations

import argparse
import re
import sys

ID_PATTERN = re.compile(r"(?:v=|/shorts/|/embed/|/live/|youtu\.be/)([A-Za-z0-9_-]{11})")


def video_id(text: str) -> str:
    if match := ID_PATTERN.search(text):
        return match.group(1)
    if re.fullmatch(r"[A-Za-z0-9_-]{11}", text):
        return text
    sys.exit(f"error: no YouTube video id found in {text!r}")


def stamp(seconds: float) -> str:
    h, rest = divmod(int(seconds), 3600)
    m, s = divmod(rest, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("video", help="YouTube URL or 11-character video id")
    parser.add_argument("--from", dest="start", type=float, default=0, help="start minute")
    parser.add_argument("--to", dest="end", type=float, help="end minute")
    parser.add_argument("--lang", default="en", help="preferred caption language (default en)")
    args = parser.parse_args()

    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ImportError:
        print("Missing package. Run once: pip install youtube-transcript-api", file=sys.stderr)
        sys.exit(2)

    vid = video_id(args.video)
    languages = list(dict.fromkeys([args.lang, "en", "en-US", "en-GB", "hi"]))
    try:
        snippets = YouTubeTranscriptApi().fetch(vid, languages=languages)
    except Exception as exc:  # captions off, video private, network/IP block, ...
        print(f"No transcript for {vid} ({type(exc).__name__}). "
              "Quiz from the curriculum's key concepts instead.", file=sys.stderr)
        sys.exit(2)

    start_s, end_s = args.start * 60, (args.end * 60 if args.end is not None else float("inf"))
    kept = [s for s in snippets if start_s <= s.start <= end_s]
    if not kept:
        print("No captions in that time range.", file=sys.stderr)
        sys.exit(2)
    paragraph, began = [], kept[0].start
    for snip in kept:
        if snip.start - began >= 60 and paragraph:
            print(f"[{stamp(began)}] {' '.join(paragraph)}\n")
            paragraph, began = [], snip.start
        paragraph.append(snip.text.replace("\n", " "))
    print(f"[{stamp(began)}] {' '.join(paragraph)}")


if __name__ == "__main__":
    main()
