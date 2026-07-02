import pytest
from Math.Algebra.Polynomials.polynomial import evaluate_polynomial

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
    assert evaluate_polynomial([1.5, 2.5], [2, 1], 2.0) == 11.0

def test_evaluate_polynomial_empty():
    # Empty polynomial
    assert evaluate_polynomial([], [], 5) == 0

def test_evaluate_polynomial_negative_powers():
    # P(x) = 2x^-1 + 3
    # P(2) = 2(2^-1) + 3 = 1 + 3 = 4
    assert evaluate_polynomial([2, 3], [-1, 0], 2) == 4
