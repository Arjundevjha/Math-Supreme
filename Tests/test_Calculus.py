import os
import sys
import pytest

# Add root directory to path to allow "Math.Calculus..." imports
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from Math.Calculus.Differentiation.chain_rule import format_polynomial

def test_format_polynomial_basic():
    assert format_polynomial([1, 2, 3], [2, 1, 0]) == "1x^2 + 2x^1 + 3x^0"

def test_format_polynomial_floats():
    assert format_polynomial([1.5, 2.5], [2.0, 1.0]) == "1.5x^2 + 2.5x^1"

def test_format_polynomial_empty():
    assert format_polynomial([], []) == ""

def test_format_polynomial_negative_powers():
    assert format_polynomial([5], [-2]) == "5x^-2"

def test_format_polynomial_negative_coeffs():
    assert format_polynomial([-3, -4], [2, 1]) == "-3x^2 + -4x^1"
