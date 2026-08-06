# Area of a polygon with n sides
from typing import Union

from Math.Geometry.Trigonometry.Trig_Functions.tan import tangent


def area_of_polygon(n: int, s: Union[int, float]) -> float:
    """
    Calculate the area of a regular polygon with n sides.

    Parameters:
    n (int): The number of sides of the polygon.
    s (Union[int, float]): The length of each side.

    Returns:
    float: The area of the polygon.
    """
    if n < 3:
        raise ValueError("A polygon must have at least 3 sides.")
    if s < 0:
        raise ValueError("Side length cannot be negative.")
    
    # Use pi approximation: π ≈ 3.14159265358979323846
    pi = 3.14159265358979323846
    
    angle = pi / n
    tan_value = tangent(angle)
    
    # Calculate area using formula: A = (n × s²) / (4 × tan(π/n))
    return (n * s**2) / (4 * tan_value)