---
name: explain-paper
description: Explain a research paper for understanding and selective personal reading. Map its framework, state the takeaways, then identify core passages and research-provoking remarks, experiments, or limitations. Use for paper explanation, guided reading, 解读论文, 导读, or 精读路线.
---

# Explain Paper

Help the user understand a paper before deciding what to read closely. Follow the requested language; when continuing a Chinese research conversation, explain in Chinese while preserving the paper's technical terms and notation. Unless the user requests a short summary, make the first explanation detailed and self-contained enough to understand the paper's formulation and argument. Do not defer the basic setup or the connections between formulas to a follow-up. A targeted follow-up answers the current question without repeating the whole guide.

## Inspect the source

Identify the paper and version from the supplied file, link, or citation; resolve a title or identifier against a primary paper page. Ask for a source only when none is usable or the paper cannot be identified. Read the source needed for the explanation and state any access or reading limit. An abstract or search snippet cannot establish an uninspected method, theorem, experiment, or remark.

## Default explanation

Start from the user's stated reading progress and what their questions show they understand. Cover expected results and standard steps briefly, keeping the definitions and assumptions needed to follow the argument. Spend more time where a result, assumption, or proof step changes what the reader would predict. Explain the plausible expectation, what actually happens, why, and what it changes. Use a small calculation or example when it resolves the surprise.

1. **Story and outline.** Explain the problem that motivates the paper, the limitation or obstacle it addresses, the key idea, and how the method and evidence support the main claim. Give a compact logical outline so the reader knows the role of each major part and how they connect; a table of contents or a slogan alone is insufficient.
2. **Framework.** Build the formulation before introducing specialized definitions or theorems: what is given or observed, what is unknown, what the learner or procedure can do, what it outputs, and how success is evaluated. Then explain the method or construction and its main results in that setup. Introduce notation incrementally, unpack important formulas in words, and use a small running example or derivation when abstraction would otherwise hide the mechanism. State which parts of learning or optimization are assumed solved and which are actually analyzed.
3. **Takeaways.** Distill the explanation into the few conclusions the reader should remember, usually one to three. Prioritize what changes their understanding or how they would use the result. Keep the assumptions and limits that matter to each conclusion.
4. **What to read personally.** Give two distinct groups: core content needed to understand the contribution; and interesting remarks, experimental findings, exceptions, or limitations that could prompt deeper research. For each selection, give an exact locator, why it is worth reading, and the question the user should bring to it. The reading route supplements the explanation; it does not replace explaining the central formulation and mechanism.

These are content requirements, not mandatory headings or a section-by-section paraphrase. Prefer enough connected explanation to establish understanding over a compressed first answer that forces the user to ask what the setup means.

For a full paper guide or a technically substantial explanation, read [references/reading-guide.md](references/reading-guide.md). Separate the paper's findings from the assistant's interpretations and possible research directions. An interesting limitation is not proof that a question is open or a proposed idea is novel.

## Deliver

Return the explanation in conversation unless the user requests a saved artifact. Prefer a focused reading route to an exhaustive checklist. Use literature skills for broader discovery and review-manuscript for a requested manuscript critique; this skill's purpose is understanding the supplied paper.
