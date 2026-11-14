# Research Agent Skills

A collection of 19 skills for doing research with Codex and Claude Code. They
cover literature search, reading and explaining papers, mathematical research,
academic writing and review, figures, and research talks.

## Install

Clone this repository somewhere you plan to keep it, then run the following
from the clone:

```sh
git clone https://github.com/xiong-zx/skills.git
cd skills
```

Choose the client directories you want. This example links the full collection
into both clients and preserves any skills you already have under the same names.

```sh
for destination in "$HOME/.agents/skills" "$HOME/.claude/skills"; do
  mkdir -p "$destination"
  for source in "$PWD"/skills/*; do
    [ -f "$source/SKILL.md" ] || continue
    target="$destination/${source##*/}"
    if [ -e "$target" ] || [ -L "$target" ]; then
      printf 'Already exists: %s\n' "$target"
      continue
    fi
    ln -s "$source" "$target"
  done
done
```

Keep the bundles together in the clone because some skills link to their
siblings. Run `git pull` in the clone to update. Open a new session if a skill
does not appear. In Codex, use e.g. `$explain-paper`. In Claude Code, use
`/explain-paper`. See the [Codex skill guide][codex] and
[Claude Code skill guide][claude] for other discovery options.

## Skill catalog

| Goal | Skills |
| --- | --- |
| Search the literature | [literature-fast](skills/literature-fast/SKILL.md) builds a short reading list. [literature-review](skills/literature-review/SKILL.md) searches, verifies and organizes a larger body of work. [doc-literature](skills/doc-literature/SKILL.md) turns checked sources into a written review. |
| Understand a paper or project | [explain-paper](skills/explain-paper/SKILL.md) guides a close reading. [explain-literature](skills/explain-literature/SKILL.md) maps an existing collection. [explain-project](skills/explain-project/SKILL.md) explains the goal, progress and decisions. |
| Develop and run research | [research-brainstorm](skills/research-brainstorm/SKILL.md) develops and compares questions. [research-auto](skills/research-auto/SKILL.md) supervises authorized theory exploration and independent checks. [grill-me](skills/grill-me/SKILL.md) challenges a plan or idea in conversation. |
| Write and review research | [writing-research](skills/writing-research/SKILL.md) supports general academic prose and notes. [doc-paper](skills/doc-paper/SKILL.md) prepares submission papers. [review-manuscript](skills/review-manuscript/SKILL.md) audits a draft and polishes its language. |
| Develop math and document results | [doc-math](skills/doc-math/SKILL.md) develops definitions, statements and proofs. [doc-experiment](skills/doc-experiment/SKILL.md) records reproducible experiments. [plot-paper](skills/plot-paper/SKILL.md) prepares publication figures. |
| Prepare meetings and talks | [doc-meeting](skills/doc-meeting/SKILL.md) writes a technical pre-read. [doc-advisor-conversation](skills/doc-advisor-conversation/SKILL.md) prepares talking points. [doc-slides](skills/doc-slides/SKILL.md) makes research decks. [doc-script](skills/doc-script/SKILL.md) writes a speakable script. |

Each bundle starts at `SKILL.md`. Read its requirements before using optional
helpers. The literature-review helper reads `OPENALEX_API_KEY` from the
environment for OpenAlex calls. Figure and slide workflows may need Python
packages, a TeX engine, or PowerPoint, depending on the output.

## Sources and licenses

Source credits are recorded in the relevant bundles. The adapted
[literature-review bundle](skills/literature-review/SKILL.md) carries its
[Apache 2.0 license](skills/literature-review/LICENSE) and
[provenance notes](skills/literature-review/references/provenance.md).

[codex]: https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills
[claude]: https://code.claude.com/docs/en/skills#choose-where-skills-load
