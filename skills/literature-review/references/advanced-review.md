# Advanced review modes

Read this reference only for evidence-map, review-draft, or systematic-review mode. Rapid triage should remain lightweight.

## Review contract

Record:

- research question, intended reader, and decision the review will support;
- retrieval cutoff and unit of analysis;
- inclusion and exclusion criteria;
- comparison axes and evidence-quality rules;
- allowed source classes and inaccessible databases;
- expected corpus and stopping or review budget.

Treat scope changes as amendments. Do not silently redefine the question after seeing results.

## Corpus lifecycle

Keep these states distinct:

1. `candidate`: discovered but not screened;
2. `screened`: title and abstract assessed with an inclusion decision and reason;
3. `approved`: included by the user or the declared protocol and available for evidence extraction;
4. `cited`: supports a specific synthesis claim with a locator.

Resolve DOI, arXiv, accepted-manuscript, and published-version relationships before counting studies. Record post-freeze additions and whether they change conclusions.

## Evidence ledger

For an approved corpus, keep one compact table with:

| Field | Meaning |
| --- | --- |
| `source_id` | Stable DOI, arXiv ID, or project identifier |
| `version` | Published/preprint version actually checked |
| `claim_id` | Atomic synthesis claim |
| `locator` | Page, section, theorem, table, figure, or appendix |
| `evidence` | What the source reports |
| `status` | Reported, derived, inferred, conflicting, or not disclosed |
| `limits` | Assumptions, population, benchmark, regime, or uncertainty |

Draft prose only after load-bearing claims have ledger entries. Absence of a disclosed detail is not evidence for a plausible reconstruction.

## Contradictions and gaps

For conflicting findings, compare before synthesizing:

- definitions and estimands;
- assumptions and mathematical regimes;
- populations, datasets, benchmarks, and baselines;
- method variants, hyperparameters, and publication versions;
- statistical power, uncertainty, and negative or null results.

Classify a gap as missing evidence, unresolved contradiction, limited regime, missing method comparison, or apparently unstudied within the stated search scope. Search directly for each candidate gap under alternative terminology before presenting it.

## Systematic-review assurance

A systematic label requires more than a search log. Record:

- explicit review profile and protocol;
- database and venue coverage;
- visible seed set and recovery check;
- backward and forward citation-search decisions;
- deduplication and screening reasons;
- corpus-freeze rule and amendments;
- stopping rationale based on marginal yield and residual omission risk;
- coverage blind spots and confidence limits.

Use PRISMA-style accounting only when the underlying counts and decisions were actually recorded. Structural consistency does not prove comprehensive recall or scientific validity.

## Human gates and artifacts

Require user confirmation before:

- upgrading rapid triage to review drafting or a systematic claim;
- freezing or materially expanding the approved corpus;
- writing to Zotero or another external system;
- changing a manuscript's scientific claims.

Prefer one evidence table and one review document for ordinary evidence-map work. Create a larger protocol/search/screening artifact pack only when a formal systematic review justifies the overhead.
