# Technical workflow

## Choose a route by operation

| Operation | Preferred route when available and verified | Boundary |
| --- | --- | --- |
| Read or locally adjust a deck open in PowerPoint | Direct local `ppt-mcp` over STDIO and macOS Apple Events | Needs the running application and automation consent; not a file-only library |
| Inspect actual PowerPoint rendering | PowerPoint-native export through MCP, then inspect the produced PDF/images | A success message, cached screenshot, or other renderer does not establish this |
| Generate a whole draft or perform a structured package edit | Available file-authoring tools with an explicit maintained entry point | Work on a copy and verify template, equations, and source freshness |
| Create or replace mathematical expressions | Verified native Office Math conversion or LaTeX-to-SVG pipeline | MCP control alone does not supply a mathematical typesetter |

Keep commands in the current Codex or Claude session when that is the requested workflow. A PowerPoint-sidebar AI is a different interaction model; do not substitute it without agreement. File and MCP routes may coexist, but must not write the same deck concurrently or maintain competing output authorities.

Use [build lifecycle](build-lifecycle.md) for run ownership, source/asset publication, frozen last-good recovery, measured reuse and success-only cleanup. Do not accumulate candidate/checked/final decks or multiple preview sets as permanent build history.

## Runtime and connection

The local control option is the community [ykuwai/ppt-mcp](https://github.com/ykuwai/ppt-mcp), not a Microsoft/OpenAI product. Its Mac backend uses Apple Events and does not require a separately maintained HTTP/WebSocket bridge or Office add-in. STDIO is launched by the client; a server process and dependencies still exist.

Use a reviewed, pinned installation in an isolated environment and register its executable with the intended clients. Codex, Claude Code, and Claude Desktop have separate configuration locations; sharing one installed executable does not synchronize those configurations or their permissions. Keep machine paths and client configuration out of this synced skill.

Inspect the connected server's actual tool list and schemas before constructing calls. Package installation, saved configuration, and successful MCP initialization are different checks. An already-running client may need to reload MCP configuration before tools appear; a direct protocol smoke test is not proof that its UI has reloaded.

macOS may request automation consent for the application that launches the server. Leave that decision to the user. Do not change global privacy/security settings, dismiss unrelated dialogs, restart the user's application, or force-close other documents to make a test pass.

## Live read/edit/preview sequence

1. Save or resolve existing unsaved work with the user. For first use, capability tests, or broad changes, snapshot the source hash and work on a named copy. Never use the original as the installation test target.
2. List open presentations. Open/activate the intended copy and verify its returned `full_name`, slide count, dimensions, and saved/read-only status.
3. Pass the returned full path as `presentation` on every presentation-bound call. A global activated target alone is insufficient when several chats or clients share access. If the named deck is unavailable, stop rather than falling back to another window.
4. Read only the relevant slides/shapes. In this backend slide indices are 1-based and geometry is in points; verify dimensions instead of copying pixel coordinates from a file renderer. Prefer inspected shape names and check for ambiguity.
5. Apply a small change, read it back, then save the named copy. For wording changes, prefer span replacement over replacing the entire text frame, which can discard run formatting. Do not use `ppt_set_text` on a structured equation as a math-editing shortcut.
6. Export/preview through PowerPoint. On Mac this server renders PowerPoint-exported PDF pages with Quartz. Inspect the images, not just their paths; verify page count and mapping when hidden slides or ranges are involved.
7. Save, close and reopen only the test/assigned copy when round-trip verification is needed. Re-read the edited object and check equations, figures, notes, and scientific content. Recheck the original hash after a copy-only test.

Call native tools serially. Across Codex, Claude Code, and Claude Desktop, use one active PowerPoint writer/operator at a time, even with separate MCP processes. Do not automatically enable dialog dismissal. Stop on permission, busy, or missing-target errors and report the actual state instead of repeatedly mutating or switching routes silently.

The Mac server stages exports inside PowerPoint's own container because Office's sandbox can reject writes elsewhere. Verify the actual saved/exported file and copy it to the requested output location only after success. Do not change the user's filesystem permissions or treat a reported success with no file as completion.

## Formula route and replacement gate

Use [equations](equations.md) for LaTeX source retention, vector assets, scale, and batch manifests. Preserve working native Office Math and its SVG compatibility representation rather than converting them to plain text or images during unrelated edits.

The inspected `ppt-mcp` 2.3.0 tool list has no dedicated LaTeX, OMML, or equation-generation/editing tool. A generic textbox, shape, or SVG-icon tool does not establish that capability. Its Mac SVG-icon route can rasterize artwork, so a `.svg` input is not proof that vector math is retained.

Keep the tested LaTeX-to-SVG helper, or a project-maintained LaTeX/Pandoc-to-OMML route with source-linked fallbacks, for unsupported equation operations. When using OMML, verify the equation object, its mathematical identity, and native PowerPoint display independently; another renderer may show the compatibility fallback with different metrics.

Retire a previous formula step only after its replacement demonstrates source-to-equation conversion, editing, exact source retention, correct native rendering, and save/reopen preservation for the structures the deck needs. Ordinary text editing, moving an equation box, or previewing existing math does not meet this gate. If only control and preview pass, keep formula creation on the existing route and document that division explicitly.

## File-authoring route

- Use the active environment's presentation tools for a new draft. Keep content, layout choices, formula specifications, and the maintained build entry point in the project rather than in disposable build history. Resolve runtime paths from the environment; do not hardcode another Mac's username or package-version directory.
- For an existing manually edited deck, the latest saved/in-memory file is authoritative. Do not rerun an old full builder over it. Use a narrow package edit on a fresh snapshot only when needed and authorized; preserve unrelated objects and relationships.
- Before a file-level replacement, require the target closed throughout publication, compare the source hash again, and stage the result separately. A hash cannot detect unsaved UI edits or prevent autosave races. Do not add automatic two-way synchronization or layer more ad hoc conversion steps over a broken build.
- Keep a native-equation deliverable separate from any preview-only fallback copy. Never replace the editable deck with the temporary rendering copy.

## Animation integrity and Repair warnings

- Deleting, replacing, regrouping or recreating a shape can leave animations
  pointing to its old ID. Update the affected animation sequence and build
  list together with the shape edit. Preserve intended reveals; do not remove
  all animations just to make a file open.
- After **every PPTX edit**, run the read-only shared checker on the exact
  final staged bytes, across all slides including hidden backups:

  ```sh
  python3 scripts/check_pptx_animation_targets.py /absolute/path/to/staged.pptx
  ```

  The path to the script is relative to this skill. Exit 0 means all checked
  animation/build-list shape references resolve within their own slide;
  exit 1 reports dangling targets, and exit 2 reports an unreadable package.
  Resolve failures in the writer before publishing. The checker selects the
  primary markup-compatibility branch; it is not a full OOXML schema validator
  or a substitute for native rendering.
- If the native application is available, verify the expected slide count,
  normal saved document identity and successful rendering. After structural
  edits, close/reopen only the assigned copy and verify that no Repair dialog
  or repaired/pathless document appears. An MCP Open success alone is
  insufficient: a pending repair dialog can accompany an incomplete count.
  If native validation is unavailable, report that limitation explicitly.
- A repair dialog is a failed check, not a routine export step. Keep the
  author input unchanged, diagnose on private copies, fix the generator and
  regenerate. Do not suppress warnings, enable automatic dialog dismissal or
  overwrite the author's file with a repaired copy as the workaround. Use
  computer control only within the user's authorization.
- Confirmed incident (2026-10-24, PowerPoint 16.114.1): deleting an
  initialization textbox left animation target 33 behind. A single-slide
  negative control reproduced Repair; rebuilding the sequence restored normal
  opening. A math-only control did **not** reproduce the warning. Preserve
  native math compatibility metadata, but do not misattribute this confirmed
  animation failure to equation markup or assume every Repair has this cause.

## Capability checks, not stability claims

For a new backend/version, test discovery, targeted reading, a small edit, native preview, save/reopen, and preservation of unrelated content on a disposable copy. Inspect a mathematical page and a quantitative-chart page. Record actual success, warnings, and unsupported operations; a short successful test is not a long-term reliability guarantee.

Mac limitations include unsupported tools and operations that recreate charts/paths via the clipboard, potentially losing animations. Check warnings before proceeding. Prefer in-place ordinary edits and keep untested chart, animation, SVG insertion, and equation-generation capabilities unclaimed.

### Observed validation: 2026-10-18

On a Mac with PowerPoint 16.114, pinned `ppt-mcp` 2.3.0 passed MCP discovery (156 tools), targeted reading, native previews, ordinary title-span replacement, save, close/reopen, and readback on an 18-slide test copy. Six representative pages were exported for visual inspection. The 30 native equations, 30 SVG assets, original artwork, and chart data survived the round trip; PowerPoint normalized mathematical Unicode and chart-number serialization. The original file's SHA-256 was unchanged.

The exported PDF contained 15 visible pages while the PPTX retained three hidden backups. This validates only the tested control/preview/local-edit operations, not equation creation/editing, arbitrary chart edits, long-term reliability, or another machine's client permissions. Preserve the existing formula route until the replacement gate above passes.

References: [server and Mac limitations](https://github.com/ykuwai/ppt-mcp#-macos-support), [Codex MCP configuration](https://developers.openai.com/codex/mcp), and [Microsoft Office Math](https://learn.microsoft.com/en-us/office/math/).
