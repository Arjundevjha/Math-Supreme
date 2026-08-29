import math
from decimal import Decimal
from Math.Numerical_Methods.Constants.Pi_Algorithms.Chudnovsky_algo import calculate_pi_chudnovsky


class TestChudnovskyAlgorithm:
    def test_calculate_pi_chudnovsky_basic(self):
        """Test that the algorithm returns a value very close to math.pi."""
        pi_val = float(calculate_pi_chudnovsky(50))
        assert math.isclose(pi_val, math.pi, rel_tol=1e-15)

    def test_calculate_pi_chudnovsky_precision(self):
        """Test that the function returns a Decimal object."""
        pi_val = calculate_pi_chudnovsky(50)
        assert isinstance(pi_val, Decimal)

    def test_calculate_pi_chudnovsky_exact_digits(self):
        """Test against the first 50 known digits of Pi to verify arbitrary precision."""
        # 50 decimal places of pi
        pi_50_digits = "3.14159265358979323846264338327950288419716939937510"

        # Calculate with slightly higher precision to avoid rounding issues on the last digit
        pi_val = calculate_pi_chudnovsky(55)

        # Check if it starts with the 50 digits
        assert str(pi_val).startswith(pi_50_digits)

    def test_calculate_pi_chudnovsky_invalid_precision_bounds(self):
        """Test that invalid precision values raise ValueError."""
        import pytest
        for invalid_precision in [0, -10, 10001, True, "50", 50.5]:
            with pytest.raises(ValueError, match=r"Precision must be an integer between 1 and 10000\."):
                calculate_pi_chudnovsky(invalid_precision)
