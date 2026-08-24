# Mathematical utilities and shared constants
import math
from decimal import Decimal

# Mathematical constants
PI = 3.14159265358979323846


def factorial(n: int) -> int:
    """
    Calculate the factorial of a number.

    Parameters:
    n (int): The number to calculate factorial for.

    Returns:
    int: The factorial of n (n!).
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    return math.factorial(n)


def factorial_decimal(n: int) -> Decimal:
    """
    Calculate factorial as a Decimal for high precision.

    Parameters:
    n (int): The number to calculate factorial for.

    Returns:
    Decimal: The factorial of n as a Decimal.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    result = Decimal(1)
    for i in range(1, n + 1):
        result *= i
    return result


