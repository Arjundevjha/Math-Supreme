import pytest
from Math.Calculus.Differentiation.quotient_rule import format_polynomial


def test_format_polynomial_basic():
    coeffs = [2, 3]
    powers = [2, 1]
    result = format_polynomial(coeffs, powers)
    terms = [t.strip() for t in result.split('+')]
    assert "2x^2" in terms
    assert "3x^1" in terms

def test_format_polynomial_floats():
    coeffs = [2.5, 3.1]
    powers = [2.0, 0.0]
    result = format_polynomial(coeffs, powers)
    terms = [t.strip() for t in result.split('+')]
    assert "2.5x^2" in terms
    assert "3.1x^0" in terms

def test_format_polynomial_negative_powers_and_coeffs():
    coeffs = [-1, 0]
    powers = [-2, 3]
    result = format_polynomial(coeffs, powers)
    terms = [t.strip() for t in result.split('+')]
    assert "-1x^-2" in terms
    assert "0x^3" in terms

def test_format_polynomial_empty():
    coeffs = []
    powers = []
    result = format_polynomial(coeffs, powers)
    assert result.strip() == ""
