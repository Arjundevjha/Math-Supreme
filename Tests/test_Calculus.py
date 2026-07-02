import os
import sys
import unittest

import pytest

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

math_dir = os.path.abspath(os.path.join(root_dir, 'Math'))
if math_dir not in sys.path:
    sys.path.insert(0, math_dir)

from Math.Calculus.Differentiation.quotient_rule import compute_polynomial_derivative_str

class TestQuotientRule(unittest.TestCase):
    def test_compute_polynomial_derivative_str_basic(self):
        self.assertEqual(compute_polynomial_derivative_str([3], [2]), "6x^1")

    def test_compute_polynomial_derivative_str_multiple_terms(self):
        self.assertEqual(compute_polynomial_derivative_str([3, 2, 1], [2, 1, 0]), "6x^1 + 2x^0")

    def test_compute_polynomial_derivative_str_constant(self):
        self.assertEqual(compute_polynomial_derivative_str([5], [0]), "0")

    def test_compute_polynomial_derivative_str_zero_coefficient(self):
        self.assertEqual(compute_polynomial_derivative_str([0], [2]), "0x^1")

    def test_compute_polynomial_derivative_str_float(self):
        self.assertEqual(compute_polynomial_derivative_str([1.5, 2.5], [2, 1]), "3.0x^1 + 2.5x^0")

    def test_compute_polynomial_derivative_str_negative_powers(self):
        self.assertEqual(compute_polynomial_derivative_str([3], [-2]), "-6x^-3")

    def test_compute_polynomial_derivative_str_empty(self):
        self.assertEqual(compute_polynomial_derivative_str([], []), "0")

if __name__ == '__main__':
    unittest.main()
