import math
import random
import pytest

from Math.Discrete_Math.Number_Theory.gcd import compute_gcd


def test_compute_gcd_coprime():
    assert compute_gcd(17, 19) == 1
    assert compute_gcd(8, 9) == 1


def test_compute_gcd_multiples():
    assert compute_gcd(10, 5) == 5
    assert compute_gcd(5, 10) == 5
    assert compute_gcd(12, 36) == 12


def test_compute_gcd_identical():
    assert compute_gcd(7, 7) == 7
    assert compute_gcd(100, 100) == 100


def test_compute_gcd_common_factors():
    assert compute_gcd(48, 18) == 6
    assert compute_gcd(54, 24) == 6


def test_compute_gcd_errors():
    with pytest.raises(ValueError, match="Both numbers must be positive."):
        compute_gcd(0, 5)
    with pytest.raises(ValueError, match="Both numbers must be positive."):
        compute_gcd(5, 0)
    with pytest.raises(ValueError, match="Both numbers must be positive."):
        compute_gcd(-5, 5)


def test_compute_gcd_against_math_gcd():
    """
    Test compute_gcd against Python's built-in math.gcd with a wide range
    of randomly generated pairs to ensure broad correctness.
    """
    random.seed(42)  # For reproducibility
    for _ in range(100):
        a = random.randint(1, 10000)
        b = random.randint(1, 10000)
        assert compute_gcd(a, b) == math.gcd(a, b)


def test_compute_gcd_large_numbers():
    assert compute_gcd(123456, 789012) == 12
