import os
import sys
import math
import unittest

# Add root directory to path to allow imports
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from Math.Algebra.Polynomials.polynomial import evaluate_polynomial
from Math.Algebra.Polynomials.remainnder_theorem import remainder_theorem

class TestEvaluatePolynomial(unittest.TestCase):
    def test_evaluate_polynomial_basic(self):
        """Test with a simple quadratic polynomial: P(x) = x^2 + 2x + 1 at x=2"""
        # P(2) = 2^2 + 2*2 + 1 = 9
        self.assertEqual(evaluate_polynomial([1, 2, 1], [2, 1, 0], 2), 9)

    def test_evaluate_polynomial_zero_x(self):
        """Test polynomial at x=0"""
        self.assertEqual(evaluate_polynomial([1, 2, 1], [2, 1, 0], 0), 1)

    def test_evaluate_polynomial_negative_x(self):
        """Test polynomial at x=-1"""
        self.assertEqual(evaluate_polynomial([1, 2, 1], [2, 1, 0], -1), 0)

    def test_evaluate_polynomial_fractional_powers(self):
        """Test with fractional powers"""
        # P(x) = x^0.5, P(4) = 4^0.5 = 2.0
        self.assertEqual(evaluate_polynomial([1], [0.5], 4), 2.0)

    def test_evaluate_polynomial_float_coefficients(self):
        """Test with float coefficients and float x"""
        # P(x) = 1.5x^2 + 0.5, P(2.0) = 1.5*(4) + 0.5 = 6.5
        self.assertEqual(evaluate_polynomial([1.5, 0.5], [2, 0], 2.0), 6.5)

    def test_evaluate_polynomial_empty(self):
        """Test with empty coefficients and powers"""
        self.assertEqual(evaluate_polynomial([], [], 5), 0)

    def test_evaluate_polynomial_negative_powers(self):
        """Test with negative powers"""
        # P(x) = 4x^-1 + 2x^-2, P(2) = 4/2 + 2/4 = 2.5
        self.assertEqual(evaluate_polynomial([4, 2], [-1, -2], 2), 2.5)

    def test_evaluate_polynomial_zero_division_error(self):
        """Test dividing by zero raises an exception when power is negative"""
        with self.assertRaises(ZeroDivisionError):
            evaluate_polynomial([1], [-1], 0)

    def test_evaluate_polynomial_mismatched_lengths(self):
        """Test with mismatched lengths (zip stops at shortest list)"""
        # P(x) = 2x^2 + 3x
        # Coefficients length 2, powers length 1
        self.assertEqual(evaluate_polynomial([2, 3], [2], 2), 8)
    def test_evaluate_polynomial_large_numbers(self):
        """Test with large numbers"""
        self.assertEqual(evaluate_polynomial([1e10, 1e10], [1, 0], 10), 1.1e11)

class TestRemainderTheorem(unittest.TestCase):
    def test_remainder_theorem_basic(self):
        """Test P(x) = x^2 - 3x + 2 divided by (x - 3). Remainder = P(3)."""
        # P(3) = 3^2 - 3(3) + 2 = 9 - 9 + 2 = 2
        self.assertEqual(remainder_theorem([1, -3, 2], [2, 1, 0], 3), 2)

    def test_remainder_theorem_exact_factor(self):
        """Test division by exact factor where remainder should be 0."""
        # P(x) = x^2 - 4, divide by (x - 2). P(2) = 0.
        self.assertEqual(remainder_theorem([1, -4], [2, 0], 2), 0)

    def test_remainder_theorem_negative_a(self):
        """Test dividing by (x - a) where a is negative, i.e., (x + 2) -> a = -2."""
        # P(x) = x^3 + 2x^2 - x - 2, divide by (x + 2). P(-2) = -8 + 8 + 2 - 2 = 0
        self.assertEqual(remainder_theorem([1, 2, -1, -2], [3, 2, 1, 0], -2), 0)

    def test_remainder_theorem_float(self):
        """Test with float values."""
        # P(x) = 2x^2 + x - 1, divide by (x - 0.5). P(0.5) = 2(0.25) + 0.5 - 1 = 0
        self.assertEqual(remainder_theorem([2, 1, -1], [2, 1, 0], 0.5), 0)

    def test_remainder_theorem_floating_point_precision(self):
        """Test cases where floating point precision might be an issue."""
        # P(x) = 0.1x + 0.2, divide by (x - 1). P(1) = 0.3
        result = remainder_theorem([0.1, 0.2], [1, 0], 1)
        self.assertTrue(math.isclose(result, 0.3, rel_tol=1e-9))

    def test_remainder_theorem_empty(self):
        """Test empty polynomial"""
        self.assertEqual(remainder_theorem([], [], 5), 0)

    def test_remainder_theorem_large_numbers(self):
        """Test remainder theorem with large numbers"""
        self.assertEqual(remainder_theorem([1e10, 1e10], [1, 0], 10), 1.1e11)

if __name__ == '__main__':
    unittest.main()
