import importlib.util
from pathlib import Path
import tempfile
import unittest
import xml.etree.ElementTree as ET


skill = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('render_equation', skill / 'scripts/render_equation.py')
renderer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)


def document(expression):
    return (r'\documentclass[border=2pt]{standalone}' '\n'
            r'\usepackage{amsmath,amssymb,lmodern,xcolor}' '\n'
            r'\begin{document}\color[HTML]{18202B}\(\displaystyle ' + expression +
            r'\)\end{document}' '\n')


class EquationTests(unittest.TestCase):
    def test_representative_structures_and_source_retention(self):
        expressions = [
            r'x_{t+1}=x_t-\eta_t\frac{v_t}{\lVert v_t\rVert}',
            r'\left(\mathbb{E}\lVert X-\mathbb{E}X\rVert^p\right)^{1/p}\leq\sigma',
            r'\sum_{i=1}^{n}\frac{a_i}{1+\sqrt{b_i^2+c_i^2}}',
            r'A=\begin{pmatrix}1&\alpha\\0&1\end{pmatrix}',
            r'f(x)=\begin{cases}x^2&x\geq0\\-x&x<0\end{cases}',
            r'\begin{aligned}y&=Ax+b\\\operatorname{Var}(y)&=A\Sigma A^\top\end{aligned}',
        ]
        with tempfile.TemporaryDirectory() as directory:
            work = Path(directory)
            for index, expression in enumerate(expressions):
                with self.subTest(expression=expression):
                    source = work / f'input-{index}.tex'
                    output = work / 'assets' / f'eq-{index}.svg'
                    content = document(expression)
                    source.write_text(content)
                    result = renderer.render_equation(source, output)
                    self.assertEqual(output.with_suffix('.tex').read_text(), content)
                    self.assertEqual(source.read_text(), content)
                    bounds = list(map(float, result['viewBox'].split()))
                    self.assertGreater(bounds[2], 0)
                    self.assertGreater(bounds[3], 0)
                    root = ET.fromstring(output.read_bytes())
                    self.assertTrue(any(e.tag.endswith('}path') for e in root.iter()))

    def test_invalid_tex_creates_no_deliverable(self):
        with tempfile.TemporaryDirectory() as directory:
            work = Path(directory)
            source = work / 'input.tex'
            source.write_text(document(r'\undefinedFormulaCommand{x}'))
            output = work / 'result.svg'
            with self.assertRaises(RuntimeError):
                renderer.render_equation(source, output)
            self.assertFalse(output.exists())
            self.assertFalse(output.with_suffix('.tex').exists())

    def test_existing_assets_are_not_overwritten(self):
        with tempfile.TemporaryDirectory() as directory:
            work = Path(directory)
            source = work / 'input.tex'
            source.write_text(document('x'))
            output = work / 'result.svg'
            output.write_text('existing asset')
            with self.assertRaises(FileExistsError):
                renderer.render_equation(source, output)
            self.assertEqual(output.read_text(), 'existing asset')

    def test_multiple_pages_are_not_silently_truncated(self):
        with tempfile.TemporaryDirectory() as directory:
            work = Path(directory)
            source = work / 'input.tex'
            source.write_text(r'\documentclass{article}\begin{document}x\newpage y\end{document}')
            with self.assertRaises(ValueError):
                renderer.render_equation(source, work / 'result.svg')
            self.assertFalse((work / 'result.svg').exists())


if __name__ == '__main__':
    unittest.main()
