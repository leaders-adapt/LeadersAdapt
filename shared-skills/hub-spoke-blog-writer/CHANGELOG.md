# Changelog

## 2.1.0 (2026-07-18, late)

Added the per-post uniqueness interview. Phase 2 now asks whether the user wants a short Q&A before each post (recommended) and how many questions per post (3 to 5 recommended, 1 to 10 accepted). When enabled, Phase 3 generates fresh questions per post from its SERP brief and information-gain gap (first-hand stories, contrarian takes, real numbers, client moments, hard-won mistakes), saves answers to interviews/NN-slug-interview.md as user-confirmed evidence, requires at least one answer woven into the post, and the scorecard cites which. Skipped answers are written around, never invented. This turns the author's lived experience into per-post information gain, the material no competitor and no model can reproduce.

## 2.0.1 (2026-07-18, evening)

Recalibrated against live research into mid-2026 practice, including Google's official "Optimizing for generative AI features" guide (updated 2026-07-10), current llms.txt adoption and crawler data, and the published GEO research on citation lifts.

- llms.txt demoted to optional hygiene everywhere: Google officially ignores it and crawl monitoring shows major AI crawlers almost never fetch it. Keep it accurate if maintained; never a priority or a citation lever.
- Fan-out anti-spam guardrail made explicit: cover the fan-out set inside the page; a page per query variation is scaled content abuse under Google's spam policy. (Google's guide confirms query fan-out and RAG grounding as the actual mechanisms, validating the brief design.)
- Measurement upgraded: Search Console's Generative AI performance report added as the primary Google-side citation measure; reference rate named as the GEO KPI alongside Semrush AI mentions and the prompt panel.
- Freshness tightened: GEO-priority pages refresh every 3 to 6 months (AI answers favor sources updated within 6 months; citations decay after about 3). Mode D trigger updated. Real changes only; no dateModified games.
- Citable assets: attributed practitioner quotations added as a first-class information-gain asset (strongest measured lift in the Princeton/AI2 research, about +28%).
- SERP brief: honest ranked-list guidance for commercial clusters whose answers are list-shaped.
- Schema metric reframed honestly: not required by Google for AI features; kept for entity clarity and rich-result eligibility.
- Snippet-eligibility noted as a hard precondition for AI Overviews and AI Mode inclusion.

## 2.0.0 (2026-07-18)

Folds in the unreleased 1.1.0 and adds the full SEO, AEO, and GEO layer for mid-2026. Built from the 2026-07-18 expert review (7.9/10 as installed; this release targets the 9.4 ceiling).

Added
- Phase 2 SERP and fan-out briefs, one per page, required before writing (references/serp-brief.md). Includes the winnability call, the length band, the entity set, and 6 to 12 fan-out questions as a coverage contract.
- GEO layer (references/geo-citability.md): zoned writing (neutral answer zones, persuasion zones), the information-gain requirement (one business-unique citable asset per post), JSON-LD emission per post (Article, Person with credential and sameAs, Organization, FAQPage mirroring the FAQ, DefinedTerm for frameworks, stable @ids), llms.txt and sitemap reminders, AI-citation tracking columns in the cluster map, and refresh triggers.
- Mode D: refresh a published post (SERP re-brief, diff, update, re-score, log).
- seo_check.py v2: Quick Answer detection, FAQ answer length checks (40 to 90 words), definition callout count, --entities coverage, --questions fan-out coverage, --schema JSON-LD validation, --min-words/--max-words band overrides, dynamic body-occurrence minimum. Tested on a fixture before release.
- Scoring rubric v2: 14 metrics (adds Information Gain and Schema and Entity Integrity; renames Keyword Hierarchy to Search Signals and AEO Citability to Answer Extractability; Sales Page Traffic Potential becomes Conversion Path with the price-public rule).
- Intake v2: price-public flag per offer, author page URL for the Person @id, CMS JSON-LD capability, no-JS render and llms.txt checks.

Changed
- Keyword density floor removed. Stuffing ceiling only (fail above 1.2%, warn above 1.0%). Placements stay.
- Length is intent-driven per the SERP brief, not a universal word count. Script defaults widened, brief overrides preferred.
- Psychology principles now live in persuasion zones only; persuasion inside answer zones is a scoring deduction.
- Publish order is a per-cluster setting (spokes-first default).
- Conclusion requires an H2 (closes the FAQ block cleanly for the checker).
- Banned vocabulary extended (revolutionize, harness the power, dive into, in the realm of).
- Competitive Edge is scored against the pre-write brief and caps at 8 without one.

From 1.1.0 (built 2026-06-16, never installed)
- Phase 0.5 Context Intelligence: connection menu, author-voice-profile.md, evidence-bank.md, existing-content-map.md, readiness gate, E-E-A-T ceiling, cannibalization cross-check. Extended in 2.0.0: the evidence bank gains the citable-asset inventory that feeds the information-gain requirement, and the content map gains the AI-citation baseline.

From the 1.2 spec (2026-07-02, never applied; fully folded in)
- Change A: cluster sameness gate (scripts/sameness_check.py, Phase 4 step 0). Any 12+ word sentence in 2+ posts fails the wave before scoring.
- Change B: live-render QA (scripts/live_qa.py, new Phase 6). A post is done when the live guest render passes, not when the CMS says published. v2 script adds h1-count and canonical checks over the spec version.
- Change C: live cannibalization gate in Phase 2 (sitemaps plus CMS search, verdict per hit, decision column, 7-day staleness rerun).
- Change D: verified-credit scoring (no credit above 7 without quoted evidence) and the published-means-live-verified rule.

From the 1.3 QA additions (2026-07-04; folded into references/publishing-qa.md)
- The bare ld+json tag rule, builder widgets stripping inline scripts (schema via tag manager), render-time injector diagnosis order, SEO-plugin indexable rebuild sequence, per-post builder-data encoding variance with JSON.parse guards, raw-HTML replacement pairs to preserve citation anchors, and verify-live-after-purge as the only DONE.

## 1.0.0 (2026-06-10)

Initial release: hub-and-spoke architecture, 12-metric rubric with 9.0 gate, seo_check.py objective checker, AI-tell removal, no-fabrication rules.
