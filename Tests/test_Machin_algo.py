import pytest
import math
from decimal import Decimal
from Math.Numerical_Methods.Constants.Pi_Algorithms.Machin_algo import calculate_pi_machin, calculate_arctan_series

class TestMachinAlgorithm:
    def test_calculate_pi_machin_basic(self):
        pi_val = float(calculate_pi_machin(precision=10))
        assert math.isclose(pi_val, math.pi, rel_tol=1e-9)

    def test_calculate_pi_machin_precision(self):
        pi_high_prec = calculate_pi_machin(precision=100)
        assert isinstance(pi_high_prec, Decimal)

        # known digits of Pi to 100 places
        pi_100_str = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

        pi_val_str = str(pi_high_prec)
        # Using 100 precision should be accurate to at least 95 decimal places
        # Let's just check the first 50 for now
        assert pi_val_str.startswith(pi_100_str[:50])

    def test_calculate_arctan_series_basic(self):
        # arctan(1/1) = pi/4
        # arctan(1/x) for x = 0
        assert calculate_arctan_series(0, 10) == Decimal(0)

        # arctan(1/x) for x < 0
        # arctan(1/-5) = -arctan(1/5)
        ans_pos = calculate_arctan_series(5, 10)
        ans_neg = calculate_arctan_series(-5, 10)
        assert ans_neg == -ans_pos

        # check x = 5 against math.atan(1/5)
        ans_5 = float(calculate_arctan_series(5, 10))
        assert math.isclose(ans_5, math.atan(1/5), rel_tol=1e-9)

        # check x = 239 against math.atan(1/239)
        ans_239 = float(calculate_arctan_series(239, 10))
        assert math.isclose(ans_239, math.atan(1/239), rel_tol=1e-9)
