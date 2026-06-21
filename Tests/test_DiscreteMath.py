import pytest
from Math.Discrete_Math.Number_Theory.gcd import prime_factorization_for_gcd

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
