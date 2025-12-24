# Chudnovsky algorithm for calculating Pi
from decimal import Decimal, getcontext


def calculate_pi_chudnovsky(precision: int = 50) -> Decimal:
    """
    Calculate Pi using the Chudnovsky algorithm.
    
    This is one of the fastest known algorithms for calculating Pi.

    Parameters:
    precision (int): The number of decimal places for the result (default: 50).

    Returns:
    Decimal: The value of Pi to the specified precision.
    """
    # Set precision for Decimal calculations
    getcontext().prec = precision + 20
    
    # Chudnovsky algorithm constants
    C = 426880 * Decimal(10005).sqrt()
    K = Decimal(6)
    M = Decimal(1)
    L = Decimal(13591409)
    X = Decimal(1)
    S = L

    # Apply Chudnovsky series
    for n in range(1, precision):
        M *= (K**3 - 16*K) / (n**3)
        L += 545140134
        X *= -262537412640768000
        S += M * L / X
        K += 12

    # Calculate π = C / S
    pi = C / S
    return pi
