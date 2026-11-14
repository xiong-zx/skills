#!/usr/bin/env python3
"""Read-only check for slide-local animation references to deleted shapes.

Uses the presentation's relationship order, including hidden slides. For
AlternateContent it checks the first Choice (or Fallback if no Choice exists).
This is a focused reference check, not full OOXML or native-render validation.
"""
import argparse
import json
from pathlib import Path
import posixpath
import sys
import xml.etree.ElementTree as ET
import zipfile

P = 'http://schemas.openxmlformats.org/presentationml/2006/main'
R = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
MC = 'http://schemas.openxmlformats.org/markup-compatibility/2006'


def primary_elements(element):
    yield element
    if element.tag == f'{{{MC}}}AlternateContent':
        branch = element.find(f'{{{MC}}}Choice')
        if branch is None:
            branch = element.find(f'{{{MC}}}Fallback')
        if branch is not None:
            yield from primary_elements(branch)
    else:
        for child in element:
            yield from primary_elements(child)


def id_key(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return value


def check(presentation):
    errors = []
    checked = 0
    with zipfile.ZipFile(presentation) as package:
        root = ET.fromstring(package.read('ppt/presentation.xml'))
        relations = ET.fromstring(package.read('ppt/_rels/presentation.xml.rels'))
        targets = {r.get('Id'): r.get('Target') for r in relations
                   if r.get('Type', '').endswith('/slide')
                   and r.get('TargetMode') != 'External'}
        slides = root.find(f'{{{P}}}sldIdLst')
        if slides is None:
            raise ValueError('Presentation has no slide list')
        for index, entry in enumerate(slides, 1):
            target = targets.get(entry.get(f'{{{R}}}id'))
            if not target:
                raise ValueError(f'Missing slide relationship at slide {index}')
            part = target.lstrip('/') if target.startswith('/') else posixpath.normpath('ppt/' + target)
            slide = ET.fromstring(package.read(part))
            elements = list(primary_elements(slide))
            shape_ids = {id_key(e.get('id')) for e in elements
                         if e.tag == f'{{{P}}}cNvPr' and e.get('id') is not None}
            for timing in (e for e in elements if e.tag == f'{{{P}}}timing'):
                for element in primary_elements(timing):
                    if 'spid' not in element.attrib:
                        continue
                    checked += 1
                    identifier = element.get('spid')
                    if id_key(identifier) not in shape_ids:
                        errors.append({'slide': index, 'part': part,
                                       'element': element.tag.split('}')[-1],
                                       'shape_id': identifier})
    return {'status': 'fail' if errors else 'pass', 'slides_checked': len(slides),
            'shape_references_checked': checked, 'error_count': len(errors),
            'errors': errors}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('presentation', type=Path)
    args = parser.parse_args(argv)
    try:
        report = check(args.presentation)
    except (OSError, zipfile.BadZipFile, ET.ParseError, KeyError, ValueError) as error:
        print(json.dumps({'status': 'error', 'message': str(error)}))
        return 2
    print(json.dumps(report))
    return 1 if report['errors'] else 0


if __name__ == '__main__':
    sys.exit(main())
