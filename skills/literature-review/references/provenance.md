# Provenance and audit boundary

## Source

- Repository: `https://github.com/HughYau/AcademicForge`
- Branch: `site-first`
- Audited commit: `01b6d90c5b50ba0aa48b6564e45ee4a0ade9487c`
- Source path: `skills/claude-science/literature-review`
- Audit date: 2026-08-31

AcademicForge labels this collection as Anthropic Claude Science skills and the source file declares `Apache-2.0`. Anthropic's public Claude Science announcement confirms the product architecture, curated skills/connectors, specialist agents, reviewer agent, and Allen Institute review workflow, but does not publish or authenticate this repository's file contents. Treat this as an AcademicForge community copy adapted for local evaluation, not as verified production source from Anthropic.

The AcademicForge file history shows this skill introduced and later modified by the AcademicForge maintainer. One commit message states that kernel functions were changed to remove Claude Science host dependencies. This contradicts any claim that the checked-in bytes are demonstrably unmodified production files.

## Local hardening

- Adapted first as a local literature-review workflow, later separated into `literature-fast`, `literature-review`, and `doc-literature` responsibilities.
- Added the user's web-first evidence states, corpus lifecycle, advanced-review modes, and multi-topic subagent workflow.
- Restricted the current `literature-review` boundary to retrieval, verification, evidence mapping, and evidence-packet handoff; durable document structure now belongs to `doc-literature`.
- Removed fallback collection of `git config user.email`; contact email is opt-in only.
- Changed identifying User-Agent text from `ClaudeScience` to `Local`.
- Changed `crossref_lookup` to return several candidates because the top CrossRef result can be a later reprint or title collision.
- Reworded Claude Science-specific credential guidance for a cross-agent local environment.

No OpenAlex key is bundled or stored. OpenAlex-backed search and citation expansion remain unavailable until the user separately configures `OPENALEX_API_KEY`.

## Static audit

The bundled kernel uses Python standard-library HTTP calls to Crossref, doi.org, and OpenAlex. The audited source contained no file writes, package installation, deserialization, or secondary LLM API calls. Its only shell execution read `git config user.email`; that behavior was removed locally.
