# Secant function
from typing import Union


def factorial(n: int) -> int:
    """Calculate factorial of n."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def cosine_taylor(radians: Union[int, float]) -> float:
    """Calculate cosine using Taylor series."""
    cos_value = 1
    sign = 1
    for idx in range(2, 100, 2):
        fact = factorial(idx)
        if sign % 2 == 0:
            cos_value += radians**idx / fact
        else:
            cos_value -= radians**idx / fact
        sign += 1
    return cos_value


def secant(radians: Union[int, float]) -> float:
    """
    Calculate the secant of an angle.

    Parameters:
    radians (Union[int, float]): The angle in radians.

    Returns:
    float: The secant of the angle.
    """
    cos_value = cosine_taylor(radians)
    if cos_value == 0:
        raise ValueError("Secant is undefined for angles where cos(x) = 0.")
    
    # Calculate secant using formula: sec(x) = 1 / cos(x)
    return 1 / cos_value
