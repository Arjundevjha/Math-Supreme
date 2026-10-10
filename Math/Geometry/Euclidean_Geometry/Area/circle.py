# Area of circle
from typing import Union

from Math.utils.math_utils import PI


def area_of_circle(radius: Union[int, float]) -> float:
    """
    Calculate the area of a circle given its radius.

    Parameters:
    radius (Union[int, float]): The radius of the circle.

    Returns:
    float: The area of the circle.
    """
    # Security: Validate radius type to prevent unexpected type coercion or errors
    if isinstance(radius, bool) or not isinstance(radius, (int, float)):
        raise TypeError("Radius must be numeric (int or float).")

    if radius < 0:
        raise ValueError("Radius cannot be negative.")

    # Security: Validate upper magnitude limit to prevent DoS via OverflowError
    if radius > 1e150:
        raise ValueError("Radius exceeds maximum limit of 1e150.")

    # Calculate area using formula: A = πr²
    return PI * (radius**2)
