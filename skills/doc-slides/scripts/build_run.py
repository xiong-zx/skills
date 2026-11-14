#!/usr/bin/env python3
"""Create an owned slide-build run; clean it only after a verified receipt."""

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def regular(path):
    path = Path(path).absolute()
    if any(p.is_symlink() for p in (path, *path.parents)) or not path.is_file():
        raise ValueError(f'Expected a regular, non-symlink file: {path}')
    return path.resolve()


def begin(build_root):
    root = Path(build_root).absolute()
    if root.name != '.build' or any(p.is_symlink() for p in (root, *root.parents)):
        raise ValueError('Use a non-symlink project .build directory.')
    work = root / 'work'
    work.mkdir(parents=True, exist_ok=True)
    if work.is_symlink():
        raise ValueError('The work directory must not be a symlink.')
    run = Path(tempfile.mkdtemp(prefix='run-', dir=work))
    (run / 'run.json').write_text(json.dumps({
        'generator': 'doc-slides', 'schema_version': 1, 'run': str(run.resolve()),
    }) + '\n')
    return run


def finish(run, receipt_path, apply=False):
    run = Path(run).absolute()
    if (run.parent.name != 'work' or run.parent.parent.name != '.build'
            or not run.name.startswith('run-')
            or any(p.is_symlink() for p in (run, *run.parents))):
        raise ValueError('Expected a managed .build/work/run-* directory.')
    run = run.resolve()
    marker = regular(run / 'run.json')
    owner = json.loads(marker.read_text())
    if owner != {'generator': 'doc-slides', 'schema_version': 1, 'run': str(run)}:
        raise ValueError('Unrecognized run ownership marker.')
    receipt_path = regular(receipt_path)
    if receipt_path.is_relative_to(run.parent):
        raise ValueError('Keep the success receipt outside all work directories.')
    receipt = json.loads(receipt_path.read_text())
    if (receipt.get('generator') != 'doc-slides' or receipt.get('schema_version') != 1
            or receipt.get('status') != 'verified'
            or not isinstance(receipt.get('checks'), list) or not receipt['checks']):
        raise ValueError('A verified receipt with actual checks is required.')
    records = [receipt['output'], *receipt.get('sources', [])]
    if not receipt.get('sources'):
        raise ValueError('Declare the durable source/dependency records.')
    for record in records:
        path = regular(record['path'])
        if path.is_relative_to(run.parent) or digest(path) != record['sha256']:
            raise ValueError(f'Non-durable or changed output/dependency: {path}')
    if not isinstance(receipt.get('generated'), list):
        raise ValueError('Explicit generated-file records are required.')
    generated = {}
    for record in receipt['generated']:
        relative = Path(record['path'])
        if relative.is_absolute() or '..' in relative.parts or relative == Path('run.json'):
            raise ValueError('Generated paths must be relative to this run, excluding run.json.')
        path = regular(run / relative)
        if not path.is_relative_to(run) or path in generated or digest(path) != record['sha256']:
            raise ValueError(f'Changed, duplicate, or escaping generated file: {path}')
        generated[path] = record['sha256']
    actual = set()
    directories = []
    for path in run.rglob('*'):
        if path.is_symlink():
            raise ValueError(f'Refusing a symlink in the run: {path}')
        if path.is_dir():
            directories.append(path)
        elif path.is_file() and path != marker:
            actual.add(path)
        elif path != marker:
            raise ValueError(f'Unrecognized filesystem object: {path}')
    if actual != set(generated):
        raise ValueError('Unlisted or missing files; inspect the run before cleanup.')
    result = {'run': str(run), 'files': len(generated),
              'bytes': sum(p.stat().st_size for p in generated), 'removed': False}
    if not apply:
        return result
    lsof = shutil.which('lsof')
    if not lsof:
        raise ValueError('Open-file check unavailable; leave the run for manual inspection.')
    opened = subprocess.run([lsof, '-n', '-F', 'n', '+D', str(run)],
                            capture_output=True, text=True, timeout=20)
    if opened.returncode != 1 or opened.stdout or opened.stderr:
        raise ValueError('Open files or uncertain open-file check; refusing cleanup.')
    # Recheck the complete receipt immediately before deletion, then unlink only
    # the enumerated regular files. This is not a lock against a manual writer.
    for record in records:
        if digest(regular(record['path'])) != record['sha256']:
            raise ValueError('Output/dependency changed before cleanup.')
    for path, expected in generated.items():
        if digest(regular(path)) != expected:
            raise ValueError('Generated file changed before cleanup.')
    for path in generated:
        path.unlink()
    for directory in sorted(directories, key=lambda p: len(p.parts), reverse=True):
        directory.rmdir()
    marker.unlink()
    run.rmdir()
    result['removed'] = True
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    create = commands.add_parser('begin')
    create.add_argument('--build-root', type=Path, required=True)
    clean = commands.add_parser('finish')
    clean.add_argument('--run', type=Path, required=True)
    clean.add_argument('--receipt', type=Path, required=True)
    clean.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    try:
        result = {'run': str(begin(args.build_root))} if args.command == 'begin' else finish(args.run, args.receipt, args.apply)
        print(json.dumps(result))
    except (OSError, ValueError, KeyError, TypeError, subprocess.TimeoutExpired) as error:
        parser.exit(1, f'Build lifecycle stopped: {error}\n')


if __name__ == '__main__':
    main()
