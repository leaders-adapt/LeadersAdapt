#!/usr/bin/env python3
"""seo_check.py v2: objective SEO, AEO, and GEO checker for hub-spoke-blog-writer posts.

Counts what can be counted so the model never grades its own homework:
keyword occurrences and stuffing ceiling, the 9 placement points, headings,
FAQ presence and answer lengths, Quick Answer block, definition callouts,
entity coverage, fan-out question coverage, JSON-LD schema validation,
links, metadata lengths, em dashes, banned AI vocabulary, paragraph and
sentence rhythm. Stdlib only.

Usage:
  python3 seo_check.py post.md --keyword "exact phrase" \
      [--secondary "a,b,c"] [--type spoke|hub|single] \
      [--min-words N --max-words N] \
      [--entities "e1,e2,e3"] \
      [--questions "q1?;q2?;q3?"] \
      [--schema schema/NN-slug-schema.json] \
      [--json]

v2 changes: density floor removed (stuffing ceiling only, fail above 1.2%),
body occurrence minimum scales with length, Quick Answer and FAQ answer
length checks, definition callout count, --entities coverage, --questions
fan-out coverage, --schema JSON-LD validation, --min/--max word overrides
from the SERP brief.
"""

import argparse
import json
import re
import statistics
import sys

WORD_RANGES = {"spoke": (1500, 4000), "hub": (2000, 5000), "single": (1500, 4000)}

HARD_PHRASES = ["in conclusion", "it's important to note", "it is important to note"]

SOFT_VOCAB = [
    "delve", "robust", "holistic", "foster", "facilitate", "seamless",
    "empower", "streamline", "cultivate", "paradigm", "synergy",
    "comprehensive", "utilize", "cutting-edge", "game-changer",
    "supercharge", "ever-evolving", "tapestry", "embark",
    "furthermore", "moreover", "needless to say", "in today's fast-paced",
    "navigate the landscape", "unlock the power", "elevate your",
    "it's worth mentioning", "revolutionize", "harness the power",
    "dive into", "in the realm of",
]

STOPWORDS = {"a", "an", "the", "to", "for", "of", "in", "on", "at", "as",
             "is", "are", "and", "or", "your", "my", "with", "do", "you",
             "what", "how", "why", "when", "which", "who", "can", "does",
             "it", "be", "i", "we", "they"}


def kw_pattern(keyword):
    words = [re.escape(w) for w in keyword.strip().split()]
    if not words:
        return None
    return re.compile(r"\b" + r"[\s\-]+".join(words) + r"\b", re.IGNORECASE)


def count_kw(pattern, text):
    return len(pattern.findall(text)) if pattern else 0


def visible_text(md):
    md = re.sub(r"```.*?```", " ", md, flags=re.DOTALL)
    md = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", md)
    md = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", md)
    md = re.sub(r"^#{1,6}\s*", "", md, flags=re.MULTILINE)
    md = re.sub(r"[*_`>|]", " ", md)
    return md


def split_post(raw):
    lines = raw.splitlines()
    for i, line in enumerate(lines):
        if line.strip() == "---":
            return "\n".join(lines[:i]), "\n".join(lines[i + 1:])
    return "", raw


def meta_field(meta, label):
    m = re.search(r"\*\*" + label + r"[^:]*:\*\*\s*(.+)", meta, re.IGNORECASE)
    return m.group(1).strip() if m else ""


def norm_tokens(text):
    return [w for w in re.findall(r"[a-z0-9']+", text.lower()) if w not in STOPWORDS]


def analyze(raw, keyword, secondary, post_type, min_words, max_words,
            entities, questions, schema_raw, schema_path):
    meta, body = split_post(raw)
    warnings = []
    if not meta:
        warnings.append("No metadata block found (expected '---' separator); treating whole file as body.")

    title_tag = meta_field(meta, "TITLE TAG")
    meta_desc = meta_field(meta, "META DESCRIPTION")
    slug = meta_field(meta, "URL SLUG").lower()
    h1_m = re.search(r"^#\s+(.+)$", meta + "\n" + body, re.MULTILINE)
    h1 = h1_m.group(1).strip() if h1_m else ""

    pat = kw_pattern(keyword)
    body_vis = visible_text(body)
    words = body_vis.split()
    word_count = len(words)

    h2s = re.findall(r"^##\s+(.+)$", body, re.MULTILINE)
    h3s = re.findall(r"^###\s+(.+)$", body, re.MULTILINE)

    # FAQ section
    faq_text, faq_questions, faq_answer_words = "", [], []
    faq_match = re.search(
        r"^##\s+.*(faq|frequently asked|questions).*?$(.*?)(?=^##\s|\Z)",
        body, re.MULTILINE | re.DOTALL | re.IGNORECASE)
    if faq_match:
        faq_text = faq_match.group(2)
        parts = re.split(r"^###\s+", faq_text, flags=re.MULTILINE)
        for part in parts[1:]:
            lines = part.splitlines()
            q = lines[0].strip()
            if not q.endswith("?"):
                continue
            faq_questions.append(q)
            ans = visible_text("\n".join(lines[1:]))
            faq_answer_words.append(len(ans.split()))

    faq_answers_out_of_range = sum(1 for n in faq_answer_words if not (40 <= n <= 90))

    body_count = count_kw(pat, body_vis)
    density = round(body_count / word_count * 100, 2) if word_count else 0.0

    kw_words = [w for w in re.findall(r"[a-z0-9']+", keyword.lower()) if w not in STOPWORDS]
    slug_ok = bool(kw_words) and all(w.replace("'", "") in slug for w in kw_words)

    body_min_occ = max(4, word_count // 800)

    placements = {
        "title_tag": bool(pat and title_tag and pat.search(title_tag)),
        "h1": bool(pat and h1 and pat.search(h1)),
        "first_100_words": bool(pat and pat.search(" ".join(words[:100]))),
        "meta_description": bool(pat and meta_desc and pat.search(meta_desc)),
        "url_slug": slug_ok,
        "h2_heading": bool(pat and any(pat.search(h) for h in h2s)),
        "body_min_occurrences": body_count >= body_min_occ,
        "faq_section": bool(pat and faq_text and pat.search(visible_text(faq_text))),
        "last_200_words": bool(pat and pat.search(" ".join(words[-200:]))),
    }
    placements_hit = sum(placements.values())

    secondary_counts = {}
    for s in secondary:
        sp = kw_pattern(s)
        secondary_counts[s] = count_kw(sp, body_vis)

    links = re.findall(r"\[([^\]]+)\]\(([^)\s]+)\)", body)
    internal = [(t, u) for t, u in links if u.startswith("/")]
    external = [(t, u) for t, u in links if u.startswith("http")]

    # Paragraph inventory (skip headings, lists, tables, quotes)
    paragraphs = [b.strip() for b in re.split(r"\n\s*\n", body)
                  if b.strip() and not re.match(r"^(#|\-|\*\s|\d+\.|\||>)", b.strip())]

    # Quick Answer: a paragraph starting with bold within the first 8 paragraphs,
    # visible length 35 to 80 words.
    quick_answer = {"present": False, "word_count": 0, "position": None}
    for i, p in enumerate(paragraphs[:8]):
        if p.startswith("**"):
            n = len(visible_text(p).split())
            if 25 <= n <= 100:
                quick_answer = {"present": 35 <= n <= 80, "word_count": n, "position": i + 1}
                if not quick_answer["present"]:
                    warnings.append(f"Bold-lead block found ({n} words) but outside the 35-80 word window.")
                break

    # Definition callouts: bolded sentence containing " is " or " means ", <= 45 words.
    def_callouts = 0
    for m in re.finditer(r"\*\*([^*]{10,400})\*\*", body):
        t = m.group(1).strip()
        if re.search(r"\b(is|means)\b", t) and len(t.split()) <= 45 and t.endswith("."):
            def_callouts += 1

    # Entity coverage
    entity_hits, entity_misses = [], []
    low_body = body_vis.lower()
    for e in entities:
        if e.lower() in low_body:
            entity_hits.append(e)
        else:
            entity_misses.append(e)
    entity_cov = round(len(entity_hits) / len(entities) * 100) if entities else None

    # Fan-out question coverage: >= 60% of a question's tokens present in any
    # single heading or FAQ question.
    heading_pool = [h.lower() for h in h2s + h3s + faq_questions]
    q_covered, q_uncovered = [], []
    for q in questions:
        toks = norm_tokens(q)
        hit = False
        for h in heading_pool:
            if toks and sum(1 for t in toks if t in h) / len(toks) >= 0.6:
                hit = True
                break
        (q_covered if hit else q_uncovered).append(q)
    fanout_cov = round(len(q_covered) / len(questions) * 100) if questions else None

    # Schema validation
    schema = {"provided": bool(schema_raw), "valid_json": None, "types": [],
              "has_article": None, "has_faqpage": None, "faq_count_match": None,
              "has_person": None, "person_has_description": None, "path": schema_path}
    if schema_raw:
        try:
            data = json.loads(schema_raw)
            schema["valid_json"] = True
            nodes = []

            def walk(x):
                if isinstance(x, dict):
                    nodes.append(x)
                    for v in x.values():
                        walk(v)
                elif isinstance(x, list):
                    for v in x:
                        walk(v)
            walk(data)
            types = []
            for n in nodes:
                t = n.get("@type")
                if isinstance(t, str):
                    types.append(t)
                elif isinstance(t, list):
                    types += [x for x in t if isinstance(x, str)]
            schema["types"] = sorted(set(types))
            schema["has_article"] = any(t in ("Article", "BlogPosting") for t in types)
            faq_nodes = [n for n in nodes if n.get("@type") == "FAQPage"]
            schema["has_faqpage"] = bool(faq_nodes)
            if faq_nodes:
                main = faq_nodes[0].get("mainEntity", [])
                schema["faq_count_match"] = (len(main) == len(faq_questions))
                if not schema["faq_count_match"]:
                    warnings.append(
                        f"FAQPage has {len(main)} questions; the post has {len(faq_questions)}. They must mirror.")
            persons = [n for n in nodes if n.get("@type") == "Person"]
            schema["has_person"] = bool(persons)
            if persons:
                schema["person_has_description"] = bool(persons[0].get("description"))
        except (json.JSONDecodeError, ValueError) as e:
            schema["valid_json"] = False
            warnings.append(f"Schema file is not valid JSON: {e}")

    # Style flags
    em_dashes = body.count("—") + meta.count("—")
    en_dashes = body.count("–")
    low = body_vis.lower()
    hard_hits = {p: low.count(p) for p in HARD_PHRASES if low.count(p)}
    soft_hits = {}
    for v in SOFT_VOCAB:
        n = len(re.findall(r"\b" + re.escape(v).replace(r"\ ", r"\s+") + r"\b", low))
        if n:
            soft_hits[v] = n

    long_paras = 0
    sentence_lengths = []
    for p in paragraphs:
        p_vis = visible_text(p)
        sents = [s for s in re.split(r"(?<=[.!?])\s+", p_vis) if len(s.split()) > 2]
        if len(sents) > 4:
            long_paras += 1
        sentence_lengths += [len(s.split()) for s in sents]
    rhythm_stdev = round(statistics.pstdev(sentence_lengths), 1) if len(sentence_lengths) >= 10 else None
    low_variance = rhythm_stdev is not None and rhythm_stdev < 4.0

    if min_words and max_words:
        lo, hi = min_words, max_words
        band_src = "serp-brief override"
    else:
        lo, hi = WORD_RANGES.get(post_type, WORD_RANGES["spoke"])
        band_src = f"default for {post_type}"

    checks = {
        "word_count_in_band": lo <= word_count <= hi,
        "no_stuffing": density <= 1.2,
        "placements_8_of_9": placements_hit >= 8,
        "no_em_dashes": em_dashes == 0,
        "no_hard_phrases": not hard_hits,
        "title_max_60": 0 < len(title_tag) <= 60,
        "meta_max_160": 0 < len(meta_desc) <= 160,
        "faq_5_or_6": 5 <= len(faq_questions) <= 6,
        "faq_answers_40_90": bool(faq_questions) and faq_answers_out_of_range == 0,
        "quick_answer_present": quick_answer["present"],
        "definition_callout_present": def_callouts >= 1,
    }
    if entities:
        checks["entity_coverage_60"] = entity_cov >= 60
    if questions:
        checks["fanout_coverage_80"] = fanout_cov >= 80
    if schema["provided"]:
        checks["schema_valid"] = bool(schema["valid_json"] and schema["has_article"]
                                      and schema["has_faqpage"]
                                      and schema["faq_count_match"] is not False
                                      and schema["has_person"])

    objective_pass = all(checks.values())

    if density > 1.0 and density <= 1.2:
        warnings.append(f"Density {density}% is under the 1.2% ceiling but high; prefer natural use.")
    if entities and entity_cov < 80:
        warnings.append(f"Entity coverage {entity_cov}% (missing: {', '.join(entity_misses)}).")
    if soft_hits:
        warnings.append("Banned-vocabulary hits found: " + ", ".join(f"{k} x{n}" for k, n in soft_hits.items()))
    if low_variance:
        warnings.append(f"Sentence rhythm variance is low (stdev {rhythm_stdev} words): vary sentence lengths.")
    if long_paras:
        warnings.append(f"{long_paras} paragraph(s) exceed 4 sentences.")
    if en_dashes:
        warnings.append(f"{en_dashes} en dash(es) found: replace unless inside a numeric range.")

    return {
        "post_type": post_type,
        "word_count": word_count,
        "word_band": [lo, hi],
        "word_band_source": band_src,
        "primary_keyword": keyword,
        "keyword_count": body_count,
        "density_percent": density,
        "body_min_occurrences_required": body_min_occ,
        "placements": placements,
        "placements_hit": f"{placements_hit}/9",
        "secondary_counts": secondary_counts,
        "entity_coverage_percent": entity_cov,
        "entities_missing": entity_misses,
        "fanout_coverage_percent": fanout_cov,
        "fanout_covered": q_covered,
        "fanout_uncovered": q_uncovered,
        "quick_answer": quick_answer,
        "definition_callouts": def_callouts,
        "title_tag": {"text": title_tag, "length": len(title_tag)},
        "meta_description": {"text": meta_desc, "length": len(meta_desc)},
        "url_slug": slug,
        "headings": {"h2": len(h2s), "h3": len(h3s)},
        "faq_question_count": len(faq_questions),
        "faq_answer_word_counts": faq_answer_words,
        "links": {"internal": len(internal), "external": len(external),
                  "internal_anchors": [t for t, _ in internal]},
        "schema": schema,
        "style": {"em_dashes": em_dashes, "en_dashes": en_dashes,
                  "hard_phrase_hits": hard_hits, "banned_vocab_hits": soft_hits,
                  "long_paragraphs": long_paras, "rhythm_stdev": rhythm_stdev,
                  "low_rhythm_variance": low_variance},
        "checks": checks,
        "warnings": warnings,
        "objective_pass": objective_pass,
    }


def human_summary(r):
    ok = lambda b: "PASS" if b else "FAIL"
    c = r["checks"]
    lines = [
        "SEO CHECK SUMMARY (v2)",
        f"  Type/words:    {r['post_type']}, {r['word_count']} words "
        f"(band {r['word_band'][0]}-{r['word_band'][1]}, {r['word_band_source']}) [{ok(c['word_count_in_band'])}]",
        f"  Keyword:       \"{r['primary_keyword']}\" x{r['keyword_count']}, "
        f"density {r['density_percent']}% (ceiling 1.2) [{ok(c['no_stuffing'])}]",
        f"  Placements:    {r['placements_hit']} "
        f"(missing: {', '.join(k for k, v in r['placements'].items() if not v) or 'none'})",
        f"  Quick Answer:  {'present, ' + str(r['quick_answer']['word_count']) + ' words' if r['quick_answer']['present'] else 'MISSING'} "
        f"[{ok(c['quick_answer_present'])}]",
        f"  Definitions:   {r['definition_callouts']} callout(s) [{ok(c['definition_callout_present'])}]",
        f"  FAQ:           {r['faq_question_count']} questions, answer words {r['faq_answer_word_counts']} "
        f"[{ok(c['faq_5_or_6'] and c.get('faq_answers_40_90', False))}]",
        f"  Title/meta:    {r['title_tag']['length']} / {r['meta_description']['length']} chars "
        f"[{ok(c['title_max_60'] and c['meta_max_160'])}]",
        f"  Links:         {r['links']['internal']} internal, {r['links']['external']} external",
        f"  Em dashes:     {r['style']['em_dashes']} [{ok(c['no_em_dashes'])}]",
    ]
    if r["entity_coverage_percent"] is not None:
        lines.append(f"  Entities:      {r['entity_coverage_percent']}% covered [{ok(c['entity_coverage_60'])}]")
    if r["fanout_coverage_percent"] is not None:
        lines.append(f"  Fan-out:       {r['fanout_coverage_percent']}% of questions covered [{ok(c['fanout_coverage_80'])}]")
    if r["schema"]["provided"]:
        s = r["schema"]
        lines.append(f"  Schema:        types {s['types']} [{ok(c['schema_valid'])}]")
    lines.append(f"  Secondary:     " + (", ".join(f"{k} x{v}" for k, v in r['secondary_counts'].items()) or "none given"))
    lines.append(f"  OBJECTIVE PASS: {'YES' if r['objective_pass'] else 'NO'}")
    for w in r["warnings"]:
        lines.append(f"  WARNING: {w}")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description="Objective SEO/AEO/GEO checker for blog posts (v2).")
    ap.add_argument("file", help="Markdown post file")
    ap.add_argument("--keyword", required=True, help="Primary keyword phrase")
    ap.add_argument("--secondary", default="", help="Comma-separated secondary keywords")
    ap.add_argument("--type", default="spoke", choices=["spoke", "hub", "single"], dest="post_type")
    ap.add_argument("--min-words", type=int, default=0, help="Length band floor from the SERP brief")
    ap.add_argument("--max-words", type=int, default=0, help="Length band ceiling from the SERP brief")
    ap.add_argument("--entities", default="", help="Comma-separated entity set from the SERP brief")
    ap.add_argument("--questions", default="", help="Semicolon-separated fan-out questions from the SERP brief")
    ap.add_argument("--schema", default="", help="Path to the post's JSON-LD schema file")
    ap.add_argument("--json", action="store_true", help="Emit JSON only")
    args = ap.parse_args()

    try:
        raw = open(args.file, encoding="utf-8").read()
    except OSError as e:
        sys.exit(f"Cannot read {args.file}: {e}")

    schema_raw = ""
    if args.schema:
        try:
            schema_raw = open(args.schema, encoding="utf-8").read()
        except OSError as e:
            sys.exit(f"Cannot read schema file {args.schema}: {e}")

    secondary = [s.strip() for s in args.secondary.split(",") if s.strip()]
    entities = [s.strip() for s in args.entities.split(",") if s.strip()]
    questions = [s.strip() for s in args.questions.split(";") if s.strip()]

    result = analyze(raw, args.keyword, secondary, args.post_type,
                     args.min_words, args.max_words, entities, questions,
                     schema_raw, args.schema)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(human_summary(result))
        print("\nJSON:")
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
