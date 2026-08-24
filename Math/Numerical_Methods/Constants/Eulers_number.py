# Euler's number calculation
from decimal import Decimal, getcontext

from Math.utils.math_utils import factorial_decimal



def compute_eulers_number(iterations: int = 100, decimal_places: int = 50) -> Decimal:
    """
    Compute Euler's number (e) using the series expansion: e = Σ(1/n!) for n=0 to infinity.

    Parameters:
    iterations (int): The number of terms to use in the series (default: 100).
    decimal_places (int): The number of decimal places for precision (default: 50).

    Returns:
    Decimal: Euler's number e to the specified precision.
    """
    # Validate inputs to prevent DoS via excessive memory/CPU consumption
    if iterations <= 0 or iterations > 10000:
        raise ValueError("Iterations must be between 1 and 10000.")
    if decimal_places <= 0 or decimal_places > 10000:
        raise ValueError("Decimal places must be between 1 and 10000.")

    # Set precision for Decimal calculations
    getcontext().prec = decimal_places + 10
    
    e = Decimal(0)
    factorial_n = Decimal(1)
    
    # Calculate e using series: e = 1/0! + 1/1! + 1/2! + ...
    for n in range(iterations):
        if n > 0:
            factorial_n *= n
        e += Decimal(1) / factorial_n
    
    return e
