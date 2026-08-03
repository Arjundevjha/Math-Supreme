from decimal import Decimal
from Math.Numerical_Methods.Constants.Pi_Algorithms.Machin_algo import (
    calculate_arctan_series,
    calculate_pi_machin,
)


class TestMachinAlgorithm:
    def test_calculate_pi_machin_basic(self):
        """Test that the algorithm converges towards Pi with default precision"""
        pi_val = calculate_pi_machin(15)
        # 3.141592653589793
        expected_pi_prefix = "3.14159265358979"
        assert str(pi_val).startswith(expected_pi_prefix)

    def test_calculate_pi_machin_precision(self):
        """Test the precision parameter of the calculate_pi_machin function"""
        result = calculate_pi_machin(precision=10)
        assert isinstance(result, Decimal)
        # Check that we can get high precision without errors
        high_prec_result = calculate_pi_machin(precision=100)
        assert isinstance(high_prec_result, Decimal)

        # 100 digits of Pi
        expected_pi_prefix = "3.14159265358979323846264338327950288419716939937510"
        assert str(high_prec_result).startswith(expected_pi_prefix)

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
        val_5 = calculate_arctan_series(5, 15)
        # arctan(1/5) ~ 0.1973955598498807
        expected_5_prefix = "0.197395559849880"
        assert str(val_5).startswith(expected_5_prefix)

        val_239 = calculate_arctan_series(239, 15)
        # arctan(1/239) ~ 0.0041840760020747
        expected_239_prefix = "0.00418407600207"
        assert str(val_239).startswith(expected_239_prefix)
