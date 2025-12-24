# Area of circle
from typing import Union


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
    
    # Use pi approximation: π ≈ 3.14159265358979323846
    pi = 3.14159265358979323846
    
    # Calculate area using formula: A = πr²
    return pi * (radius ** 2)