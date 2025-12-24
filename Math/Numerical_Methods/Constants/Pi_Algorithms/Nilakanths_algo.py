# Nilakantha series for calculating Pi
from decimal import Decimal, getcontext


def calculate_pi_nilakantha(terms: int = 100, precision: int = 50) -> Decimal:
    """
    Calculate Pi using Nilakantha's algorithm.
    
    Formula: π = 3 + 4/(2×3×4) - 4/(4×5×6) + 4/(6×7×8) - ...

    Parameters:
    terms (int): The number of terms to calculate (default: 100).
    precision (int): The number of decimal places for precision (default: 50).

    Returns:
    Decimal: The calculated value of Pi.
    """
    if terms <= 0:
        raise ValueError("Number of terms must be a positive integer.")
    
    # Set precision for Decimal calculations
    getcontext().prec = precision + 10
    
    pi = Decimal(3.0)
    sign = 1  # Start with positive sign for the first term

    # Apply Nilakantha series: π = 3 + Σ(sign × 4/(i×(i+1)×(i+2)))
    for i in range(2, 2 * terms + 1, 2):
        term = sign * (Decimal(4.0) / (i * (i + 1) * (i + 2)))
        pi += term
        sign *= -1  # Alternate the sign for the next term

    return pi