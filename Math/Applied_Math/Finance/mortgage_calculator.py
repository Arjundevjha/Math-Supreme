"""Calculate mortgage payments, total interest, and amortization schedule."""
from typing import Dict, List, Union


def _validate_mortgage_inputs(
    principal: Union[int, float],
    annual_interest_rate: Union[int, float],
    years: Union[int, float],
) -> None:
    """
    Validate input parameters for mortgage calculations.

    Parameters:
    principal (Union[int, float]): Loan principal amount.
    annual_interest_rate (Union[int, float]): Annual rate as a percentage.
    years (Union[int, float]): Loan term in years.

    Returns:
    None
    """
    for name, val in [
        ("principal", principal),
        ("annual_interest_rate", annual_interest_rate),
        ("years", years),
    ]:
        if isinstance(val, bool) or not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be a numeric int or float.")
        if not -float("inf") < val < float("inf"):
            raise ValueError(f"{name} must be a finite number.")

    if principal < 0 or annual_interest_rate < 0:
        raise ValueError(
            "principal and annual_interest_rate must be non-negative."
        )
    if years <= 0:
        raise ValueError("years must be greater than zero.")
    if principal > 1e12 or annual_interest_rate > 1000 or years > 100:
        raise ValueError("Parameter values exceed maximum allowed limits.")


def monthly_mortgage_payment(
    principal: Union[int, float],
    annual_interest_rate: Union[int, float],
    years: Union[int, float],
) -> float:
    """
    Calculate the fixed monthly payment for a mortgage loan.

    Parameters:
    principal (Union[int, float]): Loan principal amount.
    annual_interest_rate (Union[int, float]): Annual rate as a percentage.
    years (Union[int, float]): Loan term in years.

    Returns:
    float: The fixed monthly mortgage payment.

    Examples:
    >>> round(monthly_mortgage_payment(200000, 6.0, 30), 2)
    1199.10
    """
    _validate_mortgage_inputs(principal, annual_interest_rate, years)

    if principal == 0:
        return 0.0

    num_months = years * 12
    monthly_rate = (annual_interest_rate / 100.0) / 12.0

    if monthly_rate == 0:
        return float(principal / num_months)

    growth = (1.0 + monthly_rate) ** num_months
    payment = principal * (monthly_rate * growth) / (growth - 1.0)
    return float(payment)


def total_mortgage_payment(
    principal: Union[int, float],
    annual_interest_rate: Union[int, float],
    years: Union[int, float],
) -> float:
    """
    Calculate the total amount paid over the life of a mortgage.

    Parameters:
    principal (Union[int, float]): Loan principal amount.
    annual_interest_rate (Union[int, float]): Annual rate as a percentage.
    years (Union[int, float]): Loan term in years.

    Returns:
    float: Total cumulative payments over the loan term.
    """
    monthly_pmt = monthly_mortgage_payment(
        principal, annual_interest_rate, years
    )
    return float(monthly_pmt * (years * 12))


def total_mortgage_interest(
    principal: Union[int, float],
    annual_interest_rate: Union[int, float],
    years: Union[int, float],
) -> float:
    """
    Calculate the total interest paid over the life of a mortgage.

    Parameters:
    principal (Union[int, float]): Loan principal amount.
    annual_interest_rate (Union[int, float]): Annual rate as a percentage.
    years (Union[int, float]): Loan term in years.

    Returns:
    float: Total interest paid over the loan term.
    """
    total_paid = total_mortgage_payment(principal, annual_interest_rate, years)
    return float(total_paid - principal)


def amortization_schedule(
    principal: Union[int, float],
    annual_interest_rate: Union[int, float],
    years: int,
) -> List[Dict[str, float]]:
    """
    Generate a month-by-month mortgage amortization schedule.

    Parameters:
    principal (Union[int, float]): Loan principal amount.
    annual_interest_rate (Union[int, float]): Annual rate as a percentage.
    years (int): Loan term in whole years.

    Returns:
    List[Dict[str, float]]: Monthly schedule entries with payment breakdown.
    """
    if isinstance(years, bool) or not isinstance(years, int):
        raise TypeError("years must be an integer for amortization_schedule.")

    monthly_pmt = monthly_mortgage_payment(
        principal, annual_interest_rate, years
    )
    monthly_rate = (annual_interest_rate / 100.0) / 12.0
    num_months = years * 12

    balance = float(principal)
    schedule: List[Dict[str, float]] = []

    for month in range(1, num_months + 1):
        interest_paid = balance * monthly_rate
        principal_paid = monthly_pmt - interest_paid
        if month == num_months or principal_paid > balance:
            principal_paid = balance
            actual_payment = principal_paid + interest_paid
        else:
            actual_payment = monthly_pmt
        balance = max(0.0, balance - principal_paid)
        schedule.append(
            {
                "month": float(month),
                "payment": float(actual_payment),
                "principal_paid": float(principal_paid),
                "interest_paid": float(interest_paid),
                "remaining_balance": float(balance),
            }
        )

    return schedule
