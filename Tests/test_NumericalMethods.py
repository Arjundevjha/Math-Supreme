import pytest
from Math.Numerical_Methods.Functions.Factorial.factorial import factorial

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_one():
    assert factorial(1) == 1

def test_factorial_positive():
    assert factorial(5) == 120
    assert factorial(10) == 3628800

def test_factorial_negative():
    with pytest.raises(ValueError, match="Factorial is not defined for negative numbers."):
        factorial(-1)
