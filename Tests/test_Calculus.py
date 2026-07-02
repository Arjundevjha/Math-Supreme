import os
import sys
import pytest

# Add root directory to path to allow "Math.Calculus..." imports
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from Math.Calculus.Differentiation.second_derivatives import second_derivative
from Math.Calculus.Differentiation.product_rule import compute_polynomial_derivative_str

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

