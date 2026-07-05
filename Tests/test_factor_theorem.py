import os
import sys
import pytest
import math

# Add root directory to path
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from Math.Algebra.Polynomials.factor_theorem import evaluate_polynomial, check_factor

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

    def test_check_factor_float(self):
        # P(x) = 2x^2 - x - 1
        # Factors are (2x+1)(x-1) => x = -0.5, x = 1
        coefficients = [2, -1, -1]
        powers = [2, 1, 0]
        assert check_factor(coefficients, powers, -0.5) is True
        assert check_factor(coefficients, powers, 1.0) is True
        assert check_factor(coefficients, powers, 0.5) is False

    def test_check_factor_floating_point_imprecision(self):
        # A case that mathematically equals 0, but due to floating point math might not be exactly 0
        # For example, x^3 - x^2 = 0 where x = 1/3
        # Let's use P(x) = 3x - 1, x = 1/3
        assert check_factor([3, -1], [1, 0], 1/3) is True

    def test_check_factor_empty(self):
        # Empty polynomial evaluates to 0
        assert check_factor([], [], 5) is True

    def test_check_factor_all_zeros(self):
        # Polynomial 0x^2 + 0x + 0
        assert check_factor([0, 0, 0], [2, 1, 0], 100) is True

    def test_check_factor_gaps_in_powers(self):
        # P(x) = x^4 - 16
        # Factors are x=2, x=-2
        assert check_factor([1, -16], [4, 0], 2) is True
        assert check_factor([1, -16], [4, 0], -2) is True
        assert check_factor([1, -16], [4, 0], 1) is False

class TestEvaluatePolynomialPoly:
    def test_evaluate_polynomial_poly_basic(self):
        from Math.Algebra.Polynomials.polynomial import evaluate_polynomial as evaluate_polynomial_poly
        # P(x) = 2x^2 + 3x + 1
        # P(2) = 2(2^2) + 3(2) + 1 = 8 + 6 + 1 = 15
        assert evaluate_polynomial_poly([2, 3, 1], [2, 1, 0], 2) == 15

    def test_evaluate_polynomial_poly_zero_x(self):
        from Math.Algebra.Polynomials.polynomial import evaluate_polynomial as evaluate_polynomial_poly
        # P(x) = 5x^3 - 2x^2 + 4
        # P(0) = 4
        assert evaluate_polynomial_poly([5, -2, 4], [3, 2, 0], 0) == 4

    def test_evaluate_polynomial_poly_negative_x(self):
        from Math.Algebra.Polynomials.polynomial import evaluate_polynomial as evaluate_polynomial_poly
        # P(x) = x^3 - x^2 + x - 1
        # P(-2) = (-2)^3 - (-2)^2 + (-2) - 1 = -8 - 4 - 2 - 1 = -15
        assert evaluate_polynomial_poly([1, -1, 1, -1], [3, 2, 1, 0], -2) == -15

    def test_evaluate_polynomial_poly_floating_point(self):
        from Math.Algebra.Polynomials.polynomial import evaluate_polynomial as evaluate_polynomial_poly
        # P(x) = 1.5x^2 + 2.5x
        # P(2.0) = 1.5(2.0^2) + 2.5(2.0) = 6.0 + 5.0 = 11.0
        assert evaluate_polynomial_poly([1.5, 2.5], [2, 1], 2.0) == 11.0

    def test_evaluate_polynomial_poly_empty(self):
        from Math.Algebra.Polynomials.polynomial import evaluate_polynomial as evaluate_polynomial_poly
        # Empty polynomial
        assert evaluate_polynomial_poly([], [], 5) == 0

    def test_evaluate_polynomial_poly_negative_powers(self):
        from Math.Algebra.Polynomials.polynomial import evaluate_polynomial as evaluate_polynomial_poly
        # P(x) = 2x^-1 + 3
        # P(2) = 2(2^-1) + 3 = 1 + 3 = 4
        assert evaluate_polynomial_poly([2, 3], [-1, 0], 2) == 4
