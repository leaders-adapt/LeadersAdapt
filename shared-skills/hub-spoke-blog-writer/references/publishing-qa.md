# Publishing QA (read before publishing or debugging a live-render failure)

Every rule here was learned and verified live during real fix waves on a production WordPress site (July 2026). The pattern behind all of them: the CMS database, the REST API, and logged-in views all lie at some point. The logged-out guest render after a full cache purge is the only ground truth.

## The prime rule

DONE means: a fresh fetch of the live URL as a logged-out guest (real browser user agent, cache-buster query) shows the change AFTER the full purge sequence. DB confirmation, REST reads, and logged-in views do not count. Log DONE only with that evidence, and paste the live_qa.py PASS line as the proof.

## Publishing rules

1. Publish via REST with clean HTML, never rich-text paste. Rich-text paste flattens headings, strips links and schema, and mangles markup. The June failures (flattened H2s, lost link mesh, lost FAQ schema) all trace to paste.
2. Purge before verifying. Cache layers (LiteSpeed, edge workers, CDN) serve stale renders in both directions: a fix can look absent, and a regression can look fine. Sequence that works: page-builder cache clear (if the post uses one), then full page cache purge, then object cache purge whenever meta, schema, or head values changed. Then fetch.
3. Excerpt hygiene. Excerpt and social-description layers can inject em dashes and duplicate metas even when the post body is clean. live_qa.py checks the meta and og:description for em dashes; fix at the excerpt field, not the body.

## Schema delivery rules (field-verified)

4. Inline JSON-LD must be a bare tag. A bare `<script type="application/ld+json">` block inside post content survives for guests. Adding an id attribute to that same tag gets the whole block stripped by the optimizer for guests. Never put attributes on ld+json tags in content. For idempotent re-runs, precede the tag with an HTML comment marker (for example `<!-- schema-{postId} -->`) instead of an id.
5. Page-builder HTML widgets strip ALL inline scripts for guests, including ld+json (verified on Elementor). Posts rendered fully by the builder cannot carry schema in widgets. Deliver schema for those posts via a tag manager (custom HTML tag on a page-path trigger, verified working) or convert the post to classic rendering first.

## Debugging rules (when a fix will not take)

6. Check render-time injectors BEFORE re-editing content. If edits to post content and builder data do not change the live render, a code-snippet plugin (WPCode or similar) or an mu-plugin may be injecting stale blocks at render time. Verified case: a snippet injected stale per-slug FAQ blocks into the head graph on 7 posts for weeks while every content-layer fix was correct. Diagnosis order: post content, builder data, snippet plugins, mu-plugins.
7. Stale head values need an indexable rebuild. og:image, author, and other head values can stay stale after a correct edit because the SEO plugin's indexable is stale, and the REST head JSON can itself serve the stale value. Fix sequence: a no-op re-save of the post (same featured media is enough), then object cache purge AND page cache purge, then re-check. Never trust the first REST read after a media change.
8. Builder data is JSON with per-post escaping. Page-builder data fields are JSON strings whose escaping varies per post (quotes and slashes both escaped, quotes only, or plain). Test each variant for presence and apply replacements exactly once per matching variant, counting occurrences before and after. Pure swaps are idempotent; insertions need a marker guard. Never insert text containing raw double quotes into an escaped field: it corrupts the JSON. Always JSON.parse the new string BEFORE saving, and keep the pre-edit value for instant restore.
9. Tag-stripped scans hide inline anchors. Sentence extraction from tag-stripped text drops inline `<a>` markup, so exact-match replacements built from it miss the stored string. Before building replacement pairs, pull the raw HTML window around the target from the live render and build pairs against the marked-up form. This also preserves citation links while rewriting the sentence around them.

## The live QA checklist (what live_qa.py automates)

| # | Check | Pass condition |
|---|---|---|
| 1 | One H1 | exactly one h1 in live HTML |
| 2 | Headings render | h2 count at least 4 |
| 3 | Cluster links | every cluster-map link exists as a real anchor |
| 4 | FAQ schema | FAQPage JSON-LD present in live HTML |
| 5 | Meta description | exactly matches the approved metadata block |
| 6 | Social card | og:image present |
| 7 | Canonical | canonical link present (verify self-referencing manually) |
| 8 | No placeholder | "lorem ipsum" absent |
| 9 | Excerpt hygiene | no em dash in meta or og description |
| 10 | Manual pass | title tag correct, Person schema present |

Purge first, then run. A URL that cannot pass gets its failure recorded in the cluster map honestly, never marked done.
