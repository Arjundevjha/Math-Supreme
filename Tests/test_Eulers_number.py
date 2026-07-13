import pytest
import math
from decimal import Decimal

from Math.Numerical_Methods.Constants.Eulers_number import factorial_decimal, compute_eulers_number

class TestFactorialDecimal:
    def test_factorial_zero(self):
        assert factorial_decimal(0) == Decimal('1')

    def test_factorial_one(self):
        assert factorial_decimal(1) == Decimal('1')

    def test_factorial_positive(self):
        assert factorial_decimal(5) == Decimal('120')
        assert factorial_decimal(10) == Decimal('3628800')

    def test_factorial_negative(self):
        with pytest.raises(ValueError, match="Factorial is not defined for negative numbers."):
            factorial_decimal(-1)


class TestComputeEulersNumber:
    def test_compute_eulers_number_small_iterations(self):
        # 0 iterations is ValueError
        with pytest.raises(ValueError, match="Iterations must be positive."):
            compute_eulers_number(0)

        with pytest.raises(ValueError, match="Iterations must be positive."):
            compute_eulers_number(-5)

        # e for 1 iteration: 1/0! = 1
        assert compute_eulers_number(1) == Decimal('1')

        # e for 2 iterations: 1/0! + 1/1! = 2
        assert compute_eulers_number(2) == Decimal('2')

        # e for 3 iterations: 1/0! + 1/1! + 1/2! = 2.5
        assert compute_eulers_number(3) == Decimal('2.5')

    def test_compute_eulers_number_convergence(self):
        # After 20 iterations, the value should be very close to math.e
        e_approx = compute_eulers_number(20)
        assert math.isclose(float(e_approx), math.e, rel_tol=1e-15)

    def test_compute_eulers_number_precision(self):
        # Test that we can specify the precision
        result = compute_eulers_number(50, 100)
        assert isinstance(result, Decimal)

        # Check if the context precision was indeed increased
        # The decimal context precision is set globally in the function to decimal_places + 10
        # For decimal_places=100, the context precision should be 110.
        from decimal import getcontext
        assert getcontext().prec >= 110
