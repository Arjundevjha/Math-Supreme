import math
from decimal import Decimal
from Math.Numerical_Methods.Constants.Pi_Algorithms.Machin_algo import (
    calculate_arctan_series,
    calculate_pi_machin,
)


class TestMachinAlgorithm:
    def test_calculate_pi_machin_basic(self):
        """Test that the algorithm converges towards math.pi with default precision"""
        pi_val = float(calculate_pi_machin(15))
        assert math.isclose(pi_val, math.pi, rel_tol=1e-15)

    def test_calculate_pi_machin_precision(self):
        """Test the precision parameter of the calculate_pi_machin function"""
        result = calculate_pi_machin(precision=10)
        assert isinstance(result, Decimal)
        # Check that we can get high precision without errors
        high_prec_result = calculate_pi_machin(precision=100)
        assert isinstance(high_prec_result, Decimal)

    def test_calculate_arctan_series_zero(self):
        """Test arctan of 1/x where x is 0 (handled gracefully as returning 0)"""
        assert calculate_arctan_series(0, 50) == Decimal(0)

    def test_calculate_arctan_series_negative(self):
        """Test arctan of 1/x where x is negative"""
        pos_val = calculate_arctan_series(5, 50)
        neg_val = calculate_arctan_series(-5, 50)
        assert neg_val == -pos_val

    def test_calculate_arctan_series_basic(self):
        """Test arctan of 1/x for basic values"""
        val_5 = float(calculate_arctan_series(5, 15))
        expected_5 = math.atan(1 / 5)
        assert math.isclose(val_5, expected_5, rel_tol=1e-15)

        val_239 = float(calculate_arctan_series(239, 15))
        expected_239 = math.atan(1 / 239)
        assert math.isclose(val_239, expected_239, rel_tol=1e-15)
