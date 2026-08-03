import unittest
from decimal import Decimal
import decimal
import math

from Math.Geometry.Trigonometry.Arc_Functions.arctan import calculate_arctan

class TestArcTanSecurity(unittest.TestCase):
    def test_dos_infinite_loop(self):
        # Should not loop infinitely and should raise ValueError
        with self.assertRaises(ValueError):
            calculate_arctan(0.5)

    def test_float_underflow(self):
        val = calculate_arctan(1e-200)
        self.assertIsNotNone(val)

    def test_decimal_divzero(self):
        val = calculate_arctan(Decimal('1e-600000'))
        self.assertIsNotNone(val)

if __name__ == '__main__':
    unittest.main()
