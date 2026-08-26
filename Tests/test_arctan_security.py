import unittest
from decimal import Decimal

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

    def test_broad_exception_handling(self):
        # Verify normal calculation works with integer, float, Decimal
        self.assertIsNotNone(calculate_arctan(2))
        self.assertIsNotNone(calculate_arctan(2.0))
        self.assertIsNotNone(calculate_arctan(Decimal('2')))

    def test_precision_bounds(self):
        # Test non-positive precision
        with self.assertRaisesRegex(ValueError, "precision must be a positive integer"):
            calculate_arctan(2, precision=0)
        with self.assertRaisesRegex(ValueError, "precision must be a positive integer"):
            calculate_arctan(2, precision=-10)

        # Test precision exceeding maximum limit
        with self.assertRaisesRegex(ValueError, "precision exceeds maximum allowed limit"):
            calculate_arctan(2, precision=10001)

if __name__ == '__main__':
    unittest.main()
