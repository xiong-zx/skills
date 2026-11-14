# Paper figure style and scientific constraints

Apply this paper-wide style when using paperplot.py. Read the target venue's style file for its actual column and text widths; the values below are starting points, not a substitute for the live template.

## Figure contract and chart choice

- Know the claim each figure supports, its data source, statistic, uncertainty, and intended place in the main text or appendix. Draw from recorded analysis outputs, never numbers typed into a plotting script for convenience.
- Choose a curve for progress, a dot or dumbbell for comparisons across settings, a grouped or stacked bar for a few categorical counts, and a contour for paths on a 2-D landscape. Reuse the same chart type when two experiments ask the same question.
- Distinguish missing, zero, excluded, and censored observations. Do not interpolate or smooth missing data to make a curve look continuous unless a documented analysis justifies that transformation.

## Printed size and typography

| Venue | One column | Full text width |
|---|---|---|
| AISTATS, ICML (two columns) | 3.25 in | 6.75 in |
| NeurIPS, ICLR (one column) | 5.5 in | 5.5 in |

Confirm these widths from the manuscript's style file and the author's page plan. Draw each figure at the width it will occupy; include it in LaTeX at natural size without a width override or resizebox. Constrained layout places axes inside that fixed size, and paperplot.save checks for text leaving the canvas.

| Use | Width | Typical height |
|---|---|---|
| main-text grid, 2 x 2 | column | 3.0–3.2 in with a two-row legend |
| main-text pair of panels | column | 1.8–2.0 in |
| two side-by-side subfigures in one column | 1.6 in each | 2.0 in |
| appendix row of 3 to 5 panels | text width | 2.2–2.5 in |
| appendix grid (2 x 3, 4 x 3) | text width | 2.15 in per row |

Use sans-serif type (Helvetica, then Arial, then DejaVu Sans), with mathematics in the same face. At printed size, labels and short panel titles are about 8 pt, ticks and legends about 7 pt, and landmark notes about 6.5 pt. A title distinguishes panels; the full description, statistic, and caveats belong in the caption. Shorten a title that overruns a narrow panel rather than shrinking every label.

## Method identities, colour, and legends

Register a method's label, colour, and line style once per paper. Keep them identical in the main text and appendix. Ours is the single saturated highlight, drawn above baselines without a thicker line; baselines are muted and grouped by family. One colour cannot name two methods.

| Role | Colours | Line style |
|---|---|---|
| ours | #D55E00 (vermillion) | solid |
| baseline family 1 | #0072B2, #56B4E9, #1B3F8B | solid |
| baseline family 2 | #009E73, #5CC8A8, #00674B | dashed (4, 1.6) |
| one-off baseline | #CC79A7 | dash-dot |
| controls | #737373, #ABABAB | solid, dashed, dotted |
| variants of ours | #D55E00 dashed or dotted; ordinal ramp #F2A365, #D55E00, #953A05, #4A1C02; grey #8C8C8C for off | follow variant meaning |
| reference lines | #8A8A8A | dotted target or dashed level |
| landscape outcomes | #2C7FB8 low, #7FCDBB middle, #EDF8B1 high, white other | distinct from method paths |

The highlight has protan/deutan separation of at least ΔE 10 from listed colours in the previous dataviz check; the closest cross-family pair (#CC79A7 versus #009E73, ΔE 7.6) also differs in line style. Shades within a family are intentionally related and differ in lightness. Recheck any new colour against the rendered background and in grayscale; colour alone must not carry a comparison.

Order legend entries by method family, one family per row through paperplot.legend. Use one shared legend when panels show the same methods. When legends differ, save separate panels for LaTeX layout; an empty grid cell can hold a long legend. Keep labels short enough to fit without reducing the figure's type below print size.

## Curves, bars, and contours

- Progress curves use samples N or deployments/iterations T on the x-axis and the quantity of interest on y. Use mathematical notation such as F(x_t), estimated F(x_t), or F(x_t) − F⋆ where defined. Avoid dual y-axes. Panels in one row showing the same quantity share a y range.
- Use one line width for all methods. Show a computed 95% confidence band at low opacity (about 0.15) when relevant and legible. Define its computation and sampling unit centrally in the corresponding Setup/Metrics; give a run count where it is needed to identify the displayed data. Do not invent a band from a lone trajectory.
- A curve keeps one configuration across its sequence; it may summarize several recorded runs when the statistic is named. Never splice per-budget configurations into one line; use tables for per-budget comparisons. Interpolate a crossing mark in the axes' scale so it lies on the drawn segment.
- Show each curve's trend. Do not leave a method visible only for a short stretch or let it leave and re-enter the axes. Widen the range, choose a justified log scale, or omit the method with an explanation. Truncate progress only where at least one method, ideally ours, has reached its stationary level; disclose earlier data limits.
- A single-run panel uses a run fixed in advance or selected by a stated rule, never by eye. Show all runs' outcomes elsewhere and name the rule in the caption.
- Grouped bars include zero because length encodes magnitude. Use paperplot.grouped_bars for a few categorical comparisons, keeping the method registry and stable hatches when grayscale separation is poor. Prefer dots when differences lie in a narrow nonzero range.
- Contours use a light blue-green-yellow fill (valleys blue, hills pale yellow) covering the lowest band, with dense thin grey level lines. Add levels around each local minimum so closed rings remain visible. Hollow haloed landmarks sit above the paths without hiding endpoints; case an overlapping lower path with a wide light band. For a path too dense to read, use faint points.

## Check, caption, and deliver

paperplot.save checks canvas bounds, colliding tick labels, and data curves that are mostly outside the axes or leave and re-enter. Run it before inspecting PNGs. Inspect every figure at final size and in compiled manuscript pages; [visual-design.md](visual-design.md) guides the aesthetic and scientific visual review.

For this author, band definitions, error computations, resampling units, aggregation and significance conventions are stated once in the main Setup/Metrics and once in the appendix Setup/Metrics. Identify there any figures using different summaries, such as interquartile bands or implementation uncertainty rather than bootstrap intervals. Captions identify the quantity, comparator, problem/instance, necessary run count, marks/reference lines and log or clipped axes; do not repeat statistical calculations or band methodology. Keep a selection rule with its reproducibility explanation and make its location clear. The caption and text must describe the same comparison the figure actually draws.

A main-text table follows the page plan and normally fits one column. Use fewer decimals when differences permit, concise two-level headers, and restrained spacing or font changes before scaling. Compile to check overfull boxes. Explain best-entry and significance marks in the caption.

Save vector PDF and PNG, plus a CSV of plotted numbers. Record plotting code revision, input paths and hashes, and caption-relevant transformations, truncations, configurations, or selection rules. A clean render establishes visual and mechanical properties, not the scientific correctness of the underlying analysis.
