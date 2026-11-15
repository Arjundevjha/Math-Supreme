import math
import unittest

from Math.Algebra.Polynomials.polynomial import (
    add_polynomials,
    evaluate_polynomial,
    format_polynomial,
    multiply_polynomials,
    power_polynomial,
    subtract_polynomials,
    trim_polynomial,
)


class TestEvaluatePolynomial(unittest.TestCase):
    def test_evaluate_polynomial_basic(self):
        # 1 + 2x + x^2 at x = 2 -> 9
        self.assertAlmostEqual(evaluate_polynomial([1, 2, 1], 2), 9.0)

    def test_evaluate_polynomial_zero_x(self):
        self.assertAlmostEqual(evaluate_polynomial([5, 2, 1], 0), 5.0)

    def test_evaluate_polynomial_negative_x(self):
        # 1 + 2x + x^2 at x = -1 -> 0
        self.assertAlmostEqual(evaluate_polynomial([1, 2, 1], -1), 0.0)

    def test_evaluate_polynomial_float_coefficients(self):
        # 0.5 + 0*x + 1.5*x^2 at x = 2.0 -> 6.5
        self.assertAlmostEqual(evaluate_polynomial([0.5, 0, 1.5], 2.0), 6.5)

    def test_evaluate_polynomial_empty(self):
        self.assertAlmostEqual(evaluate_polynomial([], 5), 0.0)

    def test_evaluate_polynomial_zero_coeffs(self):
        self.assertAlmostEqual(evaluate_polynomial([0, 0, 0], 5), 0.0)

    def test_evaluate_polynomial_precision(self):
        self.assertTrue(
            math.isclose(evaluate_polynomial([0.2, 0.1], 1), 0.3, rel_tol=1e-9)
        )


class TestFormatPolynomial(unittest.TestCase):
    def test_format_polynomial_basic(self):
        self.assertEqual(format_polynomial([4, 3, 2]), "4 + 3x + 2x^2")

    def test_format_polynomial_empty_and_zero(self):
        self.assertEqual(format_polynomial([]), "0")
        self.assertEqual(format_polynomial([0, 0]), "0")

    def test_format_polynomial_single_term(self):
        self.assertEqual(format_polynomial([0, 0, 0, 5]), "5x^3")

    def test_format_polynomial_floats(self):
        self.assertEqual(
            format_polynomial([3.1, -2.5, 1.5]), "3.1 + -2.5x + 1.5x^2"
        )


class TestPolynomialOperations(unittest.TestCase):
    def test_trim_polynomial(self):
        self.assertEqual(trim_polynomial([1, 2, 0, 0]), [1, 2])
        self.assertEqual(trim_polynomial([0, 0]), [])

    def test_add_and_subtract(self):
        self.assertEqual(add_polynomials([1, 2, 3], [4, -2]), [5, 0, 3])
        self.assertEqual(subtract_polynomials([1, 2, 3], [1, 2, 3]), [])

    def test_multiply_and_power(self):
        # (1 + x) * (1 - x) = 1 - x^2
        self.assertEqual(multiply_polynomials([1, 1], [1, -1]), [1, 0, -1])
        # (1 + x)^3 = 1 + 3x + 3x^2 + x^3
        self.assertEqual(power_polynomial([1, 1], 3), [1, 3, 3, 1])
        self.assertEqual(power_polynomial([1, 1], 0), [1])
        self.assertEqual(power_polynomial([], 3), [])


if __name__ == "__main__":
    unittest.main()
