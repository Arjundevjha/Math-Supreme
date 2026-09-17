# Calculate total amount after simple interest
from typing import Union


def simple_interest(principal_amount: Union[int, float], interest_rate: Union[int, float], time: Union[int, float]) -> Union[int, float]:
    """
    Calculate the total amount after applying simple interest.

    Parameters:
    principal_amount (Union[int, float]): The initial principal amount.
    interest_rate (Union[int, float]): The annual interest rate (as a percentage).
    time (Union[int, float]): The time period in years.

    Returns:
    Union[int, float]: The total amount after interest.
    """
    # Security: Validate input types and bounds to prevent DoS or unexpected behavior
    for param_name, param_val in [
        ("principal_amount", principal_amount),
        ("interest_rate", interest_rate),
        ("time", time),
    ]:
        if isinstance(param_val, bool) or not isinstance(param_val, (int, float)):
            raise TypeError(f"{param_name} must be a numeric value (int or float).")

    if principal_amount < 0 or interest_rate < 0 or time < 0:
        raise ValueError("Principal amount, interest rate, and time must be non-negative.")

    if time > 100000:
        raise ValueError("time exceeds maximum allowed limit of 100000.")

    # Calculate simple interest using formula: I = (P × R × T) / 100
    interest = (principal_amount * interest_rate * time) / 100

    # Calculate total amount
    total_amount = principal_amount + interest
    
    return total_amount
