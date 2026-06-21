import sys
import os
import pytest

# Add paths to enable imports
app_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(app_root, 'Math'))
sys.path.append(os.path.join(app_root, 'Math', 'Discrete_Math', 'Combinatorics'))

from binomial_theorem import expand_binomial

def test_expand_binomial_basic():
    # (x + y)^2 = 1*x^2*y^0 + 2*x^1*y^1 + 1*x^0*y^2
    result = expand_binomial('x', 'y', 2)
    terms = [term.strip() for term in result.split('+')]

    assert "1*x^2*y^0" in terms
    assert "2*x^1*y^1" in terms
    assert "1*x^0*y^2" in terms
    assert len(terms) == 3

def test_expand_binomial_n_0():
    # (x + y)^0 = 1*x^0*y^0
    result = expand_binomial('x', 'y', 0)
    terms = [term.strip() for term in result.split('+')]

    assert "1*x^0*y^0" in terms
    assert len(terms) == 1

def test_expand_binomial_n_3():
    # (a + b)^3 = 1*a^3*b^0 + 3*a^2*b^1 + 3*a^1*b^2 + 1*a^0*b^3
    result = expand_binomial('a', 'b', 3)
    terms = [term.strip() for term in result.split('+')]

    assert "1*a^3*b^0" in terms
    assert "3*a^2*b^1" in terms
    assert "3*a^1*b^2" in terms
    assert "1*a^0*b^3" in terms
    assert len(terms) == 4

def test_expand_binomial_negative_n():
    with pytest.raises(ValueError, match="Power n must be non-negative."):
        expand_binomial('x', 'y', -1)
