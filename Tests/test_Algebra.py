import pytest
from Math.Algebra.Polynomials.factor_theorem import evaluate_polynomial

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
