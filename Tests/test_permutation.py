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

from Math.Discrete_Math.Combinatorics.permutation import factorial, n_permute_r

@pytest.mark.parametrize("n, r, expected", [
    (5, 0, 1),
    (5, 1, 5),
    (5, 2, 20),
    (5, 3, 60),
    (5, 4, 120),
    (5, 5, 120),
    (10, 5, 30240),
    (100, 2, 9900),
    (0, 0, 1),
    (1, 0, 1),
    (1, 1, 1),
])
def test_n_permute_r_happy_path(n, r, expected):
    """Test n_permute_r with valid inputs."""
    assert n_permute_r(n, r) == expected

@pytest.mark.parametrize("n, r", [
    (5, 6),   # r > n
    (3, 5),   # r > n
])
def test_n_permute_r_invalid_inputs(n, r):
    """Test n_permute_r raises ValueError for invalid inputs."""
    with pytest.raises(ValueError):
        n_permute_r(n, r)

@pytest.mark.parametrize("n, r", [
    ("5", 2),
    (5, "2"),
    (None, 2),
])
def test_n_permute_r_invalid_types(n, r):
    """Test n_permute_r raises TypeError for non-integer inputs."""
    with pytest.raises(TypeError):
        n_permute_r(n, r)

def test_n_permute_r_value_error_message():
    """Test that n_permute_r raises ValueError with the correct message."""
    with pytest.raises(ValueError, match="n should be greater than or equal to r for permutations to be valid."):
        n_permute_r(5, 6)

def test_n_permute_r_large_numbers():
    """Test n_permute_r with slightly larger numbers."""
    # 20P10 = 20! / 10! = 670442572800
    assert n_permute_r(20, 10) == 670442572800
    # 50P5 = 50! / 45! = 254251200
    assert n_permute_r(50, 5) == 254251200

def test_n_permute_r_negative_n_valid_r():
    """Test n_permute_r with negative n but valid r."""
    with pytest.raises(ValueError, match="n and r must be non-negative integers"):
        n_permute_r(-5, 2)

def test_n_permute_r_negative_r():
    """Test n_permute_r with valid n but negative r."""
    with pytest.raises(ValueError, match="n and r must be non-negative integers"):
        n_permute_r(5, -2)


def test_factorial_happy_path():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120

def test_factorial_negative():
    with pytest.raises(ValueError, match="Factorial is not defined for negative numbers."):
        factorial(-1)

def test_factorial_limit():
    with pytest.raises(ValueError, match="Factorial calculation limit exceeded"):
        factorial(1001)
