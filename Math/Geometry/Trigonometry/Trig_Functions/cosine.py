# Cosine function using Taylor series
from typing import Union


def factorial(n: int) -> int:
    """Calculate factorial of n."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def cosine(radians: Union[int, float]) -> float:
    """
    Calculate the cosine of an angle using Taylor series expansion.

    Parameters:
    radians (Union[int, float]): The angle in radians.

    Returns:
    float: The cosine of the angle.
    """
    cos_value = 1
    sign = 1
    
    # Calculate cosine using Taylor series: cos(x) = Σ((-1)ⁿ × x^(2n)) / (2n)!
    for idx in range(2, 100, 2):
        fact = factorial(idx)
        
        if sign % 2 == 0:
            cos_value += radians**idx / fact
        else:
            cos_value -= radians**idx / fact
        sign += 1
    
    return cos_value
