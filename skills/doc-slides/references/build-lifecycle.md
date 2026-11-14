# Build artifacts and cleanup

## Retain inputs, not build history

- Reuse the project's existing source/output locations. Keep one active deck, requested alternatives/previews, exact formula sources and current verified assets, maintained code, original data and explicit historical originals. Never overwrite manual edits by rerunning an old full builder.
- Work in one owned `.build/work/run-*` directory per attempt. Keep one verified last-good recovery point outside it; freeze recovery across failed/partial live edits. Protect any unique manual pre-edit input until the failure is resolved. Pinned originals are durable inputs, not rolling recovery or cache entries.
- After success, delete the run's candidate/preview-only PPTX, conversion PDF, redundant renders, extracted package trees and compiler debris. Do not retain extra `validated/color/final` copies or timestamped full logs. Retain one small last-success receipt.
- Current source-linked SVGs can be reused directly; do not maintain a second persistent copy. A requested preview set is also kept only once. Do not remove PPTX-internal vector/raster compatibility pairs.

## Generate less and reuse conservatively

- An ordinary text edit does not require a full rebuild or formula compilation. Regenerate only changed expressions. Render the affected slides; changes to a master, theme, fonts or global geometry can affect the whole deck. Audience/flow review remains [explicit-only](audience-review.md).
- The batch renderer is not a general dependency cache. Reuse current SVGs only when their exact source/helper provenance and intact bytes are verified and the trusted self-contained TeX's fixed rendering environment is known unchanged. Unknown dependencies or changed/unverified tools/fonts require rendering. Do not compile every unchanged equation just to compare outputs.
- Pass changed expressions to the batch helper in a run-specific output directory; merge their successful records into the durable current asset mapping, retaining unaffected records. Publish source/assets before updating the current deck/mapping. Do not replace a complete mapping with a changed-only subset or delete assets still referenced by any retained deck/recovery/pinned source.
- Do not add a preview cache until measurements justify it. For an optional reusable render, require saved-deck hash, renderer/context, slide/hidden-page mapping and resolution to match; an old PNG's presence is not a hit. Keep only current useful renders, not historical generations.
- Measure end-to-end waiting time and rendering time on copies for unchanged repetition, one formula edit and one ordinary text edit. Compare with/without retaining optional derived outputs. Delete cheap-to-regenerate outputs even if unique; retain expensive ones only for a measured benefit. No arbitrary capacity budget or general dependency/LRU service.

## Finish safely, then clean

File publication requires the target deck closed throughout publication, one writer, a fresh source hash and one staged candidate on the same filesystem. Make new source/asset bytes durable first without destroying the previous mapping, publish the checked deck and its mapping, and confirm that output hashes and all dependency locators agree. Interrupted/inconsistent publication preserves the run; it is not success.

For live MCP, resolve unsaved work, coordinate exclusive editing, target every call explicitly, save/read back authorized changes and inspect native previews. Do not replace an open deck from the filesystem or force quit PowerPoint. Failure preserves/fixes the last-good recovery and reports partial edits; do not rotate recovery from the partial current file.

Before deleting any run PPTX, use the available native document inventory to confirm that no presentation under that run is loaded in PowerPoint, matching full paths. A document can remain loaded after its OS file handle closes, so `lsof` alone is insufficient. If native loaded-document state cannot be confirmed, leave the run for later cleanup; never close unrelated documents or introduce a UI bridge to force a pass.

Use [build_run.py](../scripts/build_run.py) for owned runs. It does not perform editing, publish decks, rotate recovery, certify QA or garbage-collect sources. It validates a receipt and removes only explicitly listed generated files. Dry-run is the default; after successful validation and the native-inventory check above, `--apply` performs cleanup.

```sh
python3 scripts/build_run.py begin --build-root /path/to/project/.build
python3 scripts/build_run.py finish --run /path/to/project/.build/work/run-ID --receipt /path/to/project/.build/last-build.json
python3 scripts/build_run.py finish --run /path/to/project/.build/work/run-ID --receipt /path/to/project/.build/last-build.json --apply
```

Write the durable receipt after actual scoped checks and publication. Its minimal shape is:

```json
{
  "generator": "doc-slides", "schema_version": 1, "status": "verified",
  "output": {"path": "/durable/talk.pptx", "sha256": "actual hash"},
  "sources": [{"path": "/durable/current-mapping.json", "sha256": "actual hash"}],
  "checks": ["describe checks actually performed"],
  "generated": [{"path": "candidate.pptx", "sha256": "actual hash"}]
}
```

List every required source/asset and the current mapping in `sources`, not just a manifest that points at missing files. No source/output/receipt may live under `.build/work`. List every generated file relative to this run, excluding its ownership marker. The helper refuses changed hashes, unlisted files, symlinks and OS-observable open file descriptors. It does not query native in-memory documents; record that separate inventory check in `checks`. A receipt attests the agent's checks; it is not independent mathematical or visual verification. Coordinate one writer; filesystem checks are not a universal lock against manual edits.

On failure or interruption, keep necessary input snapshots, the candidate and useful diagnostics. Propose exact cleanup targets for old failed/unknown directories; do not retire them automatically by age. A cleanup warning does not invalidate a good deck. For read-only reviews, clean only the review's owned temporary exports after they are inspected/reported; do not mutate sources or create permanent recovery copies.

## Existing legacy directories

First inventory files/hashes and references. Move necessary inputs, unique code/data, retained originals and author-comment snapshots to durable locations; update live links and verify supported operations without the legacy build tree. Explicitly label historical one-time converters: do not claim they can regenerate a manually edited current deck. Then remove only reviewed, authorized disposable paths. Never apply the owned-run helper retroactively to an unclassified legacy `.build` tree.
