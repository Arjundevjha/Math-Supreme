# Volume of cone
from typing import Union


def volume_of_cone(radius: Union[int, float], height: Union[int, float]) -> float:
    """
    Calculate the volume of a cone given its radius and height.

    Parameters:
    radius (Union[int, float]): The radius of the base of the cone.
    height (Union[int, float]): The height of the cone.

    Returns:
    float: The volume of the cone.
    """
    if radius < 0 or height < 0:
        raise ValueError("Radius and height cannot be negative.")
    
    # Use pi approximation: π ≈ 3.14159265358979323846
    pi = 3.14159265358979323846
    
    # Calculate volume using formula: V = (1/3)πr²h
    return (1 / 3) * pi * (radius ** 2) * height