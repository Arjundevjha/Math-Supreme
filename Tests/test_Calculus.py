import os
import sys
import unittest


# Add root directory to path
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from Math.Calculus.Differentiation.simple_diffrentiation_function import differentiate_polynomial

class TestDifferentiatePolynomial(unittest.TestCase):
    def test_basic_polynomial(self):
        # d/dx(3x^2 + 2x + 1) = 6x + 2
        # coeffs = [3, 2, 1], powers = [2, 1, 0]
        # derivative coeffs = [6, 2], powers = [1, 0]
        self.assertEqual(
            differentiate_polynomial([3, 2, 1], [2, 1, 0]),
            [(6, 1), (2, 0)]
        )

    def test_single_term(self):
        # d/dx(5x^3) = 15x^2
        self.assertEqual(
            differentiate_polynomial([5], [3]),
            [(15, 2)]
        )

    def test_constant_value(self):
        # d/dx(7) = 0
        self.assertEqual(
            differentiate_polynomial([7], [0]),
            []
        )

    def test_empty_lists(self):
        # d/dx() = 0
        self.assertEqual(
            differentiate_polynomial([], []),
            []
        )

    def test_floating_point(self):
        # d/dx(2.5x^2.0 + 1.5x^0.5) = 5.0x^1.0 + 0.75x^-0.5
        self.assertEqual(
            differentiate_polynomial([2.5, 1.5], [2.0, 0.5]),
            [(5.0, 1.0), (0.75, -0.5)]
        )

    def test_negative_power(self):
        # Based on the current implementation, powers <= 0 are ignored
        # d/dx(4x^-2) -> empty list since power is not > 0
        self.assertEqual(
            differentiate_polynomial([4], [-2]),
            []
        )

    def test_mixed_skipped_and_kept(self):
        # d/dx(2x^3 + 5 + 4x^-1) -> only 2x^3 is differentiated -> 6x^2
        self.assertEqual(
            differentiate_polynomial([2, 5, 4], [3, 0, -1]),
            [(6, 2)]
        )

if __name__ == '__main__':
    unittest.main()
