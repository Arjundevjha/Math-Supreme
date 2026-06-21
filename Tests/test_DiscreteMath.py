import sys
import os
import pytest

# Adjusting sys.path to allow imports from Math/Discrete_Math/Combinatorics
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../Math/Discrete_Math/Combinatorics')))
# Adjusting sys.path to allow imports like 'from Numerical_Methods...'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../Math')))

from binomial_theorem import binomial_coefficient

def test_binomial_coefficient_normal():
    assert binomial_coefficient(5, 2) == 10
    assert binomial_coefficient(10, 3) == 120
    assert binomial_coefficient(6, 3) == 20

def test_binomial_coefficient_edge_cases():
    assert binomial_coefficient(5, 0) == 1
    assert binomial_coefficient(5, 5) == 1
    assert binomial_coefficient(0, 0) == 1

def test_binomial_coefficient_error_handling():
    with pytest.raises(ValueError, match="Invalid values for n and r"):
        binomial_coefficient(5, 6)
    with pytest.raises(ValueError, match="Invalid values for n and r"):
        binomial_coefficient(5, -1)
