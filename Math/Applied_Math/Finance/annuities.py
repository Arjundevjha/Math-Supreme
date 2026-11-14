"""Calculate present value, future value, and payments for annuities."""
from typing import Union


def _validate_annuity_inputs(
    amount: Union[int, float],
    rate_per_period: Union[int, float],
    num_periods: Union[int, float],
    annuity_due: bool,
) -> None:
    """
    Validate common input parameters for annuity calculations.

    Parameters:
    amount (Union[int, float]): Payment or present value amount.
    rate_per_period (Union[int, float]): Periodic interest rate as a decimal.
    num_periods (Union[int, float]): Number of compounding/payment periods.
    annuity_due (bool): Whether payments occur at the beginning of a period.

    Returns:
    None
    """
    for name, val in [
        ("amount", amount),
        ("rate_per_period", rate_per_period),
        ("num_periods", num_periods),
    ]:
        if isinstance(val, bool) or not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be a numeric int or float.")
        if not -float("inf") < val < float("inf"):
            raise ValueError(f"{name} must be a finite number.")

    if not isinstance(annuity_due, bool):
        raise TypeError("annuity_due must be a boolean.")

    if amount < 0:
        raise ValueError("Amount must be non-negative.")
    if rate_per_period < 0:
        raise ValueError("rate_per_period must be non-negative.")
    if num_periods < 0:
        raise ValueError("num_periods must be non-negative.")
    if amount > 1e12 or rate_per_period > 100 or num_periods > 10000:
        raise ValueError("Parameter values exceed maximum allowed limits.")


def present_value_annuity(
    payment: Union[int, float],
    rate_per_period: Union[int, float],
    num_periods: Union[int, float],
    annuity_due: bool = False,
) -> float:
    """
    Calculate the present value of an ordinary annuity or annuity due.

    Parameters:
    payment (Union[int, float]): Periodic payment amount.
    rate_per_period (Union[int, float]): Interest rate per period (decimal).
    num_periods (Union[int, float]): Total number of payment periods.
    annuity_due (bool): If True, payments occur at period start.

    Returns:
    float: The present value of the annuity.

    Examples:
    >>> round(present_value_annuity(1000, 0.05, 5), 2)
    4329.48
    """
    _validate_annuity_inputs(payment, rate_per_period, num_periods, annuity_due)

    if num_periods == 0 or payment == 0:
        return 0.0

    if rate_per_period == 0:
        return float(payment * num_periods)

    factor = (1.0 - (1.0 + rate_per_period) ** (-num_periods)) / rate_per_period
    pv = payment * factor
    if annuity_due:
        pv *= 1.0 + rate_per_period
    return float(pv)


def future_value_annuity(
    payment: Union[int, float],
    rate_per_period: Union[int, float],
    num_periods: Union[int, float],
    annuity_due: bool = False,
) -> float:
    """
    Calculate the future value of an ordinary annuity or annuity due.

    Parameters:
    payment (Union[int, float]): Periodic payment amount.
    rate_per_period (Union[int, float]): Interest rate per period (decimal).
    num_periods (Union[int, float]): Total number of payment periods.
    annuity_due (bool): If True, payments occur at period start.

    Returns:
    float: The future value of the annuity.

    Examples:
    >>> round(future_value_annuity(1000, 0.05, 5), 2)
    5525.63
    """
    _validate_annuity_inputs(payment, rate_per_period, num_periods, annuity_due)

    if num_periods == 0 or payment == 0:
        return 0.0

    if rate_per_period == 0:
        return float(payment * num_periods)

    factor = ((1.0 + rate_per_period) ** num_periods - 1.0) / rate_per_period
    fv = payment * factor
    if annuity_due:
        fv *= 1.0 + rate_per_period
    return float(fv)


def annuity_payment(
    present_value: Union[int, float],
    rate_per_period: Union[int, float],
    num_periods: Union[int, float],
    annuity_due: bool = False,
) -> float:
    """
    Calculate the periodic payment required to amortize a present value.

    Parameters:
    present_value (Union[int, float]): Initial present value or loan amount.
    rate_per_period (Union[int, float]): Interest rate per period (decimal).
    num_periods (Union[int, float]): Total number of payment periods.
    annuity_due (bool): If True, payments occur at period start.

    Returns:
    float: The periodic payment amount.

    Examples:
    >>> round(annuity_payment(10000, 0.05, 5), 2)
    2309.75
    """
    _validate_annuity_inputs(
        present_value, rate_per_period, num_periods, annuity_due
    )

    if num_periods == 0:
        raise ValueError("num_periods must be greater than zero.")

    if present_value == 0:
        return 0.0

    if rate_per_period == 0:
        return float(present_value / num_periods)

    factor = rate_per_period / (1.0 - (1.0 + rate_per_period) ** (-num_periods))
    pmt = present_value * factor
    if annuity_due:
        pmt /= 1.0 + rate_per_period
    return float(pmt)
