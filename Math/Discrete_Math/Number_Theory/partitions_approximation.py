# Partition approximation using Ramanujan's asymptotic formula
from decimal import Decimal, getcontext


def partition_approximation(num: int) -> int:
    """
    Calculate an approximation of the number of partitions p(n) using Ramanujan's formula.

    Parameters:
    num (int): The non-negative integer to approximate partitions for.

    Returns:
    int: An integer approximation of p(n).
    """
    if num < 0:
        raise ValueError("Number must be a non-negative integer.")
    if num == 0:
        return 1

    # Use Decimal for high-precision arithmetic
    getcontext().prec = 60
    n_dec = Decimal(num)

    # Calculate sqrt(2n/3)
    sqrt_term = (Decimal(2) * n_dec / Decimal(3)).sqrt()

    # Use pi approximation
    pi_dec = Decimal("3.14159265358979323846264338327950288419716939937510")

    # Calculate exponent: π × sqrt(2n/3)
    exponent = pi_dec * sqrt_term

    # Calculate numerator: exp(π × sqrt(2n/3))
    numerator = exponent.exp()

    # Calculate denominator: 4n × sqrt(3)
    denominator = Decimal(4) * n_dec * Decimal(3).sqrt()

    # Apply Ramanujan's formula: p(n) ≈ exp(π√(2n/3)) / (4n√3)
    partition_number = numerator / denominator

    return int(partition_number)