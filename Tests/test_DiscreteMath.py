import sys
import os

from Math.Discrete_Math.Combinatorics.trinomial_theorem import trinomial_coefficient

def test_trinomial_coefficient():
    # Test cases with positive values for n, i, j
    assert trinomial_coefficient(2, 1, 1) == 2
    assert trinomial_coefficient(3, 1, 1) == 6
    assert trinomial_coefficient(3, 2, 1) == 3
    assert trinomial_coefficient(3, 3, 0) == 1
    assert trinomial_coefficient(0, 0, 0) == 1

    # Test cases where i + j > n
    assert trinomial_coefficient(2, 2, 1) == 0
    assert trinomial_coefficient(3, 2, 2) == 0

    # Test cases with negative indices
    assert trinomial_coefficient(2, -1, 1) == 0
    assert trinomial_coefficient(2, 1, -1) == 0
