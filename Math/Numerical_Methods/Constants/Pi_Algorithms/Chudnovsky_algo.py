# Chudnovsky algorithm for calculating Pi
import math
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
    if precision <= 0 or precision > 10000:
        raise ValueError("Precision must be between 1 and 10000.")

    # Set precision for Decimal calculations
    getcontext().prec = precision + 20
    
    # Optimization: Each term of the Chudnovsky series yields ~14.18 decimal digits of precision.
    # Dynamically calculating the required number of terms (num_terms) avoids performing
    # redundant Decimal iterations up to `precision` (e.g. 500 terms when only 37 are needed for precision=500).
    # Using integer arithmetic for intermediate term updates further speeds up computation.
    num_terms = max(1, math.ceil((precision + 20) / 14.181647462725477))

    # Chudnovsky algorithm constants
    C = Decimal(426880) * Decimal(10005).sqrt()
    K = 6
    M = 1
    L = 13591409
    X = 1
    S = Decimal(L)

    # Apply Chudnovsky series up to required num_terms
    for n in range(1, num_terms):
        M = (M * (K**3 - 16 * K)) // (n**3)
        L += 545140134
        X *= -262537412640768000
        S += (Decimal(M) * Decimal(L)) / Decimal(X)
        K += 12

    # Calculate π = C / S
    pi = C / S
    return pi
