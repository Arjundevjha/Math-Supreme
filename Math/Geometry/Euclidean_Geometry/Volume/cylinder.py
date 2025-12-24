# Volume of cylinder
from typing import Union


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
    
    # Use pi approximation: π ≈ 3.14159265358979323846
    pi = 3.14159265358979323846
    
    # Calculate volume using formula: V = πr²h
    return pi * (radius ** 2) * height