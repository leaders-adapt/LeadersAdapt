# Installing Hub-Spoke-Blog-Writer v2.0.0

Date: 2026-07-18

This folder is a complete drop-in replacement for the skill. It supersedes everything before it: the installed v1.0.0, the never-installed v1.1.0 (2026-06-16 Phase 0.5 Context Intelligence), the v1.2 spec (2026-07-02 sameness gate, live-render QA, live cannibalization gate, verified-only scoring), and the v1.3 QA additions (2026-07-04 publishing rules). All of it is folded in here; no other file from this folder needs to be applied separately.

## What is in the package

```
v2/
  SKILL.md                          the orchestration, v2.0.0
  references/
    context-research.md             Phase 0.5 (from v1.1, extended for information gain)
    intake-guide.md                 Phase 1 (price-public flag, author page URL, schema capability)
    serp-brief.md                   NEW: pre-write SERP and fan-out brief, per page
    geo-citability.md               NEW: zones, information gain, JSON-LD templates, citation tracking
    post-template.md                v2: three files per post (post, schema, scorecard)
    writing-style.md                v2: zone discipline, definition callouts, expanded banned list
    psychology-principles.md        v2: zoning rule
    scoring-rubric.md               v2: 14 metrics
    publishing-qa.md                NEW: field-verified publishing and live-debug rules (from v1.3)
  scripts/
    seo_check.py                    v2: tested; stuffing ceiling, Quick Answer, FAQ lengths,
                                    entities, fan-out, schema validation, band overrides
    sameness_check.py               NEW: cross-post sameness gate (tested; from the v1.2 spec)
    live_qa.py                      NEW: live-render QA gate (from the v1.2 spec, plus h1 and
                                    canonical checks; run on the machine that can reach the site)
  README-INSTALL.md                 this file
  CHANGELOG.md
```

## How to install

The skill package on your machine mirrors this structure (SKILL.md at the root, references/ and scripts/ beside it).

1. Open Claude settings, Capabilities, find Hub Spoke Blog Writer.
2. Replace the skill's files with the contents of this v2 folder: SKILL.md at the root, the eight files into references/, seo_check.py into scripts/. Delete no other files; v2 replaces everything it ships.
3. Save. New sessions will load v2.0.0 (check the version in the skill's metadata to confirm).

If your settings flow installs from a zip, zip THIS folder's contents (SKILL.md at the zip root) and upload it as the new version.

## First run after install

- Run Mode A on a small cluster and confirm the new phases appear: the connection menu (Phase 0.5), SERP briefs before writing (Phase 2), and a schema/ folder in the output.
- The checker has new arguments; the skill passes them automatically from the SERP brief. To verify manually: `python3 scripts/seo_check.py --help`.
- For Leaders ADAPT specifically: point Phase 0.5 at the Website Leaders ADAPT folder (business profile, evidence, content inventory) and the Nordic Leadership folder (thesis, evidence bank sources), and use the Tier 1 MVP cluster map as the Phase 2 input.
