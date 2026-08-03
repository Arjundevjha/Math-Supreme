import math
import os
import sys
import pytest

# Add root directory to path

from Math.Algebra.Polynomials.polynomial import format_polynomial, evaluate_polynomial
from Math.Algebra.Linear_Equations.linear_eqn import linear_eqn
from Math.Algebra.Polynomials.factor_theorem import check_factor

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

def test_format_polynomial_single_term():
    result = format_polynomial([5], [3])
    terms = [t.strip() for t in result.split("+")]
    assert "5x^3" in terms

def test_format_polynomial_negative_powers():
    result = format_polynomial([2, -3], [-1, -2])
    terms = [t.strip() for t in result.split("+")]
    assert "2x^-1" in terms
    assert "-3x^-2" in terms

def test_format_polynomial_all_zero_powers():
    result = format_polynomial([1, 2], [0, 0])
    terms = [t.strip() for t in result.split("+")]
    assert "1" in terms
    assert "2" in terms

def test_format_polynomial_all_ones_powers():
    result = format_polynomial([3, 4], [1, 1])
    terms = [t.strip() for t in result.split("+")]
    assert "3x" in terms
    assert "4x" in terms

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

def test_linear_eqn_identical_points():
    # Points: (2, 3) and (2, 3)
    # x1 == x2, expects ValueError
    with pytest.raises(ValueError, match="The x-coordinates cannot be the same \\(vertical line\\)."):
        linear_eqn(2, 3, 2, 3)

def test_linear_eqn_origin():
    # Points: (0, 0) and (2, 4)
    # m = (4 - 0) / (2 - 0) = 2.0
    # b = 0 - 2.0 * 0 = 0.0
    assert linear_eqn(0, 0, 2, 4) == "y = 2.0x + 0.0"

def test_linear_eqn_all_negative():
    # Points: (-2, -3) and (-4, -7)
    # m = (-7 - -3) / (-4 - -2) = -4 / -2 = 2.0
    # b = -3 - 2.0 * (-2) = -3 + 4 = 1.0
    assert linear_eqn(-2, -3, -4, -7) == "y = 2.0x + 1.0"

def test_linear_eqn_fractional_slope():
    # Points: (1, 1) and (4, 2)
    # m = (2 - 1) / (4 - 1) = 1 / 3
    # b = 1 - (1/3) * 1 = 2 / 3
    # Since python uses floats, computing m and b explicitly and then doing format
    m = (2.0 - 1.0) / (4.0 - 1.0)
    b = 1.0 - m * 1.0
    assert linear_eqn(1, 1, 4, 2) == f"y = {m}x + {b}"

def test_linear_eqn_large_coordinates():
    # Points: (1000000, 2000000) and (3000000, 6000000)
    # m = 4000000 / 2000000 = 2.0
    # b = 2000000 - 2.0 * 1000000 = 0.0
    assert linear_eqn(1000000, 2000000, 3000000, 6000000) == "y = 2.0x + 0.0"
class TestEvaluatePolynomial:
    def test_evaluate_polynomial_zero_division(self):
        """Test evaluating at x=0 with negative powers, expecting ZeroDivisionError"""
        with pytest.raises(ZeroDivisionError):
            evaluate_polynomial([1], [-1], 0)

    def test_evaluate_polynomial_mismatched_lengths(self):
        """Test that zip handles mismatched list lengths by truncating to the shortest"""
        # [1, 2], [2] -> only evaluates 1 * x^2
        assert evaluate_polynomial([1, 2], [2], 3) == 9

    def test_evaluate_polynomial_complex_floats(self):
        """Test with floating point values that might cause precision issues"""
        # 0.1 * (0.1)^2 + 0.2 * (0.1)^1 = 0.001 + 0.02 = 0.021
        assert math.isclose(evaluate_polynomial([0.1, 0.2], [2, 1], 0.1), 0.021)

    def test_evaluate_polynomial_basic(self):
        """Test with a simple quadratic polynomial: x^2 + 2x + 1 at x=2"""
        # (2)^2 + 2*(2) + 1 = 4 + 4 + 1 = 9
        assert math.isclose(evaluate_polynomial([1, 2, 1], [2, 1, 0], 2), 9, rel_tol=1e-9)

    def test_evaluate_polynomial_zero_x(self):
        """Test polynomial at x=0"""
        # (0)^2 + 2*(0) + 1 = 1
        assert math.isclose(evaluate_polynomial([1, 2, 1], [2, 1, 0], 0), 1, rel_tol=1e-9)

    def test_evaluate_polynomial_negative_x(self):
        """Test polynomial at x=-1"""
        # (-1)^2 + 2*(-1) + 1 = 1 - 2 + 1 = 0
        assert math.isclose(evaluate_polynomial([1, 2, 1], [2, 1, 0], -1), 0, abs_tol=1e-9)

    def test_evaluate_polynomial_fractional_powers(self):
        """Test with fractional powers (square root)"""
        # 1 * (4)^0.5 = 2.0
        assert math.isclose(evaluate_polynomial([1], [0.5], 4), 2.0, rel_tol=1e-9)
        assert math.isclose(evaluate_polynomial([1], [0.5], 4), 2.0)

    def test_evaluate_polynomial_float_coefficients(self):
        """Test with float coefficients and float x"""
        # 1.5 * (2.0)^2 + 0.5 * (2.0)^0 = 1.5*4 + 0.5 = 6.0 + 0.5 = 6.5
        assert math.isclose(evaluate_polynomial([1.5, 0.5], [2, 0], 2.0), 6.5, rel_tol=1e-9)
        assert math.isclose(evaluate_polynomial([1.5, 0.5], [2, 0], 2.0), 6.5)

    def test_evaluate_polynomial_empty(self):
        """Test with empty coefficients and powers"""
        assert math.isclose(evaluate_polynomial([], [], 5), 0, abs_tol=1e-9)

    def test_evaluate_polynomial_negative_powers(self):
        """Test with negative powers"""
        # 4 * (2)^-1 + 2 * (2)^-2 = 4/2 + 2/4 = 2 + 0.5 = 2.5
        assert math.isclose(evaluate_polynomial([4, 2], [-1, -2], 2), 2.5, rel_tol=1e-9)

    def test_evaluate_polynomial_precision_variance(self):
        """Test that known floating point precision issues are handled correctly."""
        # Evaluating 0.1x + 0.2 at x=1 should yield 0.3 (but floats often give 0.30000000000000004)
        assert math.isclose(evaluate_polynomial([0.1, 0.2], [1, 0], 1), 0.3, rel_tol=1e-9)

    def test_evaluate_polynomial_zero_x_negative_power(self):
        """Test evaluating at x=0 with negative powers expects ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError):
            evaluate_polynomial([1], [-1], 0)

    def test_evaluate_polynomial_zero_coefficient(self):
        """Test evaluating polynomial where a coefficient is zero."""
        # 0*x^3 + 2*x^2 + 0*x^1 = 2*(3^2) = 18 at x=3
        assert math.isclose(evaluate_polynomial([0, 2, 0], [3, 2, 1], 3), 18, rel_tol=1e-9)

    def test_evaluate_polynomial_large_inputs(self):
        """Test evaluating polynomials with large inputs/powers."""
        # 1 * 10^10 = 10000000000
        assert math.isclose(evaluate_polynomial([1], [10], 10), 10**10, rel_tol=1e-9)

    def test_evaluate_polynomial_multiple_terms_same_power(self):
        """Test that multiple terms with the same power sum correctly."""
        # 2x^2 + 3x^2 = 5x^2 => 5*(2^2) = 20 at x=2
        assert math.isclose(evaluate_polynomial([2, 3], [2, 2], 2), 20, rel_tol=1e-9)

    def test_evaluate_polynomial_unsorted_powers(self):
        """Test evaluating polynomial with unsorted powers."""
        # 3x^1 + 2x^2 + 1x^0 = 3(2) + 2(4) + 1 = 6 + 8 + 1 = 15 at x=2
        assert math.isclose(evaluate_polynomial([3, 2, 1], [1, 2, 0], 2), 15, rel_tol=1e-9)
        assert math.isclose(evaluate_polynomial([4, 2], [-1, -2], 2), 2.5)
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

    def test_evaluate_polynomial_all_zero_coefficients(self):
        """Test with all zero coefficients"""
        # 0*x^3 + 0*x^2 + 0*x = 0
        assert evaluate_polynomial([0, 0, 0], [3, 2, 1], 10) == 0

    def test_evaluate_polynomial_sparse_terms(self):
        """Test with missing intermediate powers"""
        # 3*x^5 - 2*x^0 at x=2 -> 3*32 - 2*1 = 96 - 2 = 94
        assert evaluate_polynomial([3, -2], [5, 0], 2) == 94

    def test_evaluate_polynomial_large_powers(self):
        """Test with large powers"""
        # x^10 at x=2 -> 1024
        assert evaluate_polynomial([1], [10], 2) == 1024

    def test_evaluate_polynomial_excessive_power(self):
        """Test with power exceeding maximum allowed value raises ValueError"""
        with pytest.raises(ValueError, match="Power 1001 exceeds maximum allowed value of 1000"):
            evaluate_polynomial([1], [1001], 2)

    def test_evaluate_polynomial_precision(self):
        """Test with small floats where precision might be an issue"""
        # 0.1 * x^2 + 0.2 * x at x=0.3
        # 0.1 * 0.09 + 0.2 * 0.3 = 0.009 + 0.06 = 0.069
        assert math.isclose(evaluate_polynomial([0.1, 0.2], [2, 1], 0.3), 0.069, rel_tol=1e-9)
def test_check_factor_true():
    # P(x) = x^2 - 4x + 4, check if (x - 2) is a factor
    # P(2) = 2^2 - 4*2 + 4 = 4 - 8 + 4 = 0 -> True
    assert check_factor([1, -4, 4], [2, 1, 0], 2) is True
class TestCheckFactor:
    def test_check_factor_true(self):
        # P(x) = x^2 - 4x + 4, check if (x - 2) is a factor
        # P(2) = 2^2 - 4*2 + 4 = 4 - 8 + 4 = 0 -> True
        assert check_factor([1, -4, 4], [2, 1, 0], 2) is True

    def test_check_factor_false(self):
        # P(x) = x^2 - 4x + 4, check if (x - 3) is a factor
        # P(3) = 3^2 - 4*3 + 4 = 9 - 12 + 4 = 1 -> False
        assert check_factor([1, -4, 4], [2, 1, 0], 3) is False

    def test_check_factor_linear(self):
        # P(x) = 2x - 6, check if (x - 3) is a factor
        # P(3) = 2*3 - 6 = 0 -> True
        assert check_factor([2, -6], [1, 0], 3) is True

    def test_check_factor_linear_false(self):
        # P(x) = 2x - 6, check if (x - 2) is a factor
        # P(2) = 2*2 - 6 = -2 -> False
        assert check_factor([2, -6], [1, 0], 2) is False

    def test_check_factor_cubic(self):
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

def test_check_factor_precision():
    # P(x) = x^2 - 2
    # Factor is (x - sqrt(2)) => x = sqrt(2)
    assert check_factor([1, -2], [2, 0], math.sqrt(2)) is True

    # P(x) = x^3 - 3
    # Factor is (x - cbrt(3))
    assert check_factor([1, -3], [3, 0], 3**(1/3)) is True

def test_check_factor_empty():
    # Empty polynomial evaluates to 0, so any x should technically yield 0 and therefore True
    assert check_factor([], [], 5) is True

def test_check_factor_zero_polynomial():
    # Zero polynomial P(x) = 0
    assert check_factor([0], [2], 10) is True
    # P(x) = 0.1x^2 + 0.2x - 0.3
    # P(1.0) = 0.1 + 0.2 - 0.3 = 0 (but floating point arithmetic gives 5.55e-17)
    assert check_factor([0.1, 0.2, -0.3], [2, 1, 0], 1.0) is True

def test_check_factor_empty():
    # Empty polynomial evaluates to 0, so any x should be a factor
    assert check_factor([], [], 5) is True

def test_check_factor_zero_coefficients():
    # P(x) = 0x^2 + 0x + 0 = 0
    assert check_factor([0, 0, 0], [2, 1, 0], 100) is True

def test_check_factor_negative_powers():
    # P(x) = x^-1 - 0.5
    # P(2) = 0.5 - 0.5 = 0
    assert check_factor([1, -0.5], [-1, 0], 2) is True

    # P(x) = x^2 - 2, check if x = sqrt(2) is a factor
    # This evaluates to ~4.44e-16 instead of exactly 0 due to float precision
    assert check_factor([1, -2], [2, 0], math.sqrt(2)) is True

def test_check_factor_empty():
    # P(x) = 0
    assert check_factor([], [], 5) is True

def test_check_factor_zero():
    # P(x) = 0x^2
    assert check_factor([0], [2], 10) is True
def test_check_factor_irrational():
    # P(x) = x^2 - 2
    # Factors are (x - sqrt(2))(x + sqrt(2))
    coefficients = [1, -2]
    powers = [2, 0]
    assert check_factor(coefficients, powers, math.sqrt(2)) is True
    assert check_factor(coefficients, powers, -math.sqrt(2)) is True

def test_check_factor_empty():
    # P(x) = 0
    # Empty polynomial evaluates to 0, so any (x - a) divides 0
    assert check_factor([], [], 5) is True

def test_check_factor_zero_value():
    # P(x) = x^2 - x
    # Factors are x(x - 1), so (x - 0) is a factor
    coefficients = [1, -1]
    powers = [2, 1]
    assert check_factor(coefficients, powers, 0) is True
    assert check_factor(coefficients, powers, 1) is True
    assert check_factor(coefficients, powers, 2) is False

    def test_check_factor_float(self):
        # P(x) = 2x^2 - x - 1
        # Factors are (2x+1)(x-1) => x = -0.5, x = 1
        coefficients = [2, -1, -1]
        powers = [2, 1, 0]
        assert check_factor(coefficients, powers, -0.5) is True
        assert check_factor(coefficients, powers, 1.0) is True
        assert check_factor(coefficients, powers, 0.5) is False

    def test_check_factor_float_precision(self):
        # P(x) = x^2 - 0.2x + 0.01
        # Factor is (x - 0.1)^2
        coefficients = [1, -0.2, 0.01]
        powers = [2, 1, 0]
        # Evaluates to a very small floating point number (e.g. 1.7e-18), checking if it properly approximates to True
        assert check_factor(coefficients, powers, 0.1) is True

    def test_check_factor_empty(self):
        # Empty polynomial P(x) = 0
        # For any x, P(x) = 0, so any (x - a) is a factor
        assert check_factor([], [], 5) is True
def test_evaluate_polynomial_basic():
    # P(x) = 2x^2 + 3x + 1
    # P(2) = 2(2^2) + 3(2) + 1 = 8 + 6 + 1 = 15
    assert evaluate_polynomial([2, 3, 1], [2, 1, 0], 2) == 15

def test_evaluate_polynomial_zero_x():
    # P(x) = 5x^3 - 2x^2 + 4
    # P(0) = 4
    assert evaluate_polynomial([5, -2, 4], [3, 2, 0], 0) == 4

def test_evaluate_polynomial_negative_x():
    # P(x) = x^3 - x^2 + x - 1
    # P(-2) = (-2)^3 - (-2)^2 + (-2) - 1 = -8 - 4 - 2 - 1 = -15
    assert evaluate_polynomial([1, -1, 1, -1], [3, 2, 1, 0], -2) == -15

def test_evaluate_polynomial_floating_point():
    # P(x) = 1.5x^2 + 2.5x
    # P(2.0) = 1.5(2.0^2) + 2.5(2.0) = 6.0 + 5.0 = 11.0
    assert math.isclose(evaluate_polynomial([1.5, 2.5], [2, 1], 2.0), 11.0)

def test_evaluate_polynomial_empty():
    # Empty polynomial
    assert evaluate_polynomial([], [], 5) == 0

def test_evaluate_polynomial_negative_powers():
    # P(x) = 2x^-1 + 3
    # P(2) = 2(2^-1) + 3 = 1 + 3 = 4
    assert evaluate_polynomial([2, 3], [-1, 0], 2) == 4

def test_evaluate_polynomial_precision():
    import math
def test_evaluate_polynomial_poly_precision():
    # P(x) = 0.1x + 0.2
    # P(1.0) = 0.1(1.0) + 0.2 = 0.3
    # Use math.isclose to account for floating point precision issues (0.1 + 0.2 = 0.30000000000000004)
    assert math.isclose(evaluate_polynomial([0.1, 0.2], [1, 0], 1.0), 0.3)

def test_evaluate_polynomial_zero_power_zero_x():
    # x=0, power=0 -> 0**0 = 1 in Python
    # P(x) = 3x^0
    # P(0) = 3 * 0^0 = 3
    assert evaluate_polynomial([3], [0], 0) == 3

def test_evaluate_polynomial_unequal_lists():
    # zip truncates to shortest list
    # P(x) = 2x^2 + 3x
    # with extra power or extra coeff
    assert evaluate_polynomial([2, 3, 4], [2, 1], 2) == 14
    assert evaluate_polynomial([2, 3], [2, 1, 0], 2) == 14

def test_evaluate_polynomial_zero_division():
    # x=0 with negative power raises ZeroDivisionError
    # P(x) = 2x^-1
    with pytest.raises(ZeroDivisionError):
        evaluate_polynomial([2], [-1], 0)

def test_evaluate_polynomial_all_zero_coeffs():
    # P(x) = 0x^2 + 0x + 0
    assert evaluate_polynomial([0, 0, 0], [2, 1, 0], 5) == 0
    assert math.isclose(evaluate_polynomial([2, 3], [-1, 0], 2), 4.0)
def test_evaluate_polynomial_fractional_powers():
    # P(x) = 1x^0.5
    # P(4) = 1 * 4^0.5 = 2.0
    assert evaluate_polynomial([1], [0.5], 4) == 2.0

def test_evaluate_polynomial_precision():
    # P(x) = 0.1x + 0.2x
    # P(1) = 0.1(1) + 0.2(1) = 0.3
    # Direct equality might fail due to floating point precision: 0.1 + 0.2 = 0.30000000000000004
    result = evaluate_polynomial([0.1, 0.2], [1, 1], 1)
    assert math.isclose(result, 0.3, rel_tol=1e-9, abs_tol=1e-9)

def test_evaluate_polynomial_zero_coef():
    # P(x) = 0x^2 + 0x + 0
    assert evaluate_polynomial([0, 0, 0], [2, 1, 0], 100) == 0

def test_evaluate_polynomial_large_numbers():
    # P(x) = 1x^10
    # P(10) = 10^10 = 10000000000
    assert evaluate_polynomial([1], [10], 10) == 10000000000

def test_evaluate_polynomial_zero_to_zero():
    # P(x) = 1x^0
    # P(0) = 1(0^0) = 1.0 (in python, 0**0 is 1)
    assert evaluate_polynomial([1], [0], 0) == 1
def test_evaluate_polynomial_fractional_powers():
    # P(x) = x^0.5 + 2
    # P(4) = 4^0.5 + 2 = 2 + 2 = 4.0
    assert evaluate_polynomial([1, 2], [0.5, 0], 4) == 4.0

def test_evaluate_polynomial_large_numbers():
    # P(x) = x^10
    # P(2) = 2^10 = 1024
    assert evaluate_polynomial([1], [10], 2) == 1024

def test_evaluate_polynomial_zero_division_error():
    # P(x) = x^-1
    # P(0) should raise ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        evaluate_polynomial([1], [-1], 0)

def test_evaluate_polynomial_mismatched_lengths():
    # Evaluate polynomial with mismatched lengths of coefficients and powers
    # P(x) = 2x^2 + 3x
    # Should zip up to the shortest list (coefficients has 2, powers has 1)
    # result = 2*(2^2) = 8
    assert evaluate_polynomial([2, 3], [2], 2) == 8
