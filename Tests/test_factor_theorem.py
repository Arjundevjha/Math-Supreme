import os
import sys
import pytest
import math

# Add root directory to path to allow imports
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from Math.Algebra.Polynomials.factor_theorem import evaluate_polynomial, check_factor

class TestEvaluatePolynomial:
    def test_evaluate_polynomial_basic(self):
        """Test with a simple quadratic polynomial: x^2 + 2x + 1 at x=2"""
        assert math.isclose(evaluate_polynomial([1, 2, 1], [2, 1, 0], 2), 9, rel_tol=1e-9)

    def test_evaluate_polynomial_zero_x(self):
        """Test polynomial at x=0"""
        assert math.isclose(evaluate_polynomial([1, 2, 1], [2, 1, 0], 0), 1, rel_tol=1e-9)

    def test_evaluate_polynomial_negative_x(self):
        """Test polynomial at x=-1"""
        assert math.isclose(evaluate_polynomial([1, 2, 1], [2, 1, 0], -1), 0, abs_tol=1e-9)

    def test_evaluate_polynomial_fractional_powers(self):
        """Test with fractional powers (square root)"""
        assert math.isclose(evaluate_polynomial([1], [0.5], 4), 2.0, rel_tol=1e-9)

    def test_evaluate_polynomial_float_coefficients(self):
        """Test with float coefficients and float x"""
        assert math.isclose(evaluate_polynomial([1.5, 0.5], [2, 0], 2.0), 6.5, rel_tol=1e-9)

    def test_evaluate_polynomial_empty(self):
        """Test with empty coefficients and powers"""
        assert math.isclose(evaluate_polynomial([], [], 5), 0, abs_tol=1e-9)

    def test_evaluate_polynomial_negative_powers(self):
        """Test with negative powers"""
        assert math.isclose(evaluate_polynomial([4, 2], [-1, -2], 2), 2.5, rel_tol=1e-9)

    def test_evaluate_polynomial_precision(self):
        """Test floating-point precision evaluation."""
        assert math.isclose(evaluate_polynomial([0.1, 0.2], [1, 0], 1), 0.3, rel_tol=1e-9)

    def test_evaluate_polynomial_large_numbers(self):
        """Test evaluation with very large numbers."""
        assert math.isclose(evaluate_polynomial([1e10, 1e5], [2, 1], 10), 1e12 + 1e6, rel_tol=1e-9)

def test_check_factor_true():
    assert check_factor([1, -4, 4], [2, 1, 0], 2) is True

def test_check_factor_false():
    assert check_factor([1, -4, 4], [2, 1, 0], 3) is False

def test_check_factor_linear():
    assert check_factor([2, -6], [1, 0], 3) is True

def test_check_factor_linear_false():
    assert check_factor([2, -6], [1, 0], 2) is False

def test_check_factor_cubic():
    coefficients = [1, -6, 11, -6]
    powers = [3, 2, 1, 0]
    assert check_factor(coefficients, powers, 1) is True
    assert check_factor(coefficients, powers, 2) is True
    assert check_factor(coefficients, powers, 3) is True
    assert check_factor(coefficients, powers, 4) is False

def test_check_factor_float():
    coefficients = [2, -1, -1]
    powers = [2, 1, 0]
    assert check_factor(coefficients, powers, -0.5) is True
    assert check_factor(coefficients, powers, 1.0) is True
    assert check_factor(coefficients, powers, 0.5) is False
