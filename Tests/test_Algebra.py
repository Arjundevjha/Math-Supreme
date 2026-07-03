import os
import sys
import pytest

# Add root directory to path
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from Math.Algebra.Polynomials.polynomial import format_polynomial, evaluate_polynomial as evaluate_polynomial_poly
from Math.Algebra.Linear_Equations.linear_eqn import linear_eqn
from Math.Algebra.Polynomials.factor_theorem import evaluate_polynomial, check_factor

def test_format_polynomial_basic():
    result = format_polynomial([2, 3, 4], [2, 1, 0])
    terms = [t.strip() for t in result.split("+")]
    assert "2x^2" in terms
    assert "3x" in terms
    assert "4" in terms

def test_format_polynomial_negative_and_zero():
    result = format_polynomial([-1, 0], [3, 2])
    terms = [t.strip() for t in result.split("+")]
    assert "-1x^3" in terms
    assert "0x^2" in terms

def test_format_polynomial_empty():
    assert format_polynomial([], []) == ""

def test_format_polynomial_floats():
    result = format_polynomial([1.5, -2.5, 3.1], [2.5, 1.0, 0.0])
    terms = [t.strip() for t in result.split("+")]
    assert "1.5x^2.5" in terms
    assert "-2.5x" in terms
    assert "3.1" in terms

def test_linear_eqn_positive_slope():
    # Points: (1, 2) and (3, 6)
    # m = (6 - 2) / (3 - 1) = 4 / 2 = 2.0
    # b = 2 - 2.0 * 1 = 0.0
    # Result: y = 2.0x + 0.0
    assert linear_eqn(1, 2, 3, 6) == "y = 2.0x + 0.0"

def test_linear_eqn_negative_slope():
    # Points: (0, 5) and (5, 0)
    # m = (0 - 5) / (5 - 0) = -5 / 5 = -1.0
    # b = 5 - (-1.0) * 0 = 5.0
    # Result: y = -1.0x + 5.0
    assert linear_eqn(0, 5, 5, 0) == "y = -1.0x + 5.0"

def test_linear_eqn_zero_slope():
    # Points: (1, 4) and (5, 4)
    # Horizontal line
    # m = (4 - 4) / (5 - 1) = 0.0
    # b = 4 - 0.0 * 1 = 4.0
    # Result: y = 0.0x + 4.0
    assert linear_eqn(1, 4, 5, 4) == "y = 0.0x + 4.0"

def test_linear_eqn_floats():
    # Points: (1.5, 2.5) and (3.5, 6.5)
    # m = (6.5 - 2.5) / (3.5 - 1.5) = 4.0 / 2.0 = 2.0
    # b = 2.5 - 2.0 * 1.5 = 2.5 - 3.0 = -0.5
    # Result: y = 2.0x + -0.5
    assert linear_eqn(1.5, 2.5, 3.5, 6.5) == "y = 2.0x + -0.5"

def test_linear_eqn_vertical_line():
    # Points: (2, 3) and (2, 7)
    # x1 == x2, expects ValueError
    with pytest.raises(ValueError, match="The x-coordinates cannot be the same \\(vertical line\\)."):
        linear_eqn(2, 3, 2, 7)
class TestEvaluatePolynomial:
    def test_evaluate_polynomial_basic(self):
        """Test with a simple quadratic polynomial: x^2 + 2x + 1 at x=2"""
        # (2)^2 + 2*(2) + 1 = 4 + 4 + 1 = 9
        assert evaluate_polynomial([1, 2, 1], [2, 1, 0], 2) == 9

    def test_evaluate_polynomial_zero_x(self):
        """Test polynomial at x=0"""
        # (0)^2 + 2*(0) + 1 = 1
        assert evaluate_polynomial([1, 2, 1], [2, 1, 0], 0) == 1

    def test_evaluate_polynomial_negative_x(self):
        """Test polynomial at x=-1"""
        # (-1)^2 + 2*(-1) + 1 = 1 - 2 + 1 = 0
        assert evaluate_polynomial([1, 2, 1], [2, 1, 0], -1) == 0

    def test_evaluate_polynomial_fractional_powers(self):
        """Test with fractional powers (square root)"""
        # 1 * (4)^0.5 = 2.0
        assert evaluate_polynomial([1], [0.5], 4) == 2.0

    def test_evaluate_polynomial_float_coefficients(self):
        """Test with float coefficients and float x"""
        # 1.5 * (2.0)^2 + 0.5 * (2.0)^0 = 1.5*4 + 0.5 = 6.0 + 0.5 = 6.5
        assert evaluate_polynomial([1.5, 0.5], [2, 0], 2.0) == 6.5

    def test_evaluate_polynomial_empty(self):
        """Test with empty coefficients and powers"""
        assert evaluate_polynomial([], [], 5) == 0

    def test_evaluate_polynomial_negative_powers(self):
        """Test with negative powers"""
        # 4 * (2)^-1 + 2 * (2)^-2 = 4/2 + 2/4 = 2 + 0.5 = 2.5
        assert evaluate_polynomial([4, 2], [-1, -2], 2) == 2.5

    def test_evaluate_polynomial_zero_to_zero_power(self):
        """Test zero to the power of zero (should be 1 in Python)"""
        # 5 * (0)^0 = 5 * 1 = 5
        assert evaluate_polynomial([5], [0], 0) == 5

    def test_evaluate_polynomial_zero_division(self):
        """Test evaluating at x=0 with negative power"""
        with pytest.raises(ZeroDivisionError):
            evaluate_polynomial([1], [-1], 0)

    def test_evaluate_polynomial_mismatched_lengths(self):
        """Test with mismatched lengths (zip will stop at shortest length)"""
        # [2, 3, 4] and [2, 1] -> 2*x^2 + 3*x^1, ignoring the '4'
        # At x=2: 2*(4) + 3*(2) = 8 + 6 = 14
        assert evaluate_polynomial([2, 3, 4], [2, 1], 2) == 14

    def test_evaluate_polynomial_all_zero_coeffs(self):
        """Test with all zero coefficients"""
        assert evaluate_polynomial([0, 0, 0], [2, 1, 0], 5) == 0

    def test_evaluate_polynomial_large_numbers(self):
        """Test with large numbers"""
        assert evaluate_polynomial([1000], [3], 10) == 1000 * 10**3

def test_check_factor_true():
    # P(x) = x^2 - 4x + 4, check if (x - 2) is a factor
    # P(2) = 2^2 - 4*2 + 4 = 4 - 8 + 4 = 0 -> True
    assert check_factor([1, -4, 4], [2, 1, 0], 2) is True

def test_check_factor_false():
    # P(x) = x^2 - 4x + 4, check if (x - 3) is a factor
    # P(3) = 3^2 - 4*3 + 4 = 9 - 12 + 4 = 1 -> False
    assert check_factor([1, -4, 4], [2, 1, 0], 3) is False

def test_check_factor_linear():
    # P(x) = 2x - 6, check if (x - 3) is a factor
    # P(3) = 2*3 - 6 = 0 -> True
    assert check_factor([2, -6], [1, 0], 3) is True

def test_check_factor_linear_false():
    # P(x) = 2x - 6, check if (x - 2) is a factor
    # P(2) = 2*2 - 6 = -2 -> False
    assert check_factor([2, -6], [1, 0], 2) is False

def test_check_factor_cubic():
    # P(x) = x^3 - 6x^2 + 11x - 6
    # Factors are (x-1)(x-2)(x-3)
    coefficients = [1, -6, 11, -6]
    powers = [3, 2, 1, 0]
    assert check_factor(coefficients, powers, 1) is True
    assert check_factor(coefficients, powers, 2) is True
    assert check_factor(coefficients, powers, 3) is True
    assert check_factor(coefficients, powers, 4) is False

def test_check_factor_float():
    # P(x) = 2x^2 - x - 1
    # Factors are (2x+1)(x-1) => x = -0.5, x = 1
    coefficients = [2, -1, -1]
    powers = [2, 1, 0]
    assert check_factor(coefficients, powers, -0.5) is True
    assert check_factor(coefficients, powers, 1.0) is True
    assert check_factor(coefficients, powers, 0.5) is False
def test_evaluate_polynomial_poly_basic():
    # P(x) = 2x^2 + 3x + 1
    # P(2) = 2(2^2) + 3(2) + 1 = 8 + 6 + 1 = 15
    assert evaluate_polynomial_poly([2, 3, 1], [2, 1, 0], 2) == 15

def test_evaluate_polynomial_poly_zero_x():
    # P(x) = 5x^3 - 2x^2 + 4
    # P(0) = 4
    assert evaluate_polynomial_poly([5, -2, 4], [3, 2, 0], 0) == 4

def test_evaluate_polynomial_poly_negative_x():
    # P(x) = x^3 - x^2 + x - 1
    # P(-2) = (-2)^3 - (-2)^2 + (-2) - 1 = -8 - 4 - 2 - 1 = -15
    assert evaluate_polynomial_poly([1, -1, 1, -1], [3, 2, 1, 0], -2) == -15

def test_evaluate_polynomial_poly_floating_point():
    # P(x) = 1.5x^2 + 2.5x
    # P(2.0) = 1.5(2.0^2) + 2.5(2.0) = 6.0 + 5.0 = 11.0
    assert evaluate_polynomial_poly([1.5, 2.5], [2, 1], 2.0) == 11.0

def test_evaluate_polynomial_poly_empty():
    # Empty polynomial
    assert evaluate_polynomial_poly([], [], 5) == 0

def test_evaluate_polynomial_poly_negative_powers():
    # P(x) = 2x^-1 + 3
    # P(2) = 2(2^-1) + 3 = 1 + 3 = 4
    assert evaluate_polynomial_poly([2, 3], [-1, 0], 2) == 4
