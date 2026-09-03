import pytest
from Math.Discrete_Math.Number_Theory.partitions import partition

def test_partition_negative():
    assert partition(-1) == 0
    assert partition(-10) == 0

def test_partition_zero():
    assert partition(0) == 1


def test_partition_positive():
    # Known values from OEIS A000041
    # n:    0, 1, 2, 3, 4, 5, 6,  7,  8,  9, 10
    # p(n): 1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42
    assert partition(1) == 1
    assert partition(2) == 2
    assert partition(3) == 3
    assert partition(4) == 5
    assert partition(5) == 7
    assert partition(6) == 11
    assert partition(7) == 15
    assert partition(8) == 22
    assert partition(9) == 30
    assert partition(10) == 42
    assert partition(15) == 176
    assert partition(20) == 627
    assert partition(30) == 5604
    assert partition(50) == 204226


def test_partition_invalid_type():
    with pytest.raises(TypeError, match="n must be an integer."):
        partition("5")
    with pytest.raises(TypeError, match="n must be an integer."):
        partition(5.5)
    with pytest.raises(TypeError, match="n must be an integer."):
        partition(True)


def test_partition_exceeds_upper_bound():
    with pytest.raises(ValueError, match="n exceeds maximum limit of 10000."):
        partition(10001)
