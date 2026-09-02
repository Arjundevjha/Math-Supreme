import pytest
from Math.Applied_Math.Finance.Simple_Intrest import simple_interest


def test_simple_interest_basic():
    # P=1000, R=5, T=2
    # I = (1000 * 5 * 2) / 100 = 100
    # Total = 1000 + 100 = 1100
    assert simple_interest(1000, 5, 2) == 1100


def test_simple_interest_floats():
    # P=1000.50, R=4.5, T=1.5
    # I = (1000.50 * 4.5 * 1.5) / 100 = 67.53375
    # Total = 1068.03375
    res = simple_interest(1000.50, 4.5, 1.5)
    assert abs(res - 1068.03375) < 1e-9


def test_simple_interest_zero_values():
    # Principal, rate, or time equal to 0
    assert simple_interest(1000, 5, 0) == 1000
    assert simple_interest(1000, 0, 2) == 1000
    assert simple_interest(0, 5, 2) == 0


def test_simple_interest_negative_principal():
    with pytest.raises(ValueError, match=r"Principal amount, interest rate, and time must be non-negative\."):
        simple_interest(-1000, 5, 2)


def test_simple_interest_negative_rate():
    with pytest.raises(ValueError, match=r"Principal amount, interest rate, and time must be non-negative\."):
        simple_interest(1000, -5, 2)


def test_simple_interest_negative_time():
    with pytest.raises(ValueError, match=r"Principal amount, interest rate, and time must be non-negative\."):
        simple_interest(1000, 5, -2)
