# Subagent literature review

Use this reference only when independent research lanes justify delegation. The lead agent remains responsible for the scientific boundary and final synthesis.

## Decompose by evidence lane

Prefer lanes that can search independently, such as:

- distinct topics or subquestions;
- method or model families;
- theoretical, empirical, benchmark, or replication evidence;
- venue or time-period slices;
- supporting, conflicting, negative, or critical literature.

Do not assign several agents the same broad topic without a reason. Group small lanes together when coordination would cost more than the search.

Use direct workers when possible. Do not allow nested delegation unless the runtime explicitly supports and supervises it. Never exceed the runtime's available concurrency; queue remaining lanes.

## Prepare a self-contained task

Assume each worker sees no useful conversation history. Give every worker:

- the exact lane question and its boundary;
- shared inclusion/exclusion rules and date cutoff;
- web-first source policy and prohibited source classes;
- seed terms or papers without prescribing the answer;
- paper and time budget;
- evidence-status definitions;
- the required return schema below;
- the instruction to perform no writes or external mutations.

Workers search and report. They do not add to Zotero, edit shared files, draft the final review, or change the approved corpus.

## Required worker return

Each worker returns one compact packet:

1. `lane`: question and searched boundary;
2. `search_log`: sources, representative queries, date, and stopping reason;
3. `candidates`: for every paper, title, authors, year, DOI/arXiv ID, stable primary link, version, evidence status, relevance, and uncertainty;
4. `taxonomy`: method or concept clusters within the lane;
5. `contradictions`: conflicting, negative, or null evidence found;
6. `gaps`: missing evidence and the next search that might resolve it;
7. `blind_spots`: inaccessible sources, weak coverage, or likely terminology misses.

Require source URLs and identifiers. A worker's summary is not itself citable evidence.

## Lead-agent synthesis

After all available packets return, the lead agent:

1. records failed, timed-out, or missing lanes instead of silently dropping them;
2. resolves DOI, arXiv, accepted-manuscript, and publication-version lineages;
3. deduplicates centrally rather than asking workers to coordinate;
4. compares coverage and search quality across lanes;
5. identifies cross-lane overlaps, contradictions, and terminology mismatches;
6. checks load-bearing claims against primary sources at the required evidence level;
7. produces one prioritized reading list and one coverage statement.

Do not merge disagreements by majority vote or smooth them into consensus. Resolve against the source when possible; otherwise preserve the disagreement for the user.

## Selective independent reading

Use two independent readers only for a load-bearing paper whose interpretation would materially change the review, novelty assessment, or research decision. The readers must not see each other's notes. A separate lead or reviewer compares both against the source and records unresolved disagreements.

Do not double-read routine background papers. Parallelism is for context isolation and independent evidence gathering, not for multiplying confident paraphrases.

## Cost and stopping rules

- Prefer a small number of coherent lanes over one worker per paper.
- Stop spawning when remaining work is sequential, duplicative, or below the value of coordination.
- Apply the parent review's paper/time budget across workers; parallel execution does not expand scope.
- If a worker fails, retry only when that lane is load-bearing and a retry is proportionate. Otherwise mark the gap.
