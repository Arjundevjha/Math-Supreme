import pytest
import math
from decimal import Decimal
from Math.Numerical_Methods.Constants.Pi_Algorithms.Chudnovsky_algo import calculate_pi_chudnovsky

class TestChudnovskyAlgorithm:
    def test_calculate_pi_chudnovsky_basic(self):
        # 50 terms precision should be close to math.pi
        pi_val = float(calculate_pi_chudnovsky(precision=50))
        assert math.isclose(pi_val, math.pi, rel_tol=1e-15)

    def test_calculate_pi_chudnovsky_precision(self):
        # First 50 digits of Pi after the decimal point
        pi_50_str = "3.14159265358979323846264338327950288419716939937510"
        pi_val = calculate_pi_chudnovsky(precision=50)

        assert isinstance(pi_val, Decimal)
        # Check if the result converted to string starts with the known string
        pi_val_str = str(pi_val)[:len(pi_50_str)]
        assert pi_val_str == pi_50_str

    def test_calculate_pi_chudnovsky_100_precision(self):
        # First 100 digits of Pi
        pi_100_str = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
        pi_val = calculate_pi_chudnovsky(precision=100)

        assert isinstance(pi_val, Decimal)
        pi_val_str = str(pi_val)[:len(pi_100_str)]
        assert pi_val_str == pi_100_str
