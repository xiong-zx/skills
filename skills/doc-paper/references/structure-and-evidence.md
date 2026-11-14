# Paper structure and evidence narrative

Choose sections for argumentative functions, not a fixed template. A paper normally needs a title/Abstract conveying the problem, answer, decisive evidence and material conditions; an Introduction establishing the exact gap and supported contributions; verified context/Related Work; a setting with objects, assumptions, information model and criterion; precise main results; methods/proofs/experiments that substantiate them; Discussion/Limitations; a Conclusion when it adds synthesis; and complete appendices/supplements for deferred load-bearing material.

## Keep one coherent argument

- Name sections for their actual content: a method section describes a method, an analysis section analyses it. Prefer an informative content summary such as "End-to-end convergence rate" to a bare result label such as "End-to-end stationarity." Subsection titles identify the particular question, construction or result rather than mechanically repeating standard labels.
- Explain a technical section's question and role when unclear. Transitions state actual relationships; they are not mandatory decorative bridges at every paragraph. Parallel tasks need no invented causal relation. For multi-level methods, distinguish learning/sampling from offline optimization before formulas.
- Treat the Abstract as a map: its mechanism, results, conditions and evidence need matching treatment in the body. When the technical content changes, update the Abstract. Keep the title, Abstract, Introduction, results and closing sections aligned at the same claim strength.
- Make the leading intellectual process visible early; a familiar supporting optimization/proof device must not displace it as the headline. When adaptive learning/data collection is central, explain how observations change the next sampling decision.
- Put component-specific interpretation/caveats beside their components; reserve closing discussion for the whole paper. Keep preliminaries to core concepts; routine optimality conditions and supporting derivations belong with the proofs that use them.
- Follow the shared conservative-revision rules when consolidating an existing draft: preserve effective prose, move/cut/merge passages before incidental paraphrase, and rewrite only the unit needed to resolve the problem.

Choose a drafting order from the most settled evidence. When the technical core is being refined, drafting setting/method/analysis/experiments first can help finalize the Introduction and Related Work against real content. Do not impose that order on an author choosing another workflow. An initially expansive draft is acceptable: distinguish established claims from pending results, then trim repetition and secondary branches. Put decisive methods, results and material conditions early enough to orient readers.

For outlines/titles/Introduction, use [argument-and-introduction.md](argument-and-introduction.md). For mathematical exposition and theorem-driven completeness, use the existing [shared paper standard](mathematical-exposition.md) and [theory-paper checks](theory-paper.md), not duplicate proof rules here.

## Related work

For this author, open a Related Work subsection with a short explanation of the research strands and comparison questions before citation-led comparisons. In a comparison paragraph, normally start with the closest relevant work and what it establishes, then end with the supported comparison to this paper. Explain the new perspective, information use or guarantee without manufacturing a criticism or erasing overlap to create a novelty story. A real obstacle can motivate the paper, but its scope must be fair.

## Experimental sections

Organize numerical sections around the central evaluation questions. Introduce each experiment with its question, problem/instance setting and compared variants before analysing a figure/table. Keep implementation, tuning and detailed execution choices in the appendix; the main setup gives instances/datasets, comparators and performance metrics. Refer to the methodology without redescribing implementation.

For this author, the main experimental narrative explains figures/tables displayed in the main paper. Move a central result's artifact into the main text, or keep its detailed analysis and artifact citation in the appendix; do not build main-text results around appendix-only figures/tables. Preserve important exceptions and keep the appendix's own evidence narrative coherent.

Put band definitions, error aggregation, resampling and significance conventions together in Setup's Metrics, with one corresponding definition block in the appendix. Captions identify plotted quantities, comparisons and marks rather than repeating statistical calculations. Apply writing-research's observation-then-synthesis pattern: explain what the displayed data show and what it means in the supported regime, grouping related data-level analyses before a shared higher-level conclusion.
