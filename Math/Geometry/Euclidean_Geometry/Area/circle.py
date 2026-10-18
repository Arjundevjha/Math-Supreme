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
    # Security: Validate input parameter types to prevent unexpected behavior and type confusion
    if not isinstance(radius, (int, float)) or isinstance(radius, bool):
        raise TypeError("Radius must be numeric (int or float).")

    if radius < 0:
        raise ValueError("Radius cannot be negative.")

    # Calculate area using formula: A = πr²
    return PI * (radius**2)