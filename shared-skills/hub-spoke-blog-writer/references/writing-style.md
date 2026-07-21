# Writing Style (v2)

The posts must read like a sharp practitioner wrote them in one sitting. Three audiences judge this: human readers who bounce off robotic copy, editors and algorithms that discount AI-sounding text, and AI answer engines that quote neutral, specific passages and skip salesy ones.

## The ten core rules

1. No em dashes anywhere. Use commas, colons, or periods. The script counts them; the count must be zero.
2. Short paragraphs, 1 to 4 sentences.
3. Varied sentence rhythm. Mix short punches with longer explanatory sentences. The script flags low variance.
4. Active voice except where passive is clearly better.
5. Second person. Talk to "you".
6. Specific over vague, always. Numbers, names, scenarios. "Many companies struggle" is filler; "you cancel your third 1:1 this week" is a scene.
7. No filler sentences. If it can be cut without losing meaning, cut it.
8. Contractions are good.
9. Conversational but competent. Not academic, not bro-casual.
10. The author's voice profile outranks all of this. Apply `author-voice-profile.md` (real rhythm, signature phrases, hard avoids) on top of these defaults.

## Zone discipline (v2)

The post has two kinds of territory, and the style differs on purpose:

- Answer zones (Quick Answer, definition callouts, stat blocks, FAQ answers, tables): flat, neutral, attributed, self-contained. No second-person selling, no rhetorical questions, no product mentions, no adjectives doing sales work. These exist to be quoted by AI engines, and engines do not quote ads. Write them like a good encyclopedia with a spine.
- Persuasion zones (hook, narrative body, stories, conclusion, CTA): this is where the voice, the psychology, and the second person live.

If a sentence in an answer zone would embarrass a rival publication quoting it verbatim, rewrite it flat.

## Banned vocabulary and patterns

Never use (the script counts these): delve, leverage (as a verb), robust, holistic, foster, facilitate, seamless, empower, streamline, cultivate, paradigm, synergy, comprehensive, utilize, cutting-edge, game-changer, elevate, supercharge, unlock the power, navigate the landscape, in today's fast-paced world, ever-evolving, tapestry, embark, journey (metaphorical), furthermore, moreover, it's important to note, it's worth mentioning, needless to say, in conclusion, revolutionize, harness the power, dive into, in the realm of.

Also banned:
- Hedging chains. One hedge per claim maximum, and only when uncertainty is real.
- The mirrored conclusion ("In this article we explored X, Y, Z"). End with something earned.
- Uniform paragraph structure. Use a one-sentence paragraph for emphasis, a question, an aside, an admission.
- Emoji, unless the profile explicitly wants them.

## The statistics rule

A statistic is only allowed from one of three sources:
1. Verified via web search right now, with the real source named in the post.
2. The user's own data from `evidence-bank.md`, attributed as such.
3. Not at all. Write a specific scene instead. A scene outperforms a fake number and carries zero risk.

Never "studies show" without a study. Never invent percentages, surveys, or expert quotes. In answer zones, every number carries source and year inline.

## Definition callouts

At least one per post: a bolded single sentence, "**[Term] is [definition].**", near first use of the core concept. If the post introduces a named framework, this sentence is also the DefinedTerm description in the schema file, word for word. Write it so it survives being quoted alone.

## E-E-A-T in practice

- Experience: real first-hand moments from the stories bank. "When I ran a 150-person company" beats any citation. Never invented.
- Expertise: named frameworks, shown steps, depth competitors lack.
- Authoritativeness: real external sources, linked. The author byline carries the credential line from the voice profile.
- Trust: honest tradeoffs and who the product is not for. One honest limitation beats ten superlatives.

## Pre-scoring humanizer pass

Before running the scorer:
1. Remove any banned vocabulary that slipped in.
2. Break any stretch of 3+ similar-length sentences.
3. Make any vague claim concrete.
4. Split any paragraph over 4 sentences.
5. Sweep the answer zones for persuasion leakage and the persuasion zones for flatness.
6. Polish the opening and the closing; they carry the Peak-End weight.

Then run seo_check.py. Its flags are the floor, not the ceiling.
