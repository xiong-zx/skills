# Independent paper audit

Read this for a full or evidence-focused submission-paper review. Review the manuscript actually supplied, not a stronger paper the reviewer wishes had been written. The review is independent of the writing skill's own readiness check.

## Fix the scope and evidence

- Record the target venue and paper type when known, the authoritative version, appendices, figures, tables, references, and any available protocol, data, code, or run record. State what could not be read. Not reported in a paper does not prove a procedure was not performed.
- For editable local sources, record source paths and start/end SHA-256 hashes, including the bibliography when it is part of the review. If a file changes, compare the reviewed scope and report which version and line numbers the findings describe; do not carry a verdict to the live version without checking the relevant differences. If the requested source is unavailable, request it rather than substituting an older snapshot or project note.
- Build a short map of headline claims before judging them. For each central claim, locate the supporting theorem, proof, figure, table, experiment, or exact external result; check the quantity, comparator, setting, assumptions, magnitude, uncertainty, and cost or feedback unit. Mark support as verified, partially checked, unavailable, or contradicted. An expected result is a target to assess, not permission to strengthen the claim.
- Separate evidence visible in the manuscript from external verification. Check novelty or load-bearing literature claims against opened primary sources when authorized and needed; a title match, abstract snippet, or failed search does not establish a technical comparison or global novelty.
- For an independent correctness audit, inspect the manuscript's own assumptions and proof before consulting previous audits or research notes. A conclusion obtainable by another route still has a manuscript proof gap if the written argument omits a necessary step. Verify imported results against their actual domains, parameters, normalization conventions and quantifiers.

## Challenge the paper proportionately

- For theoretical claims, inspect whether the stated result, proof dependencies, algorithm contract, and cost accounting align. When relevant, distinguish concentration at a fixed candidate from an adaptive, all-candidate event; value accuracy from gradient accuracy; sample counts from deployment or iteration counts; and local solver success from a required global function-value gap. Check the transfer to the claimed true-objective metric, the output or averaging sequence, and the conversion from a rate to a sufficient budget. Do not call an uninspected proof verified. Route a disputed mathematical implication to a proof-audit workflow.
- For empirical claims, examine the inference unit, baseline comparability, tuning and holdout separation, metrics, uncertainty, negative results, and whether ablations isolate the claimed mechanism. Compare text, tables, figures, captions, and supplements; visual polish cannot validate the plotted statistic.
- Assess whether method and experiment records permit the central result to be checked or reproduced. Missing code or a missing detail is a reporting gap; it is not proof of faulty execution. Do not claim reproduction unless the authorized analysis was actually rerun.
- At finalization, verify current venue instructions for length, anonymity, citations, figures, and supplements. Distinguish a local compile or checklist pass from submission readiness.
- For an unpublished manuscript supplied by someone other than the author, respect the controlling review and confidentiality policy before external searches or sharing manuscript content.

## Return actionable findings

- Prioritize a blocker only when a central claim lacks required support or a material contradiction prevents a defensible interpretation; major findings materially affect interpretation or reproducibility; minor findings are localized. Aesthetic preference alone is not a scientific blocker.
- State each finding as location, observation, evidence or missing check, consequence, and proportionate action. For source-level theoretical findings, identify the failing step and affected later claims, with precise line numbers for the reviewed version and the smallest supported correction. Preserve existing labels, macros and citation relationships in proposed local replacements. Offer a narrower claim, clarification, sensitivity check, or limitation when that resolves the issue more honestly than demanding a new study.
- When correctness is in scope, give a verdict per major claim, distinguishing supported, conditional, proof gap and incorrect. Conclude by separating what the manuscript already proves, what may be true but is not proved there, and what was not checked. A language-only review does not earn a mathematical verification verdict.
- Report review coverage and confidence, including specialist checks not done. Give the author a concise list of strengths worth preserving and the highest-leverage fixes. Do not invent an editorial decision, acceptance probability, score, or proof of novelty.

Adapted as original guidance from [K-Dense peer-review](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/peer-review/SKILL.md) and [pre-submission-reviewer](https://github.com/HKUSTDial/Supervisor-Skills/blob/main/skills/pre-submission-reviewer/SKILL.md). Their heavy intake tooling, fixed scorecards, and mechanical language bans are not adopted.
