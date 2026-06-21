import pytest

from Math.Discrete_Math.Combinatorics.permutation import factorial
from Math.Discrete_Math.Number_Theory.gcd import compute_gcd


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
