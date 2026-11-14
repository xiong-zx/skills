import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import subprocess

SPEC = importlib.util.spec_from_file_location('build_run', Path(__file__).parents[1] / 'scripts/build_run.py')
build_run = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(build_run)


class BuildRunTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name).resolve()
        self.run = build_run.begin(self.root / '.build')
        self.output = self.root / 'talk.pptx'
        self.source = self.root / 'formula.tex'
        self.output.write_bytes(b'good output')
        self.source.write_bytes(b'trusted source')
        self.candidate = self.run / 'candidate.pptx'
        self.candidate.write_bytes(b'generated candidate')
        record = lambda p: {'path': str(p), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
        self.receipt = {'generator': 'doc-slides', 'schema_version': 1, 'status': 'verified',
                        'output': record(self.output), 'sources': [record(self.source)],
                        'checks': ['test fixture only'], 'generated': [record(self.candidate)]}
        self.receipt['generated'][0]['path'] = 'candidate.pptx'
        self.receipt_path = self.root / '.build/last-build.json'
        self.save()

    def tearDown(self):
        self.temp.cleanup()

    def save(self):
        self.receipt_path.write_text(json.dumps(self.receipt))

    def test_dry_run_preserves_everything(self):
        self.assertFalse(build_run.finish(self.run, self.receipt_path)['removed'])
        self.assertTrue(self.candidate.exists())

    @patch.object(build_run.shutil, 'which', return_value='/usr/sbin/lsof')
    @patch.object(build_run.subprocess, 'run', return_value=subprocess.CompletedProcess([], 1, '', ''))
    def test_cleanup_only_owned_run(self, *_):
        recovery = self.root / '.build/recovery'
        recovery.mkdir()
        protected = recovery / 'last-good.pptx'
        protected.write_bytes(b'protected')
        self.assertTrue(build_run.finish(self.run, self.receipt_path, True)['removed'])
        self.assertFalse(self.run.exists())
        self.assertEqual(self.output.read_bytes(), b'good output')
        self.assertEqual(protected.read_bytes(), b'protected')

    def test_changed_output_blocks_cleanup(self):
        self.output.write_bytes(b'manual edit')
        with self.assertRaises(ValueError):
            build_run.finish(self.run, self.receipt_path, True)
        self.assertTrue(self.candidate.exists())

    def test_changed_source_blocks_cleanup(self):
        self.source.write_bytes(b'changed source')
        with self.assertRaises(ValueError):
            build_run.finish(self.run, self.receipt_path, True)

    def test_unlisted_file_blocks_cleanup(self):
        (self.run / 'unknown.txt').write_text('must not be deleted')
        with self.assertRaises(ValueError):
            build_run.finish(self.run, self.receipt_path, True)

    def test_changed_generated_file_blocks_cleanup(self):
        self.candidate.write_bytes(b'changed')
        with self.assertRaises(ValueError):
            build_run.finish(self.run, self.receipt_path, True)

    def test_run_symlink_blocks_cleanup(self):
        (self.run / 'link').symlink_to(self.source)
        with self.assertRaises(ValueError):
            build_run.finish(self.run, self.receipt_path, True)

    def test_path_escape_blocks_cleanup(self):
        self.receipt['generated'][0]['path'] = '../candidate.pptx'
        self.save()
        with self.assertRaises(ValueError):
            build_run.finish(self.run, self.receipt_path, True)

    def test_work_dependency_blocks_cleanup(self):
        self.receipt['sources'][0] = {'path': str(self.candidate), 'sha256': build_run.digest(self.candidate)}
        self.save()
        with self.assertRaises(ValueError):
            build_run.finish(self.run, self.receipt_path, True)

    def test_failed_receipt_blocks_cleanup(self):
        self.receipt['status'] = 'failed'
        self.save()
        with self.assertRaises(ValueError):
            build_run.finish(self.run, self.receipt_path, True)

    @patch.object(build_run.shutil, 'which', return_value='/usr/sbin/lsof')
    @patch.object(build_run.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, 'nopen-file\n', ''))
    def test_open_file_blocks_cleanup(self, *_):
        with self.assertRaises(ValueError):
            build_run.finish(self.run, self.receipt_path, True)
        self.assertTrue(self.candidate.exists())

    def test_receipt_in_work_blocks_cleanup(self):
        inside = self.run / 'receipt.json'
        inside.write_text(json.dumps(self.receipt))
        with self.assertRaises(ValueError):
            build_run.finish(self.run, inside, True)


if __name__ == '__main__':
    unittest.main()
