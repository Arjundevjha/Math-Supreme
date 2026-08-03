import unittest
from Math.Calculus.Differentiation.quotient_rule import (
    format_polynomial,
    compute_polynomial_derivative_str,
    quotient_rule_derivative
)

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
        result = compute_polynomial_derivative_str([3], [2])
        terms = [t.strip() for t in result.split("+")]
        self.assertIn("6x^1", terms)
        self.assertEqual(len(terms), 1)

    def test_compute_polynomial_derivative_str_multiple_terms(self):
        result = compute_polynomial_derivative_str([3, 2, 1], [2, 1, 0])
        terms = [t.strip() for t in result.split("+")]
        self.assertIn("6x^1", terms)
        self.assertIn("2x^0", terms)
        self.assertEqual(len(terms), 2)

    def test_compute_polynomial_derivative_str_constant(self):
        self.assertEqual(compute_polynomial_derivative_str([5], [0]), "0")

    def test_compute_polynomial_derivative_str_zero_coefficient(self):
        result = compute_polynomial_derivative_str([0], [2])
        terms = [t.strip() for t in result.split("+")]
        self.assertIn("0x^1", terms)
        self.assertEqual(len(terms), 1)

    def test_compute_polynomial_derivative_str_float(self):
        result = compute_polynomial_derivative_str([1.5, 2.5], [2, 1])
        terms = [t.strip() for t in result.split("+")]
        self.assertIn("3.0x^1", terms)
        self.assertIn("2.5x^0", terms)
        self.assertEqual(len(terms), 2)

    def test_compute_polynomial_derivative_str_negative_powers(self):
        result = compute_polynomial_derivative_str([3], [-2])
        terms = [t.strip() for t in result.split("+")]
        self.assertIn("-6x^-3", terms)
        self.assertEqual(len(terms), 1)

    def test_compute_polynomial_derivative_str_empty(self):
        self.assertEqual(compute_polynomial_derivative_str([], []), "0")

    def test_quotient_rule_derivative_basic(self):
        result = quotient_rule_derivative([1], [1], [1], [1])
        self.assertEqual(result, "((1x^0) * (1x^1) - (1x^1) * (1x^0)) / (1x^1)^2")

    def test_quotient_rule_derivative_polynomials(self):
        result = quotient_rule_derivative([2], [3], [1], [2])
        self.assertEqual(result, "((6x^2) * (1x^2) - (2x^3) * (2x^1)) / (1x^2)^2")

    def test_quotient_rule_derivative_multiple_terms(self):
        result = quotient_rule_derivative([1, 2], [2, 1], [3, 4], [1, 0])
        self.assertEqual(result, "((2x^1 + 2x^0) * (3x^1 + 4x^0) - (1x^2 + 2x^1) * (3x^0)) / (3x^1 + 4x^0)^2")

    def test_quotient_rule_derivative_constant_numerator(self):
        result = quotient_rule_derivative([5], [0], [2], [1])
        self.assertEqual(result, "((0) * (2x^1) - (5x^0) * (2x^0)) / (2x^1)^2")

    def test_quotient_rule_derivative_constant_denominator(self):
        result = quotient_rule_derivative([2], [1], [5], [0])
        self.assertEqual(result, "((2x^0) * (5x^0) - (2x^1) * (0)) / (5x^0)^2")

    def test_quotient_rule_derivative_negative_coefficients_and_powers(self):
        result = quotient_rule_derivative([-3], [-2], [4], [-1])
        self.assertEqual(result, "((6x^-3) * (4x^-1) - (-3x^-2) * (-4x^-2)) / (4x^-1)^2")

    def test_quotient_rule_derivative_float_coefficients(self):
        result = quotient_rule_derivative([1.5], [2], [2.5], [3])
        self.assertEqual(result, "((3.0x^1) * (2.5x^3) - (1.5x^2) * (7.5x^2)) / (2.5x^3)^2")

    def test_quotient_rule_derivative_zero_coefficients(self):
        result = quotient_rule_derivative([0], [2], [1], [1])
        self.assertEqual(result, "((0x^1) * (1x^1) - (0x^2) * (1x^0)) / (1x^1)^2")

    def test_quotient_rule_derivative_empty_lists(self):
        result = quotient_rule_derivative([], [], [], [])
        self.assertEqual(result, "((0) * () - () * (0)) / ()^2")

    def test_quotient_rule_derivative_fractional_powers(self):
        result = quotient_rule_derivative([1], [2.5], [2], [0.5])
        self.assertEqual(result, "((2.5x^1) * (2x^0) - (1x^2) * (1.0x^0)) / (2x^0)^2")

    def test_quotient_rule_derivative_zero_power_numerator_and_denominator(self):
        result = quotient_rule_derivative([1], [0], [1], [0])
        self.assertEqual(result, "((0) * (1x^0) - (1x^0) * (0)) / (1x^0)^2")

    def test_quotient_rule_derivative_happy_path(self):
        result = quotient_rule_derivative([2], [2], [3], [1])
        self.assertEqual(result, "((4x^1) * (3x^1) - (2x^2) * (3x^0)) / (3x^1)^2")

    def test_quotient_rule_derivative_empty_numerator_edge(self):
        result = quotient_rule_derivative([], [], [1], [1])
        self.assertEqual(result, "((0) * (1x^1) - () * (1x^0)) / (1x^1)^2")

    def test_quotient_rule_derivative_empty_denominator_edge(self):
        result = quotient_rule_derivative([1], [1], [], [])
        self.assertEqual(result, "((1x^0) * () - (1x^1) * (0)) / ()^2")

    def test_quotient_rule_derivative_both_empty_edge(self):
        result = quotient_rule_derivative([], [], [], [])
        self.assertEqual(result, "((0) * () - () * (0)) / ()^2")

    def test_quotient_rule_derivative_fractional_powers_edge(self):
        result = quotient_rule_derivative([1], [0.5], [1], [1.5])
        self.assertEqual(result, "((0.5x^0) * (1x^1) - (1x^0) * (1.5x^0)) / (1x^1)^2")

    def test_quotient_rule_derivative_zero_polynomials_edge(self):
        result = quotient_rule_derivative([0], [0], [1], [1])
        self.assertEqual(result, "((0) * (1x^1) - (0x^0) * (1x^0)) / (1x^1)^2")

    def test_quotient_rule_derivative_type_error(self):
        with self.assertRaises(TypeError):
            quotient_rule_derivative(1, [1], [1], [1])

    def test_quotient_rule_derivative_mismatched_lengths(self):
        # Even though quotient_rule.py format_polynomial and compute_polynomial_derivative_str zip lists,
        # verifying behavior on mismatched array lengths can be helpful. zip() stops at the shortest list.
        result = quotient_rule_derivative([1, 2], [1], [1], [1])
        self.assertEqual(result, "((1x^0) * (1x^1) - (1x^1) * (1x^0)) / (1x^1)^2")

    def test_quotient_rule_derivative_division_by_zero_power(self):
        result = quotient_rule_derivative([1], [1], [1], [-1])
        # poly2 = 1x^-1
        # u_prime = 1x^0
        # v_prime = -1x^-2
        self.assertEqual(result, "((1x^0) * (1x^-1) - (1x^1) * (-1x^-2)) / (1x^-1)^2")

if __name__ == '__main__':
    unittest.main()
