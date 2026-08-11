# MetaBot Personal Skills

This private repository is the source of truth for personal MetaBot Skills that
do not belong in the public MetaBot product repository.

## Bundles

- `metabot-todos`: reads and validates canonical ToDos under `/imac/todo`.
- `math-report`: produces formula-first mathematical analysis reports.
- `tech-report`: produces reproducible experimental technical reports.

Each directory under `skills/` is a complete Skill bundle. Edit and review the
Git-tracked bundle first, then publish it to Skill Hub:

```bash
metabot skills publish <name> --from skills/<name> --visibility published
```

Install into a review directory before enabling engine discovery:

```bash
metabot skills install <name>
metabot skills install <name> --to ~/.codex/skills/<name> --trust
metabot skills install <name> --to ~/.agents/skills/<name> --trust
```

The Git repository is authoritative; Skill Hub is the distribution layer, and
the global engine directories are installed copies. Do not edit installed
copies directly.
