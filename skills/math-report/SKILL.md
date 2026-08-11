---
name: math-report
description: Write or revise a formula-first mathematical analysis report that explains a scientific claim, derives identities or null expectations, connects empirical measurements to theory, and states a plain-language consensus. Use for mathematical analysis, theoretical interpretation, formula-based explanation, hypothesis comparison, or a scientific consensus report rather than implementation and experiment-operations detail.
---

# Mathematical Analysis Report

Produce a self-contained mathematical argument that a reader can audit without
reading code, worker logs, or experiment orchestration history.

Follow the metadata, notation, and evidence contract below. These conventions
are part of the skill itself so they remain available after Skill Hub install.

## Metadata contract

Begin with these reader-visible fields when the information exists:

```text
Title
Report type: mathematical analysis
Project
Date
Scope / evidence cutoff
Scientific status: exploratory, descriptive, accepted, rejected, or unresolved
Supersedes / related technical report
```

Do not invent missing metadata. Mark consequential missing fields explicitly.

## Notation contract

- Treat every vector as a column vector unless the source explicitly states
  otherwise.
- For \(D\in\mathbb{R}^{r\times c}\), write its \(i\)-th row as the column
  vector \(d_i=D_{i,:}^{\top}\in\mathbb{R}^{c}\).
- Define \(x_i=d_i/\lVert d_i\rVert_2\) and set
  \(X_{i,:}=x_i^{\top}\). Do not vertically stack column vectors while
  silently treating them as rows.
- State Gram dimensions at first use:
  \(XX^{\top}\in\mathbb{R}^{r\times r}\) is the row Gram matrix, while
  \(X^{\top}X\in\mathbb{R}^{c\times c}\) is the column Gram matrix.
- Use \(\lVert\cdot\rVert_2\) for vector Euclidean norm and
  \(\lVert\cdot\rVert_F\) for Frobenius norm.
- Distinguish \(\mathbb{E}_{H_0}[T]\), a null expectation, from
  \(\widehat T\), an empirical estimate.
- State whether off-diagonal sums use \(i\ne j\) or \(i<j\), and give null
  values in the same units and normalization as observations.
- Put a short verbal interpretation immediately after each load-bearing
  displayed equation.

## Build the argument

Write these sections in order, omitting only sections that do not apply:

1. **Question and consensus** — answer the scientific question in plain
   language before details.
2. **Objects and definitions** — define variables, dimensions, normalization,
   metrics, and units.
3. **Assumptions or null model** — identify what is assumed, derived, and
   empirical.
4. **Derivation** — show enough intermediate algebra to audit the result.
   Explain each displayed equation immediately afterward.
5. **Observable predictions** — translate theory into measured quantities.
6. **Empirical evidence** — report estimates, seed variation, and relevant
   null/control values.
7. **Hypothesis comparison** — mark each original claim supported, rejected,
   or unidentified, with a reason.
8. **Final consensus and open question** — state the strongest justified
   conclusion and the minimal unresolved causal or mathematical question.

## Separate kinds of statements

Distinguish:

- an algebraic identity or theorem;
- an expectation under a stated null;
- an empirical measurement;
- an interpretation combining theory and measurement;
- a conjecture or unresolved causal claim.

Never present an empirical regularity as a theorem or a descriptive subspace as
a causal mechanism.

## Make metrics interpretable

- Give the formula, summation domain, normalization, and random/chance value.
- Explain why the metric is used. For RMS, explain that squaring prevents
  positive and negative correlations from cancelling.
- Convert normalized ratios to an intuitive scale where possible.
- Translate statements such as “3/6 passed” into the actual grouping and
  scientific meaning.
- Replace “strong,” “near-null,” “gate failed,” and similar labels with
  numerical values and an operational interpretation.

## Keep the report mathematical

Exclude worker IDs, dispatch history, contract status, Git mechanics, file
recovery, and validation plumbing unless they change the mathematical validity
of the evidence. Put those details in a technical report.

Use tables only for compact hypothesis-to-evidence mappings. Prefer equations
and prose for the central reasoning.

## Audit before delivery

Verify:

- every vector convention and transpose is consistent;
- every matrix multiplication has compatible dimensions;
- every denominator and summation range is explicit;
- finite-sample observations are not confused with expectations;
- null, control, and observed values use the same normalization;
- the final consensus is understandable without internal project terminology.

End by listing supported, rejected, and unresolved statements, followed by the
minimal discriminating next experiment when one is needed.
