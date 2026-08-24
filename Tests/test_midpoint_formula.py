import os
import sys
import unittest
import math

# Add project root and Math directory to sys.path to avoid ModuleNotFoundError
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
math_dir = os.path.join(project_root, 'Math')
if math_dir not in sys.path:
    sys.path.insert(0, math_dir)

from Math.Geometry.Analytic_Geometry.midpoint_formula import midpoint_formula

class TestMidpointFormula(unittest.TestCase):
    def test_positive_coordinates(self):
        self.assertEqual(midpoint_formula(2, 4, 6, 8), (4.0, 6.0))

    def test_negative_coordinates(self):
        self.assertEqual(midpoint_formula(-2, -4, -6, -8), (-4.0, -6.0))

    def test_mixed_coordinates(self):
        self.assertEqual(midpoint_formula(-4, 2, 4, -2), (0.0, 0.0))

    def test_float_coordinates(self):
        result = midpoint_formula(1.5, 2.5, 3.5, 4.5)
        self.assertTrue(math.isclose(result[0], 2.5))
        self.assertTrue(math.isclose(result[1], 3.5))

    def test_same_point(self):
        self.assertEqual(midpoint_formula(5, 5, 5, 5), (5.0, 5.0))

    def test_origin_to_point(self):
        self.assertEqual(midpoint_formula(0, 0, 10, 10), (5.0, 5.0))

if __name__ == '__main__':
    unittest.main()
