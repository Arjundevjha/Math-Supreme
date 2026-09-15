import unittest
import math
import pytest
from Math.Geometry.Trigonometry.Arc_Functions.arcsin import arcsin_numerical


class TestArcSinSecurity(unittest.TestCase):
    def test_invalid_sin_value_type(self):
        with self.assertRaises(TypeError):
            arcsin_numerical(True)
        with self.assertRaises(TypeError):
            arcsin_numerical("0.5")
        with self.assertRaises(TypeError):
            arcsin_numerical(None)

    def test_invalid_sin_value_nan_inf(self):
        with self.assertRaises(ValueError):
            arcsin_numerical(float('nan'))
        with self.assertRaises(ValueError):
            arcsin_numerical(float('inf'))
        with self.assertRaises(ValueError):
            arcsin_numerical(float('-inf'))

    def test_invalid_precision_type(self):
        with self.assertRaises(TypeError):
            arcsin_numerical(0.5, precision=True)
        with self.assertRaises(TypeError):
            arcsin_numerical(0.5, precision="0.001")

    def test_invalid_precision_bounds(self):
        with self.assertRaises(ValueError):
            arcsin_numerical(0.5, precision=0)
        with self.assertRaises(ValueError):
            arcsin_numerical(0.5, precision=-0.01)
        with self.assertRaises(ValueError):
            arcsin_numerical(0.5, precision=float('nan'))
        with self.assertRaises(ValueError):
            arcsin_numerical(0.5, precision=float('inf'))


if __name__ == "__main__":
    unittest.main()
