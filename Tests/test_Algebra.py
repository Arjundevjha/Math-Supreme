import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Math.Algebra.Polynomials.polynomial import format_polynomial

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
