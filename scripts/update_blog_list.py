#!/usr/bin/env python3
"""
Rewrite the blog list on the CortexRidge GitHub org profile from the site's
own RSS feed.

The profile README is a marketing surface that goes stale the moment writing
outpaces remembering to update it. The feed is already the canonical list of
published posts, so this treats it as the source of truth and regenerates the
section between the two markers on a schedule.

Standard library only — no third-party action, nothing to trust or pin.

Usage:  python3 update_blog_list.py [path/to/README.md]
"""

import re
import sys
import urllib.request
import xml.etree.ElementTree as ET

FEED = "https://cortexridge.com/blog/rss.xml"
START = "<!-- BLOG:START -->"
END = "<!-- BLOG:END -->"
MAX_POSTS = 4
# Descriptions are written as meta descriptions (<=160 chars) so they read as
# full sentences here; trim only if a longer one ever slips through.
MAX_DESC = 165


def fetch_posts(url=FEED, limit=MAX_POSTS):
    req = urllib.request.Request(url, headers={"User-Agent": "cortexridge-profile-bot"})
    with urllib.request.urlopen(req, timeout=30) as response:
        root = ET.fromstring(response.read())

    posts = []
    for item in root.findall("./channel/item")[:limit]:
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        desc = " ".join((item.findtext("description") or "").split())
        if len(desc) > MAX_DESC:
            desc = desc[:MAX_DESC].rsplit(" ", 1)[0] + "…"
        if title and link:
            posts.append((title, link, desc))
    return posts


def render(posts):
    lines = []
    for title, link, desc in posts:
        # Escape ] and [ so a bracketed title cannot break the markdown link.
        safe = title.replace("[", "\\[").replace("]", "\\]")
        lines.append(f"- [{safe}]({link})" + (f" — {desc}" if desc else ""))
    return "\n".join(lines)


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "profile/README.md"
    readme = open(path, encoding="utf-8").read()

    if START not in readme or END not in readme:
        sys.exit(f"error: markers {START} / {END} not found in {path}")

    posts = fetch_posts()
    if not posts:
        # A transient feed problem must not wipe the existing list.
        sys.exit("error: feed returned no posts; leaving README unchanged")

    updated = re.sub(
        re.escape(START) + r".*?" + re.escape(END),
        f"{START}\n{render(posts)}\n{END}",
        readme,
        flags=re.DOTALL,
    )

    if updated == readme:
        print("no change")
        return

    open(path, "w", encoding="utf-8").write(updated)
    print(f"updated {len(posts)} posts in {path}")


if __name__ == "__main__":
    main()
