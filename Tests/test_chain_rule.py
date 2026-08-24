import unittest
from Math.Calculus.Differentiation.chain_rule import (
    chain_rule_derivative,
    format_polynomial,
)


class TestChainRuleDerivative(unittest.TestCase):
    def test_chain_rule_derivative_basic(self):
        # g(x) = x^2, n = 3 => 3(1x^2)^2 * (2x^1)
        result = chain_rule_derivative([1], [2], 3)
        self.assertEqual(result, "3(1x^2)^2 * (2x^1)")

    def test_chain_rule_derivative_multiple_terms(self):
        # g(x) = x^2 + 2x, n = 3 => 3(1x^2 + 2x^1)^2 * (2x^1 + 2x^0)
        result = chain_rule_derivative([1, 2], [2, 1], 3)
        self.assertEqual(result, "3(1x^2 + 2x^1)^2 * (2x^1 + 2x^0)")

    def test_chain_rule_derivative_constant_inner(self):
        # g(x) = 5 (power 0), n = 2 => 2(5x^0)^1 * ()
        result = chain_rule_derivative([5], [0], 2)
        self.assertEqual(result, "2(5x^0)^1 * ()")

    def test_chain_rule_derivative_zero_exponent(self):
        # g(x) = x^2 + 2, n = 0 => 0(1x^2 + 2x^0)^-1 * (2x^1)
        result = chain_rule_derivative([1, 2], [2, 0], 0)
        self.assertEqual(result, "0(1x^2 + 2x^0)^-1 * (2x^1)")

    def test_chain_rule_derivative_exponent_one(self):
        # g(x) = x^3, n = 1 => 1(1x^3)^0 * (3x^2)
        result = chain_rule_derivative([1], [3], 1)
        self.assertEqual(result, "1(1x^3)^0 * (3x^2)")

    def test_chain_rule_derivative_negative_exponent_raises_value_error(self):
        # Negative exponent should raise ValueError
        with self.assertRaisesRegex(ValueError, "Exponent must be non-negative."):
            chain_rule_derivative([1, 2], [2, 0], -1)

    def test_chain_rule_derivative_float_coefficients_and_powers(self):
        # g(x) = 1.5x^2.5, n = 2 => 2(1.5x^2)^1 * (3.75x^1)
        result = chain_rule_derivative([1.5], [2.5], 2)
        self.assertEqual(result, "2(1.5x^2)^1 * (3.75x^1)")

    def test_chain_rule_derivative_empty(self):
        # g(x) = empty, n = 3 => 3()^2 * ()
        result = chain_rule_derivative([], [], 3)
        self.assertEqual(result, "3()^2 * ()")

    def test_chain_rule_derivative_negative_powers(self):
        # g(x) = 3x^-2, n = 2 => 2(3x^-2)^1 * (-6x^-3)
        result = chain_rule_derivative([3], [-2], 2)
        self.assertEqual(result, "2(3x^-2)^1 * (-6x^-3)")

    def test_chain_rule_derivative_negative_coeffs_and_powers(self):
        # g(x) = -2x^-3, n = 4 => 4(-2x^-3)^3 * (6x^-4)
        result = chain_rule_derivative([-2], [-3], 4)
        self.assertEqual(result, "4(-2x^-3)^3 * (6x^-4)")

    def test_chain_rule_derivative_zero_coefficients(self):
        # g(x) = 0x^2, n = 3 => 3(0x^2)^2 * (0x^1)
        result = chain_rule_derivative([0], [2], 3)
        self.assertEqual(result, "3(0x^2)^2 * (0x^1)")

    def test_chain_rule_derivative_mismatched_lengths(self):
        # zip stops at shortest list
        result = chain_rule_derivative([1, 2], [2], 2)
        self.assertEqual(result, "2(1x^2)^1 * (2x^1)")


class TestChainRuleFormatPolynomial(unittest.TestCase):
    def test_format_polynomial_basic(self):
        self.assertEqual(format_polynomial([3, 2, 1], [2, 1, 0]), "3x^2 + 2x^1 + 1x^0")

    def test_format_polynomial_empty(self):
        self.assertEqual(format_polynomial([], []), "")

    def test_format_polynomial_floats(self):
        self.assertEqual(format_polynomial([1.5, 2.5], [2.0, 1.0]), "1.5x^2 + 2.5x^1")

    def test_format_polynomial_negative_powers(self):
        self.assertEqual(format_polynomial([5], [-2]), "5x^-2")


if __name__ == "__main__":
    unittest.main()
