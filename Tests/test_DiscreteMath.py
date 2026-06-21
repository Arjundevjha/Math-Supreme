import pytest
import sys
import os

# Add Math directory to sys.path so 'Numerical_Methods' can be found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../Math')))

# Add Combinatorics directory to sys.path so 'combination' can be found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../Math/Discrete_Math/Combinatorics')))

# Add root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Math.Discrete_Math.Combinatorics.binomial_theorem_general_term import binomial_general_term

def test_binomial_general_term():
    # (a + b)^2 = a^2 + 2ab + b^2
    assert binomial_general_term(2, 0, 1, 1) == 1
    assert binomial_general_term(2, 1, 1, 1) == 2
    assert binomial_general_term(2, 2, 1, 1) == 1

def test_binomial_general_term_edge_cases():
    # Test r < 0 or r > n
    with pytest.raises(ValueError, match="Invalid values for n and r"):
        binomial_general_term(2, -1, 1, 1)
    with pytest.raises(ValueError, match="Invalid values for n and r"):
        binomial_general_term(2, 3, 1, 1)

def test_binomial_general_term_powers():
    # (2 + 3)^3 = 1*2^3*3^0 + 3*2^2*3^1 + 3*2^1*3^2 + 1*2^0*3^3
    # n=3, r=0: 1 * 8 * 1 = 8
    # n=3, r=1: 3 * 4 * 3 = 36
    # n=3, r=2: 3 * 2 * 9 = 54
    # n=3, r=3: 1 * 1 * 27 = 27
    assert binomial_general_term(3, 0, 2, 3) == 8
    assert binomial_general_term(3, 1, 2, 3) == 36
    assert binomial_general_term(3, 2, 2, 3) == 54
    assert binomial_general_term(3, 3, 2, 3) == 27
