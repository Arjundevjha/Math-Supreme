import os
import sys

import pytest

# Add root directory to path to allow "Math.Discrete_Math..." imports

# the code has imports assuming "Math" is the root in some cases, so let's add it too

from Math.Discrete_Math.Number_Theory.gcd import compute_gcd, prime_factorization_for_gcd


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


@pytest.mark.parametrize("n, expected", [
    # Test composite numbers
    (12, [2, 2, 3]),
    (60, [2, 2, 3, 5]),
    (100, [2, 2, 5, 5]),

    # Test prime numbers
    (2, [2]),
    (7, [7]),
    (13, [13]),

    # Test edge cases
    (1, []),
    (0, []),
    (-5, [])
])
def test_prime_factorization_for_gcd(n, expected):
    assert prime_factorization_for_gcd(n) == expected

import math
import random
from functools import reduce

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

def test_prime_factorization_for_gcd_product():
    """
    Test that the product of prime factors equals the original number.
    """
    random.seed(42)
    for _ in range(50):
        n = random.randint(2, 5000)
        factors = prime_factorization_for_gcd(n)
        product = reduce(lambda x, y: x * y, factors, 1)
        assert product == n
def test_compute_gcd_large_numbers():
    assert compute_gcd(123456, 789012) == 12

def test_prime_factorization_for_gcd_large():
    assert prime_factorization_for_gcd(1048576) == [2] * 20
