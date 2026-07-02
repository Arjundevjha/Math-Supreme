import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from Math.Calculus.Differentiation.product_rule import (
    format_polynomial,
    compute_polynomial_derivative_str,
    product_rule_derivative
)

def test_format_polynomial():
    assert format_polynomial([1], [1]) == "1x^1"
    assert format_polynomial([2, 3], [2, 1]) == "2x^2 + 3x^1"
    assert format_polynomial([5], [0]) == "5x^0"

def test_compute_polynomial_derivative_str():
    assert compute_polynomial_derivative_str([1], [1]) == "1x^0"
    assert compute_polynomial_derivative_str([2, 3], [2, 1]) == "4x^1 + 3x^0"
    assert compute_polynomial_derivative_str([5], [0]) == "0"
    assert compute_polynomial_derivative_str([4], [3]) == "12x^2"

def test_product_rule_derivative_basic():
    # u(x) = x, v(x) = x
    # u'v + uv' = (1x^0) * (1x^1) + (1x^1) * (1x^0)
    result = product_rule_derivative([1], [1], [1], [1])
    assert result == "(1x^0) * (1x^1) + (1x^1) * (1x^0)"

def test_product_rule_derivative_complex():
    # u(x) = 2x^2 + 3x, v(x) = 4x^3
    result = product_rule_derivative([2, 3], [2, 1], [4], [3])
    assert "(4x^1 + 3x^0) * (4x^3) + (2x^2 + 3x^1) * (12x^2)" == result

def test_product_rule_derivative_constant():
    # u(x) = 5, v(x) = x
    result = product_rule_derivative([5], [0], [1], [1])
    assert result == "(0) * (1x^1) + (5x^0) * (1x^0)"

def test_product_rule_derivative_multiple_terms():
    # u(x) = 3x^3 + 2x^2 + x, v(x) = 5x^2 + 4
    # u_prime = 9x^2 + 4x^1 + 1x^0
    # v_prime = 10x^1
    result = product_rule_derivative([3, 2, 1], [3, 2, 1], [5, 4], [2, 0])
    expected = "(9x^2 + 4x^1 + 1x^0) * (5x^2 + 4x^0) + (3x^3 + 2x^2 + 1x^1) * (10x^1)"
    assert result == expected
