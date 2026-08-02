# Cosecant function
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


def cosecant(radians: Union[int, float]) -> float:
    """
    Calculate the cosecant of an angle.

    Parameters:
    radians (Union[int, float]): The angle in radians.

    Returns:
    float: The cosecant of the angle.
    """
    sin_value = sine_taylor(radians)
    if sin_value == 0:
        raise ValueError("Cosecant is undefined for angles where sin(x) = 0.")
    
    # Calculate cosecant using formula: csc(x) = 1 / sin(x)
    return 1 / sin_value
