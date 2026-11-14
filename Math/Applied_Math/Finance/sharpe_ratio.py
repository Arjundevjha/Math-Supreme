"""Calculate the Sharpe ratio for investment returns."""
from typing import Sequence, Union

from Math.Numerical_Methods.Functions.nth_root.nth_root import nth_root
from Math.Probability_and_Statistics.Descriptive_Statistics.mean import mean


def _validate_finite_number(name: str, value: Union[int, float]) -> float:
    """
    Validate that a value is a finite int or float (excluding bool).

    Parameters:
    name (str): Parameter name for error messages.
    value (Union[int, float]): Numeric value to validate.

    Returns:
    float: The validated value as a float.
    """
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a numeric int or float.")
    if not -float("inf") < value < float("inf"):
        raise ValueError(f"{name} must be a finite number.")
    return float(value)


def sharpe_ratio_from_stats(
    expected_return: Union[int, float],
    risk_free_rate: Union[int, float],
    std_dev: Union[int, float],
) -> float:
    """
    Calculate the Sharpe ratio from summary return and volatility statistics.

    Parameters:
    expected_return (Union[int, float]): Expected portfolio return.
    risk_free_rate (Union[int, float]): Risk-free rate over the same period.
    std_dev (Union[int, float]): Standard deviation of portfolio returns.

    Returns:
    float: The Sharpe ratio.

    Examples:
    >>> sharpe_ratio_from_stats(0.12, 0.02, 0.10)
    1.0
    """
    exp_ret = _validate_finite_number("expected_return", expected_return)
    rf = _validate_finite_number("risk_free_rate", risk_free_rate)
    sigma = _validate_finite_number("std_dev", std_dev)

    if sigma <= 0:
        raise ValueError("std_dev must be greater than zero.")

    return (exp_ret - rf) / sigma


def sharpe_ratio(
    returns: Sequence[Union[int, float]],
    risk_free_rate: Union[int, float] = 0.0,
    periods_per_year: Union[int, float] = 1,
) -> float:
    """
    Calculate the annualized Sharpe ratio from a sequence of periodic returns.

    Parameters:
    returns (Sequence[Union[int, float]]): Periodic return observations.
    risk_free_rate (Union[int, float]): Per-period risk-free rate.
    periods_per_year (Union[int, float]): Number of periods per year.

    Returns:
    float: The Sharpe ratio (annualized if periods_per_year != 1).

    Examples:
    >>> round(sharpe_ratio([0.05, 0.07, 0.03, 0.09], 0.01), 4)
    1.9365
    """
    if not isinstance(returns, (list, tuple)):
        raise TypeError("returns must be a list or tuple.")
    if len(returns) < 2:
        raise ValueError("returns must contain at least two observations.")
    if len(returns) > 1000000:
        raise ValueError("returns length exceeds maximum limit of 1,000,000.")

    rf = _validate_finite_number("risk_free_rate", risk_free_rate)
    ppy = _validate_finite_number("periods_per_year", periods_per_year)
    if ppy <= 0:
        raise ValueError("periods_per_year must be greater than zero.")

    excess_returns = []
    for idx, r in enumerate(returns):
        val = _validate_finite_number(f"returns[{idx}]", r)
        excess_returns.append(val - rf)

    avg_excess = mean(excess_returns)
    sq_diffs = [(x - avg_excess) * (x - avg_excess) for x in excess_returns]
    variance = sum(sq_diffs) / (len(excess_returns) - 1)
    if variance == 0:
        raise ValueError(
            "Standard deviation of excess returns is zero; Sharpe undefined."
        )

    std_dev = float(nth_root(variance, 2))
    scale = float(nth_root(ppy, 2)) if ppy != 1 else 1.0
    return (avg_excess / std_dev) * scale
