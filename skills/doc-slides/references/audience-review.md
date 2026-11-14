# Audience-perspective review (opt-in)

## Activation and scope

Run only when the user explicitly requests an audience-perspective review, a visual/readability check, a comprehension/idea-flow check, or names this module. For example: "从观众角度检查这份 slides 的视觉效果和内容理解" or "启用 audience-review，只检查第 3–8 页的公式和 flow". Merely invoking `doc-slides`, creating/editing slides, or asking to finish/export them does not activate this pass.

Default to both dimensions below when an audience review is requested without narrowing its scope. Respect visual-only, comprehension-only, and selected-slide requests. Assessment is read-only for the deck and sources; preview/export artifacts are allowed. Do not apply fixes unless the user asks for repairs. No new dependencies or separate reviewer agent is required.

Use the established purpose, occasion, audience background, and live-talk versus asynchronous-reading format. Ask only if missing context changes the judgment; otherwise state a reasonable assumption. Do not require a research storyline, novelty arc, or contribution on every slide.

## Inspect what the audience will see

1. Identify the current deck/version and requested slide range. Use [technical workflow](technical-workflow.md) for native PowerPoint preview/export when available. Check slide-to-preview mapping, including hidden backups. Do not use stale previews or silently switch to a different deck.
2. Inspect actual rendered slides at a normal full-slide viewing scale, not only extracted text or highly zoomed crops. Use a montage for consistency and sequence; zoom in to diagnose a suspected issue, not to excuse unreadable text. If only another renderer is available, qualify target-application conclusions. If no usable render is available, report a text-only comprehension review, not a completed visual review.
3. For comprehension, follow the visible slide sequence as a first-time audience member with the declared background. Do not silently supply missing definitions or transitions from project knowledge. Account for supplied speaker notes or intended spoken explanation in a live talk, but identify when an explanation exists only in notes or is merely assumed.

## Visual readability

- **Text and hierarchy:** Can the audience read titles, prose, legends, axes, captions, and subscripts at the intended viewing size? Check density, wrapping, alignment, overlap, clipping, and competing focal points. Recommend cutting or splitting overloaded content before shrinking it. Do not substitute a universal font-size cutoff for visual inspection.
- **Color and contrast:** Check text/background and curve/background contrast, consistency of semantic colors, and distinctions that disappear in projection, grayscale, or common color-vision differences. Important comparisons should not depend on color alone. Describe weak contrast as an observed concern; do not claim a measured ratio without measuring it.
- **Figures and line styles:** Check sharpness, distortion, axis/legend readability, line widths, dash visibility, marker differentiation, and annotations that guide the eye. Ensure methods remain identifiable and a primary comparator is not accidentally made faint or subordinate. Judge figures at their slide size, not their paper size; preserve data, units, and uncertainty.
- **Equations:** Check fraction/delimiter layout, glyphs, superscripts/subscripts, baseline and font compatibility, scale relative to nearby text, excessive line length, and visual grouping of multi-line expressions. A mathematically correct equation may still be unreadable. Follow [equations](equations.md); do not suggest plain-text glyphs or screenshots as a shortcut to better typesetting.
- **Deck consistency:** Check repeated title positions, margins, notation scale, color roles, and line-style meanings. Distinguish a deliberate section or emphasis change from an accidental inconsistency. Assess animation/build steps only if actually inspected; a static PDF does not establish their quality.

## Content comprehension and idea flow

- **Local purpose:** Can a first-time audience member tell what this slide explains and where to look? Does its title match the visible content? A setup or definition slide need not claim a result.
- **Prerequisites:** Are symbols, acronyms, concepts, assumptions, and comparison baselines introduced before use at a level suitable for this audience? Flag circular explanations and hidden prerequisites; distinguish audience-required background from genuinely missing explanation.
- **Sentences and concepts:** Identify exact phrases that are hard to parse, abstract without an anchor, ambiguously refer to "this/it", compress several claims, or use jargon without helping the audience. Offer a short local rewrite or concrete example when useful, without changing scientific meaning or strengthening claims.
- **Transitions:** Check whether the reason for moving to the next idea is apparent. Look for abrupt jumps, unannounced changes of setting/notation, repeated material without a purpose, and missing links between equations, diagrams, and conclusions. Separate topics may simply need headings or a bridge sentence, not an invented causal story.
- **Explanatory load:** Is the information needed to interpret a figure or equation visible or plausibly explainable within the stated talk time? Flag a missing takeaway or decoding burden where it obstructs understanding; do not require every slide to be self-contained in a speaking deck or impose a fixed slides-per-minute rule.
- **Evidence boundaries:** Check whether the audience can distinguish illustration from data, intuition from proof, and supported results from conjectures. Flag misleading implications without launching a new proof audit or literature review.

## Report and repair boundary

Start with the most consequential audience blockers. For each actionable finding give **slide number and region or exact phrase → what the audience sees/misunderstands → smallest useful repair**. Separate visual findings from comprehension findings when both are requested. Include a cross-slide finding when the problem is a transition or inconsistent convention.

Prioritize: **P1** unreadable, misleading, or comprehension-blocking; **P2** avoidable decoding effort or flow friction; **P3** optional aesthetic preference. Do not pad the report with arbitrary scores, stylistic preferences presented as errors, or a forced finding for every slide.

State which slides and dimensions were inspected, the rendering route, audience assumptions, and any unverified animations or target-application behavior. Propose local repairs before a broad redesign; surface any change to the approved outline or scientific claims. If repairs are separately authorized, re-render affected slides and recheck the relevant transitions; do not repeat the whole audit unless needed or requested.
