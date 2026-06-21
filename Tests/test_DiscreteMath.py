import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../Math')))

from Discrete_Math.Combinatorics.combination import nCr

@pytest.mark.parametrize("n, r, expected", [
    (5, 0, 1),
    (5, 1, 5),
    (5, 2, 10),
    (5, 3, 10),
    (5, 4, 5),
    (5, 5, 1),
    (10, 5, 252),
    (0, 0, 1),
    (1, 0, 1),
    (1, 1, 1),
])
def test_nCr_happy_path(n, r, expected):
    """Test nCr with valid inputs."""
    assert nCr(n, r) == expected

@pytest.mark.parametrize("n, r", [
    (5, 6),   # r > n
    (5, -1),  # r < 0
    (-1, -1), # both negative, r < 0 triggers first or both
    (-1, 0),  # r > n (-1 < 0)
])
def test_nCr_invalid_inputs(n, r):
    """Test nCr raises ValueError for invalid inputs."""
    with pytest.raises(ValueError):
        nCr(n, r)
