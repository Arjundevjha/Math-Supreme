import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Math.Calculus.Differentiation.product_rule import compute_polynomial_derivative_str

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
