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
