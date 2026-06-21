import pytest
from Math.Discrete_Math.Number_Theory.lcm import prime_factorization_simple

def test_prime_factorization_simple():
    # Edge cases
    assert prime_factorization_simple(1) == []
    assert prime_factorization_simple(0) == []
    assert prime_factorization_simple(-1) == []

    # Prime numbers
    assert prime_factorization_simple(2) == [2]
    assert prime_factorization_simple(3) == [3]
    assert prime_factorization_simple(13) == [13]

    # Composite numbers
    assert prime_factorization_simple(4) == [2, 2]
    assert prime_factorization_simple(12) == [2, 2, 3]
    assert prime_factorization_simple(100) == [2, 2, 5, 5]
    assert prime_factorization_simple(315) == [3, 3, 5, 7]
