# Explain mathematics and figures aloud

## Preserve the scientific contract

Recover definitions, claims and qualifications from the supplied authoritative material. Keep theorem, intuition, proof sketch, conjecture, observed result and illustration distinct. Never upgrade an average, expected, asymptotic, local or conditional statement into an unconditional or per-instance guarantee.

A spoken simplification can omit proof detail when appropriate, but must retain the conditions that determine what the claim means. Say the necessary restriction out loud, rather than relying on an unspoken note. If an omission would misrepresent the theorem, explain it briefly or flag a content/time conflict; do not silently change the theorem.

## Mathematics: explain what the objects do

Introduce the question an equation answers before asking the audience to parse it. Explain the important objects by their meaning, then guide attention to the term, dependency, regime or comparison that matters. Use notation verbally when the audience needs it; do not read every subscript, operator and parenthesis by default.

For example, if a supplied objective is F(x) = E[loss(x, Z)], a possible explanation is: "Here, x is the choice we control, and Z represents the randomness. We're trying to reduce the loss on average over that randomness." This says what the objective is; it does not imply that the expectation or a gradient is directly observable.

For a rate or bound, say which quantity is bounded, what changes, what is held fixed and the scope. A smaller upper bound does not establish a smaller measured error. Do not compare exponents while silently changing oracle access, sample/compute budget, norms or hidden conditions.

For a proof-focused audience, explain the claim, obstruction and role of the key argument, then provide the requested rigor. For a broader audience, intuition or a small example may carry more of the explanation. Do not universally remove proofs, prohibit equations or require all notation to be read aloud.

## Figures: orient, direct attention, interpret

Inspect the actual figure or rendered slide when available, rather than guessing from its filename. Identify only the axes, units, panels, traces and uncertainty needed for this audience. Explain what to look for before interpreting the pattern.

Direct attention to a verified feature: a crossing, gap, trend, region, comparison or counterexample. Use actual labels or positions; a color alone may be ambiguous. If builds or reveals hide part of the figure, match the speech to what is visible at that point.

State what the shown result supports and what it does not. Distinguish illustration/simulation/data, absolute/relative differences, aggregate/per-case results and correlation/mechanism. Explain an error band only if its meaning is known. Do not invent significance, measured values or a scientific explanation from appearance.

After the important feature, connect its meaning to the talk's question or next point. Do not narrate every curve or read a caption verbatim. Allow time for the audience to inspect the evidence; if the figure itself is unreadable, flag it for doc-slides rather than pretending prose solves it.

## Check against the supplied deck

Verify that each important object is introduced before use, pronouns still have audible antecedents, spoken comparisons match the slide, and removed details are not prerequisites later. If only an outline or extracted text is available, disclose unverified visuals/reveal order rather than claiming a rendered-deck check.

[MIT EECS and MIT's mathematical-communication course](sources.md) inform attention guidance and audience-appropriate intuition. The claim-preservation rules come from the user's requirements and existing research-writing conventions; they are not a claim that these sources validate the underlying mathematics.
