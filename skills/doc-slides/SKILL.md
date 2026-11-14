---
name: doc-slides
description: Create or revise research slides from an outline, paper, or existing deck, with scientifically faithful content and properly typeset equations. Use for conference talks, seminars, defenses, and mathematical presentations. Default to PowerPoint with clear vector formulas and retained LaTeX sources; use doc-meeting for a written pre-read and plot-paper for standalone paper figures.
---

# Research Slides

Prepare slides suited to their purpose, occasion, topic, and audience. Preserve an approved outline, scientific claims, and supplied template unless the user asks to change them. A research storyline is optional, not a required structure.

## Read for the current stage

- Before choosing tools, opening a deck, or editing/exporting it, read [technical workflow](references/technical-workflow.md): live MCP control, file authoring, formula handling, and verification are separate capabilities.
- Before a build or generated-artifact cleanup, read [build lifecycle](references/build-lifecycle.md): reuse current assets, publish durable dependencies first, then clean only the owned successful run.
- Before producing or repairing mathematical slides, read [equations](references/equations.md). Formula clarity is the priority: LaTeX-rendered SVG with retained source is allowed by default; never simulate structured formulas with plain text or hand-positioned glyphs.
- For purpose, outline development, slide sequencing, or timing, read [outline and flow](references/outline-and-flow.md).
- For layout or style choices, read [visual design](references/visual-design.md).
- Before handing off a deck, or for a basic assessment-only request, read [review](references/review.md) for delivery QA.
- Only when the user explicitly requests an audience-perspective, visual/readability, or idea-flow/comprehension check, read [audience review](references/audience-review.md). This optional sub-workflow is not triggered by ordinary creation, editing, export, or handoff; honor requests for only one dimension or a slide range.

Load only the relevant references. Use the verified runtime route in the technical workflow; installing an MCP is not proof of connection or formula support. Keep one authoritative PPTX and one writer during an edit.

## Workflow

1. Recover purpose, occasion, audience, speaking time, source materials, outline status, template, output format, and editability needs. Ask only about choices that change the deliverable; default to PPTX for an unspecified PowerPoint-oriented task.
2. Follow an approved outline when available; otherwise organize the supplied material for the stated purpose. Resolve mathematical notation from authoritative sources rather than guessing what a flattened formula means.
3. Select live MCP control or file authoring for the requested operation. Before creating or replacing equations, prove the equation route on representative expressions and a real slide. Use [the bundled renderer](scripts/render_equation.py) and [LaTeX template](assets/equation.tex) when suitable; verified native equations remain valid.
4. Keep ordinary text editable and figures scientifically faithful. Retain formula source and slide-to-asset locators; an SVG is not a native editable equation. Apply one semantic color mapping and capitalization convention throughout; typeset inline mathematical relations through the same verified math route as display equations.
   Use a small, explicit typography hierarchy and keep same-role text at one size across the deck and within each slide. Prefer numbered steps or bullets for distinct points rather than consecutive prose blocks; see [visual design](references/visual-design.md) for presets and list use.
   Use tool-assisted alignment by default for layout work: inspect actual shape/group coordinates and paragraph properties, choose shared anchors and spacing, then apply Align/Distribute operations or deterministic coordinate edits. Verify the measured result and the rendered slide; see visual design for group transforms, equation alignment and intentional exceptions.
   Keep visible explanations compact, not long paragraphs. Short phrases and symbol-led chains are welcome; see the visual-design guidance for relation meaning and the equations guidance for typesetting.
5. Perform basic delivery QA on the actual rendered output, repair defects, and hand off the deck with its necessary equation sources. After every PPTX edit, run [animation-target validation](scripts/check_pptx_animation_targets.py) on the final staged file, including hidden slides; dangling references block delivery. See [Repair prevention](references/technical-workflow.md#animation-integrity-and-repair-warnings) for deletion/replacement and native reopen checks. After verified publication, clean the owned run using the build lifecycle; preserve last-good recovery on failure. Run the more time-consuming audience review only when explicitly requested. Use [doc-script](../doc-script/SKILL.md) for requested oral scripts or substantive speaker-note prose; keep deck editing and notes synchronization on this skill's verified technical route, and do not make a script a compulsory deliverable. State any unverified target-application behavior.

A review request is read-only. Skill creation or a supplied example deck does not itself authorize rewriting that deck, starting a literature search, or installing new dependencies.
