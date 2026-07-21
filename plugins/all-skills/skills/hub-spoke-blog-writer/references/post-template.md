# Post Template (v2)

Every post produces three files. The post file contains Sections 1 and 2 only, clean for CMS paste. The schema file carries the JSON-LD. The scorecard file contains the audits.

## File 1: The post (posts/NN-slug.md)

### Section 1: Metadata block

```markdown
# [Post Title]

**PRIMARY KEYWORD (SEO plugin focus):** [keyword]
**TITLE TAG:** [under 60 characters, keyword near the front, compelling hook]
**META DESCRIPTION:** [under 160 characters, keyword included, clear value, curiosity]
**URL SLUG:** /[keyword-based-slug]/
**SEARCH INTENT:** [from the SERP brief]
**LENGTH BAND:** [min-max from the SERP brief]
**PUBLISH ORDER:** [position in cluster]

---
```

The `---` line matters: seo_check.py splits metadata from body on it. No `---` horizontal rules inside the body.

### Section 2: The full post

Opening, first 100 to 150 words (persuasion zone):
- Hook with a real scene or a verified statistic (per writing-style.md).
- Primary keyword inside the first 100 words.
- Establish the pain, promise the payoff.

Quick Answer block, directly after the opening (answer zone):
- 40 to 70 words that answer the primary query, self-contained, no setup, no pitch.
- Starts with a bolded answer-first sentence. Format matches the SERP brief's winning snippet format: paragraph by default, a compact list or table if that is what wins the SERP.
- This block is what AI engines quote and what the featured snippet takes.

Definition callout (answer zone):
- At least one bolded single-sentence definition near first use of the core concept: "**[Term] is [definition].**"
- If the post introduces a named framework, this definition is also the DefinedTerm text in the schema file, word for word.

Body:
- H2s for major sections; the SERP brief's fan-out questions appear as question-form H2s or FAQ items, every one of them.
- Length: the brief's band. Dense beats long. Cut before padding.
- Keyword: all 9 placement points, natural use, no stuffing (the script enforces a ceiling, not a floor). Cover the brief's entity set.
- At least one named framework, model, or step sequence usable today.
- The citable asset (information gain) from the evidence bank, formatted as an extractable block: first-party stat with method context, framework definition, original table, or operator story with a number.
- E-E-A-T: at least one real first-hand story from the stories bank; real citations for external claims; the author's vantage point.
- Stat blocks (answer zone): number, context, source, year, link. No source, no stat.
- Internal links exactly as the cluster map specifies, including real existing site URLs.
- Hubs additionally: one comparison table summarizing the cluster subject (answer zone).

FAQ section (answer zone):
- H2 with natural FAQ phrasing, 5 or 6 H3 questions phrased as people search them (pull from the brief's PAA and fan-out list).
- Each answer 40 to 90 words, standalone, neutral, substantive. These mirror into the FAQPage schema exactly.

Conclusion (persuasion zone):
- Give it an H2 with a natural phrasing (never "Conclusion" alone, never "In conclusion" in the text). The H2 matters mechanically too: it closes the FAQ block so the checker measures FAQ answer lengths correctly.
- Sharpen the core insight, give next steps, bridge to the product.

Product CTA section (persuasion zone):
- H3 connecting this post's specific problem to the solution.
- Mechanism, not adjectives. Named components, exactly one left unnamed as the curiosity gap.
- One CTA. Show the price only if the profile marks this offer's price public; otherwise the CTA is the discovery call or free assessment. Educational tone.

## File 2: The schema (schema/NN-slug-schema.json)

Built per `references/geo-citability.md`: Article referencing the site author and organization @ids, FAQPage mirroring the FAQ word for word, DefinedTerm when a framework is introduced, HowTo only for true step-by-steps. Validate with the checker (`--schema`).

## File 3: The scorecard (scorecards/NN-slug-scorecard.md)

Sections:

3. Keyword Implementation Audit: all numbers from seo_check.py (appearances, placements hit, secondary counts, entity coverage, stuffing check).
4. Psychology Implementation Audit: the 12-principle table with quoted evidence; note any persuasion found in answer zones (deduction).
5. Performance Metrics: the 14-metric table from scoring-rubric.md with evidence notes and the overall average.
6. Internal Linking Structure: links to and from this post.
7. Fan-out coverage: the brief's question list with covered/uncovered status from the script.
8. Schema validation: the script's schema block verbatim.
9. Strategic notes: 4 to 6 short notes (why this keyword, how it beats the SERP per the brief, the product connection, the citable asset it owns, its role in the cluster).
10. Interview usage (when the per-post uniqueness interview ran): which answers from interviews/NN-slug-interview.md appear in the post, quoted, and where. A post that ignored all its interview answers must say so and why.

Appendix: paste the full seo_check.py summary block.
