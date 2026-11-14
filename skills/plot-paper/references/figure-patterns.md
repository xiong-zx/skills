# Paper figure code examples

Use this reference only when a requested chart or panel layout needs an example beyond paperplot.py. The linked figures4papers scripts are project-specific Matplotlib code, not a shared library. Inspect the nearest actual script, then write a project-local script that reads this paper's recorded outputs and uses the method registry, fixed panel sizes, and visual check in plot-paper.

| Need | Example to inspect | What can transfer |
|---|---|---|
| Several categorical comparisons with a large shared legend | [Cflows trajectory comparison](https://github.com/ChenLiu-1996/figures4papers/blob/main/figure_Cflows/plot_comparison_Trajectory.py) | Panel grouping and a legend-only subplot when the usual legend band will not fit. |
| Annotated grouped bars | [ImmunoStruct bars](https://github.com/ChenLiu-1996/figures4papers/blob/main/figure_ImmunoStruct/plot_bars.py) | Bar placement and selective value labels; use paperplot.grouped_bars for the method colours and zero baseline. |
| Trends or heatmaps | [figures4papers demo index](https://github.com/ChenLiu-1996/figures4papers/blob/main/scientific-figure-making/references/demos.md) | Choose the closest script by data geometry, then adapt its layout rather than forcing a bar or curve. |

Do not copy example arrays, scientific claims, author-specific labels, palette, very wide canvas dimensions, or automatically tightened y-limits into a new paper. Determine the figure's width from the target manuscript and inspect labels at that final size. The [figures4papers API page](https://github.com/ChenLiu-1996/figures4papers/blob/main/scientific-figure-making/references/api.md) specifies helper signatures but does not ship their shared implementation; use the actual figure_* scripts for code examples.

The examples are from [Chen Liu's figures4papers](https://github.com/ChenLiu-1996/figures4papers), whose repository [license is CC BY-NC 4.0](https://github.com/ChenLiu-1996/figures4papers/blob/main/LICENSE). Record the exact source and observe its license when adapting code. The guidance above summarizes patterns in original wording; no source script is bundled with plot-paper.
