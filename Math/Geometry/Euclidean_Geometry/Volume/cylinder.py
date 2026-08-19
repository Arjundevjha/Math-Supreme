# Volume of cylinder
from typing import Union

from Math.utils.math_utils import PI


def volume_of_cylinder(radius: Union[int, float], height: Union[int, float]) -> float:
    """
    Calculate the volume of a cylinder given its radius and height.

    Parameters:
    radius (Union[int, float]): The radius of the base of the cylinder.
    height (Union[int, float]): The height of the cylinder.

    Returns:
    float: The volume of the cylinder.
    """
    if radius < 0 or height < 0:
        raise ValueError("Radius and height cannot be negative.")

    # Calculate volume using formula: V = πr²h
    return PI * (radius**2) * height