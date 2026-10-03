import unittest
from Math.Geometry.Trigonometry.Formulas.cosine_rule import sqrt_newton, arccos_series


class TestCosineRuleSecurity(unittest.TestCase):
    def test_sqrt_newton_invalid_types(self):
        with self.assertRaises(TypeError):
            sqrt_newton("4")
        with self.assertRaises(TypeError):
            sqrt_newton(True)
        with self.assertRaises(TypeError):
            sqrt_newton(None)

    def test_sqrt_newton_nan_inf(self):
        with self.assertRaises(ValueError):
            sqrt_newton(float('nan'))
        with self.assertRaises(ValueError):
            sqrt_newton(float('inf'))
        with self.assertRaises(ValueError):
            sqrt_newton(float('-inf'))

    def test_sqrt_newton_precision_invalid_types_and_values(self):
        with self.assertRaises(TypeError):
            sqrt_newton(4, precision="0.0001")
        with self.assertRaises(TypeError):
            sqrt_newton(4, precision=True)
        with self.assertRaises(ValueError):
            sqrt_newton(4, precision=0)
        with self.assertRaises(ValueError):
            sqrt_newton(4, precision=-0.01)
        with self.assertRaises(ValueError):
            sqrt_newton(4, precision=float('nan'))
        with self.assertRaises(ValueError):
            sqrt_newton(4, precision=float('inf'))

    def test_arccos_series_invalid_types(self):
        with self.assertRaises(TypeError):
            arccos_series("0.5")
        with self.assertRaises(TypeError):
            arccos_series(True)
        with self.assertRaises(TypeError):
            arccos_series(None)

    def test_arccos_series_nan_inf(self):
        with self.assertRaises(ValueError):
            arccos_series(float('nan'))
        with self.assertRaises(ValueError):
            arccos_series(float('inf'))
        with self.assertRaises(ValueError):
            arccos_series(float('-inf'))


if __name__ == "__main__":
    unittest.main()
