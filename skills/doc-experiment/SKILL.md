---
name: doc-experiment
description: Create or revise a precise, reproducible experiment document covering implementation, environment, data, configurations, instrumentation, commands, artifacts, metrics, tests, failures, and exact results. Own the technical-report language for execution evidence, run comparison, debugging, and engineering acceptance; do not use for manuscript narrative or mathematical development.
---

# Experiment Document

Produce an evidence-backed record that another researcher can reproduce,
inspect, and extend.

When `$writing-research` is explicitly combined with this skill, use it as the general academic-writing baseline; this skill's provenance, exact-record, tense, failure-reporting, and technical-language rules override any conflicting general rule.

Follow the metadata, provenance, and notation contract below. These conventions
are part of the skill itself so they remain available after Skill Hub install.

## Metadata contract

Begin with these reader-visible fields when available:

```text
Title
Report type: experimental technical report
Project
Date and evidence cutoff
Repository / worktree / branch / commit
Data snapshot or manifest
Run identifiers and seeds
Artifact root
Technical status and reviewer decision
Supersedes / related mathematical report
```

Do not invent absent metadata. State a missing field and its reproducibility
impact when material.

## Provenance contract

- Record the exact working directory for every command.
- Record configuration files plus material overrides.
- Record model, data, and initialization seeds separately.
- Record dataset identity, split, preprocessing, and hash/manifest when
  available.
- Record hardware, precision, framework, package, and driver/runtime versions
  from run-time evidence rather than the current shell.
- Record W&B project, entity, and run ID when available without exposing
  credentials.
- Record artifact paths, row counts, schemas, and checksums.
- Identify the exact artifact version used for every headline result.

## Preserve provenance

Inspect actual source files, configurations, logs, commits, manifests, and
artifacts. Do not reconstruct technical details from memory when primary
evidence is available. Distinguish observed facts from inferred or missing
metadata.

## Required structure

Write these sections in order, omitting only inapplicable items:

1. **Objective and scope** — question, compared systems, exclusions, and
   success criteria.
2. **Repository state** — repository/worktree, branch, commit, relevant dirty
   changes, and project separation.
3. **Environment** — date, hardware, framework/package versions, accelerator,
   and relevant environment variables without secrets.
4. **Data and checkpoints** — source, split, preprocessing, sampling, shapes,
   identifiers, and exclusions.
5. **Implementation and instrumentation** — changed modules, telemetry,
   artifact schema, and behavior.
6. **Experimental design** — controls, variants, seeds, intervals, ablations,
   preregistered gates, and stopping rules.
7. **Commands and configuration** — exact runnable commands and complete
   material configuration.
8. **Metric definitions** — formula, units, aggregation, chance/control value,
   and direction of improvement.
9. **Results** — per-run values before aggregates; include failures and missing
   cells.
10. **Verification** — focused tests, smoke runs, artifact checks, independent
    review, and validation gaps.
11. **Failures and recovery** — failure, scientific impact, recovery action,
    and superseded artifacts.
12. **Reproduction recipe** — prerequisites, ordered commands, expected
    outputs, and checksums/locations.
13. **Technical conclusion and next execution step** — what is ready, blocked,
    and minimally required next.

## Report dimensions precisely

- Treat vectors as columns unless a source explicitly uses another convention.
- For \(D\in\mathbb{R}^{r\times c}\), define
  \(d_i=D_{i,:}^{\top}\in\mathbb{R}^{c}\) and \(X_{i,:}=x_i^{\top}\).
- At first use, state that \(XX^{\top}\in\mathbb{R}^{r\times r}\) is the row
  Gram matrix and \(X^{\top}X\in\mathbb{R}^{c\times c}\) is the column Gram
  matrix.
- State input/output shapes around transformations and telemetry.
- Define each metric's formula, units, aggregation level, independent unit,
  chance/control value, and direction of improvement. Move long theoretical
  derivations to a mathematical report.

## Separate evidence layers

Distinguish:

- code present versus code exercised;
- process completion versus artifact validity;
- unit/smoke tests versus full-scale experiments;
- descriptive analysis versus causal intervention;
- regenerated versus stale/superseded artifacts;
- reviewer approval versus an operational assumption.

Do not ingest, promote, or treat an incomplete artifact as accepted evidence.

## Write as an evidence record

- State observations before interpretations and label inferences explicitly.
- Use past tense for completed commands, runs, failures, and measurements; use present tense for stable definitions and artifact contents.
- Preserve exact configuration values, commands, paths, versions, result values, and material error messages.
- Keep prose concise and technical. Prefer an exact fact and locator over narrative buildup or evaluative adjectives.
- Do not smooth over missing cells, failed runs, stale artifacts, uncertainty, or contradictory evidence.
- Keep causal explanations separate from descriptive results unless an intervention or validated design supports them.
- Maintain the project's established terminology without inventing friendlier synonyms for precise implementation objects.

## Make the report reusable

- Use stable relative project paths where possible.
- Use compact tables for run matrices, configurations, and results.
- Quote only log lines needed to establish a fact.
- Record exact failure messages when they affect reproducibility.
- State omissions and their consequences.
- Keep the technical conclusion separate from the mathematical consensus.

## Audit before delivery

Verify:

- every number traces to an artifact or log;
- commands are runnable from the stated working directory;
- seed, split, checkpoint, and aggregation definitions are unambiguous;
- no secret or direct personal identifier is exposed;
- stale and current artifacts are not mixed;
- another researcher can identify both successful and failure paths.
