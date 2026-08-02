import unittest
from decimal import Decimal, getcontext, Overflow, DivisionByZero
import math
from unittest.mock import patch, MagicMock

from Math.Geometry.Trigonometry.Arc_Functions.arctan import calculate_arctan

class TestArcTan(unittest.TestCase):
    def setUp(self):
        # Set a precision for test cases
        getcontext().prec = 60

    def test_calculate_arctan_one(self):
        """Test that arctan(1/1) approaches pi/4."""
        val = calculate_arctan(1, number_of_terms=10000)
        self.assertAlmostEqual(float(val), math.pi / 4, places=3)

    def test_euler_formula(self):
        """Test euler's formula: pi/4 = arctan(1/2) + arctan(1/3)"""
        atan2 = calculate_arctan(2, precision=50)
        atan3 = calculate_arctan(3, precision=50)

        pi_over_4 = atan2 + atan3
        self.assertAlmostEqual(float(pi_over_4), math.pi / 4, places=15)

    def test_machin_formula(self):
        """Test Machin's formula: pi/4 = 4*arctan(1/5) - arctan(1/239)"""
        atan5 = calculate_arctan(5, precision=50)
        atan239 = calculate_arctan(239, precision=50)

        pi_over_4 = 4 * atan5 - atan239
        self.assertAlmostEqual(float(pi_over_4), math.pi / 4, places=15)

    def test_negative_values(self):
        """Test that calculate_arctan(-x) = -calculate_arctan(x)"""
        pos = calculate_arctan(4, precision=20)
        neg = calculate_arctan(-4, precision=20)
        self.assertEqual(neg, -pos)

    def test_zero(self):
        """Test that calculate_arctan(0) returns 0"""
        self.assertEqual(calculate_arctan(0), Decimal(0))

    def test_precision(self):
        """Test precision argument"""
        high_prec = calculate_arctan(2, precision=60)
        low_prec = calculate_arctan(2, precision=10)
        self.assertNotEqual(high_prec, low_prec)

    def test_number_of_terms(self):
        """Test number_of_terms parameter"""
        val_1_term = calculate_arctan(5, number_of_terms=1)
        self.assertEqual(val_1_term, Decimal('0.2'))

        val_2_terms = calculate_arctan(5, number_of_terms=2)
        expected = Decimal('1')/5 - Decimal('1')/(3 * 125)
        self.assertAlmostEqual(float(val_2_terms), float(expected))

    def test_float_type_conversion(self):
        """Test explicit conversion from float works accurately"""
        val_float = calculate_arctan(2.0, precision=20)
        val_int = calculate_arctan(2, precision=20)
        self.assertEqual(val_float, val_int)

    def test_convergence_value_error(self):
        """Test series not converging explicitly raises ValueError for range (-1, 1)."""
        with self.assertRaisesRegex(ValueError, "Series did not converge"):
            calculate_arctan(0.5)

if __name__ == '__main__':
    unittest.main()
