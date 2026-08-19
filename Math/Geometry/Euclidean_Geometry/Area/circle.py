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
    if radius < 0:
        raise ValueError("Radius cannot be negative.")

    # Calculate area using formula: A = πr²
    return PI * (radius**2)