import unittest
import math
from decimal import Decimal
from Math.Geometry.Trigonometry.Arc_Functions.arctan import calculate_arctan

class TestArcTan(unittest.TestCase):
    def test_calculate_arctan_positive(self):
        # arctan(1/2)
        x = 2
        result = calculate_arctan(x, precision=10)
        expected = Decimal(str(math.atan(1/x)))
        # allow some small tolerance due to float/decimal conversions
        self.assertAlmostEqual(float(result), float(expected), places=9)

    def test_calculate_arctan_negative(self):
        # arctan(1/-2)
        x = -2
        result = calculate_arctan(x, precision=10)
        expected = Decimal(str(math.atan(1/x)))
        self.assertAlmostEqual(float(result), float(expected), places=9)

    def test_calculate_arctan_one(self):
        # arctan(1/1) = arctan(1) = pi/4
        # Since Taylor series for arctan(1) converges slowly, we use number_of_terms
        result = calculate_arctan(1, number_of_terms=100)
        # It's an approximation, so check it's reasonably close to pi/4
        expected = math.pi / 4
        self.assertAlmostEqual(float(result), expected, places=2)

    def test_calculate_arctan_decimal_input(self):
        # arctan(1/2.5)
        x = Decimal('2.5')
        result = calculate_arctan(x, precision=10)
        expected = Decimal(str(math.atan(1/2.5)))
        self.assertAlmostEqual(float(result), float(expected), places=9)

    def test_calculate_arctan_float_input(self):
        # arctan(1/3.0)
        x = 3.0
        result = calculate_arctan(x, precision=10)
        expected = Decimal(str(math.atan(1/3.0)))
        self.assertAlmostEqual(float(result), float(expected), places=9)

if __name__ == '__main__':
    unittest.main()
