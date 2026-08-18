# Factorial calculation
import math


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
    if n > 1000:
        raise ValueError(
            "Factorial calculation limit exceeded (maximum allowed is 1000)."
        )
    return math.factorial(n)
