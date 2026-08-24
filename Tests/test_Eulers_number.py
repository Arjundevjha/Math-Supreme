import pytest
import math
from decimal import Decimal, getcontext

from Math.Numerical_Methods.Constants.Eulers_number import factorial_decimal, compute_eulers_number


class TestFactorialDecimal:
    def test_factorial_zero(self):
        """Test factorial of zero is 1."""
        assert factorial_decimal(0) == Decimal('1')

    def test_factorial_one(self):
        """Test factorial of one is 1."""
        assert factorial_decimal(1) == Decimal('1')

    def test_factorial_positive(self):
        """Test factorial for positive integers."""
        assert factorial_decimal(5) == Decimal('120')
        assert factorial_decimal(10) == Decimal('3628800')

    def test_factorial_negative(self):
        """Test that negative numbers raise ValueError."""
        with pytest.raises(ValueError, match="Factorial is not defined for negative numbers."):
            factorial_decimal(-1)

    def test_factorial_type(self):
        """Test that the result is of type Decimal."""
        assert isinstance(factorial_decimal(5), Decimal)


class TestComputeEulersNumber:
    def test_compute_eulers_number_basic(self):
        """Test with small number of iterations."""
        # e for 1 iteration: 1/0! = 1
        assert compute_eulers_number(iterations=1) == Decimal('1')

        # e for 2 iterations: 1/0! + 1/1! = 2
        assert compute_eulers_number(iterations=2) == Decimal('2')

        # e for 3 iterations: 1/0! + 1/1! + 1/2! = 2.5
        assert compute_eulers_number(iterations=3) == Decimal('2.5')

    def test_compute_eulers_number_convergence(self):
        """Test that the algorithm converges towards math.e as iterations increase."""
        e_5 = float(compute_eulers_number(iterations=5))
        e_10 = float(compute_eulers_number(iterations=10))
        e_20 = float(compute_eulers_number(iterations=20))

        error_5 = abs(e_5 - math.e)
        error_10 = abs(e_10 - math.e)
        error_20 = abs(e_20 - math.e)

        assert error_10 < error_5
        assert error_20 < error_10

        # At 20 terms, it should be reasonably close to e
        # After 20 terms, it should be very close to e
        assert math.isclose(e_20, math.e, rel_tol=1e-15)

    def test_compute_eulers_number_precision(self):
        """Test the precision parameter."""
        result = compute_eulers_number(iterations=50, decimal_places=100)
        assert isinstance(result, Decimal)

        # Check context precision after function execution
        _ = compute_eulers_number(iterations=10, decimal_places=100)
        assert getcontext().prec >= 110

    def test_compute_eulers_number_invalid_iterations(self):
        """Test that invalid number of iterations raises ValueError."""
        with pytest.raises(ValueError, match=r"Iterations must be between 1 and 10000\."):
            compute_eulers_number(iterations=0)

        with pytest.raises(ValueError, match=r"Iterations must be between 1 and 10000\."):
            compute_eulers_number(iterations=-5)

        with pytest.raises(ValueError, match=r"Iterations must be between 1 and 10000\."):
            compute_eulers_number(iterations=10001)

    def test_compute_eulers_number_invalid_decimal_places(self):
        """Test that invalid decimal places input raises ValueError."""
        with pytest.raises(ValueError, match=r"Decimal places must be between 1 and 10000\."):
            compute_eulers_number(decimal_places=0)

        with pytest.raises(ValueError, match=r"Decimal places must be between 1 and 10000\."):
            compute_eulers_number(decimal_places=-10)

        with pytest.raises(ValueError, match=r"Decimal places must be between 1 and 10000\."):
            compute_eulers_number(decimal_places=10001)
