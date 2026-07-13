import pytest
import math
from decimal import Decimal
from Math.Numerical_Methods.Constants.Pi_Algorithms.S_Ramanujan_algo import calculate_pi_ramanujan, factorial_decimal

class TestRamanujanAlgorithm:
    def test_calculate_pi_ramanujan_basic(self):
        # 1 term should be somewhat close
        pi_1 = float(calculate_pi_ramanujan(num_decimal_places=50, num_terms=1))
        # 2 terms should be very close
        pi_2 = float(calculate_pi_ramanujan(num_decimal_places=50, num_terms=2))

        assert math.isclose(pi_1, math.pi, rel_tol=1e-5)
        assert math.isclose(pi_2, math.pi, rel_tol=1e-15)

    def test_calculate_pi_ramanujan_convergence(self):
        pi_1 = float(calculate_pi_ramanujan(50, 1))
        pi_2 = float(calculate_pi_ramanujan(50, 2))
        pi_3 = float(calculate_pi_ramanujan(50, 3))

        error_1 = abs(pi_1 - math.pi)
        error_2 = abs(pi_2 - math.pi)
        error_3 = abs(pi_3 - math.pi)

        assert error_2 < error_1
        assert error_3 < error_2

    def test_calculate_pi_ramanujan_precision(self):
        # Test higher precision parameter
        pi_high_prec = calculate_pi_ramanujan(num_decimal_places=100, num_terms=10)
        assert isinstance(pi_high_prec, Decimal)

    def test_calculate_pi_ramanujan_invalid_args(self):
        with pytest.raises(ValueError, match="Number of decimal places cannot be negative."):
            calculate_pi_ramanujan(-1, 10)

        with pytest.raises(ValueError, match="Number of terms must be at least 1."):
            calculate_pi_ramanujan(50, 0)

def test_factorial_decimal_basic():
    assert factorial_decimal(0) == Decimal(1)
    assert factorial_decimal(1) == Decimal(1)
    assert factorial_decimal(5) == Decimal(120)
    assert factorial_decimal(10) == Decimal(3628800)

def test_factorial_decimal_negative():
    with pytest.raises(ValueError, match="Factorial is not defined for negative numbers."):
        factorial_decimal(-1)
