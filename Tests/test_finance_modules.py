import pytest

from Math.Applied_Math.Finance.annuities import (
    annuity_payment,
    future_value_annuity,
    present_value_annuity,
)
from Math.Applied_Math.Finance.black_scholes_option_pricing import (
    black_scholes_call,
    black_scholes_price,
    black_scholes_put,
)
from Math.Applied_Math.Finance.mortgage_calculator import (
    amortization_schedule,
    monthly_mortgage_payment,
    total_mortgage_interest,
    total_mortgage_payment,
)
from Math.Applied_Math.Finance.sharpe_ratio import (
    sharpe_ratio,
    sharpe_ratio_from_stats,
)


class TestAnnuities:
    def test_present_value_ordinary(self):
        pv = present_value_annuity(1000, 0.05, 5)
        assert pv == pytest.approx(4329.476670630819, rel=1e-9)

    def test_present_value_due(self):
        pv_due = present_value_annuity(1000, 0.05, 5, annuity_due=True)
        assert pv_due == pytest.approx(4545.95050416236, rel=1e-9)

    def test_future_value_ordinary_and_due(self):
        fv = future_value_annuity(1000, 0.05, 5)
        assert fv == pytest.approx(5525.63125, rel=1e-9)
        fv_due = future_value_annuity(1000, 0.05, 5, annuity_due=True)
        assert fv_due == pytest.approx(5801.9128125, rel=1e-9)

    def test_zero_rate_and_zero_payment(self):
        assert present_value_annuity(500, 0, 10) == 5000.0
        assert future_value_annuity(500, 0, 10) == 5000.0
        assert present_value_annuity(0, 0.05, 10) == 0.0
        assert future_value_annuity(1000, 0.05, 0) == 0.0

    def test_annuity_payment_roundtrip(self):
        pmt = annuity_payment(10000, 0.05, 5)
        assert pmt == pytest.approx(2309.74798128268, rel=1e-9)
        assert present_value_annuity(pmt, 0.05, 5) == pytest.approx(
            10000.0, rel=1e-9
        )
        pmt_due = annuity_payment(10000, 0.05, 5, annuity_due=True)
        assert present_value_annuity(
            pmt_due, 0.05, 5, annuity_due=True
        ) == pytest.approx(10000.0, rel=1e-9)
        assert annuity_payment(1200, 0, 12) == 100.0
        assert annuity_payment(0, 0.05, 12) == 0.0

    def test_annuity_validation(self):
        with pytest.raises(TypeError):
            present_value_annuity("1000", 0.05, 5)
        with pytest.raises(TypeError):
            present_value_annuity(True, 0.05, 5)
        with pytest.raises(TypeError):
            present_value_annuity(1000, 0.05, 5, annuity_due="yes")
        with pytest.raises(ValueError):
            present_value_annuity(-100, 0.05, 5)
        with pytest.raises(ValueError):
            future_value_annuity(100, -0.01, 5)
        with pytest.raises(ValueError):
            annuity_payment(1000, 0.05, 0)
        with pytest.raises(ValueError):
            present_value_annuity(float("nan"), 0.05, 5)


class TestMortgageCalculator:
    def test_monthly_and_total_mortgage(self):
        pmt = monthly_mortgage_payment(200000, 6.0, 30)
        assert pmt == pytest.approx(1199.1010503055283, rel=1e-9)
        total = total_mortgage_payment(200000, 6.0, 30)
        assert total == pytest.approx(pmt * 360, rel=1e-9)
        interest = total_mortgage_interest(200000, 6.0, 30)
        assert interest == pytest.approx(total - 200000, rel=1e-9)

    def test_zero_interest_and_zero_principal(self):
        assert monthly_mortgage_payment(120000, 0.0, 10) == pytest.approx(
            1000.0, rel=1e-9
        )
        assert monthly_mortgage_payment(0, 5.0, 15) == 0.0

    def test_amortization_schedule(self):
        schedule = amortization_schedule(10000, 6.0, 1)
        assert len(schedule) == 12
        assert schedule[0]["month"] == 1.0
        assert schedule[-1]["remaining_balance"] == pytest.approx(
            0.0, abs=1e-9
        )
        total_principal = sum(row["principal_paid"] for row in schedule)
        assert total_principal == pytest.approx(10000.0, rel=1e-9)

    def test_mortgage_validation(self):
        with pytest.raises(TypeError):
            monthly_mortgage_payment("200000", 6.0, 30)
        with pytest.raises(TypeError):
            monthly_mortgage_payment(200000, False, 30)
        with pytest.raises(TypeError):
            amortization_schedule(10000, 6.0, 1.5)
        with pytest.raises(ValueError):
            monthly_mortgage_payment(-1000, 6.0, 30)
        with pytest.raises(ValueError):
            monthly_mortgage_payment(100000, 6.0, 0)
        with pytest.raises(ValueError):
            monthly_mortgage_payment(100000, 6.0, 101)


class TestSharpeRatio:
    def test_sharpe_from_stats(self):
        assert sharpe_ratio_from_stats(0.12, 0.02, 0.10) == pytest.approx(
            1.0, rel=1e-9
        )

    def test_sharpe_from_returns(self):
        returns = [0.05, 0.07, 0.03, 0.09]
        sr = sharpe_ratio(returns, risk_free_rate=0.01)
        # mean = 0.06, excess mean = 0.05, sample std = sqrt(0.002/3)
        assert sr == pytest.approx(1.9364916731037085, rel=1e-7)

        sr_annual = sharpe_ratio(
            returns, risk_free_rate=0.01, periods_per_year=12
        )
        assert sr_annual == pytest.approx(sr * (12**0.5), rel=1e-7)

    def test_sharpe_validation(self):
        with pytest.raises(TypeError):
            sharpe_ratio("not a list")
        with pytest.raises(TypeError):
            sharpe_ratio([0.05, True])
        with pytest.raises(ValueError):
            sharpe_ratio([0.05])
        with pytest.raises(ValueError):
            sharpe_ratio([0.05, 0.05, 0.05], 0.01)
        with pytest.raises(ValueError):
            sharpe_ratio_from_stats(0.1, 0.02, 0.0)
        with pytest.raises(ValueError):
            sharpe_ratio([0.01, 0.02], 0.0, periods_per_year=0)


class TestBlackScholes:
    def test_call_and_put_reference_values(self):
        call = black_scholes_call(100, 100, 1, 0.05, 0.2)
        put = black_scholes_put(100, 100, 1, 0.05, 0.2)
        assert call == pytest.approx(10.450583572185565, abs=1e-5)
        assert put == pytest.approx(5.573526022256971, abs=1e-5)

    def test_put_call_parity(self):
        s_val, k_val, t_val, r_val, sigma = 120, 100, 0.5, 0.04, 0.25
        call = black_scholes_price(s_val, k_val, t_val, r_val, sigma, "CALL")
        put = black_scholes_price(s_val, k_val, t_val, r_val, sigma, "put")
        # C - P = S - K * exp(-rT)
        rhs = s_val - k_val * (2.718281828459045 ** (-r_val * t_val))
        assert (call - put) == pytest.approx(rhs, abs=1e-6)

    def test_zero_time_to_maturity(self):
        assert black_scholes_call(110, 100, 0, 0.05, 0.2) == 10.0
        assert black_scholes_call(90, 100, 0, 0.05, 0.2) == 0.0
        assert black_scholes_put(90, 100, 0, 0.05, 0.2) == 10.0
        assert black_scholes_put(110, 100, 0, 0.05, 0.2) == 0.0

    def test_black_scholes_validation(self):
        with pytest.raises(TypeError):
            black_scholes_call("100", 100, 1, 0.05, 0.2)
        with pytest.raises(TypeError):
            black_scholes_call(100, True, 1, 0.05, 0.2)
        with pytest.raises(TypeError):
            black_scholes_price(100, 100, 1, 0.05, 0.2, option_type=123)
        with pytest.raises(ValueError):
            black_scholes_price(100, 100, 1, 0.05, 0.2, option_type="straddle")
        with pytest.raises(ValueError):
            black_scholes_call(0, 100, 1, 0.05, 0.2)
        with pytest.raises(ValueError):
            black_scholes_call(100, 100, -1, 0.05, 0.2)
        with pytest.raises(ValueError):
            black_scholes_call(100, 100, 1, 0.05, 0)
        with pytest.raises(ValueError):
            black_scholes_call(float("inf"), 100, 1, 0.05, 0.2)
