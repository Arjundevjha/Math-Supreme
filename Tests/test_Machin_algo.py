import math
from decimal import Decimal
from Math.Numerical_Methods.Constants.Pi_Algorithms.Machin_algo import calculate_pi_machin, calculate_arctan_series

class TestMachinAlgorithm:
    def test_calculate_pi_machin_basic(self):
        # 50 precision
        pi_val = calculate_pi_machin(precision=50)
        assert isinstance(pi_val, Decimal)
        # Verify it matches math.pi to a reasonable degree
        assert math.isclose(float(pi_val), math.pi, rel_tol=1e-15)

    def test_calculate_pi_machin_high_precision(self):
        # Calculate to 100 digits and compare with string literal
        pi_val = calculate_pi_machin(precision=100)
        # known digits of Pi
        pi_100_digits = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

        # Test exact match of the string prefix
        # Check first 90 characters to avoid any rounding errors at the very end
        assert str(pi_val).startswith(pi_100_digits[:90])

    def test_calculate_arctan_series_zero(self):
        assert calculate_arctan_series(0, 50) == Decimal(0)

    def test_calculate_arctan_series_negative(self):
        pos_val = calculate_arctan_series(5, 50)
        neg_val = calculate_arctan_series(-5, 50)
        assert neg_val == -pos_val

    def test_calculate_arctan_series_values(self):
        # We know that arctan(1/5) is approximately 0.1973955598
        # and arctan(1/239) is approximately 0.004184076
        val_5 = calculate_arctan_series(5, 10)
        val_239 = calculate_arctan_series(239, 10)
        assert math.isclose(float(val_5), math.atan(1/5), rel_tol=1e-9)
        assert math.isclose(float(val_239), math.atan(1/239), rel_tol=1e-9)
