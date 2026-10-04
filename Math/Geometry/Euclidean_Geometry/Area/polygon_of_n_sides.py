# Area of a polygon with n sides
from typing import Union

from Math.Geometry.Trigonometry.Trig_Functions.tan import tangent
from Math.utils.math_utils import PI


def area_of_polygon(n: int, s: Union[int, float]) -> float:
    """
    Calculate the area of a regular polygon with n sides.

    Parameters:
    n (int): The number of sides of the polygon.
    s (Union[int, float]): The length of each side.

    Returns:
    float: The area of the polygon.
    """
    # Security: Validate input parameter types to prevent unexpected behavior and type confusion
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("Number of sides n must be an integer.")
    if not isinstance(s, (int, float)) or isinstance(s, bool):
        raise TypeError("Side length s must be numeric (int or float).")

    if n < 3:
        raise ValueError("A polygon must have at least 3 sides.")
    if s < 0:
        raise ValueError("Side length cannot be negative.")

    angle = PI / n
    tan_value = tangent(angle)

    # Calculate area using formula: A = (n × s²) / (4 × tan(π/n))
    return (n * s**2) / (4 * tan_value)
