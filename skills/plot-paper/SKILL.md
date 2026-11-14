---
name: plot-paper
description: Create or revise publication figures and figure sets for a research paper or appendix from recorded data. Use the paper's consistent style at final print size, check scientific fidelity and visual readability, and inspect figures in the compiled manuscript. Use doc-paper for paper organization or writing-research for surrounding prose.
---

# Paper Figures

Use [scripts/paperplot.py](scripts/paperplot.py), or a project copy, for the paper's reusable Matplotlib style. Keep the scientific claim, plotted data, and method identities traceable to their sources.

## Route the work

1. Identify the figure's question and evidence, recorded input data and statistic, author-approved method labels, and its intended place and width in the paper. Preserve the author's page plan.
2. Read [references/style-details.md](references/style-details.md) for the fixed paper style and chart-specific rules. For a new figure design, an aesthetic revision, or final visual review, also read [references/visual-design.md](references/visual-design.md). Read [references/figure-patterns.md](references/figure-patterns.md) only when an unfamiliar chart or layout needs a code example.
3. Draw from recorded analysis outputs. Keep method colour and line-style assignments stable across the paper; draw at the final printed width and include figures in LaTeX at their natural size.
4. Run paperplot.save and inspect the rendered PNGs, colour and optional grayscale contact sheets, and the relevant compiled manuscript pages. Fix meaningful visual obstacles, then recheck that data, scales, uncertainty, and claims remain accurate. For authored papers, centralize error-band/aggregation definitions in the corresponding Setup/Metrics and keep captions focused on identifying the plotted evidence; see the caption rules in style-details.

## Deliver

Save vector PDF, PNG, and the plotted numbers in CSV form. Record the plotting code, input paths and hashes, statistic, run and configuration choices, and any caption-relevant truncation, transformation, or uncertainty. Report what was visually checked and any unresolved issue.
