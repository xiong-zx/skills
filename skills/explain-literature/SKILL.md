---
name: explain-literature
description: Explain an existing research corpus through a clear taxonomy, literature map, assumption and information boundaries, and unresolved questions. Use for high-level literature understanding, 文献地图, 分类比较, or research positioning from known papers; not for new paper discovery or explaining one paper.
---

# Explain Literature

Help the user see what an existing body of work does, how its parts differ, and which parts of their question remain unsupported. Follow the requested language. Lead with the organizing idea and a compact map, then explain the decisive results and boundaries.

## Fix the source boundary

Use the supplied papers, prior conversation, project evidence tables, and authorized local notes. State the corpus and its retrieval cutoff separately from the date of this synthesis. Preserve versions, evidence levels and source locators.

Do not start a new literature search, refresh citation counts, expand citation graphs, or add remembered papers unless the user authorizes discovery. Missing information stays unknown. Reading already supplied local sources to resolve a classification is allowed; external source access must respect the user's current scope. A gap means a gap in the inspected corpus, not proof that nobody has studied it.

## Build a taxonomy before assigning papers

- Choose one primary dimension that serves the research question. State what it measures, the scope, and the unit being classified, such as a mechanism, a stage of a method, or an individual result. Keep independent dimensions such as observation type, geometry, and evidence strength as annotations or in a separate comparison.
- Give each top-level category a membership rule in terms of what the mechanism does or directly produces. Use categories at the same level of abstraction. Group papers that implement the same mechanism, even when their algorithms, assumptions, or names differ.
- Aim for distinct categories at the chosen unit and coverage of the stated corpus. Test neighboring categories with a borderline example. Add a category only if the same dimension reveals a substantive, source-supported distinction. Merge categories when the difference belongs on another axis. Leave insufficient evidence unassigned.
- Assign papers through their actual mechanisms. A hybrid can appear in several categories if the source supports each role. Name the stage or operation that earns each label. Carry assumption and guarantee differences within a category.
- Lead with a cross-paper conclusion for each category. Use representative papers to support it, and keep the main table at the category level.

For example, when classifying simulator-assisted optimization by what real feedback directly does, group gradient sliding, ProxyProx, and AuxMOM under correcting future optimizer updates. A check that accepts or rejects a candidate serves a separate purpose. Fitting a simulator or a reusable discrepancy model for later queries is a third purpose. For example, a gradient offset carried by the optimizer corrects updates, while a friction parameter fitted from real trajectories changes later simulator predictions. Scalar versus gradient feedback is an observation axis. A method that both corrects a local model and accepts or rejects a candidate can have both labels.

For stochastic-noise maps, read [references/noise-map.md](references/noise-map.md). Other topics should use their own substantive axes rather than inheriting this example's labels.

## Explain coverage and results

For each populated region, identify the common question, actual assumptions, representative existing works, result type, and main boundary. Put a source beside the supported claim and use available section/theorem/equation locators; never invent them.

Separate:

- source-reported theorems and their exact metric;
- model identities or approximations;
- empirical observations and their sampling limits;
- proposed explanations, conjectures and new research questions.

Do not rank incompatible guarantees as if they measured the same thing. Keep one-step improvement, final-iterate error, averaged-iterate stationarity, estimation error and local escape distinct. Record whether a result uses extra observations, known parameters, projections, averaging, clipping or a changed optimizer.

Use these coverage verdicts precisely: directly addressed; addressed under extra structure; adjacent result with a different target; not established in this corpus; unassessed because evidence is insufficient. Distinguish "a theorem applies" from "the theorem exploits this structure."

## Locate the user's question

State the precise intersection of assumptions, information restrictions, permitted algorithmic controls, and target metric. Compare it with the nearest occupied regions of the map. Explain what changes would make existing results applicable and what new implication is still needed.

When asked to split a research problem, read [references/problem-cards.md](references/problem-cards.md). Produce independently usable questions, not shorthand references to earlier cards. Include a feasible baseline and permit an impossibility result; do not prescribe a hoped-for theorem as if it were known.

## Deliver and self-check

Return the map and explanation in conversation unless a saved artifact is requested or required by the working context. Keep the main map small and put detailed source crosswalks after it. Give a short reading route based on the conceptual dependencies.

Before delivery, check that categories have stable meanings, each source classification has evidence, information available to the analyst is not silently given to the algorithm, general bounds are not mistaken for stronger structural assumptions, and every absence claim is corpus-bounded. Preserve the distinction between literature synthesis and independent proof auditing.
