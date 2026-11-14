import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from render_equations import render_batch


def document(expression):
    return (r'\documentclass[border=2pt]{standalone}' '\n'
            r'\usepackage{amsmath,amssymb,lmodern}' '\n'
            r'\begin{document}\(\displaystyle ' + expression + r'\)\end{document}')


class BatchTests(unittest.TestCase):
    def test_changed_source_gets_new_asset_and_repeat_is_consistent(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source, listing, output = root / 'formula.tex', root / 'equations.json', root / 'output'
            source.write_text(document(r'\frac{x}{y}'))
            listing.write_text(json.dumps([{'id': 'ratio', 'source': 'formula.tex', 'slides': [2], 'source_font_pt': 10}]))
            first = render_batch(listing, output)['equations'][0]
            original_svg = (output / first['svg']).read_bytes()
            again = render_batch(listing, output)['equations'][0]
            self.assertEqual(first, again)
            source.write_text(document(r'\frac{x^2}{y+1}'))
            changed = render_batch(listing, output)['equations'][0]
            self.assertNotEqual(first['render_digest'], changed['render_digest'])
            self.assertNotEqual(first['svg'], changed['svg'])
            self.assertEqual((output / first['svg']).read_bytes(), original_svg)
            self.assertEqual((output / changed['source']).read_text(), source.read_text())
            self.assertNotEqual((output / changed['svg']).read_bytes(), original_svg)
            self.assertEqual(changed['slides'], [2])
            self.assertEqual(json.loads((output / 'equations-manifest.json').read_text())['equations'], [changed])

    def test_bad_equation_does_not_replace_existing_manifest(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source, listing, output = root / 'formula.tex', root / 'equations.json', root / 'output'
            source.write_text(document('x'))
            listing.write_text(json.dumps([{'id': 'eq', 'source': 'formula.tex'}]))
            render_batch(listing, output)
            previous = (output / 'equations-manifest.json').read_bytes()
            source.write_text(document(r'\undefinedFormulaCommand{x}'))
            with self.assertRaises(RuntimeError):
                render_batch(listing, output)
            self.assertEqual((output / 'equations-manifest.json').read_bytes(), previous)

    def test_conflicting_asset_is_not_silently_reused(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source, listing, output = root / 'formula.tex', root / 'equations.json', root / 'output'
            source.write_text(document('x'))
            listing.write_text(json.dumps([{'id': 'eq', 'source': 'formula.tex'}]))
            record = render_batch(listing, output)['equations'][0]
            asset = output / record['svg']
            asset.write_text('different existing asset')
            with self.assertRaises(FileExistsError):
                render_batch(listing, output)
            self.assertEqual(asset.read_text(), 'different existing asset')

    def test_duplicate_ids_fail_before_rendering(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            listing, output = root / 'equations.json', root / 'output'
            listing.write_text(json.dumps([{'id': 'eq', 'source': 'a.tex'}, {'id': 'eq', 'source': 'b.tex'}]))
            with self.assertRaises(ValueError):
                render_batch(listing, output)
            self.assertFalse(output.exists())


if __name__ == '__main__':
    unittest.main()
