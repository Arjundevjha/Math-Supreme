import math
from decimal import Decimal
from Math.Numerical_Methods.Constants.Pi_Algorithms.William_Shanks import (
    calculate_arctan_series_shanks,
    calculate_pi_shanks,
)


class TestWilliamShanksAlgorithm:
    def test_calculate_pi_shanks_type_and_precision(self):
        """Test that calculate_pi_shanks returns a Decimal object."""
        result = calculate_pi_shanks(precision=50)
        assert isinstance(result, Decimal)

    def test_calculate_pi_shanks_approx(self):
        """Test that calculate_pi_shanks returns a value close to math.pi."""
        pi_val = float(calculate_pi_shanks(precision=50))
        assert math.isclose(pi_val, math.pi, rel_tol=1e-15)

    def test_calculate_pi_shanks_exact_digits(self):
        """Test calculate_pi_shanks against known digits of Pi."""
        pi_50_digits = "3.14159265358979323846264338327950288419716939937510"
        pi_val = calculate_pi_shanks(precision=55)
        assert str(pi_val).startswith(pi_50_digits)

    def test_calculate_arctan_series_shanks_zero(self):
        """Test calculate_arctan_series_shanks with x=0."""
        assert calculate_arctan_series_shanks(0, 50) == Decimal(0)

    def test_calculate_arctan_series_shanks_negative(self):
        """Test calculate_arctan_series_shanks with negative inputs."""
        pos_val = calculate_arctan_series_shanks(5, 50)
        neg_val = calculate_arctan_series_shanks(-5, 50)
        assert neg_val == -pos_val

    def test_calculate_arctan_series_shanks_values(self):
        """Test calculate_arctan_series_shanks against known mathematical values."""
        # arctan(1/5) ≈ 0.1973955598
        # arctan(1/239) ≈ 0.004184076
        val_5 = calculate_arctan_series_shanks(5, 10)
        val_239 = calculate_arctan_series_shanks(239, 10)
        assert math.isclose(float(val_5), math.atan(1 / 5), rel_tol=1e-9)
        assert math.isclose(float(val_239), math.atan(1 / 239), rel_tol=1e-9)
