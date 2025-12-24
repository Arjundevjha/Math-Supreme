# Machin's formula for calculating Pi
from decimal import Decimal, getcontext


def calculate_arctan_series(x: int, precision: int) -> Decimal:
    """
    Calculate arctan(1/x) using Taylor series expansion.

    Parameters:
    x (int): The value for arctan(1/x).
    precision (int): The number of decimal places for precision.

    Returns:
    Decimal: The value of arctan(1/x).
    """
    getcontext().prec = precision + 10
    
    if x == 0:
        return Decimal(0)
    elif x < 0:
        return -calculate_arctan_series(-x, precision)

    arctan_value = Decimal(0)
    # Taylor series for arctan(1/x): arctan(1/x) = Σ((-1)ⁿ / ((2n+1) × x^(2n+1)))
    term = Decimal(1) / Decimal(x)
    n = 0

    while abs(term) > Decimal(10) ** (-precision):
        arctan_value += term / (2 * n + 1)
        n += 1
        term *= -Decimal(1) / (x * x)

    return arctan_value


def calculate_pi_machin(precision: int = 50) -> Decimal:
    """
    Calculate Pi using Machin's formula: π/4 = 4×arctan(1/5) - arctan(1/239).

    Parameters:
    precision (int): The number of decimal places for the result (default: 50).

    Returns:
    Decimal: The value of Pi to the specified precision.
    """
    # Set precision for Decimal calculations
    getcontext().prec = precision + 10
    
    # Apply Machin's formula: π/4 = 4×arctan(1/5) - arctan(1/239)
    pi_over_4 = (4 * calculate_arctan_series(5, precision) - 
                 calculate_arctan_series(239, precision))
    
    return pi_over_4 * 4
