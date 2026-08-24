import pytest
from Math.Discrete_Math.Number_Theory.prime_factorisation import prime_factorization

def test_prime_factorization_edge_case():
    assert prime_factorization(1) == []

def test_prime_factorization_prime_numbers():
    assert prime_factorization(2) == [2]
    assert prime_factorization(3) == [3]
    assert prime_factorization(7) == [7]
    assert prime_factorization(13) == [13]
    assert prime_factorization(10000019) == [10000019]
    assert prime_factorization(1000000007) == [1000000007]
    assert prime_factorization(2147483647) == [2147483647]

def test_prime_factorization_composite_numbers():
    assert prime_factorization(4) == [2, 2]
    assert prime_factorization(6) == [2, 3]
    assert prime_factorization(8) == [2, 2, 2]
    assert prime_factorization(12) == [2, 2, 3]
    assert prime_factorization(15) == [3, 5]
    assert prime_factorization(100) == [2, 2, 5, 5]
    assert prime_factorization(1024) == [2] * 10
    assert prime_factorization(315) == [3, 3, 5, 7]
    assert prime_factorization(97) == [97]
    assert prime_factorization(1048576) == [2] * 20
    assert prime_factorization(999999999) == [3, 3, 3, 3, 37, 333667]

def test_prime_factorization_invalid_input():
    with pytest.raises(ValueError, match="Number must be positive."):
        prime_factorization(0)
    with pytest.raises(ValueError, match="Number must be positive."):
        prime_factorization(-1)
    with pytest.raises(ValueError, match="Number must be positive."):
        prime_factorization(-10)
