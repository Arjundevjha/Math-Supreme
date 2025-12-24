# Arcsine using numerical approximation
from typing import Union


def sine_taylor_series(radians: Union[int, float], terms: int = 100) -> float:
    """
    Calculate sine using Taylor series expansion.

    Parameters:
    radians (Union[int, float]): The angle in radians.
    terms (int): Number of terms to use in the series.

    Returns:
    float: The sine of the angle.
    """
    sine_value = 0
    sign = 0
    
    # Calculate sine using Taylor series
    for idx in range(1, terms * 2, 2):
        factorial = 1
        for i in range(1, idx + 1):
            factorial *= i
        
        if sign % 2 == 0:
            sine_value += radians**idx / factorial
        else:
            sine_value -= radians**idx / factorial
        sign += 1
    
    return sine_value


def arcsin_numerical(sin_value: Union[int, float], precision: float = 0.0001) -> Union[float, None]:
    """
    Calculate arcsine using numerical approximation by finding angle where sin(angle) = sin_value.

    Parameters:
    sin_value (Union[int, float]): The sine value to find the arcsine for (must be between -1 and 1).
    precision (float): The precision for the approximation (default: 0.0001).

    Returns:
    Union[float, None]: The angle in radians, or None if not found.
    """
    if sin_value < -1 or sin_value > 1:
        raise ValueError("Sine value must be between -1 and 1.")
    
    # Use numerical search to find angle where sin(angle) ≈ sin_value
    import decimal
    decimal.getcontext().prec = 50
    
    pi_approx = 3.14159265358979323846
    
    # Search in range [0, π/2] for positive values
    step = 0.0001
    angle = 0.0
    
    while angle <= pi_approx / 2:
        calculated_sin = sine_taylor_series(angle)
        if abs(calculated_sin - sin_value) < precision:
            return angle
        angle += step
    
    return None