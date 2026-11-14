#!/usr/bin/env python3
"""Render a JSON list of trusted LaTeX files and index source-backed SVG assets."""

import argparse
import hashlib
import json
import math
from pathlib import Path
import re
import subprocess
import tempfile

from render_equation import render_equation


def render_batch(input_path, output_dir):
    input_path, output_dir = Path(input_path).resolve(), Path(output_dir).resolve()
    entries = json.loads(input_path.read_text())
    if not isinstance(entries, list) or not entries:
        raise ValueError('Expected a nonempty JSON array of equations.')
    index = output_dir / 'equations-manifest.json'
    if index == input_path:
        raise ValueError('Input list must not be the output manifest.')
    if index.exists():
        old = json.loads(index.read_text())
        if not isinstance(old, dict) or old.get('generator') != 'doc-slides' or old.get('schema_version') != 1:
            raise ValueError('Refusing to replace an unrelated manifest.')
    identifiers = set()
    for entry in entries:
        if not isinstance(entry, dict):
            raise ValueError('Each equation must be an object.')
        identifier = entry.get('id', '')
        if not isinstance(identifier, str) or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]*', identifier):
            raise ValueError('Equation id must contain only letters, digits, underscore or hyphen.')
        if identifier in identifiers:
            raise ValueError(f'Duplicate equation id: {identifier}')
        identifiers.add(identifier)
        if not isinstance(entry.get('source'), str):
            raise ValueError(f'{identifier}: source must be a .tex path.')
        if 'slides' in entry and not isinstance(entry['slides'], list):
            raise ValueError(f'{identifier}: slides must be a list of locators.')
        size = entry.get('source_font_pt')
        if size is not None and (isinstance(size, bool) or not isinstance(size, (int, float)) or not math.isfinite(size) or size <= 0):
            raise ValueError(f'{identifier}: source_font_pt must be positive and finite.')

    renderer_bytes = Path(__file__).with_name('render_equation.py').read_bytes()
    manifest = {'schema_version': 1, 'generator': 'doc-slides', 'equations': []}
    with tempfile.TemporaryDirectory(prefix='equation-batch-') as directory:
        staged = Path(directory)
        assets = staged / 'assets'
        for entry in entries:
            source = (input_path.parent / entry['source']).resolve()
            if source.suffix != '.tex':
                raise ValueError(f"{entry['id']}: source must be a .tex file.")
            content = source.read_bytes()
            digest = hashlib.sha256(content + b'\0' + renderer_bytes).hexdigest()
            snapshot = staged / f"{entry['id']}.tex"
            snapshot.write_bytes(content)
            stem = f"{entry['id']}-{digest[:16]}"
            result = render_equation(snapshot, assets / f'{stem}.svg')
            record = {'id': entry['id'], 'source': f'{stem}.tex', 'svg': f'{stem}.svg',
                      'render_digest': digest, 'width': result['width'],
                      'height': result['height'], 'viewBox': result['viewBox']}
            for key in ('slides', 'source_font_pt'):
                if key in entry:
                    record[key] = entry[key]
            manifest['equations'].append(record)
        # Validate all outputs before publishing. No existence-only cache reuse.
        for file in assets.iterdir():
            target = output_dir / file.name
            if target.is_symlink() or (target.exists() and target.read_bytes() != file.read_bytes()):
                raise FileExistsError(f'Existing asset differs: {target.name}; use a new output directory.')
        output_dir.mkdir(parents=True, exist_ok=True)
        for file in assets.iterdir():
            target = output_dir / file.name
            if not target.exists():
                with target.open('xb') as handle:
                    handle.write(file.read_bytes())
        # Atomically update this renderer's own index only after successful renders.
        with tempfile.NamedTemporaryFile(mode='w', dir=output_dir, suffix='.json', delete=False) as handle:
            temporary_index = Path(handle.name)
            json.dump(manifest, handle, indent=2, ensure_ascii=False)
            handle.write('\n')
        try:
            temporary_index.replace(index)
        finally:
            temporary_index.unlink(missing_ok=True)
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args()
    try:
        result = render_batch(args.input, args.output_dir)
    except (OSError, ValueError, RuntimeError, subprocess.TimeoutExpired) as error:
        parser.exit(1, f'Equation batch failed: {error}\n')
    print(f"Rendered {len(result['equations'])} equations; index: {args.output_dir / 'equations-manifest.json'}")


if __name__ == '__main__':
    main()
