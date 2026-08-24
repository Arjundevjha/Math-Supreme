import unittest
import pytest
from Math.Calculus.Differentiation.chain_rule import chain_rule_derivative


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
        # g(x) = 5 (5x^0), n = 2 => 2(5x^0)^1 * ()
        result = chain_rule_derivative([5], [0], 2)
        self.assertEqual(result, "2(5x^0)^1 * ()")

    def test_chain_rule_derivative_zero_exponent(self):
        # g(x) = x^2 + 2x^0, n = 0 => 0(1x^2 + 2x^0)^-1 * (2x^1)
        result = chain_rule_derivative([1, 2], [2, 0], 0)
        self.assertEqual(result, "0(1x^2 + 2x^0)^-1 * (2x^1)")

    def test_chain_rule_derivative_exponent_one(self):
        # g(x) = x^2, n = 1 => 1(1x^2)^0 * (2x^1)
        result = chain_rule_derivative([1], [2], 1)
        self.assertEqual(result, "1(1x^2)^0 * (2x^1)")

    def test_chain_rule_derivative_negative_exponent(self):
        # Negative exponent raises ValueError
        with self.assertRaisesRegex(ValueError, "Exponent must be non-negative."):
            chain_rule_derivative([1], [2], -1)

    def test_chain_rule_derivative_float_coefficients(self):
        # g(x) = 1.5x^2, n = 2 => 2(1.5x^2)^1 * (3.0x^1)
        result = chain_rule_derivative([1.5], [2], 2)
        self.assertEqual(result, "2(1.5x^2)^1 * (3.0x^1)")

    def test_chain_rule_derivative_float_powers(self):
        # g(x) = 2x^2.5, n = 2
        # format_polynomial uses int(power) => 2x^2
        # compute_polynomial_derivative: 2*2.5=5.0, 2.5-1=1.5 => power 1.5 cast to int is 1 => 5.0x^1
        result = chain_rule_derivative([2], [2.5], 2)
        self.assertEqual(result, "2(2x^2)^1 * (5.0x^1)")

    def test_chain_rule_derivative_negative_powers(self):
        # g(x) = 3x^-2, n = 2 => 2(3x^-2)^1 * (-6x^-3)
        result = chain_rule_derivative([3], [-2], 2)
        self.assertEqual(result, "2(3x^-2)^1 * (-6x^-3)")

    def test_chain_rule_derivative_negative_coeffs(self):
        # g(x) = -2x^3, n = 2 => 2(-2x^3)^1 * (-6x^2)
        result = chain_rule_derivative([-2], [3], 2)
        self.assertEqual(result, "2(-2x^3)^1 * (-6x^2)")

    def test_chain_rule_derivative_zero_coeffs(self):
        # g(x) = 0x^2, n = 2 => 2(0x^2)^1 * (0x^1)
        result = chain_rule_derivative([0], [2], 2)
        self.assertEqual(result, "2(0x^2)^1 * (0x^1)")

    def test_chain_rule_derivative_empty_inner(self):
        # g(x) = empty, n = 2 => 2()^1 * ()
        result = chain_rule_derivative([], [], 2)
        self.assertEqual(result, "2()^1 * ()")

    def test_chain_rule_derivative_mismatched_lengths(self):
        # Inner coeffs has extra element => zip stops at shorter length
        result = chain_rule_derivative([1, 2, 3], [2, 1], 2)
        self.assertEqual(result, "2(1x^2 + 2x^1)^1 * (2x^1 + 2x^0)")


if __name__ == "__main__":
    unittest.main()
