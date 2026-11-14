# Delivery QA and review routing

## Scope

- Basic delivery QA is part of creating or editing a deck: check the changes and their rendered output for broken exports, missing assets, obvious layout defects, and scientific fidelity. It is not an automatic second, exhaustive audience audit.
- For a local edit, scope the checks below to affected content and plausible export/style regressions; do not claim a whole-deck audit from a partial check. For a new deck, verify the delivered content as a whole.
- The optional [audience review](audience-review.md) covers visual readability and first-time comprehension of the idea flow. Load and run it only when the user explicitly requests that review. A generic request to create, finish, improve quality, or export slides does not activate it; an unspecified "check" defaults to basic QA.
- An explicitly requested audience review may be visual-only, comprehension-only, limited to named slides, or cover both dimensions across the deck. Do not expand it into manuscript refereeing, new research, or automatic rewriting.

## Scientific checks

- Verify the requested work against the confirmed outline and source material; preserve the distinction between results and interpretation. A basic edit is not authorization to reorganize an approved deck.
- Check equations in scope against their source, including brackets, indices, exponents, signs, conditioning, and assumptions. Do not rely on visual similarity alone.
- Check original figure fidelity, units, comparison groups, uncertainty, citations, and any required acknowledgments. Do not run a new literature review unless requested or necessary to resolve a specific missing source.

## File and formula checks

- Inspect PPTX package contents when useful: native mathematics normally includes Office Math nodes such as `m:oMath`; SVG assets should remain in `ppt/media/` and be referenced from slide relationships. Check actual usage, not just a nonzero asset count.
- Plain text extraction is helpful for missing text and placeholders, but it cannot verify SVG mathematics or preserve the structure of formulas split into text runs.
- Match each required mathematical expression to a rendered SVG/native object and retained source. Finding one correct equation does not validate the others. Do not flag every isolated Greek letter or variable as a fake equation.
- If a formula list/manifest is used, verify its slide locators and current source-to-asset mapping after edits. An existing asset path or a previous successful render is not evidence that changed LaTeX was regenerated.
- An SVG can coexist with a raster compatibility preview; verify that the vector asset is referenced. Keep ordinary text editable. If native equation editing was requested, SVG alone does not meet that requirement.
- Use available package-integrity and layout checks. Passing them does not establish mathematical correctness or good design.
- For every edited PPTX, run the shared [animation-target checker](../scripts/check_pptx_animation_targets.py) on the final staged file. Missing animation/build-list targets block delivery, including on hidden slides; see [Repair prevention](technical-workflow.md#animation-integrity-and-repair-warnings).

## Visual and application checks

- Render the final exported file, not only the source HTML or standalone equations. For a local edit, inspect affected slides and any deck-wide effects of template/style changes; for a newly generated deck, check the rendered output for delivery defects. Do not add a separate audience-review pass unless requested.
- Look for missing glyphs, malformed fractions or delimiters, small superscripts, clipping, baseline drift, distortion, lost color, poor contrast, and mismatched mathematical scale. Also inspect wrapping, overlap, alignment, figures, citations, and slide numbers.
- Check list-item gaps, hanging indents, continuation-line alignment, text-frame anchors and repeated heading/body spacing. Compare visible baselines and whitespace in the rendered output, not only bounding-box positions; keep comparable slides consistent while preserving deliberate section breaks. For layout edits, also read back the chosen common anchors/gaps through a geometry or app tool, accounting for parent-group transforms. Use rendered relation-sign positions for aligned mathematics where available; do not let a generic package/layout pass substitute for this check.
- Check a representative mathematical slide in the intended PowerPoint version when practical; other renderers can differ. Never claim PowerPoint validation unless it was actually opened and inspected there. A cached preview or structurally valid ZIP is not evidence of target-application rendering.
- Follow [technical workflow](technical-workflow.md) for live target selection, native preview, and copy-only tests. Report which capabilities passed; do not turn a successful MCP text edit into a claim that it replaces the formula pipeline or is generally stable.
- After structural edits, confirm the exact file's expected slide count and close/reopen it without a Repair dialog or repaired/unsaved identity. Treat an Open success with a count mismatch as incomplete validation. Follow the technical workflow when the target application is unavailable.
- Re-render changed slides after repairs; inspect inherited/template changes across the deck. Rehearse or estimate actual spoken coverage when timing is in scope.

## Handoff

Provide speaker notes or a separate script when the user wants them. Keep mathematical explanations plain, define unfamiliar terms where needed, and use content-based transitions. Notes can hold supporting explanation while visible slides stay readable. Do not add a full transcript, speaking-coach annotations, or fixed timing brackets to every deck by default. For PPTX, put requested notes in the native notes pane when supported and update them with the affected slides; do not bake them into a screenshot.

Deliver the requested deck and necessary formula sources/assets, with locators sufficient to change and regenerate an equation. Keep temporary compilation files and internal validation logs out of the deliverable. Explain use-affecting limits, especially SVG-versus-native editability, accessibility, and unverified PowerPoint behavior.

After successful source/asset publication and verification, follow [build lifecycle](build-lifecycle.md) to clean the owned run. A good PPTX with an incomplete/mismatched source mapping is not ready for cleanup. Leave failed or unknown legacy directories intact pending an exact review.

Assessment-only requests remain read-only. Write a new version for authorized repairs unless the user explicitly asks to overwrite the original.

Selective inspiration: [EvoSkills delivery and Q&A](https://github.com/EvoScientist/EvoSkills/blob/main/skills/academic-slides/references/delivery-and-qa.md) for comprehension checks and [academic-research-slides](https://github.com/Rebeccca2000/academic-slides-skill/blob/main/SKILL.md) for plain explanations and separately maintained notes. Mandatory scripts, fixed research narratives, and screenshot-only decks are not adopted.
