import pytest
import unittest
from Math.Calculus.Differentiation.chain_rule import (
    chain_rule_derivative,
    format_polynomial,
    compute_polynomial_derivative
)

def test_chain_rule_derivative_basic():
    # g(x) = x^2, n = 3 => (x^2)^3 => derivative is 3(x^2)^2 * (2x)
    result = chain_rule_derivative([1], [2], 3)
    assert "3(" in result
    assert "1x^2" in result
    assert ")^2" in result
    assert "* (2x^1)" in result

def test_chain_rule_derivative_multiple_terms():
    # g(x) = x^2 + 2x, n = 3
    result = chain_rule_derivative([1, 2], [2, 1], 3)
    assert "3(" in result
    assert "1x^2 + 2x^1" in result
    assert ")^2" in result
    assert "* (2x^1 + 2x^0)" in result

def test_chain_rule_derivative_constant_inner():
    # g(x) = 5, n = 2 => (5)^2 => derivative is 2(5)^1 * 0
    result = chain_rule_derivative([5], [0], 2)
    assert "2(5x^0)^1" in result
    assert "* ()" in result

def test_chain_rule_derivative_zero_exponent():
    # g(x) = x^2 + 2, n = 0 => (x^2 + 2)^0 => derivative is 0(...)
    result = chain_rule_derivative([1, 2], [2, 0], 0)
    assert result.startswith("0(")

def test_chain_rule_derivative_negative_exponent():
    # Negative exponent should raise ValueError
    with pytest.raises(ValueError, match="Exponent must be non-negative."):
        chain_rule_derivative([1, 2], [2, 0], -1)

def test_chain_rule_derivative_float_coefficients():
    # g(x) = 1.5x^2.5, n = 2 => 2(1.5x^2.5)^1 * (3.75x^1.5)
    result = chain_rule_derivative([1.5], [2.5], 2)
    assert "2(" in result
    assert "1.5x^2" in result
    assert ")^1" in result
    assert "* (3.75x^1)" in result

def test_chain_rule_derivative_empty():
    # g(x) = 0 (empty), n = 3 => 3()^2 * ()
    result = chain_rule_derivative([], [], 3)
    assert "3()^2 * ()" == result

def test_chain_rule_derivative_exponent_one():
    # g(x) = x^3, n = 1 => 1(1x^3)^0 * (3x^2)
    result = chain_rule_derivative([1], [3], 1)
    assert "1(" in result
    assert "1x^3" in result
    assert ")^0" in result
    assert "* (3x^2)" in result

def test_chain_rule_derivative_negative_powers():
    result = chain_rule_derivative([3], [-2], 2)
    assert result == "2(3x^-2)^1 * (-6x^-3)"

def test_chain_rule_derivative_negative_coeffs_powers():
    # g(x) = -3x^-2, n = 4
    result = chain_rule_derivative([-3], [-2], 4)
    assert "4(-3x^-2)^3 * (6x^-3)" in result

def test_chain_rule_derivative_negative_powers_and_coeffs():
    # g(x) = -2x^-3, n = 4 => derivative is 4(-2x^-3)^3 * (6x^-4)
    result = chain_rule_derivative([-2], [-3], 4)
    assert "4(" in result
    assert "-2x^-3" in result
    assert ")^3" in result
    assert "* (6x^-4)" in result

class TestChainRuleFormatPolynomial(unittest.TestCase):
    def test_format_polynomial_single_term(self):
        self.assertEqual(format_polynomial([4], [2]), "4x^2")

    def test_format_polynomial_zero_coefficient(self):
        self.assertEqual(format_polynomial([0, 5], [2, 1]), "0x^2 + 5x^1")

    def test_format_polynomial_fractional_power_cast_to_int(self):
        self.assertEqual(format_polynomial([3], [2.9]), "3x^2")

    def test_format_polynomial_zero_power(self):
        self.assertEqual(format_polynomial([7], [0]), "7x^0")

    def test_format_polynomial_mismatched_lengths(self):
        # zip will truncate to the shorter list
        self.assertEqual(format_polynomial([1, 2], [3]), "1x^3")
        self.assertEqual(format_polynomial([1], [3, 2]), "1x^3")

    def test_format_polynomial_all_zeros(self):
        self.assertEqual(format_polynomial([0, 0], [0, 0]), "0x^0 + 0x^0")

    def test_empty_lists(self):
        self.assertEqual(format_polynomial([], []), "")

class TestComputePolynomialDerivative(unittest.TestCase):
    def test_basic_polynomial(self):
        # f(x) = 3x^2 + 2x^1
        # f'(x) = 6x^1 + 2x^0
        coeffs = [3, 2]
        powers = [2, 1]
        expected_coeffs = [6, 2]
        expected_powers = [1, 0]
        self.assertEqual(compute_polynomial_derivative(coeffs, powers), (expected_coeffs, expected_powers))

    def test_constant_term(self):
        # f(x) = 5x^0
        # f'(x) = 0
        coeffs = [5]
        powers = [0]
        expected_coeffs = []
        expected_powers = []
        self.assertEqual(compute_polynomial_derivative(coeffs, powers), (expected_coeffs, expected_powers))

    def test_mixed_terms_with_constant(self):
        # f(x) = 4x^3 + 2x^0 + x^1
        # f'(x) = 12x^2 + 1x^0
        coeffs = [4, 2, 1]
        powers = [3, 0, 1]
        expected_coeffs = [12, 1]
        expected_powers = [2, 0]
        self.assertEqual(compute_polynomial_derivative(coeffs, powers), (expected_coeffs, expected_powers))

    def test_negative_powers(self):
        # f(x) = 2x^-2
        # f'(x) = -4x^-3
        coeffs = [2]
        powers = [-2]
        expected_coeffs = [-4]
        expected_powers = [-3]
        self.assertEqual(compute_polynomial_derivative(coeffs, powers), (expected_coeffs, expected_powers))

    def test_fractional_powers(self):
        # f(x) = 4x^0.5
        # f'(x) = 2.0x^-0.5
        coeffs = [4]
        powers = [0.5]
        expected_coeffs = [2.0]
        expected_powers = [-0.5]
        self.assertEqual(compute_polynomial_derivative(coeffs, powers), (expected_coeffs, expected_powers))

    def test_float_coefficients(self):
        # f(x) = 1.5x^2
        # f'(x) = 3.0x^1
        coeffs = [1.5]
        powers = [2]
        expected_coeffs = [3.0]
        expected_powers = [1]
        self.assertEqual(compute_polynomial_derivative(coeffs, powers), (expected_coeffs, expected_powers))

    def test_zero_coefficients(self):
        # f(x) = 0x^2
        # f'(x) = 0x^1
        coeffs = [0]
        powers = [2]
        expected_coeffs = [0]
        expected_powers = [1]
        self.assertEqual(compute_polynomial_derivative(coeffs, powers), (expected_coeffs, expected_powers))

    def test_negative_coefficients(self):
        # f(x) = -3x^2 - 2x^1
        # f'(x) = -6x^1 - 2x^0
        coeffs = [-3, -2]
        powers = [2, 1]
        expected_coeffs = [-6, -2]
        expected_powers = [1, 0]
        self.assertEqual(compute_polynomial_derivative(coeffs, powers), (expected_coeffs, expected_powers))

    def test_multiple_zero_powers(self):
        # f(x) = 5 + 3
        # f'(x) = 0
        coeffs = [5, 3]
        powers = [0, 0]
        expected_coeffs = []
        expected_powers = []
        self.assertEqual(compute_polynomial_derivative(coeffs, powers), (expected_coeffs, expected_powers))

    def test_mismatched_lengths(self):
        # f(x) = 3x^2 + 2x^1 (powers list has an extra element)
        coeffs = [3, 2]
        powers = [2, 1, 0]
        expected_coeffs = [6, 2]
        expected_powers = [1, 0]
        self.assertEqual(compute_polynomial_derivative(coeffs, powers), (expected_coeffs, expected_powers))

        # coeffs list has an extra element
        coeffs2 = [3, 2, 1]
        powers2 = [2, 1]
        self.assertEqual(compute_polynomial_derivative(coeffs2, powers2), (expected_coeffs, expected_powers))

    def test_empty_polynomial(self):
        # f(x) = 0
        # f'(x) = 0
        coeffs = []
        powers = []
        expected_coeffs = []
        expected_powers = []
        self.assertEqual(compute_polynomial_derivative(coeffs, powers), (expected_coeffs, expected_powers))

if __name__ == '__main__':
    unittest.main()
