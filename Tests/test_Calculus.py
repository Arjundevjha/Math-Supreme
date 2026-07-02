import pytest
from Math.Calculus.Differentiation.chain_rule import format_polynomial

def test_format_polynomial_basic():
    coeffs = [3, 5]
    powers = [2, 1]
    result = format_polynomial(coeffs, powers)
    terms = [t.strip() for t in result.split("+")]
    assert "3x^2" in terms
    assert "5x^1" in terms
    assert len(terms) == 2

def test_format_polynomial_empty():
    result = format_polynomial([], [])
    assert result == ""

def test_format_polynomial_mixed():
    result = format_polynomial([-2, 4.5], [3, 0])
    terms = [t.strip() for t in result.split("+")]
    assert "-2x^3" in terms
    assert "4.5x^0" in terms
    assert len(terms) == 2
