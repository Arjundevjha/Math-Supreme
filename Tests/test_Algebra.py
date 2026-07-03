import os
import sys
import pytest

# Add root directory to path
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from Math.Algebra.Polynomials.polynomial import format_polynomial, evaluate_polynomial as evaluate_polynomial_poly
from Math.Algebra.Linear_Equations.linear_eqn import linear_eqn

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
