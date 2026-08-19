import unittest
import math


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
