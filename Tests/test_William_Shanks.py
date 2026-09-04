import math
import pytest
from decimal import Decimal
from Math.Numerical_Methods.Constants.Pi_Algorithms.William_Shanks import (
    calculate_arctan_series_shanks,
    calculate_pi_shanks,
)


class TestWilliamShanksAlgorithm:
    def test_calculate_arctan_series_shanks_basic(self):
        val = calculate_arctan_series_shanks(2852, precision=50)
        assert isinstance(val, Decimal)
        assert math.isclose(float(val), math.atan(1 / 2852), rel_tol=1e-15)

    def test_calculate_arctan_series_shanks_zero(self):
        assert calculate_arctan_series_shanks(0, precision=50) == Decimal(0)

    def test_calculate_arctan_series_shanks_negative(self):
        pos_val = calculate_arctan_series_shanks(2852, precision=50)
        neg_val = calculate_arctan_series_shanks(-2852, precision=50)
        assert neg_val == -pos_val

    def test_calculate_pi_shanks_default_precision(self):
        pi_val = calculate_pi_shanks()
        assert isinstance(pi_val, Decimal)
        assert math.isclose(float(pi_val), math.pi, rel_tol=1e-15)

    def test_calculate_pi_shanks_basic(self):
        pi_val = calculate_pi_shanks(precision=50)
        assert isinstance(pi_val, Decimal)
        assert math.isclose(float(pi_val), math.pi, rel_tol=1e-15)

    def test_calculate_pi_shanks_high_precision(self):
        pi_val = calculate_pi_shanks(precision=100)
        pi_100_digits = (
            "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
        )
        # Check first 90 characters to avoid rounding on last digit
        assert str(pi_val).startswith(pi_100_digits[:90])

    def test_calculate_pi_shanks_invalid_precision(self):
        invalid_precisions = [0, -5, 10001, 3.14, "50", True, False]
        for prec in invalid_precisions:
            with pytest.raises(ValueError, match=r"precision must be an integer between 1 and 10000\."):
                calculate_pi_shanks(precision=prec)
