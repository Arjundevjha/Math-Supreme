# Calculate total amount after compound interest
from typing import Union


def compound_interest(
    principal_amount: Union[int, float],
    interest_rate: Union[int, float],
    time: Union[int, float],
    compound_frequency: Union[int, float],
) -> Union[int, float]:
    """
    Calculate the total amount after applying compound interest.

    Parameters:
    principal_amount (Union[int, float]): The initial principal amount.
    interest_rate (Union[int, float]): The annual interest rate (as a percentage).
    time (Union[int, float]): The time period in years.
    compound_frequency (Union[int, float]): The number of times interest is compounded per year.

    Returns:
    Union[int, float]: The total amount after compound interest.
    """
    # Security: Validate input types and resource bounds to prevent DoS via CPU/memory exhaustion
    for param_name, param_val in [
        ("principal_amount", principal_amount),
        ("interest_rate", interest_rate),
        ("time", time),
        ("compound_frequency", compound_frequency),
    ]:
        if isinstance(param_val, bool) or not isinstance(param_val, (int, float)):
            raise TypeError(f"{param_name} must be a numeric value (int or float).")

    if principal_amount < 0 or interest_rate < 0 or time < 0:
        raise ValueError(
            "Principal amount, interest rate, and time must be non-negative."
        )
    if compound_frequency <= 0:
        raise ValueError("Compound frequency must be positive.")

    if compound_frequency > 100000:
        raise ValueError("compound_frequency exceeds maximum allowed limit of 100000.")

    if time > 100000 or compound_frequency * time > 100000:
        raise ValueError("Compound exponent (frequency * time) exceeds maximum allowed limit of 100000.")

    # Calculate compound interest using formula: A = P(1 + r/n)^(nt)
    total_amount = principal_amount * (
        1 + (interest_rate / 100) / compound_frequency
    ) ** (compound_frequency * time)

    return total_amount
