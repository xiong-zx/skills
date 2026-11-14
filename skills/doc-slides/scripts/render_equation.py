#!/usr/bin/env python3
"""Render a trusted, self-contained, one-page LaTeX document to outlined SVG."""

import argparse
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import xml.etree.ElementTree as ET


def find_tool(name):
    found = shutil.which(name)
    mac_tex = Path('/Library/TeX/texbin') / name
    if found:
        return found
    if mac_tex.is_file():
        return str(mac_tex)
    raise RuntimeError(f'Missing {name}; configure an existing TeX installation first.')


def run(command, directory):
    result = subprocess.run(command, cwd=directory, capture_output=True, text=True, timeout=45)
    if result.returncode:
        detail = (result.stdout + result.stderr)[-5000:]
        raise RuntimeError(f'{Path(command[0]).name} failed:\n{detail}')


def render_equation(source, output):
    source = Path(source).resolve()
    output = Path(output).resolve()
    if source.suffix != '.tex' or output.suffix != '.svg':
        raise ValueError('Expected a complete .tex input and an .svg output.')
    content = source.read_bytes()
    saved_source = output.with_suffix('.tex')
    if output.exists() or (saved_source.exists() and saved_source != source):
        raise FileExistsError('Output SVG or matching source already exists; choose a new revision name.')
    latex, dvisvgm = find_tool('latex'), find_tool('dvisvgm')
    with tempfile.TemporaryDirectory(prefix='equation-render-') as directory:
        work = Path(directory)
        (work / 'equation.tex').write_bytes(content)
        run([latex, '-no-shell-escape', '-interaction=nonstopmode', '-halt-on-error',
             '-file-line-error', 'equation.tex'], work)
        run([dvisvgm, '--no-fonts', '--exact-bbox', '--bbox=1pt', '--cache=none',
             '--page=1-', '--output=render-%p.svg', 'equation.dvi'], work)
        pages = sorted(work.glob('render-*.svg'))
        if len(pages) != 1:
            raise ValueError(f'Expected one formula page, found {len(pages)}.')
        svg = pages[0].read_bytes()
        root = ET.fromstring(svg)
        if not root.tag.endswith('}svg') or not root.get('viewBox'):
            raise ValueError('Renderer did not produce a bounded SVG.')
        if not any(element.tag.endswith('}path') for element in root.iter()):
            raise ValueError('Rendered SVG has no outlined glyphs.')
        for element in root.iter():
            tag = element.tag.rsplit('}', 1)[-1]
            if tag in {'text', 'font', 'image', 'script', 'foreignObject'}:
                raise ValueError(f'Unexpected non-outline SVG element: {tag}')
            for key, value in element.attrib.items():
                if key.rsplit('}', 1)[-1] == 'href' and not value.startswith('#'):
                    raise ValueError('SVG references an external resource.')
        output.parent.mkdir(parents=True, exist_ok=True)
        # Exclusive creation protects existing project assets even on a concurrent run.
        if saved_source != source:
            with saved_source.open('xb') as handle:
                handle.write(content)
        with output.open('xb') as handle:
            handle.write(svg)
    return {'svg': str(output), 'source': str(saved_source),
            'width': root.get('width'), 'height': root.get('height'),
            'viewBox': root.get('viewBox')}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path, help='Trusted self-contained LaTeX document.')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    try:
        print(json.dumps(render_equation(args.source, args.output)))
    except (OSError, ValueError, RuntimeError, subprocess.TimeoutExpired) as error:
        parser.exit(1, f'Equation render failed: {error}\n')


if __name__ == '__main__':
    main()
