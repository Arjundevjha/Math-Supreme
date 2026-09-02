import pytest
from Math.Applied_Math.Finance.Compund_intrest import compound_interest


def test_compound_interest_regular_intervals():
    # Annually
    expected_annually = 1628.894626777442
    assert abs(compound_interest(1000, 5, 10, 1) - expected_annually) < 1e-7

    # Semi-annually
    expected_semi_annually = 1638.616440288897
    assert abs(compound_interest(1000, 5, 10, 2) - expected_semi_annually) < 1e-7

    # Quarterly
    expected_quarterly = 1643.6194634289874
    assert abs(compound_interest(1000, 5, 10, 4) - expected_quarterly) < 1e-7

    # Monthly
    expected_monthly = 1647.00949769028
    assert abs(compound_interest(1000, 5, 10, 12) - expected_monthly) < 1e-7

    # Daily
    expected_daily = 1648.6648137652346
    assert abs(compound_interest(1000, 5, 10, 365) - expected_daily) < 1e-7


def test_compound_interest_float_inputs():
    # P=1000.50, rate=4.5%, time=2.5 years, monthly frequency (n=12)
    expected = 1119.3962342681201
    assert abs(compound_interest(1000.50, 4.5, 2.5, 12) - expected) < 1e-7


def test_compound_interest_zero_values():
    # Zero time
    assert abs(compound_interest(1000, 5, 0, 1) - 1000.0) < 1e-7

    # Zero interest rate
    assert abs(compound_interest(1000, 0, 10, 1) - 1000.0) < 1e-7

    # Zero principal amount
    assert abs(compound_interest(0, 5, 10, 1) - 0.0) < 1e-7


def test_compound_interest_negative_principal():
    with pytest.raises(
        ValueError,
        match=r"^Principal amount, interest rate, and time must be non-negative\.$",
    ):
        compound_interest(-1000, 5, 10, 1)


def test_compound_interest_negative_rate():
    with pytest.raises(
        ValueError,
        match=r"^Principal amount, interest rate, and time must be non-negative\.$",
    ):
        compound_interest(1000, -5, 10, 1)


def test_compound_interest_negative_time():
    with pytest.raises(
        ValueError,
        match=r"^Principal amount, interest rate, and time must be non-negative\.$",
    ):
        compound_interest(1000, 5, -10, 1)


def test_compound_interest_invalid_frequency():
    # Zero frequency
    with pytest.raises(
        ValueError,
        match=r"^Compound frequency must be positive\.$",
    ):
        compound_interest(1000, 5, 10, 0)

    # Negative frequency
    with pytest.raises(
        ValueError,
        match=r"^Compound frequency must be positive\.$",
    ):
        compound_interest(1000, 5, 10, -1)
