#!/usr/bin/env python3
"""Check every link in the course's Markdown files.

YouTube links go through YouTube's oEmbed endpoint, which returns the video's real title, so a
deleted video or a wrong id is caught (YouTube's normal pages return 200 even for dead videos).
Other links get a GET with a browser user agent.

Only clear breakage fails the run: HTTP 404/410, YouTube ids that don't exist, and DNS errors.
403, 429, timeouts and 5xx are reported as warnings, because many sites block automated checkers.

  python scripts/check_links.py              check everything, exit 1 on broken links
  python scripts/check_links.py --titles     also print every YouTube title (for manual review)
  python scripts/check_links.py FILE.md ...  check only these files
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import http.cookiejar
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
URL = re.compile(r"https?://[^\s)>\]\"'`|]+")
AGENT = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/128.0 Safari/537.36"}
SKIP_HOSTS = ("localhost", "127.0.0.1", "example.com", "api.groq.com")  # API base URLs, placeholders
SKIP_DIRS = ("docs/research", "node_modules", ".venv")


def status(url: str) -> tuple[str, str]:
    """Return (verdict, detail) where verdict is ok | warn | broken."""
    if any(h in urllib.parse.urlparse(url).netloc for h in SKIP_HOSTS):
        return "ok", "skipped"
    if re.search(r"youtube\.com/(watch|playlist)|youtu\.be/", url):
        oembed = "https://www.youtube.com/oembed?format=json&url=" + urllib.parse.quote(url, safe="")
        try:
            with urllib.request.urlopen(urllib.request.Request(oembed, headers=AGENT), timeout=25) as r:
                data = json.load(r)
                return "ok", f"{data.get('author_name')} | {data.get('title')}"
        except urllib.error.HTTPError as e:
            if e.code == 401:
                return "ok", "exists (embedding disabled)"
            return ("broken" if e.code in (400, 404) else "warn"), f"YouTube HTTP {e.code}"
        except Exception as e:  # noqa: BLE001
            return "warn", f"YouTube {type(e).__name__}"
    try:
        # A cookie jar lets sites that redirect through a cookie check (e.g. Google docs) resolve.
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
        with opener.open(urllib.request.Request(url, headers=AGENT), timeout=30) as r:
            return "ok", str(r.status)
    except urllib.error.HTTPError as e:
        return ("broken" if e.code in (404, 410) else "warn"), f"HTTP {e.code}"
    except urllib.error.URLError as e:
        reason = str(e.reason)
        return ("broken" if "getaddrinfo" in reason or "Name or service" in reason else "warn"), reason[:80]
    except Exception as e:  # noqa: BLE001
        return "warn", type(e).__name__


def collect(files: list[Path]) -> dict[str, set[str]]:
    found: dict[str, set[str]] = {}
    for f in files:
        for url in URL.findall(f.read_text(encoding="utf-8")):
            found.setdefault(url.rstrip(".,;:*"), set()).add(f.relative_to(ROOT).as_posix())
    return found


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Check links in Markdown files.")
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--titles", action="store_true")
    args = parser.parse_args()
    files = [f.resolve() for f in args.files] or [
        f for f in ROOT.rglob("*.md") if not any(part in f.relative_to(ROOT).as_posix() for part in SKIP_DIRS)]
    urls = collect(files)
    with cf.ThreadPoolExecutor(12) as pool:
        results = dict(zip(urls, pool.map(status, urls)))
    broken = warned = 0
    for url, (verdict, detail) in sorted(results.items()):
        where = ", ".join(sorted(urls[url]))
        if verdict == "broken":
            broken += 1
            print(f"BROKEN  {url}  ({detail})  in {where}")
        elif verdict == "warn":
            warned += 1
            print(f"warn    {url}  ({detail})  in {where}")
        elif args.titles and "|" in detail:
            print(f"ok      {url}  {detail}")
    print(f"\n{len(urls)} links checked: {broken} broken, {warned} warnings.")
    sys.exit(1 if broken else 0)


if __name__ == "__main__":
    main()
