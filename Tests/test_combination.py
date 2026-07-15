import os
import sys
import pytest

# Add root directory to path to allow "Math.Discrete_Math..." imports
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

# the code has imports assuming "Math" is the root in some cases, so let's add it too
math_dir = os.path.abspath(os.path.join(root_dir, 'Math'))
if math_dir not in sys.path:
    sys.path.insert(0, math_dir)

from Math.Discrete_Math.Combinatorics.combination import nCr

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

def test_nCr_large_numbers():
    """Test nCr with slightly larger numbers."""
    # 20C10 = 184756
    assert nCr(20, 10) == 184756
    # 50C5 = 2118760
    assert nCr(50, 5) == 2118760

def test_nCr_negative_n_valid_r():
    """Test nCr with negative n but valid r."""
    # nCr formula requires factorial(n). factorial raises ValueError for negative numbers
    with pytest.raises(ValueError, match="Invalid values for n and r."):
        nCr(-5, 2)
