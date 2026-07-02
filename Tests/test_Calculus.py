import os
import sys
import unittest

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from Math.Calculus.Differentiation.product_rule import format_polynomial

class TestCalculusDifferentiation(unittest.TestCase):
    def test_format_polynomial_basic(self):
        self.assertEqual(format_polynomial([2, 3], [1, 2]), "2x^1 + 3x^2")

    def test_format_polynomial_empty(self):
        self.assertEqual(format_polynomial([], []), "")

    def test_format_polynomial_single_term(self):
        self.assertEqual(format_polynomial([5], [0]), "5x^0")

    def test_format_polynomial_floats(self):
        self.assertEqual(format_polynomial([2.5, 3.1], [1.0, 2.0]), "2.5x^1 + 3.1x^2")

    def test_format_polynomial_zero_coeff(self):
        self.assertEqual(format_polynomial([0, 1], [2, 1]), "0x^2 + 1x^1")

if __name__ == "__main__":
    unittest.main()
