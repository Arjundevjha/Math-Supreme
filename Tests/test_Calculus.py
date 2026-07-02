import pytest
from Math.Calculus.Differentiation.quotient_rule import quotient_rule_derivative

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
