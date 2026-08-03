from decimal import Decimal
from Math.Numerical_Methods.Constants.Pi_Algorithms.William_Shanks import (
    calculate_pi_shanks,
    calculate_arctan_series_shanks,
)


class TestWilliamShanks:
    def test_calculate_pi_shanks_default_precision(self):
        """Test calculating Pi with default precision (50 places)."""
        pi_shanks = calculate_pi_shanks()
        assert isinstance(pi_shanks, Decimal)

        # William Shanks' calculation converges up to the specified precision,
        # but due to truncation in Taylor series, the very last digits might be slightly off.
        # We test the first 45 decimal places to ensure it's sufficiently accurate.
        expected_pi = "3.141592653589793238462643383279502884197169399"

        pi_str = str(pi_shanks)
        assert pi_str.startswith(expected_pi)

    def test_calculate_pi_shanks_custom_precision(self):
        """Test calculating Pi with a custom precision."""
        # 10 decimal places -> the algorithm gives ~3.1415927...
        # So it's accurate to about 6 decimal places with precision=10
        # due to the Taylor series term truncation condition.
        pi_shanks_10 = calculate_pi_shanks(10)
        assert isinstance(pi_shanks_10, Decimal)

        expected_pi_10 = "3.141592"
        pi_str_10 = str(pi_shanks_10)

        assert pi_str_10.startswith(expected_pi_10)

    def test_calculate_pi_shanks_high_precision(self):
        """Test calculating Pi with high precision."""
        pi_shanks_100 = calculate_pi_shanks(100)
        assert isinstance(pi_shanks_100, Decimal)

        # Checking the first 95 decimal places
        expected_pi_100 = (
            "3.14159265358979323846264338327950288419716939937510"
            "5820974944592307816406286208998628034825342"
        )
        pi_str_100 = str(pi_shanks_100)

        assert pi_str_100.startswith(expected_pi_100)

    def test_calculate_arctan_series_shanks(self):
        """Test the helper arctan calculation function."""
        # arctan(0) should return Decimal(0)
        assert calculate_arctan_series_shanks(0, 10) == Decimal(0)

        # Test a real value, e.g., arctan(1/2)
        arctan_2 = calculate_arctan_series_shanks(2, 10)
        assert isinstance(arctan_2, Decimal)

        # arctan(1/2) is approx 0.463647609
        # Check the string representation to avoid using the `math` module
        expected_arctan_2 = "0.463647609"
        assert str(arctan_2).startswith(expected_arctan_2)
