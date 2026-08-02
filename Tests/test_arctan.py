import unittest
import math
from decimal import Decimal
from Math.Geometry.Trigonometry.Arc_Functions.arctan import calculate_arctan

class TestArcTan(unittest.TestCase):
    def test_calculate_arctan_positive_integer(self):
        # arctan(1/2)
        result = calculate_arctan(2, precision=10)
        expected = math.atan(1/2)
        self.assertAlmostEqual(float(result), expected, places=10)

    def test_calculate_arctan_positive_float(self):
        # arctan(1/2.5)
        result = calculate_arctan(2.5, precision=10)
        expected = math.atan(1/2.5)
        self.assertAlmostEqual(float(result), expected, places=10)

    def test_calculate_arctan_decimal(self):
        # arctan(1/3)
        result = calculate_arctan(Decimal('3'), precision=10)
        expected = math.atan(1/3)
        self.assertAlmostEqual(float(result), expected, places=10)

    def test_calculate_arctan_negative_value(self):
        # arctan(1/-2)
        result = calculate_arctan(-2, precision=10)
        expected = math.atan(1/-2)
        self.assertAlmostEqual(float(result), expected, places=10)

    def test_calculate_arctan_zero(self):
        # Custom logic returns 0 when x=0
        result = calculate_arctan(0)
        self.assertEqual(result, Decimal(0))

    def test_calculate_arctan_x_equals_one_fixed_terms(self):
        # arctan(1/1) = pi/4
        # Since it converges slowly, we use fixed number of terms
        result = calculate_arctan(1, number_of_terms=10000)
        expected = math.pi / 4
        self.assertAlmostEqual(float(result), expected, places=4)

if __name__ == '__main__':
    unittest.main()
