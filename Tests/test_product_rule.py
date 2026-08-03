import unittest
from Math.Calculus.Differentiation.product_rule import (
    product_rule_derivative,
    format_polynomial as format_polynomial_product_rule,
    compute_polynomial_derivative_str
)

def test_product_rule_derivative_basic():
    # u(x) = x, v(x) = x
    # u'v + uv' = (1x^0) * (1x^1) + (1x^1) * (1x^0)
    result = product_rule_derivative([1], [1], [1], [1])
    assert result == "(1x^0) * (1x^1) + (1x^1) * (1x^0)"

def test_product_rule_derivative_complex():
    # u(x) = 2x^2 + 3x, v(x) = 4x^3
    result = product_rule_derivative([2, 3], [2, 1], [4], [3])
    assert "(4x^1 + 3x^0) * (4x^3) + (2x^2 + 3x^1) * (12x^2)" == result

def test_product_rule_derivative_constant():
    # u(x) = 5, v(x) = x
    result = product_rule_derivative([5], [0], [1], [1])
    assert result == "(0) * (1x^1) + (5x^0) * (1x^0)"

def test_product_rule_derivative_multiple_terms():
    # u(x) = 3x^3 + 2x^2 + x, v(x) = 5x^2 + 4
    # u_prime = 9x^2 + 4x^1 + 1x^0
    # v_prime = 10x^1
    result = product_rule_derivative([3, 2, 1], [3, 2, 1], [5, 4], [2, 0])
    expected = "(9x^2 + 4x^1 + 1x^0) * (5x^2 + 4x^0) + (3x^3 + 2x^2 + 1x^1) * (10x^1)"
    assert result == expected

def test_product_rule_derivative_empty_polynomials():
    # u(x) = empty, v(x) = empty
    result = product_rule_derivative([], [], [], [])
    assert result == "0"

def test_product_rule_derivative_floating_point():
    # u(x) = 1.5x^2, v(x) = 2.5x^3
    result = product_rule_derivative([1.5], [2.0], [2.5], [3.0])
    assert result == "(3.0x^1) * (2.5x^3) + (1.5x^2) * (7.5x^2)"

def test_product_rule_derivative_negative_powers():
    # u(x) = 2x^-1, v(x) = 3x^-2
    result = product_rule_derivative([2], [-1], [3], [-2])
    assert result == "(-2x^-2) * (3x^-2) + (2x^-1) * (-6x^-3)"

def test_product_rule_derivative_zero_coefficients():
    # u(x) = 0x^2, v(x) = 5x^3
    result = product_rule_derivative([0], [2], [5], [3])
    assert result == "(0x^1) * (5x^3) + (0x^2) * (15x^2)"

def test_product_rule_derivative_both_constants():
    # u(x) = 5, v(x) = 7
    result = product_rule_derivative([5], [0], [7], [0])
    assert result == "(0) * (7x^0) + (5x^0) * (0)"


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

    def test_format_polynomial_product_rule_negative_powers_split(self):
        result = format_polynomial_product_rule([2, 3], [-1, -2])
        terms = [t.strip() for t in result.split('+')]
        self.assertIn("2x^-1", terms)
        self.assertIn("3x^-2", terms)
        self.assertEqual(len(terms), 2)

    def test_format_polynomial_product_rule_mixed_signs_split(self):
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


class TestProductRuleComputePolynomialDerivativeStr(unittest.TestCase):
    def test_compute_polynomial_derivative_str_single_term(self):
        self.assertEqual(compute_polynomial_derivative_str([3], [2]), "6x^1")

    def test_compute_polynomial_derivative_str_multiple_terms(self):
        self.assertEqual(compute_polynomial_derivative_str([3, 4], [2, 1]), "6x^1 + 4x^0")

    def test_compute_polynomial_derivative_str_constant_term(self):
        self.assertEqual(compute_polynomial_derivative_str([5], [0]), "0")

    def test_compute_polynomial_derivative_str_zero_coefficient(self):
        self.assertEqual(compute_polynomial_derivative_str([0], [2]), "0x^1")

    def test_compute_polynomial_derivative_str_float(self):
        self.assertEqual(compute_polynomial_derivative_str([1.5, 2.5], [2, 1]), "3.0x^1 + 2.5x^0")

    def test_compute_polynomial_derivative_str_negative_powers(self):
        self.assertEqual(compute_polynomial_derivative_str([3], [-2]), "-6x^-3")

    def test_compute_polynomial_derivative_str_empty(self):
        self.assertEqual(compute_polynomial_derivative_str([], []), "0")

    def test_compute_polynomial_derivative_str_mixed_terms(self):
        # 2x^3 + 5x^0 + 1x^1 -> derivative is 6x^2 + 1x^0
        self.assertEqual(compute_polynomial_derivative_str([2, 5, 1], [3, 0, 1]), "6x^2 + 1x^0")


if __name__ == '__main__':
    unittest.main()
