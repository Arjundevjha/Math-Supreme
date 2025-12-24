# Arctangent (inverse tangent) function using Taylor series
from decimal import Decimal, getcontext
from typing import Union, Optional


def calculate_arctan(x: Union[int, float, Decimal], precision: int = 50, number_of_terms: Optional[int] = None) -> Decimal:
    """
    Calculate the arctangent of (1/x) in radians with specified precision using Taylor series.

    Parameters:
    x (Union[int, float, Decimal]): The value to calculate arctan(1/x) for.
    precision (int): The number of decimal places for the result (default: 50).
    number_of_terms (Optional[int]): Number of terms to use in the series. If None, continues until convergence.

    Returns:
    Decimal: The arctangent value in radians.
    """
    # Set precision for Decimal calculations
    getcontext().prec = precision + 2
    
    if x == 0:
        return Decimal(0)
    elif x < 0:
        return -calculate_arctan(-x, precision, number_of_terms)

    arctan_value = Decimal(0)
    # First term of the Taylor series: arctan(1/x) = Σ((-1)ⁿ / ((2n+1) × x^(2n+1)))
    term = Decimal(1) / Decimal(x)
    n = 0

    if number_of_terms is not None:
        # Use fixed number of terms
        while n < number_of_terms:
            arctan_value += term / (2 * n + 1)
            n += 1
            term *= -Decimal(1) / (x * x)
    else:
        # Continue until convergence
        while abs(term) > Decimal(10) ** (-precision):
            arctan_value += term / (2 * n + 1)
            n += 1
            term *= -Decimal(1) / (x * x)

    return arctan_value
