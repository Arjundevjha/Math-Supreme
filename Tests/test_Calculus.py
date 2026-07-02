import pytest
from Math.Calculus.Differentiation.chain_rule import chain_rule_derivative

def test_chain_rule_derivative_basic():
    # g(x) = x^2, n = 3 => (x^2)^3 => derivative is 3(x^2)^2 * (2x)
    result = chain_rule_derivative([1], [2], 3)
    # Check parts of the string independently to avoid brittle tests
    assert "3(" in result
    assert "1x^2" in result
    assert ")^2" in result
    assert "* (2x^1)" in result

def test_chain_rule_derivative_multiple_terms():
    # g(x) = x^2 + 2x, n = 3
    result = chain_rule_derivative([1, 2], [2, 1], 3)
    assert "3(" in result
    assert "1x^2 + 2x^1" in result
    assert ")^2" in result
    assert "* (2x^1 + 2x^0)" in result

def test_chain_rule_derivative_constant_inner():
    # g(x) = 5, n = 2 => (5)^2 => derivative is 2(5)^1 * 0
    result = chain_rule_derivative([5], [0], 2)
    assert "2(5x^0)^1" in result
    assert "* ()" in result

def test_chain_rule_derivative_zero_exponent():
    # g(x) = x^2 + 2, n = 0 => (x^2 + 2)^0 => derivative is 0(...)
    result = chain_rule_derivative([1, 2], [2, 0], 0)
    assert result.startswith("0(")

def test_chain_rule_derivative_negative_exponent():
    # Negative exponent should raise ValueError
    with pytest.raises(ValueError, match="Exponent must be non-negative."):
        chain_rule_derivative([1, 2], [2, 0], -1)
