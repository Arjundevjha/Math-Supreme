# Tangent function
from typing import Union


def factorial(n: int) -> int:
    """Calculate factorial of n."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def sine_taylor(radians: Union[int, float]) -> float:
    """Calculate sine using Taylor series."""
    sine_value = 0
    sign = 0
    for idx in range(1, 100, 2):
        fact = factorial(idx)
        if sign % 2 == 0:
            sine_value += radians**idx / fact
        else:
            sine_value -= radians**idx / fact
        sign += 1
    return sine_value


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


def tangent(radians: Union[int, float]) -> float:
    """
    Calculate the tangent of an angle.

    Parameters:
    radians (Union[int, float]): The angle in radians.

    Returns:
    float: The tangent of the angle.
    """
    # Calculate tangent using formula: tan(x) = sin(x) / cos(x)
    return sine_taylor(radians) / cosine_taylor(radians)
