import hashlib
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

SCRIPT = Path(__file__).parents[1] / 'scripts/check_pptx_animation_targets.py'
SPEC = importlib.util.spec_from_file_location('animation_targets', SCRIPT)
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


def slide(shapes='', timing='', hidden=False):
    return (f'<p:sld xmlns:p="{checker.P}" xmlns:mc="{checker.MC}"'
            + (' show="0"' if hidden else '') + '><p:cSld><p:spTree>'
            + shapes + '</p:spTree></p:cSld><p:timing>' + timing + '</p:timing></p:sld>')


def shape(identifier):
    return f'<p:sp><p:nvSpPr><p:cNvPr id="{identifier}"/></p:nvSpPr></p:sp>'


class AnimationTargetsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.path = Path(self.temp.name) / 'test.pptx'

    def tearDown(self):
        self.temp.cleanup()

    def package(self, slides):
        ids = ''.join(f'<p:sldId id="{255+i}" r:id="r{i}"/>' for i in range(1, len(slides)+1))
        rels = ''.join(f'<Relationship Id="r{i}" Type="{checker.R}/slide" Target="slides/slide{99-i}.xml"/>'
                       for i in range(1, len(slides)+1))
        with zipfile.ZipFile(self.path, 'w') as z:
            z.writestr('ppt/presentation.xml', f'<p:presentation xmlns:p="{checker.P}" xmlns:r="{checker.R}"><p:sldIdLst>{ids}</p:sldIdLst></p:presentation>')
            z.writestr('ppt/_rels/presentation.xml.rels', '<Relationships>'+rels+'</Relationships>')
            for i, content in enumerate(slides, 1):
                z.writestr(f'ppt/slides/slide{99-i}.xml', content)

    def test_valid_targets_are_read_only(self):
        self.package([slide(shape(33), '<p:spTgt spid="33"/><p:bldLst><p:bldP spid="33"/></p:bldLst>')])
        before = hashlib.sha256(self.path.read_bytes()).digest()
        result = checker.check(self.path)
        self.assertEqual(result['status'], 'pass')
        self.assertEqual(result['shape_references_checked'], 2)
        self.assertEqual(before, hashlib.sha256(self.path.read_bytes()).digest())

    def test_deleted_textbox_fails_and_rebuilt_sequence_passes(self):
        self.package([slide(shape(2), '<p:spTgt spid="33"/>')])
        self.assertEqual(checker.check(self.path)['errors'][0]['shape_id'], '33')
        process = subprocess.run([sys.executable, str(SCRIPT), str(self.path)], capture_output=True)
        self.assertEqual(process.returncode, 1)
        self.package([slide(shape(2), '<p:spTgt spid="2"/>')])
        self.assertEqual(checker.check(self.path)['status'], 'pass')

    def test_stale_build_list_alone_fails(self):
        self.package([slide(shape(2), '<p:bldLst><p:bldP spid="33"/></p:bldLst>')])
        error = checker.check(self.path)['errors'][0]
        self.assertEqual(error['element'], 'bldP')

    def test_hidden_slides_and_actual_relationship_order(self):
        self.package([slide(shape(2)), slide(shape(2), '<p:spTgt spid="33"/>', hidden=True)])
        result = checker.check(self.path)
        self.assertEqual(result['slides_checked'], 2)
        self.assertEqual(result['errors'][0]['slide'], 2)
        self.assertEqual(result['errors'][0]['part'], 'ppt/slides/slide97.xml')

    def test_shape_on_another_slide_does_not_resolve_target(self):
        self.package([slide(shape(33)), slide(shape(2), '<p:spTgt spid="33"/>')])
        self.assertEqual(checker.check(self.path)['error_count'], 1)

    def test_fallback_does_not_mask_missing_primary_target(self):
        content = '<mc:AlternateContent><mc:Choice Requires="a14">'+shape(2)+'</mc:Choice><mc:Fallback>'+shape(33)+'</mc:Fallback></mc:AlternateContent>'
        self.package([slide(content, '<p:spTgt spid="33"/>')])
        self.assertEqual(checker.check(self.path)['error_count'], 1)

    def test_unreadable_package_has_distinct_exit_status(self):
        self.path.write_bytes(b'not a zip file')
        process = subprocess.run([sys.executable, str(SCRIPT), str(self.path)], capture_output=True)
        self.assertEqual(process.returncode, 2)


if __name__ == '__main__':
    unittest.main()
