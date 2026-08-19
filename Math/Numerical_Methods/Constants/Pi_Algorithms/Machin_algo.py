# Machin's formula for calculating Pi
from decimal import Decimal, getcontext

from Math.Geometry.Trigonometry.Arc_Functions.arctan import calculate_arctan


def calculate_arctan_series(x: int, precision: int) -> Decimal:
    """
    Calculate arctan(1/x) using Taylor series expansion.

    Parameters:
    x (int): The value for arctan(1/x).
    precision (int): The number of decimal places for precision.

    Returns:
    Decimal: The value of arctan(1/x).
    """
    return calculate_arctan(x, precision=precision)



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
