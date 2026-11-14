# Visual design and review for paper figures

Read this when designing a new figure, improving an unattractive one, or preparing a final visual review. Apply the paper's fixed style from [style-details.md](style-details.md); use this guide to decide what the reader should see first and which visual changes actually help.

## Design before coding

- State the figure's central question and the observation or comparison that should answer it. Identify what belongs in the main view, what serves as context, and what can move to a caption, table, or appendix.
- Give every panel a distinct role and a reading order. Use equally sized panels for equally weighted comparisons; use an asymmetric layout only when one overview or mechanism genuinely leads the others. Sketch a complex layout before coding, including the plot, legend, annotation, and colour roles.
- Choose the chart by the data and claim. A line shows change over a meaningful sequence; dots expose close numerical comparisons; bars show magnitudes or counts from a shared zero; a contour shows a field and trajectories. Explain a less familiar encoding to the reader.
- Make the primary evidence visually dominant. Keep baselines, grids, confidence bands, and decorative shapes subordinate but legible. Use annotations to direct attention to a real result or mechanism; remove an annotation that merely repeats the caption.
- Prefer short, concrete labels. Use a shared legend or direct labels when they reduce searching across panels. Keep line styles or markers as a second cue when hue or lightness is ambiguous.

## Review the actual output

Run the deterministic paperplot.save checks first. Those checks can measure clipping, tick collisions, and curve visibility. Do not call a figure aesthetically good merely because they pass. When exact font size, colour distance, or geometry has not been measured, report it as an inspection judgment rather than a numeric result.

View each PNG at the printed width, then inspect it beside the relevant manuscript text and caption in the compiled PDF. For multiple colour-coded series, compare a colour contact sheet with an optional grayscale contact sheet using paperplot.tile. Check:

1. **Clarity:** can a reader identify the question, axes, units, comparison, and principal observation?
2. **Hierarchy:** does the most important evidence attract attention before legends, decorative marks, or dense annotation?
3. **Alignment and space:** do panel boundaries, labels, gutters, and margins look deliberate and give the data room?
4. **Colour and redundancy:** do methods retain their paper-wide identities, remain visible on the background, and have another cue when colour fails?
5. **Manuscript fit:** is the figure legible at its natural size, and do caption and surrounding text describe what the plot actually shows?

Report a concrete issue and its effect on reading, then the smallest likely improvement. A visual judgment does not verify the plotted statistics or prove compliance with a venue's current rules.

## Revise by comparison

For an aesthetic revision, save the original and one or two candidate renderings from the same data. Change one design decision at a time: panel arrangement, emphasis, whitespace, label or legend placement, or type hierarchy. Compare them side by side at printed width and in the manuscript. Preserve values, uncertainty definitions, axes meaning, method identity, and source provenance; any scientifically justified range or transformation change needs its own explanation.

Choose the version whose message reads most clearly and whose technical content remains intact. Stop when further polish does not improve comprehension. Update the shared style only after a candidate works across representative figures rather than one isolated example.

This guide adapts design ideas from [HKUSTDial figure-designer](https://github.com/HKUSTDial/Supervisor-Skills/blob/main/skills/figure-designer/SKILL.md) (CC BY 4.0), [neuromechanist figure-qa](https://github.com/neuromechanist/research-skills/blob/main/plugins/figures/skills/figure-qa/references/figure-qa-procedure.md), and [K-Dense scientific-visualization](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-visualization/SKILL.md). The instructions here are tailored to plot-paper's existing script and paper-wide style.
