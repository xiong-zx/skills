# Equation typesetting

## Representation and source

- Prioritize clear mathematical typography. For PPTX, LaTeX-rendered SVG is the default reusable route when no stricter editability requirement exists. Preserve the compilable `.tex` beside the SVG. A working native Office equation is also acceptable; require it when the user explicitly needs direct equation editing.
- Do not put raw LaTeX, Unicode substitutes, or manually positioned numerator/denominator/glyph text boxes on slides as a replacement for structured mathematics. Plain isolated variables and simple labels may remain text when they match the notation and read naturally.
- Treat inline relations, ranges, and constraints as mathematics too: for example, `1 < p \le 2`, `q \ge 1`, and `K=1` need the verified math route, not ordinary prose glyphs. Keep surrounding prose editable and align the math at a compatible physical size and baseline. Standalone variables in prose should follow the deck's mathematical styling, usually italic lowercase letters, without turning whole explanatory paragraphs into images.
- In compact explanatory chains, typeset `=>`, `<=>` and approximation as proper mathematical relations (for example, `\Rightarrow`, `\Leftrightarrow`, `\approx`) through the same verified math route. Keep adjacent words editable. Using a symbol to explain an analogy or tuning decision must not silently assert a stronger theorem.
- LaTeX input is not itself a rendered formula. Native Office Math must be converted into a real equation object; SVG is an image whose mathematical content is edited in its source and then regenerated. Do not describe SVG path editing as equation editability.
- For Beamer use native LaTeX mathematics; for HTML use a verified TeX renderer. Do not change the requested output format to avoid solving the PPTX equation problem.

## Recover exact mathematics

Use the approved outline, manuscript, or explicit user formula as authority. Expand project macros or include their definitions. Keep expectations, conditioning, subscripts, norm powers, domains, quantifiers, and asymptotic exponents unchanged. A rendered view or flattened text extraction can lose grouping: if the source is ambiguous, resolve it before conversion.

For a mathematical proposition, retain the assumptions needed to interpret it; move supporting proof details to speaker notes or backup slides rather than strengthening the claim.

For an important nontrivial equation, provide a brief indication of what it describes and which term or relationship matters. Put this on the slide or in the planned spoken explanation as appropriate. Do not read every symbol aloud, invent an interpretation, or add redundant glosses to obvious labels.

## LaTeX to SVG

The bundled Python standard-library helper uses installed `latex` and `dvisvgm`, with `standalone`, `amsmath`, `amssymb`, `lmodern`, and `xcolor`. It does not install TeX. Check dependencies first; on macOS TeX tools may be in `/Library/TeX/texbin` rather than the current PATH.

1. Copy `assets/equation.tex` to the project and replace its illustrative expression. The input is a complete, trusted, self-contained one-page document, not a raw math string. Keep definitions and color in this source; no private machine paths.
2. Run the helper, resolving its path from this skill:

   ```sh
   python3 scripts/render_equation.py expression.tex --output figures/equations/eq-01.svg
   ```

3. The output SVG has outlined glyphs and no external fonts/images. Its matching `.tex` is the exact input snapshot. Existing outputs are not overwritten; use a new revision name when updating an asset. The helper rejects failed compilation and multiple pages instead of returning a partial formula.
4. Embed the actual SVG as a vector asset. Use contain/aspect-preserving sizing and transparent background. Do not replace it with a screenshot or let an image-generation model redraw it.
5. Verify the final PPTX still embeds SVG, rather than only a raster preview. A PNG compatibility fallback alongside SVG is acceptable. If the exporter cannot preserve SVG, report the limitation and use a verified native-math/vector route; do not claim a raster-only result meets the vector requirement.

TeX is executable input. Compile only reviewed/trusted sources, with shell escape disabled and within the authorized workspace. These flags are not a security sandbox for arbitrary downloaded TeX.

## Manage several equations

For a formula-heavy deck, use a small formula list rather than tracking assets by memory. A JSON array can contain `id`, `source` (a complete `.tex`, relative to the JSON file), and optional `slides` and `source_font_pt`. Stable IDs locate the formula; they do not prove that its rendered file is current.

```json
[{"id":"update","source":"update.tex","slides":[3],"source_font_pt":10}]
```

Run `python3 scripts/render_equations.py equations.json --output-dir figures/equations`. It uses the single-equation renderer, retains the exact source, and writes `equations-manifest.json` with source/SVG locators, dimensions, and a digest of source plus renderer. This first version rerenders inputs on each run instead of maintaining a cache. Changed source, macros, or color produce a new content-addressed asset; it never assumes an existing filename means a current equation. Existing different asset bytes are not overwritten, and failed compilation does not replace the manifest. Old revisions are not deleted automatically.

Keep the declared source font size consistent with the actual TeX. It is sizing metadata, not an automatically verified font measurement. Use it with the asset dimensions to maintain a common mathematical scale rather than setting every formula to the same box height.

For an incremental edit, follow [build lifecycle](build-lifecycle.md): reuse verified unchanged current assets under the known fixed rendering environment, render only changed expressions in the owned run, and merge their records into the durable complete mapping. This helper still renders every input it is given; do not pass the full unchanged list to simulate a cache. Do not automatically prune old source assets referenced by other retained decks or recovery points.

The formula-list/manifest approach is selectively inspired by [Noi1r's formula pipeline](https://github.com/Noi1r/powerpoint-skill/blob/main/powerpoint-slides/formula-rendering.md); the bundled implementation is independently written. Plain-text failure fallback and existence-only cache reuse are not adopted.

## Sizing and layout

- Use one coherent mathematical font and scale. Render upright operators such as `\log`, `\exp`, and `\operatorname{Var}` correctly; maintain the intended distinction between scalar, vector, matrix, and blackboard-bold notation.
- Preserve full-size fractions, scalable delimiters, accents, matrix alignment, and multi-line alignment. Align related derivation lines at the relation sign, and do not stretch SVG independently in width and height.
- Choose final physical equation size, not merely a bounding-box height. Short and tall expressions at the same scale must have comparable glyph sizes. Check nested indices and exponents at presentation size.
- Split a long derivation into meaningful steps or slides before shrinking it. Prefer a short label, highlighting, or spoken explanation over dense explanatory text inside the formula.
- For inline SVG, inspect baseline and spacing against adjacent prose; when that becomes fragile, move the expression to a separate display line. Do not reconstruct a fraction as separate editable text boxes.

## Verification and handoff

Pilot the structures actually used: simple update, nested fraction or rate exponent, expectation/norm, and any matrix, cases, or aligned expression. Inspect both the SVG and an exported slide. Check mathematical identity against source and visual appearance separately.

Keep sources, matching assets, and a small slide-to-equation locator in the existing deck source or asset index. Regenerate from source after edits. Add meaningful alt text or a readable formula transcript when supported; path outlines alone do not provide semantic math accessibility.

Engineering references: [dvisvgm manual](https://dvisvgm.de/Manpage/) for outlined glyphs and bounding boxes; [Microsoft SVG support](https://support.microsoft.com/en-us/office/graphics-visuals/edit-svg-images-in-microsoft-365); [Microsoft Office Math](https://learn.microsoft.com/en-us/office/math/) and [LaTeX conversion](https://learn.microsoft.com/en-us/office/math/latex). Check the target version rather than promising universal cross-application behavior.
