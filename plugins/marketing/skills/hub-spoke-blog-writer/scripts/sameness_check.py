#!/usr/bin/env python3
"""Cross-post sameness gate: FAIL if any 12+ word sentence appears in 2+ posts.

Run after all posts in a wave are drafted, before scoring any of them:
  python3 sameness_check.py posts/*.md

Headings, blockquotes, tables, and code blocks are excluded. Link anchor text
is compared with URLs stripped. Comparison is case- and punctuation-insensitive.
Exit 0 = PASS, exit 1 = shared sentences exist (rewrite them, rerun).
"""
import collections
import glob
import re
import sys

MIN_WORDS = 12


def sentences(path):
    text = open(path, encoding="utf-8").read()
    text = re.sub(r"`{3}.*?`{3}", " ", text, flags=re.S)             # code blocks out
    text = re.sub(r"^\s*(#|>|\||-{3,}).*$", " ", text, flags=re.M)   # headings/quotes/tables out
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)             # keep anchor text, drop URLs
    for raw in re.split(r"(?<=[.!?])\s+", text):
        norm = re.sub(r"[^a-z0-9 ]", "", re.sub(r"\s+", " ", raw).lower()).strip()
        if len(norm.split()) >= MIN_WORDS:
            yield norm


def main(paths):
    if len(paths) < 2:
        sys.exit("Need 2+ post files, e.g. posts/*.md")
    owners = collections.defaultdict(set)
    for p in paths:
        for s in set(sentences(p)):
            owners[s].add(p)
    shared = sorted((s, ps) for s, ps in owners.items() if len(ps) > 1)
    for s, ps in shared:
        print("SHARED in %d posts: %s..." % (len(ps), s[:90]))
        for p in sorted(ps):
            print("    %s" % p)
    print("%s: %d shared sentence(s) across %d files"
          % ("FAIL" if shared else "PASS", len(shared), len(paths)))
    sys.exit(1 if shared else 0)


if __name__ == "__main__":
    main(sys.argv[1:] or sorted(glob.glob("posts/*.md")))
