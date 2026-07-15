import pytest
import math
from decimal import Decimal
from Math.Numerical_Methods.Constants.Pi_Algorithms.Nilakanths_algo import calculate_pi_nilakantha
from Math.Numerical_Methods.Functions.Factorial.factorial import factorial

class TestNilakanthaAlgorithm:
    def test_calculate_pi_nilakantha_basic(self):
        """Test with small number of terms to check exact values"""
        # π = 3 + 4/(2×3×4) = 3 + 4/24 = 3 + 1/6 = 19/6
        assert float(calculate_pi_nilakantha(1)) == pytest.approx(19/6)

        # π = 3 + 4/(2×3×4) - 4/(4×5×6) = 19/6 - 4/120 = 19/6 - 1/30 = (95-1)/30 = 94/30 = 47/15
        assert float(calculate_pi_nilakantha(2)) == pytest.approx(47/15)

    def test_calculate_pi_nilakantha_convergence(self):
        """Test that the algorithm converges towards math.pi as terms increase"""
        pi_10 = float(calculate_pi_nilakantha(10))
        pi_100 = float(calculate_pi_nilakantha(100))
        pi_1000 = float(calculate_pi_nilakantha(1000))

        # The error should decrease as the number of terms increases
        error_10 = abs(pi_10 - math.pi)
        error_100 = abs(pi_100 - math.pi)
        error_1000 = abs(pi_1000 - math.pi)

        assert error_100 < error_10
        assert error_1000 < error_100

        # At 1000 terms, it should be reasonably close to pi
        assert math.isclose(pi_1000, math.pi, rel_tol=1e-5)

    def test_calculate_pi_nilakantha_precision(self):
        """Test the precision parameter"""
        result = calculate_pi_nilakantha(terms=10, precision=10)
        assert isinstance(result, Decimal)
        # Check that we can get high precision without errors
        high_prec_result = calculate_pi_nilakantha(terms=10, precision=100)
        assert isinstance(high_prec_result, Decimal)

    def test_calculate_pi_nilakantha_invalid_terms(self):
        """Test that invalid number of terms raises ValueError"""
        with pytest.raises(ValueError, match="Number of terms must be a positive integer."):
            calculate_pi_nilakantha(0)

        with pytest.raises(ValueError, match="Number of terms must be a positive integer."):
            calculate_pi_nilakantha(-5)


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
