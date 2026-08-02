# Euler's number calculation
from decimal import Decimal, getcontext
from Math.math_utils import factorial_decimal


def compute_eulers_number(iterations: int = 100, decimal_places: int = 50) -> Decimal:
    """
    Compute Euler's number (e) using the series expansion: e = Σ(1/n!) for n=0 to infinity.

    Parameters:
    iterations (int): The number of terms to use in the series (default: 100).
    decimal_places (int): The number of decimal places for precision (default: 50).

    Returns:
    Decimal: Euler's number e to the specified precision.
    """
    if iterations <= 0:
        raise ValueError("Iterations must be positive.")
    
    # Set precision for Decimal calculations
    getcontext().prec = decimal_places + 10
    
    e = Decimal(0)
    
    # Calculate e using series: e = 1/0! + 1/1! + 1/2! + ...
    for n in range(iterations):
        factorial_n = factorial_decimal(n)
        e += Decimal(1) / factorial_n
    
    return e
