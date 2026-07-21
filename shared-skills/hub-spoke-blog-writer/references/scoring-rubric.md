# Scoring Rubric (v2)

Fourteen metrics, each 0 to 10.0. Overall is the plain average, one decimal. The gate is 9.0. A flattering score that does not survive scrutiny makes the whole system worthless.

## How to score

- Objective inputs come from seo_check.py. Subjective metrics require quoted or pointed-to evidence in Notes.
- Default to skepticism: start from the anchor the evidence supports, do not round up.
- 10.0 means you could not improve it given the constraints, and is rare. 9 is excellent with a named minor gap. 7 to 8 is solid with real gaps. 6 or below forces revision regardless of the average.
- Every score below 10 names its deduction.

## The 14 metrics

### 1. Search Signals
Placement points, natural keyword use, secondary coverage, entity coverage.
10: all 9 placement points, no stuffing flag, 3+ secondaries natural, entity coverage 90%+. 9: 8 of 9 points, entities 80%+. 7 to 8: 7 points or entities 60 to 79%. Below: stuffing flag (over 1.2%) or core placements missing.
The 9 placement points (script-verified): title tag, H1, first 100 words, meta description, URL slug, at least one H2, body minimum occurrences (scaled to length), FAQ section, final 200 words.

### 2. Content Depth
Substance a competitor cannot copy in an afternoon.
10: named original framework plus concrete steps, examples, objections handled. 9: framework plus most of that. 7 to 8: useful but interchangeable. Below: generic advice.

### 3. Structural SEO
10: logical H2/H3 tree, keyword variations natural in headings, FAQ present (5 or 6), short paragraphs. 9: minor gaps. 7 to 8: weak heading use or thin FAQ. Below: wall of text.

### 4. Readability
10: rhythm variance passes, zero banned-vocabulary hits, paragraphs 4 sentences max. 9: one or two minor flags. 7 to 8: several flags. Below: robotic rhythm or AI-tell density.

### 5. Search Intent Match
10: the brief's intent is matched from the first screen and the page format matches what the SERP rewards. 9: matches with a slow start. 7 to 8: partial. Below: mismatch.

### 6. Technical Optimization
10: title 60 or fewer with keyword early, meta 160 or fewer with hook, clean slug, Quick Answer block present at correct length and format, length inside the brief's band. 9: one element off. 7 to 8: two off. Below: metadata sloppy or band ignored.

### 7. Competitive Edge
10: the SERP brief exists, and the post visibly beats the named incumbents on at least two axes (depth, experience, recency, format, information gain). 9: beats on one axis. 7 to 8: parity. Below: weaker than incumbents. No brief for the page: cap at 8 and say so.

### 8. Psychology Integration (zoned)
10: 10+ principles deployed with 8+ Strong (quoted evidence), all inside persuasion zones, answer zones clean. 9: 10+ deployed, 6 or 7 Strong, zones clean. 7 to 8: fewer Strong or one zone breach. Below: under 10 deployed, or persuasion language inside answer zones (each breach is a deduction).

### 9. Conversion Path
10: pain-to-product bridge feels inevitable, CTA follows the template, price shown only if the profile marks it public, product link appears once naturally mid-body. 9: strong bridge, one element off. 7 to 8: CTA bolted on. Below: weak or missing bridge, or a price shown for an offer whose price is not public.

### 10. Internal Linking Value
10: all cluster-map links present with keyword-rich varied anchors, including links to real existing site URLs, positioned where they help. 9: one missing or weak anchor. 7 to 8: generic anchors. Below: mesh incomplete.

### 11. Answer Extractability (AEO)
10: Quick Answer at 40 to 70 words in the SERP-winning format, all FAQ answers 40 to 90 words standalone, at least one definition callout, tables where the brief calls for them, every extractable block neutral. 9: one block off spec. 7 to 8: several off. Below: nothing cleanly extractable.

### 12. Information Gain (GEO)
10: at least one citable asset unique to this business (first-party stat with method, named framework definition, original table, operator story with a number, or an attributed quotable line from a real practitioner), formatted extractably, sourced from the evidence bank. 9: asset present, formatting or context slightly thin. 7: no unique asset available in the evidence bank (cap; scorecard names what data to collect). Below: the post pretends to originality it does not have.

### 13. Schema and Entity Integrity
10: schema file validates, Article + FAQPage present, FAQPage mirrors the FAQ exactly, author Person carries the credential and sameAs, stable @ids used, DefinedTerm present when a framework is introduced, no schema for content the page does not contain. 9: one minor mismatch. 7 to 8: schema present but incomplete. Below: missing or invalid schema file. (Context for honest scoring: Google states schema is not required for its AI features; this metric exists because schema is the cheapest unambiguous declaration of the author entity and framework definitions, and keeps rich-result eligibility. It measures integrity, not magic.)

### 14. E-E-A-T and Originality
10: real first-hand story from the stories bank, real citations, zero unverifiable claims, the author's vantage point unmistakable. Capped by the Phase 0.5 readiness gate: no real story or no confirmed credential means this metric cannot exceed 8, and the scorecard names the gap. Below 7: unverifiable claims present (mandatory revision).

## The gate and revision protocol

1. Overall below 9.0, any metric at 6 or below, or objective_pass false: revise.
2. Revise the 2 or 3 lowest metrics specifically.
3. Rerun seo_check.py after every revision; rescore all 14.
4. Maximum two revision cycles, then deliver with the honest score and the what-would-raise-it list. An honest 8.6 with a reason is a valid deliverable.
5. Record score history in the scorecard if revised.

## Scorecard integrity checklist

- Every countable number came from the script output pasted in the appendix.
- Every Strong has a quoted line. Every zone breach is named.
- Every metric below 10 names its deduction.
- Estimates are marked "est."; unverified items are flagged.
- The fan-out coverage list and schema validation block are present.
- The overall score is the recomputed average of all 14.
