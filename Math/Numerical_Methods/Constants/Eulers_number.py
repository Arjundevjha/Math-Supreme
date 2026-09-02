# Euler's number calculation
from decimal import Decimal, getcontext


def compute_eulers_number(iterations: int = 100, decimal_places: int = 50) -> Decimal:
    """
    Compute Euler's number (e) using the series expansion: e = Σ(1/n!) for n=0 to infinity.

    Parameters:
    iterations (int): The number of terms to use in the series (default: 100).
    decimal_places (int): The number of decimal places for precision (default: 50).

    Returns:
    Decimal: Euler's number e to the specified precision.
    """
    # Security: Validate inputs to prevent Denial of Service (DoS) via resource exhaustion or invalid types
    if not isinstance(iterations, int) or isinstance(iterations, bool) or iterations < 1 or iterations > 10000:
        raise ValueError("Iterations must be an integer between 1 and 10000.")
    if not isinstance(decimal_places, int) or isinstance(decimal_places, bool) or decimal_places < 1 or decimal_places > 10000:
        raise ValueError("Decimal places must be an integer between 1 and 10000.")

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
