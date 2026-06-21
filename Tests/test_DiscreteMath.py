import pytest
from Math.Discrete_Math.Combinatorics.permutation import factorial

def test_factorial_zero():
    """Test that factorial of 0 is 1."""
    assert factorial(0) == 1

def test_factorial_one():
    """Test that factorial of 1 is 1."""
    assert factorial(1) == 1

def test_factorial_positive_integers():
    """Test factorial calculation for positive integers."""
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120
    assert factorial(10) == 3628800

def test_factorial_large_number():
    """Test factorial calculation for a slightly larger number."""
    # 20! = 2432902008176640000
    assert factorial(20) == 2432902008176640000

def test_factorial_negative_number():
    """Test factorial with a negative number, which should raise RecursionError due to infinite recursion."""
    with pytest.raises(RecursionError):
        factorial(-1)
