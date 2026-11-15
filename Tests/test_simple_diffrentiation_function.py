import unittest

from Math.Calculus.Differentiation.simple_diffrentiation_function import (
    differentiate_polynomial,
)


class TestDifferentiatePolynomial(unittest.TestCase):
    def test_basic_polynomial(self):
        # 5 + 4x + 3x^2 -> 4 + 6x
        self.assertEqual(differentiate_polynomial([5, 4, 3]), [4, 6])

    def test_constant_value(self):
        self.assertEqual(differentiate_polynomial([5]), [])

    def test_empty_list(self):
        self.assertEqual(differentiate_polynomial([]), [])

    def test_floating_point(self):
        # 1.0 + 2.5x + 1.5x^2 -> 2.5 + 3.0x
        self.assertEqual(differentiate_polynomial([1.0, 2.5, 1.5]), [2.5, 3.0])

    def test_negative_coefficients(self):
        # 0 - 3x^2 -> [0, -6]
        self.assertEqual(differentiate_polynomial([0, 0, -3]), [0, -6])

    def test_zero_coefficients(self):
        self.assertEqual(differentiate_polynomial([0, 0, 0]), [])

    def test_trailing_zeros_trimmed(self):
        self.assertEqual(differentiate_polynomial([1, 2, 0, 0]), [2])


if __name__ == "__main__":
    unittest.main()
