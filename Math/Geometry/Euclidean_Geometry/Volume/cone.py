# Volume of cone
from typing import Union

from Math.utils.math_utils import PI


def volume_of_cone(radius: Union[int, float], height: Union[int, float]) -> float:
    """
    Calculate the volume of a cone given its radius and height.

    Parameters:
    radius (Union[int, float]): The radius of the base of the cone.
    height (Union[int, float]): The height of the cone.

    Returns:
    float: The volume of the cone.
    """
    # Security: Validate input parameter types to prevent unexpected behavior and type confusion
    if not isinstance(radius, (int, float)) or isinstance(radius, bool):
        raise TypeError("Radius must be numeric (int or float).")
    if not isinstance(height, (int, float)) or isinstance(height, bool):
        raise TypeError("Height must be numeric (int or float).")

    if radius < 0 or height < 0:
        raise ValueError("Radius and height cannot be negative.")

    # Calculate volume using formula: V = (1/3)πr²h
    return (1 / 3) * PI * (radius**2) * height