# Sine function using Taylor series
from typing import Union


def factorial(n: int) -> int:
    """Calculate factorial of n."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def sine(radians: Union[int, float]) -> float:
    """
    Calculate the sine of an angle using Taylor series expansion.

    Parameters:
    radians (Union[int, float]): The angle in radians.

    Returns:
    float: The sine of the angle.
    """
    sine_value = 0
    sign = 0
    
    # Calculate sine using Taylor series: sin(x) = Σ((-1)ⁿ × x^(2n+1)) / (2n+1)!
    for idx in range(1, 100, 2):
        fact = factorial(idx)
        
        if sign % 2 == 0:
            sine_value += radians**idx / fact
        else:
            sine_value -= radians**idx / fact
        sign += 1
    
    return sine_value
