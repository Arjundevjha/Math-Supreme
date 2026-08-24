import math
import unittest

import pytest

from Math.Calculus.Differentiation.product_rule import product_rule_derivative
from Math.Calculus.Differentiation.quotient_rule import quotient_rule_derivative
from Math.Calculus.Differentiation.simple_diffrentiation_function import (
    differentiate_polynomial,
)
from Math.Calculus.Differentiation.utils import (
    compute_polynomial_derivative,
    compute_polynomial_derivative_str,
    format_polynomial,
)

format_polynomial_product_rule = format_polynomial
compute_polynomial_derivative_str_quotient = compute_polynomial_derivative_str



def test_compute_polynomial_derivative_str_single_term():
    assert compute_polynomial_derivative_str([3], [2]) == "6x^1"

def test_compute_polynomial_derivative_str_multiple_terms():
    assert compute_polynomial_derivative_str([3, 4], [2, 1]) == "6x^1 + 4x^0"

def test_compute_polynomial_derivative_str_constant_term():
    assert compute_polynomial_derivative_str([5], [0]) == "0"

def test_compute_polynomial_derivative_str_mixed_terms():
    # 2x^3 + 5x^0 + 1x^1 -> derivative is 6x^2 + 1x^0
    assert compute_polynomial_derivative_str([2, 5, 1], [3, 0, 1]) == "6x^2 + 1x^0"

def test_compute_polynomial_derivative_str_empty():
    assert compute_polynomial_derivative_str([], []) == "0"

def test_compute_polynomial_derivative_str_negative_powers_and_floats():
    assert compute_polynomial_derivative_str([2.5, 3], [-2, 0]) == "-5.0x^-3"

def test_format_polynomial_basic():
    coeffs = [2, 3]
    powers = [2, 1]
    result = format_polynomial(coeffs, powers)
    terms = [t.strip() for t in result.split('+')]
    assert "2x^2" in terms
    assert "3x^1" in terms

def test_format_polynomial_floats():
    coeffs = [2.5, 3.1]
    powers = [2.0, 0.0]
    result = format_polynomial(coeffs, powers)
    terms = [t.strip() for t in result.split('+')]
    assert "2.5x^2" in terms
    assert "3.1x^0" in terms

def test_format_polynomial_negative_powers_and_coeffs():
    coeffs = [-1, 0]
    powers = [-2, 3]
    result = format_polynomial(coeffs, powers)
    terms = [t.strip() for t in result.split('+')]
    assert "-1x^-2" in terms
    assert "0x^3" in terms

def test_format_polynomial_empty():
    coeffs = []
    powers = []
    result = format_polynomial(coeffs, powers)
    assert result.strip() == ""

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
def test_quotient_rule_derivative_basic():
    # u(x) = x, v(x) = x
    # u' = 1x^0, v' = 1x^0
    # Expected: ((1x^0) * (1x^1) - (1x^1) * (1x^0)) / (1x^1)^2
    result = quotient_rule_derivative([1], [1], [1], [1])
    assert result == "((1x^0) * (1x^1) - (1x^1) * (1x^0)) / (1x^1)^2"

def test_quotient_rule_derivative_polynomials():
    # u(x) = 2x^3, v(x) = x^2
    # u' = 6x^2, v' = 2x^1
    # Expected: ((6x^2) * (1x^2) - (2x^3) * (2x^1)) / (1x^2)^2
    result = quotient_rule_derivative([2], [3], [1], [2])
    assert result == "((6x^2) * (1x^2) - (2x^3) * (2x^1)) / (1x^2)^2"

def test_quotient_rule_derivative_multiple_terms():
    # u(x) = x^2 + 2x, v(x) = 3x + 4
    # u' = 2x^1 + 2x^0, v' = 3x^0
    # Expected: ((2x^1 + 2x^0) * (3x^1 + 4x^0) - (1x^2 + 2x^1) * (3x^0)) / (3x^1 + 4x^0)^2
    result = quotient_rule_derivative([1, 2], [2, 1], [3, 4], [1, 0])
    assert result == "((2x^1 + 2x^0) * (3x^1 + 4x^0) - (1x^2 + 2x^1) * (3x^0)) / (3x^1 + 4x^0)^2"

def test_quotient_rule_derivative_constant_numerator():
    # u(x) = 5, v(x) = 2x
    # u' = 0, v' = 2x^0
    # Expected: ((0) * (2x^1) - (5x^0) * (2x^0)) / (2x^1)^2
    result = quotient_rule_derivative([5], [0], [2], [1])
    assert result == "((0) * (2x^1) - (5x^0) * (2x^0)) / (2x^1)^2"

def test_quotient_rule_derivative_constant_denominator():
    # u(x) = 2x, v(x) = 5
    # u' = 2x^0, v' = 0
    # Expected: ((2x^0) * (5x^0) - (2x^1) * (0)) / (5x^0)^2
    result = quotient_rule_derivative([2], [1], [5], [0])
    assert result == "((2x^0) * (5x^0) - (2x^1) * (0)) / (5x^0)^2"

def test_quotient_rule_derivative_negative_coefficients_and_powers():
    # u(x) = -3x^-2, v(x) = 4x^-1
    # u' = 6x^-3, v' = -4x^-2
    # Expected: ((6x^-3) * (4x^-1) - (-3x^-2) * (-4x^-2)) / (4x^-1)^2
    result = quotient_rule_derivative([-3], [-2], [4], [-1])
    assert result == "((6x^-3) * (4x^-1) - (-3x^-2) * (-4x^-2)) / (4x^-1)^2"

def test_quotient_rule_derivative_float_coefficients():
    # u(x) = 1.5x^2, v(x) = 2.5x^3
    # u' = 3.0x^1, v' = 7.5x^2
    # Expected: ((3.0x^1) * (2.5x^3) - (1.5x^2) * (7.5x^2)) / (2.5x^3)^2
    result = quotient_rule_derivative([1.5], [2], [2.5], [3])
    assert result == "((3.0x^1) * (2.5x^3) - (1.5x^2) * (7.5x^2)) / (2.5x^3)^2"

def test_quotient_rule_derivative_zero_coefficients():
    # u(x) = 0x^2, v(x) = 1x^1
    # u' = 0x^1, v' = 1x^0
    # Expected: ((0x^1) * (1x^1) - (0x^2) * (1x^0)) / (1x^1)^2
    result = quotient_rule_derivative([0], [2], [1], [1])
    assert result == "((0x^1) * (1x^1) - (0x^2) * (1x^0)) / (1x^1)^2"

def test_quotient_rule_derivative_empty_lists():
    # u(x) = empty, v(x) = empty
    # u' = 0, v' = 0
    # Expected: ((0) * () - () * (0)) / ()^2
    result = quotient_rule_derivative([], [], [], [])
    assert result == "((0) * () - () * (0)) / ()^2"

def test_quotient_rule_derivative_fractional_powers():
    # u(x) = 1x^2.5 -> format converts power to int, so 1x^2
    # compute derivative converts new power to int: 2.5 * 1 = 2.5, power = 1.5 -> int is 1
    # u' = 2.5x^1
    # v(x) = 2x^0.5 -> format converts power to int, so 2x^0
    # v' = 0.5 * 2 = 1.0, power = -0.5 -> int is 0
    # v' = 1.0x^0
    result = quotient_rule_derivative([1], [2.5], [2], [0.5])
    assert result == "((2.5x^1) * (2x^0) - (1x^2) * (1.0x^0)) / (2x^0)^2"

def test_quotient_rule_derivative_zero_power_numerator_and_denominator():
    # u(x) = 1x^0, v(x) = 1x^0
    # u' = 0, v' = 0
    result = quotient_rule_derivative([1], [0], [1], [0])
    assert result == "((0) * (1x^0) - (1x^0) * (0)) / (1x^0)^2"
class TestQuotientRule(unittest.TestCase):
    def test_format_polynomial_quotient_rule_basic(self):
        self.assertEqual(format_polynomial([3], [2]), "3x^2")

    def test_format_polynomial_quotient_rule_multiple_terms(self):
        self.assertEqual(format_polynomial([3, 2, 1], [2, 1, 0]), "3x^2 + 2x^1 + 1x^0")

    def test_format_polynomial_quotient_rule_floats(self):
        self.assertEqual(format_polynomial([1.5, 2.5], [2, 1]), "1.5x^2 + 2.5x^1")

    def test_format_polynomial_quotient_rule_negative_powers(self):
        self.assertEqual(format_polynomial([3], [-2]), "3x^-2")

    def test_format_polynomial_quotient_rule_empty(self):
        self.assertEqual(format_polynomial([], []), "")

    def test_compute_polynomial_derivative_str_basic(self):
        result = compute_polynomial_derivative_str_quotient([3], [2])
        terms = [t.strip() for t in result.split("+")]
        self.assertIn("6x^1", terms)
        self.assertEqual(len(terms), 1)

    def test_compute_polynomial_derivative_str_multiple_terms(self):
        result = compute_polynomial_derivative_str_quotient([3, 2, 1], [2, 1, 0])
        terms = [t.strip() for t in result.split("+")]
        self.assertIn("6x^1", terms)
        self.assertIn("2x^0", terms)
        self.assertEqual(len(terms), 2)

    def test_compute_polynomial_derivative_str_constant(self):
        self.assertEqual(compute_polynomial_derivative_str_quotient([5], [0]), "0")

    def test_compute_polynomial_derivative_str_zero_coefficient(self):
        result = compute_polynomial_derivative_str_quotient([0], [2])
        terms = [t.strip() for t in result.split("+")]
        self.assertIn("0x^1", terms)
        self.assertEqual(len(terms), 1)

    def test_compute_polynomial_derivative_str_float(self):
        result = compute_polynomial_derivative_str_quotient([1.5, 2.5], [2, 1])
        terms = [t.strip() for t in result.split("+")]
        self.assertIn("3.0x^1", terms)
        self.assertIn("2.5x^0", terms)
        self.assertEqual(len(terms), 2)

    def test_compute_polynomial_derivative_str_negative_powers(self):
        result = compute_polynomial_derivative_str_quotient([3], [-2])
        terms = [t.strip() for t in result.split("+")]
        self.assertIn("-6x^-3", terms)
        self.assertEqual(len(terms), 1)

    def test_compute_polynomial_derivative_str_empty(self):
        self.assertEqual(compute_polynomial_derivative_str_quotient([], []), "0")

class TestComputePolynomialDerivative:
    def test_basic_polynomial(self):
        # f(x) = 3x^2 + 2x^1
        # f'(x) = 6x^1 + 2x^0
        coeffs = [3, 2]
        powers = [2, 1]
        expected_coeffs = [6, 2]
        expected_powers = [1, 0]
        assert compute_polynomial_derivative(coeffs, powers) == (expected_coeffs, expected_powers)

    def test_constant_term(self):
        # f(x) = 5x^0
        # f'(x) = 0
        coeffs = [5]
        powers = [0]
        expected_coeffs = []
        expected_powers = []
        assert compute_polynomial_derivative(coeffs, powers) == (expected_coeffs, expected_powers)

    def test_mixed_terms_with_constant(self):
        # f(x) = 4x^3 + 2x^0 + x^1
        # f'(x) = 12x^2 + 1x^0
        coeffs = [4, 2, 1]
        powers = [3, 0, 1]
        expected_coeffs = [12, 1]
        expected_powers = [2, 0]
        assert compute_polynomial_derivative(coeffs, powers) == (expected_coeffs, expected_powers)

    def test_negative_powers(self):
        # f(x) = 2x^-2
        # f'(x) = -4x^-3
        coeffs = [2]
        powers = [-2]
        expected_coeffs = [-4]
        expected_powers = [-3]
        assert compute_polynomial_derivative(coeffs, powers) == (expected_coeffs, expected_powers)

    def test_fractional_powers(self):
        # f(x) = 4x^0.5
        # f'(x) = 2.0x^-0.5
        coeffs = [4]
        powers = [0.5]
        expected_coeffs = [2.0]
        expected_powers = [-0.5]
        assert compute_polynomial_derivative(coeffs, powers) == (expected_coeffs, expected_powers)

    def test_float_coefficients(self):
        # f(x) = 1.5x^2
        # f'(x) = 3.0x^1
        coeffs = [1.5]
        powers = [2]
        expected_coeffs = [3.0]
        expected_powers = [1]
        assert compute_polynomial_derivative(coeffs, powers) == (expected_coeffs, expected_powers)

    def test_zero_coefficients(self):
        # f(x) = 0x^2
        # f'(x) = 0x^1
        coeffs = [0]
        powers = [2]
        expected_coeffs = [0]
        expected_powers = [1]
        assert compute_polynomial_derivative(coeffs, powers) == (expected_coeffs, expected_powers)

    def test_negative_coefficients(self):
        # f(x) = -3x^2 - 2x^1
        # f'(x) = -6x^1 - 2x^0
        coeffs = [-3, -2]
        powers = [2, 1]
        expected_coeffs = [-6, -2]
        expected_powers = [1, 0]
        assert compute_polynomial_derivative(coeffs, powers) == (expected_coeffs, expected_powers)

    def test_multiple_zero_powers(self):
        # f(x) = 5 + 3
        # f'(x) = 0
        coeffs = [5, 3]
        powers = [0, 0]
        expected_coeffs = []
        expected_powers = []
        assert compute_polynomial_derivative(coeffs, powers) == (expected_coeffs, expected_powers)

    def test_mismatched_lengths(self):
        # f(x) = 3x^2 + 2x^1 (powers list has an extra element)
        coeffs = [3, 2]
        powers = [2, 1, 0]
        expected_coeffs = [6, 2]
        expected_powers = [1, 0]
        assert compute_polynomial_derivative(coeffs, powers) == (expected_coeffs, expected_powers)

        # coeffs list has an extra element
        coeffs2 = [3, 2, 1]
        powers2 = [2, 1]
        assert compute_polynomial_derivative(coeffs2, powers2) == (expected_coeffs, expected_powers)

    def test_empty_polynomial(self):
        # f(x) = 0
        # f'(x) = 0
        coeffs = []
        powers = []
        expected_coeffs = []
        expected_powers = []
        assert compute_polynomial_derivative(coeffs, powers) == (expected_coeffs, expected_powers)
class TestCalculusDifferentiation(unittest.TestCase):
    def test_format_polynomial_product_rule_basic(self):
        result = format_polynomial_product_rule([2, 3], [1, 2])
        terms = [t.strip() for t in result.split('+')]
        self.assertIn("2x^1", terms)
        self.assertIn("3x^2", terms)
        self.assertEqual(len(terms), 2)

    def test_format_polynomial_product_rule_empty(self):
        self.assertEqual(format_polynomial_product_rule([], []), "")

    def test_format_polynomial_product_rule_single_term(self):
        self.assertEqual(format_polynomial_product_rule([5], [0]).strip(), "5x^0")

    def test_format_polynomial_product_rule_floats(self):
        result = format_polynomial_product_rule([2.5, 3.1], [1.0, 2.0])
        terms = [t.strip() for t in result.split('+')]
        self.assertIn("2.5x^1", terms)
        self.assertIn("3.1x^2", terms)
        self.assertEqual(len(terms), 2)

    def test_format_polynomial_product_rule_zero_coeff(self):
        result = format_polynomial_product_rule([0, 1], [2, 1])
        terms = [t.strip() for t in result.split('+')]
        self.assertIn("0x^2", terms)
        self.assertIn("1x^1", terms)
        self.assertEqual(len(terms), 2)

    def test_format_polynomial_product_rule_negative_coeffs(self):
        result = format_polynomial_product_rule([-2, -3], [1, 2])
        terms = [t.strip() for t in result.split('+')]
        self.assertIn("-2x^1", terms)
        self.assertIn("-3x^2", terms)
        self.assertEqual(len(terms), 2)

    def test_format_polynomial_product_rule_negative_powers(self):
        result = format_polynomial_product_rule([2, 3], [-1, -2])
        terms = [t.strip() for t in result.split('+')]
        self.assertIn("2x^-1", terms)
        self.assertIn("3x^-2", terms)
        self.assertEqual(len(terms), 2)

    def test_format_polynomial_product_rule_mixed_signs(self):
        result = format_polynomial_product_rule([-2.5, 4], [3, -1.0])
        terms = [t.strip() for t in result.split('+')]
        self.assertIn("-2.5x^3", terms)
        self.assertIn("4x^-1", terms)
        self.assertEqual(len(terms), 2)

    def test_format_polynomial_product_rule_negative_coeff(self):
        self.assertEqual(format_polynomial_product_rule([-2, -3], [1, 2]), "-2x^1 + -3x^2")

    def test_format_polynomial_product_rule_negative_powers(self):
        self.assertEqual(format_polynomial_product_rule([2, 3], [-1, -2]), "2x^-1 + 3x^-2")

    def test_format_polynomial_product_rule_mismatched_lengths(self):
        # zip behavior will stop at the shortest list
        self.assertEqual(format_polynomial_product_rule([2, 3, 4], [1, 2]), "2x^1 + 3x^2")
        self.assertEqual(format_polynomial_product_rule([2, 3], [1, 2, 3]), "2x^1 + 3x^2")

    def test_format_polynomial_product_rule_negative_powers_and_coeffs(self):
        self.assertEqual(format_polynomial_product_rule([-1, -2], [-1, -2]), "-1x^-1 + -2x^-2")

    def test_format_polynomial_product_rule_mixed_signs(self):
        self.assertEqual(format_polynomial_product_rule([-3, 4], [2, -1]), "-3x^2 + 4x^-1")

def test_quotient_rule_derivative_happy_path():
    # Normal polynomial differentiation: u(x) = 2x^2, v(x) = 3x^1
    # u' = 4x^1, v' = 3x^0
    result = quotient_rule_derivative([2], [2], [3], [1])
    assert result == "((4x^1) * (3x^1) - (2x^2) * (3x^0)) / (3x^1)^2"

def test_quotient_rule_derivative_empty_numerator_edge():
    # u(x) = 0 (empty), v(x) = x
    result = quotient_rule_derivative([], [], [1], [1])
    assert result == "((0) * (1x^1) - () * (1x^0)) / (1x^1)^2"

def test_quotient_rule_derivative_empty_denominator_edge():
    # u(x) = x, v(x) = 0 (empty)
    result = quotient_rule_derivative([1], [1], [], [])
    assert result == "((1x^0) * () - (1x^1) * (0)) / ()^2"

def test_quotient_rule_derivative_both_empty_edge():
    # u(x) = 0 (empty), v(x) = 0 (empty)
    result = quotient_rule_derivative([], [], [], [])
    assert result == "((0) * () - () * (0)) / ()^2"

def test_quotient_rule_derivative_fractional_powers_edge():
    result = quotient_rule_derivative([1], [0.5], [1], [1.5])
    assert result == "((0.5x^0) * (1x^1) - (1x^0) * (1.5x^0)) / (1x^1)^2"

def test_quotient_rule_derivative_zero_polynomials_edge():
    result = quotient_rule_derivative([0], [0], [1], [1])
    assert result == "((0) * (1x^1) - (0x^0) * (1x^0)) / (1x^1)^2"

if __name__ == '__main__':
    unittest.main()

