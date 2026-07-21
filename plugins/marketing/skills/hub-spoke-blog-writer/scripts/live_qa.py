#!/usr/bin/env python3
"""Live-render QA gate: verify a published URL renders what the gate approved.

Fetches the live page as a logged-out guest and checks the render. Purge all
caches BEFORE running, or you may verify a stale render.

Usage:
  python3 live_qa.py URL [--meta "expected description"] [--links "/hub/,/spoke/"]

Checks: exactly one h1; h2 count >= 4; every given internal link present as a
real anchor; FAQPage JSON-LD present; meta description present (and exactly
matching --meta when given); og:image present; canonical present; no lorem
ipsum; no em dash in meta or og description. Exit 0 = PASS, 1 = any FAIL.
"""
import argparse
import re
import sys
import urllib.request


def fetch(url):
    req = urllib.request.Request(
        url + ("&" if "?" in url else "?") + "qa=1",
        headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) LiveQA/2.0"})
    return urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")


def meta_content(html, key, val):
    m = re.search(r'<meta[^>]+%s=["\']%s["\'][^>]*\scontent=["\']([^"\']*)' % (key, val),
                  html, re.I) or re.search(
        r'<meta[^>]+content=["\']([^"\']*)["\'][^>]+%s=["\']%s["\']' % (key, val), html, re.I)
    return m.group(1).strip() if m else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--meta", default="", help="expected meta description, exact match")
    ap.add_argument("--links", default="", help="comma-separated paths that must be <a> hrefs")
    a = ap.parse_args()
    try:
        html = fetch(a.url)
    except Exception as e:
        sys.exit("FETCH FAILED for %s: %s" % (a.url, e))

    checks = {}
    checks["h1_count==1"] = len(re.findall(r"<h1[\s>]", html, re.I)) == 1
    checks["h2_count>=4"] = len(re.findall(r"<h2[\s>]", html, re.I)) >= 4
    for path in [p.strip() for p in a.links.split(",") if p.strip()]:
        checks["a_href:" + path] = bool(
            re.search(r'<a[^>]+href=["\'][^"\']*%s' % re.escape(path), html, re.I))
    blocks = re.findall(r"<script[^>]+ld\+json[^>]*>(.*?)</script>", html, re.I | re.S)
    checks["faqpage_jsonld"] = any("faqpage" in b.lower() for b in blocks)
    desc = meta_content(html, "name", "description")
    checks["meta_description_present"] = bool(desc)
    if a.meta:
        checks["meta_description_matches"] = desc == a.meta.strip()
    checks["og_image"] = bool(meta_content(html, "property", "og:image"))
    checks["canonical_present"] = bool(re.search(r'<link[^>]+rel=["\']canonical["\']', html, re.I))
    checks["no_lorem_ipsum"] = "lorem ipsum" not in html.lower()
    og_desc = meta_content(html, "property", "og:description")
    checks["no_em_dash_in_excerpt"] = chr(0x2014) not in (desc + og_desc)

    failed = [k for k, ok in checks.items() if not ok]
    for k, ok in sorted(checks.items()):
        print(("PASS  " if ok else "FAIL  ") + k)
    print("%s: %d/%d checks passed for %s"
          % ("FAIL" if failed else "PASS", len(checks) - len(failed), len(checks), a.url))
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
