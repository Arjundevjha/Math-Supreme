import os
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)
math_dir = os.path.join(root_dir, 'Math')
if math_dir not in sys.path:
    sys.path.insert(0, math_dir)


math_dir = os.path.join(root_dir, 'Math')
if math_dir not in sys.path:
    sys.path.insert(0, math_dir)
import pytest
import math
import unittest
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
math_dir = os.path.join(root_dir, 'Math')
math_dir = os.path.join(root_dir, "Math")
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)
if math_dir not in sys.path:
    sys.path.insert(0, math_dir)

math_dir = os.path.abspath(os.path.join(root_dir, 'Math'))
if math_dir not in sys.path:
    sys.path.insert(0, math_dir)

math_dir = os.path.join(root_dir, 'Math')
if math_dir not in sys.path:
    sys.path.insert(0, math_dir)

math_dir = os.path.join(root_dir, 'Math')
math_dir = os.path.join(root_dir, "Math")
if math_dir not in sys.path:
    sys.path.insert(0, math_dir)
math_dir = os.path.join(root_dir, 'Math')
if math_dir not in sys.path:
    sys.path.insert(0, math_dir)

math_dir = os.path.join(root_dir, 'Math')
if math_dir not in sys.path:
    sys.path.insert(0, math_dir)

    sys.path.insert(0, os.path.join(root_dir, "Math"))

math_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Math'))
if math_dir not in sys.path:
    sys.path.insert(0, math_dir)

from Math.Calculus.Differentiation.second_derivatives import second_derivative
math_dir = os.path.join(root_dir, "Math")
if math_dir not in sys.path:
    sys.path.insert(0, math_dir)
from Math.Calculus.Differentiation.product_rule import compute_polynomial_derivative_str, product_rule_derivative, format_polynomial as format_polynomial_product_rule
from Math.Calculus.Integration.NumIntegration import integrate_polynomial, format_polynomial_integration
from Math.Calculus.Differentiation.quotient_rule import format_polynomial, quotient_rule_derivative, compute_polynomial_derivative_str as compute_polynomial_derivative_str_quotient
from Math.Calculus.Differentiation.chain_rule import chain_rule_derivative, format_polynomial as format_polynomial_chain_rule, compute_polynomial_derivative
from Math.Calculus.Integration.TrigIntegration import integrate_cos, integrate_sin
from Math.Calculus.Differentiation.simple_diffrentiation_function import differentiate_polynomial

def test_second_derivative_quadratic():
    # 3x^2 + 2x + 1 -> y'' = 6
    coeffs = [3, 2, 1]
    powers = [2, 1, 0]
    assert second_derivative(coeffs, powers) == [(6, 0)]

def test_second_derivative_cubic():
    # 4x^3 - 2x^2 + x - 5 -> y'' = 24x - 4
    coeffs = [4, -2, 1, -5]
    powers = [3, 2, 1, 0]
    assert second_derivative(coeffs, powers) == [(24, 1), (-4, 0)]

def test_second_derivative_constant():
    # y = 5 -> y'' = 0 (represented as empty list)
    coeffs = [5]
    powers = [0]
    assert second_derivative(coeffs, powers) == []

def test_second_derivative_linear():
    # y = 3x -> y'' = 0 (represented as empty list)
    coeffs = [3]
    powers = [1]
    assert second_derivative(coeffs, powers) == []

def test_second_derivative_empty():
    assert second_derivative([], []) == []

def test_second_derivative_floats():
    # 2.5x^4 -> y'' = 30.0x^2
    coeffs = [2.5]
    powers = [4.0]
    assert second_derivative(coeffs, powers) == [(30.0, 2.0)]

def test_second_derivative_negative_powers():
    # Based on the current implementation, powers <= 0 are ignored
    # d/dx(3x^-2) -> empty list since power is not > 0
    coeffs = [3]
    powers = [-2]
    assert second_derivative(coeffs, powers) == []

def test_second_derivative_zero_coefficients():
    # d/dx(0x^3) -> 0x^2 -> 0x^1
    coeffs = [0]
    powers = [3]
    assert second_derivative(coeffs, powers) == [(0, 1)]

def test_second_derivative_mixed():
    # 3x^3 + 2x^2 + 5x - 4x^-2 -> y'' = 18x + 4
    coeffs = [3, 2, 5, -4]
    powers = [3, 2, 1, -2]
    assert second_derivative(coeffs, powers) == [(18, 1), (4, 0)]
def test_second_derivative_zero_coeffs():
    # 0x^3 + 0x^2 -> y'' = 0x
    coeffs = [0, 0]
    powers = [3, 2]
    assert second_derivative(coeffs, powers) == [(0, 1), (0, 0)]

def test_second_derivative_unordered_powers():
    # x + 4x^3 - 2x^2 - 5 -> y'' = 24x - 4
    coeffs = [1, 4, -2, -5]
    powers = [1, 3, 2, 0]
    assert second_derivative(coeffs, powers) == [(24, 1), (-4, 0)]

def test_second_derivative_mismatched_lengths():
    # zip() behavior
    coeffs = [4, -2]
    powers = [3]
    assert second_derivative(coeffs, powers) == [(24, 1)]

def test_second_derivative_negative_powers():
    # Currently code ignores powers <= 0 for derivatives
    # Let's verify this behavior
    coeffs = [3, 2]
    powers = [-2, -1]
    assert second_derivative(coeffs, powers) == []

def test_second_derivative_large_numbers():
    # 1000x^1000 -> y'' = 1000 * 1000 * 999 x^998 = 999000000x^998
    coeffs = [1000]
    powers = [1000]
    assert second_derivative(coeffs, powers) == [(999000000, 998)]
    # Negative powers are skipped in the current implementation
    assert second_derivative([3], [-2]) == []

def test_second_derivative_fractional_powers_skipped():
    # Power becomes <= 0 after first derivative
    assert second_derivative([4], [0.5]) == []

def test_second_derivative_fractional_powers_kept():
    # Power remains > 0 after first derivative
    assert second_derivative([4], [2.5]) == [(15.0, 0.5)]

def test_second_derivative_mixed_skipped():
    # Mix of valid and skipped powers
    assert second_derivative([3, 2, 1], [3, 0.5, -1]) == [(18, 1)]

def test_second_derivative_zero_coefficients():
    # Zero coefficients should be processed properly
    assert second_derivative([0], [3]) == [(0, 1)]

def test_second_derivative_mismatched_lengths():
    # zip handles mismatched lengths by stopping at the shortest
    assert second_derivative([1, 2], [3]) == [(6, 1)]

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

def test_integrate_polynomial_basic():

    # ∫(3x^2 + 2x + 1)dx = x^3 + x^2 + x + C
    coeffs = [3, 2, 1]
    powers = [2, 1, 0]
    expected_coeffs = [1.0, 1.0, 1.0]
    expected_powers = [3, 2, 1]

    assert integrate_polynomial(coeffs, powers) == (expected_coeffs, expected_powers)

def test_integrate_polynomial_negative_powers():
    # ∫(x^-2)dx = -x^-1
    coeffs = [1]
    powers = [-2]
    expected_coeffs = [-1.0]
    expected_powers = [-1]

    assert integrate_polynomial(coeffs, powers) == (expected_coeffs, expected_powers)

def test_integrate_polynomial_fractional_powers():
    # ∫(x^0.5)dx = (2/3)x^1.5
    coeffs = [1]
    powers = [0.5]
    expected_coeffs = [1 / 1.5]
    expected_powers = [1.5]

    assert integrate_polynomial(coeffs, powers) == (expected_coeffs, expected_powers)

def test_integrate_polynomial_zero_coefficients():
    # ∫(0x^2)dx = 0
    coeffs = [0]
    powers = [2]
    expected_coeffs = [0.0]
    expected_powers = [3]

    assert integrate_polynomial(coeffs, powers) == (expected_coeffs, expected_powers)

def test_integrate_polynomial_empty():
    # ∫(0)dx = C
    coeffs = []
    powers = []
    expected_coeffs = []
    expected_powers = []

    assert integrate_polynomial(coeffs, powers) == (expected_coeffs, expected_powers)

def test_integrate_polynomial_power_minus_one():
    # ∫(x^-1)dx raises ZeroDivisionError in this naive implementation
    coeffs = [1]
    powers = [-1]

    with pytest.raises(ZeroDivisionError):
        integrate_polynomial(coeffs, powers)

    assert integrate_polynomial([], []) == ([], [])

def test_integrate_polynomial_power_negative_one():
    # ∫(x^-1)dx requires ln|x|, the power rule fails with ZeroDivisionError
    coeffs = [1]
    powers = [-1]
    with pytest.raises(ZeroDivisionError):
        integrate_polynomial(coeffs, powers)

def test_integrate_polynomial_mixed_terms():
    coeffs = [3, -2, 1.5, 0]
    powers = [2, -3, 0.5, 1]
    expected_coeffs = [1.0, 1.0, 1.0, 0.0]
    expected_powers = [3, -2, 1.5, 2]
    assert integrate_polynomial(coeffs, powers) == (expected_coeffs, expected_powers)

def test_format_polynomial_integration_basic():
    # x^3 + x^2 + x + C
    coeffs = [1.0, 1.0, 1.0]
    powers = [3, 2, 1]

    assert format_polynomial_integration(coeffs, powers) == "1.0x^3 + 1.0x^2 + 1.0x + C"

def test_format_polynomial_integration_zero_power():
    # 5
    coeffs = [5.0]
    powers = [0]

    assert format_polynomial_integration(coeffs, powers) == "5.0 + C"

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

def test_chain_rule_derivative_basic():
    # g(x) = x^2, n = 3 => (x^2)^3 => derivative is 3(x^2)^2 * (2x)
    result = chain_rule_derivative([1], [2], 3)
    # Check parts of the string independently to avoid brittle tests
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
def test_chain_rule_derivative_empty():
    result = chain_rule_derivative([], [], 2)
    assert result == "2()^1 * ()"

def test_chain_rule_derivative_float_coeffs():
    result = chain_rule_derivative([2.5], [2.0], 4)
    assert "4(" in result
    assert "2.5x^2" in result
    assert ")^3" in result
    assert "* (5.0x^1)" in result

def test_chain_rule_derivative_negative_powers():
    result = chain_rule_derivative([3], [-2], 2)
    assert result == "2(3x^-2)^1 * (-6x^-3)"

def test_chain_rule_derivative_exponent_one():
    result = chain_rule_derivative([4, 1], [3, 0], 1)
    assert "1(" in result
    assert "4x^3 + 1x^0" in result
    assert ")^0" in result
    assert "* (12x^2)" in result
def test_chain_rule_derivative_empty():
    # g(x) = 0, n = 2 => (0)^2 => derivative is 2()^1 * ()
    result = chain_rule_derivative([], [], 2)
    assert result == "2()^1 * ()"

def test_chain_rule_derivative_floats():
    # g(x) = 1.5x^2 + 2.5x, n = 2
    result = chain_rule_derivative([1.5, 2.5], [2.0, 1.0], 2)
    assert "2(" in result
    assert "1.5x^2 + 2.5x^1" in result
    assert ")^1" in result
    assert "* (3.0x^1 + 2.5x^0)" in result

def test_chain_rule_derivative_negative_coeffs_powers():
    # g(x) = -3x^-2, n = 4
    result = chain_rule_derivative([-3], [-2], 4)
    assert "4(-3x^-2)^3 * (6x^-3)" in result

def test_chain_rule_derivative_exponent_one():
    # g(x) = x^2 + 2x, n = 1
    result = chain_rule_derivative([1, 2], [2, 1], 1)
    assert "1(1x^2 + 2x^1)^0 * (2x^1 + 2x^0)" in result
def test_chain_rule_derivative_float_coefficients():
    # g(x) = 1.5x^2, n = 2 => derivative is 2(1.5x^2)^1 * (3.0x^1)
    result = chain_rule_derivative([1.5], [2], 2)
    assert "2(" in result
    assert "1.5x^2" in result
    assert ")^1" in result
    assert "* (3.0x^1)" in result

def test_chain_rule_derivative_negative_powers_and_coeffs():
    # g(x) = -2x^-3, n = 4 => derivative is 4(-2x^-3)^3 * (6x^-4)
    result = chain_rule_derivative([-2], [-3], 4)
    assert "4(" in result
    assert "-2x^-3" in result
    assert ")^3" in result
    assert "* (6x^-4)" in result

def test_chain_rule_derivative_empty_inner():
    # g(x) = empty, n = 3 => derivative is 3()^2 * ()
    result = chain_rule_derivative([], [], 3)
    assert result == "3()^2 * ()"

def test_integrate_cos_basic():
    # Integral of cos(x) from 0 to pi/2 should be sin(pi/2) - sin(0) = 1 - 0 = 1
    result = integrate_cos(0, math.pi / 2)
    assert math.isclose(result, 1.0, rel_tol=1e-5)

def test_integrate_cos_full_period():
    # Integral of cos(x) from 0 to 2*pi should be 0
    result = integrate_cos(0, 2 * math.pi)
    assert math.isclose(result, 0.0, abs_tol=1e-5)

def test_integrate_cos_negative_bounds():
    # Integral of cos(x) from -pi/2 to 0 should be sin(0) - sin(-pi/2) = 0 - (-1) = 1
    result = integrate_cos(-math.pi / 2, 0)
    assert math.isclose(result, 1.0, rel_tol=1e-5)

def test_integrate_cos_same_bounds():
    # Integral of cos(x) from a to a should be 0
    result = integrate_cos(math.pi, math.pi)
    assert math.isclose(result, 0.0, abs_tol=1e-5)

def test_integrate_sin_basic():
    # Integral of sin(x) from 0 to pi/2 should be -cos(pi/2) - (-cos(0)) = 0 + 1 = 1
    result = integrate_sin(0, math.pi / 2)
    assert math.isclose(result, 1.0, rel_tol=1e-5)

def test_integrate_sin_full_period():
    # Integral of sin(x) from 0 to 2*pi should be 0
    result = integrate_sin(0, 2 * math.pi)
    assert math.isclose(result, 0.0, abs_tol=1e-5)

def test_integrate_sin_negative_bounds():
    # Integral of sin(x) from -pi/2 to 0 should be -cos(0) - (-cos(-pi/2)) = -1 - 0 = -1
    result = integrate_sin(-math.pi / 2, 0)
    assert math.isclose(result, -1.0, rel_tol=1e-5)

def test_integrate_sin_same_bounds():
    # Integral of sin(x) from a to a should be 0
    result = integrate_sin(math.pi, math.pi)
    assert math.isclose(result, 0.0, abs_tol=1e-5)

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


from Math.Calculus.Differentiation.chain_rule import format_polynomial as direct_format_polynomial_chain_rule
class TestChainRuleFormatPolynomial(unittest.TestCase):
    def test_format_polynomial_single_term(self):
        self.assertEqual(direct_format_polynomial_chain_rule([4], [2]), "4x^2")

    def test_format_polynomial_zero_coefficient(self):
        self.assertEqual(direct_format_polynomial_chain_rule([0, 5], [2, 1]), "0x^2 + 5x^1")

    def test_format_polynomial_fractional_power_cast_to_int(self):
        self.assertEqual(direct_format_polynomial_chain_rule([3], [2.9]), "3x^2")

    def test_format_polynomial_zero_power(self):
        self.assertEqual(direct_format_polynomial_chain_rule([7], [0]), "7x^0")

    def test_format_polynomial_mismatched_lengths(self):
        # zip will truncate to the shorter list
        self.assertEqual(direct_format_polynomial_chain_rule([1, 2], [3]), "1x^3")
        self.assertEqual(direct_format_polynomial_chain_rule([1], [3, 2]), "1x^3")

    def test_format_polynomial_all_zeros(self):
        self.assertEqual(direct_format_polynomial_chain_rule([0, 0], [0, 0]), "0x^0 + 0x^0")

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
def test_format_polynomial_chain_rule_basic():
    coeffs = [3, 5]
    powers = [2, 1]
    result = format_polynomial_chain_rule(coeffs, powers)
    terms = [t.strip() for t in result.split("+")]
    assert "3x^2" in terms
    assert "5x^1" in terms
    assert len(terms) == 2

def test_format_polynomial_chain_rule_empty():
    result = format_polynomial_chain_rule([], [])
    assert result == ""

def test_format_polynomial_chain_rule_mixed():
    result = format_polynomial_chain_rule([-2, 4.5], [3, 0])
    terms = [t.strip() for t in result.split("+")]
    assert "-2x^3" in terms
    assert "4.5x^0" in terms
    assert len(terms) == 2

def test_format_polynomial_chain_rule_zero_coeffs():
    assert format_polynomial_chain_rule([0, 0], [2, 1]) == "0x^2 + 0x^1"

def test_format_polynomial_chain_rule_float_powers():
    assert format_polynomial_chain_rule([2, 3], [2.5, 1.2]) == "2x^2 + 3x^1"

def test_format_polynomial_chain_rule_zero_power():
    assert format_polynomial_chain_rule([4], [0]) == "4x^0"

def test_format_polynomial_chain_rule_mixed_types():
    assert format_polynomial_chain_rule([1.5, 2], [3.8, 0]) == "1.5x^3 + 2x^0"
def test_format_polynomial_chain_rule_single_term():
    result = format_polynomial_chain_rule([7], [3])
    terms = [t.strip() for t in result.split("+")]
    assert "7x^3" in terms
    assert len(terms) == 1

def test_format_polynomial_chain_rule_zero_coeff():
    result = format_polynomial_chain_rule([0, 5], [2, 1])
    terms = [t.strip() for t in result.split("+")]
    assert "0x^2" in terms
    assert "5x^1" in terms
    assert len(terms) == 2

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

def test_format_polynomial_integration_multiple_terms():
    result = format_polynomial_integration([2.0, 3.5, 1.0], [2.0, 1.0, 0.0])
    terms = [term.strip() for term in result.split('+')]
    assert "2.0x^2" in terms
    assert "3.5x" in terms
    assert "1.0" in terms
    assert "C" in terms

def test_format_polynomial_integration_single_term_power_zero():
    result = format_polynomial_integration([5.0], [0.0])
    terms = [term.strip() for term in result.split('+')]
    assert "5.0" in terms
    assert "C" in terms

def test_format_polynomial_integration_single_term_power_one():
    result = format_polynomial_integration([2.5], [1.0])
    terms = [term.strip() for term in result.split('+')]
    assert "2.5x" in terms
    assert "C" in terms

def test_format_polynomial_integration_single_term_power_gt_one():
    result = format_polynomial_integration([4.0], [3.0])
    terms = [term.strip() for term in result.split('+')]
    assert "4.0x^3" in terms
    assert "C" in terms

def test_format_polynomial_integration_empty():
    result = format_polynomial_integration([], [])
    assert result.strip() == "+ C" or result.strip() == "C"

def test_format_polynomial_integration_negative_coefficients():
    result = format_polynomial_integration([-2.0, -3.5], [2.0, 1.0])
    terms = [term.strip() for term in result.split('+')]
    assert "-2.0x^2" in terms
    assert "-3.5x" in terms
    assert "C" in terms

def test_format_polynomial_integration_negative_powers():
    result = format_polynomial_integration([4.0, 5.0], [-2.0, -3.0])
    terms = [term.strip() for term in result.split('+')]
    assert "4.0x^-2" in terms
    assert "5.0x^-3" in terms
    assert "C" in terms

def test_format_polynomial_integration_zero_coefficients():
    result = format_polynomial_integration([0.0, 0.0], [2.0, 1.0])
    terms = [term.strip() for term in result.split('+')]
    assert "0.0x^2" in terms
    assert "0.0x" in terms
    assert "C" in terms
def test_format_polynomial_chain_rule_zero_coeff():
    assert format_polynomial_chain_rule([0, 2], [2, 1]) == "0x^2 + 2x^1"

def test_format_polynomial_chain_rule_float_power():
    assert format_polynomial_chain_rule([3], [2.5]) == "3x^2"

def test_format_polynomial_chain_rule_unequal_lengths():
    assert format_polynomial_chain_rule([3, 2, 1], [2, 1]) == "3x^2 + 2x^1"

def test_format_polynomial_chain_rule_2_basic():
    result = format_polynomial_chain_rule([1, 2, 3], [2, 1, 0])
    terms = [t.strip() for t in result.split("+")]
    assert "1x^2" in terms
    assert "2x^1" in terms
    assert "3x^0" in terms
    assert len(terms) == 3

def test_format_polynomial_chain_rule_2_floats():
    result = format_polynomial_chain_rule([1.5, 2.5], [2.0, 1.0])
    terms = [t.strip() for t in result.split("+")]
    assert "1.5x^2" in terms
    assert "2.5x^1" in terms
    assert len(terms) == 2

def test_format_polynomial_chain_rule_2_empty():
    assert format_polynomial_chain_rule([], []) == ""

def test_format_polynomial_chain_rule_2_negative_powers():
    result = format_polynomial_chain_rule([5], [-2])
    terms = [t.strip() for t in result.split("+")]
    assert "5x^-2" in terms
    assert len(terms) == 1

def test_format_polynomial_chain_rule_2_negative_coeffs():
    assert format_polynomial_chain_rule([-3, -4], [2, 1]) == "-3x^2 + -4x^1"

def test_format_polynomial_chain_rule_zero_coeff():
    assert format_polynomial_chain_rule([0, 2], [2, 1]) == "0x^2 + 2x^1"

def test_format_polynomial_chain_rule_zero_power():
    assert format_polynomial_chain_rule([3], [0]) == "3x^0"

def test_format_polynomial_chain_rule_mismatched_lengths():
    # zip should truncate to the shortest list
    assert format_polynomial_chain_rule([1, 2, 3], [2, 1]) == "1x^2 + 2x^1"
    assert format_polynomial_chain_rule([1, 2], [2, 1, 0]) == "1x^2 + 2x^1"

    result = format_polynomial_chain_rule([-3, -4], [2, 1])
    terms = [t.strip() for t in result.split("+")]
    assert "-3x^2" in terms
    assert "-4x^1" in terms
    assert len(terms) == 2
def test_format_polynomial_chain_rule_floating_point_powers():
    # Floating point powers should be cast to int as per the code: `int(power)`
    assert format_polynomial_chain_rule([2, 3], [2.5, 1.9]) == "2x^2 + 3x^1"

def test_format_polynomial_chain_rule_zero_coefficients():
    # Test with 0 as coefficient
    assert format_polynomial_chain_rule([0, 1], [2, 1]) == "0x^2 + 1x^1"

def test_format_polynomial_chain_rule_zero_power():
    # Test with 0 as power
    assert format_polynomial_chain_rule([5, 2], [1, 0]) == "5x^1 + 2x^0"

def test_format_polynomial_chain_rule_unequal_lengths():
    # zip should truncate to the shorter list
    assert format_polynomial_chain_rule([1, 2, 3], [1, 0]) == "1x^1 + 2x^0"
    assert format_polynomial_chain_rule([1, 2], [2, 1, 0]) == "1x^2 + 2x^1"
    assert format_polynomial_chain_rule([0], [2]) == "0x^2"

def test_format_polynomial_chain_rule_single_term():
    assert format_polynomial_chain_rule([5], [3]) == "5x^3"

def test_format_polynomial_chain_rule_float_power_cast():
    assert format_polynomial_chain_rule([2], [3.9]) == "2x^3"

def test_format_polynomial_chain_rule_zero_power():
    assert format_polynomial_chain_rule([7], [0]) == "7x^0"

    assert format_polynomial_chain_rule([5], [0]) == "5x^0"

def test_format_polynomial_chain_rule_float_power_truncation():
    assert format_polynomial_chain_rule([1, 2], [2.9, 1.1]) == "1x^2 + 2x^1"

def test_format_polynomial_chain_rule_mismatched_lengths():
    assert format_polynomial_chain_rule([1, 2, 3], [2, 1]) == "1x^2 + 2x^1"
    assert format_polynomial_chain_rule([1], [2, 1]) == "1x^2"

def test_format_polynomial_chain_rule_negative_float():
    assert format_polynomial_chain_rule([-1.5, -2.5], [2, 1]) == "-1.5x^2 + -2.5x^1"
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

class TestTrigIntegration:
    def test_integrate_sin_basic(self):
        """Test integral of sin(x) from 0 to pi = 2"""
        result = integrate_sin(0, math.pi)
        assert math.isclose(result, 2.0, rel_tol=1e-5)

    def test_integrate_sin_zero(self):
        """Test integral of sin(x) from 0 to 0 = 0"""
        result = integrate_sin(0, 0)
        assert math.isclose(result, 0.0, abs_tol=1e-9)

    def test_integrate_sin_full_period(self):
        """Test integral of sin(x) from 0 to 2pi = 0"""
        result = integrate_sin(0, 2 * math.pi)
        assert math.isclose(result, 0.0, abs_tol=1e-9)

    def test_integrate_sin_negative_bounds(self):
        """Test integral of sin(x) from -pi to 0 = -2"""
        result = integrate_sin(-math.pi, 0)
        assert math.isclose(result, -2.0, rel_tol=1e-5)

    def test_integrate_sin_reversed_bounds(self):
        """Test integral of sin(x) from pi to 0 = -2"""
        result = integrate_sin(math.pi, 0)
        assert math.isclose(result, -2.0, rel_tol=1e-5)

    def test_integrate_sin_fractional_pi(self):
        """Test integral of sin(x) from 0 to pi/3 = 0.5"""
        result = integrate_sin(0, math.pi / 3)
        assert math.isclose(result, 0.5, rel_tol=1e-5)

    def test_integrate_sin_float_bounds(self):
        """Test integral of sin(x) from 0.5 to 1.5"""
        result = integrate_sin(0.5, 1.5)
        expected = -math.cos(1.5) + math.cos(0.5)
        assert math.isclose(result, expected, rel_tol=1e-5)

    def test_integrate_cos_basic(self):
        """Test integral of cos(x) from 0 to pi/2 = 1"""
        result = integrate_cos(0, math.pi / 2)
        assert math.isclose(result, 1.0, rel_tol=1e-5)

    def test_integrate_cos_zero(self):
        """Test integral of cos(x) from 0 to 0 = 0"""
        result = integrate_cos(0, 0)
        assert math.isclose(result, 0.0, abs_tol=1e-9)

    def test_integrate_cos_full_period(self):
        """Test integral of cos(x) from 0 to 2pi = 0"""
        result = integrate_cos(0, 2 * math.pi)
        assert math.isclose(result, 0.0, abs_tol=1e-9)

    def test_integrate_cos_negative_bounds(self):
        """Test integral of cos(x) from -pi/2 to 0 = 1"""
        result = integrate_cos(-math.pi / 2, 0)
        assert math.isclose(result, 1.0, rel_tol=1e-5)

    def test_integrate_cos_half_period(self):
        """Test integral of cos(x) from -pi/2 to pi/2 = 2"""
        result = integrate_cos(-math.pi / 2, math.pi / 2)
        assert math.isclose(result, 2.0, rel_tol=1e-5)
    def test_integrate_cos_same_bounds(self):
        """Test integral of cos(x) from a to a = 0"""
        result = integrate_cos(math.pi, math.pi)
        assert math.isclose(result, 0.0, abs_tol=1e-9)
    def test_integrate_cos_same_bounds(self):
        """Test integral of cos(x) from a to a = 0"""
        result = integrate_cos(math.pi, math.pi)
        assert math.isclose(result, 0.0, abs_tol=1e-5)
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


class TestFormatPolynomialChainRule(unittest.TestCase):
    def test_single_term(self):
        self.assertEqual(format_polynomial_chain_rule([5], [2]), "5x^2")

    def test_zero_coefficient(self):
        self.assertEqual(format_polynomial_chain_rule([0], [3]), "0x^3")

    def test_zero_power(self):
        self.assertEqual(format_polynomial_chain_rule([4], [0]), "4x^0")

    def test_float_power_truncation(self):
        # int() truncates floats towards zero
        self.assertEqual(format_polynomial_chain_rule([2], [3.9]), "2x^3")

    def test_negative_power(self):
        self.assertEqual(format_polynomial_chain_rule([7], [-2]), "7x^-2")

    def test_multiple_terms(self):
        self.assertEqual(format_polynomial_chain_rule([3, -2, 4.5], [2, 1, 0]), "3x^2 + -2x^1 + 4.5x^0")

    def test_empty_lists(self):
        self.assertEqual(format_polynomial_chain_rule([], []), "")

    def test_mismatched_list_lengths(self):
        # zip() truncates to the shortest list
        self.assertEqual(format_polynomial_chain_rule([1, 2], [3]), "1x^3")
        self.assertEqual(format_polynomial_chain_rule([1], [3, 2]), "1x^3")
        """Test integral of cos(x) from -pi to 0 = 0"""
        result = integrate_cos(-math.pi, 0)
        assert math.isclose(result, 0.0, abs_tol=1e-9)

    def test_integrate_cos_reversed_bounds(self):
        """Test integral of cos(x) from pi/2 to 0 = -1"""
        result = integrate_cos(math.pi / 2, 0)
        assert math.isclose(result, -1.0, rel_tol=1e-5)

    def test_integrate_cos_fractional_bounds(self):
        """Test integral of cos(x) from pi/6 to pi/3 = (sqrt(3)/2 - 1/2)"""
        result = integrate_cos(math.pi / 6, math.pi / 3)
        expected = math.sin(math.pi / 3) - math.sin(math.pi / 6)
        assert math.isclose(result, expected, rel_tol=1e-5)
    def test_integrate_cos_same_bounds(self):
        """Test integral of cos(x) from pi to pi = 0"""
        result = integrate_cos(math.pi, math.pi)
        assert math.isclose(result, 0.0, abs_tol=1e-9)

    def test_integrate_cos_half_period(self):
        """Test integral of cos(x) from 0 to pi = 0"""
        result = integrate_cos(0, math.pi)
        assert math.isclose(result, 0.0, abs_tol=1e-9)

    def test_integrate_cos_multiple_periods(self):
        """Test integral of cos(x) over multiple periods"""
        result = integrate_cos(-2 * math.pi, 4 * math.pi)
        assert math.isclose(result, 0.0, abs_tol=1e-9)
        """Test integral of cos(x) from -pi/2 to pi/2 = 2"""
        result = integrate_cos(-math.pi / 2, math.pi / 2)
        assert math.isclose(result, 2.0, rel_tol=1e-5)


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


class TestFormatPolynomialChainRule(unittest.TestCase):
    def test_basic_positive_powers(self):
        result = format_polynomial_chain_rule([1, 2, 3], [2, 1, 0])
        self.assertEqual(result, "1x^2 + 2x^1 + 3x^0")

    def test_zero_coefficients(self):
        result = format_polynomial_chain_rule([0, 0], [2, 1])
        self.assertEqual(result, "0x^2 + 0x^1")

    def test_zero_powers(self):
        result = format_polynomial_chain_rule([5, 4], [0, 0])
        self.assertEqual(result, "5x^0 + 4x^0")

    def test_negative_powers(self):
        result = format_polynomial_chain_rule([5, -2], [-2, -3])
        self.assertEqual(result, "5x^-2 + -2x^-3")

    def test_negative_coefficients(self):
        result = format_polynomial_chain_rule([-3, -4], [2, 1])
        self.assertEqual(result, "-3x^2 + -4x^1")

    def test_floating_point_coefficients(self):
        result = format_polynomial_chain_rule([1.5, 2.5], [2.0, 1.0])
        self.assertEqual(result, "1.5x^2 + 2.5x^1")

    def test_empty_lists(self):
        result = format_polynomial_chain_rule([], [])
        self.assertEqual(result, "")

    def test_single_element(self):
        result = format_polynomial_chain_rule([7], [3])
        self.assertEqual(result, "7x^3")
