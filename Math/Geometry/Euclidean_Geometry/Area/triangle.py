# Area of triangle
from typing import Union


def area_of_triangle(base: Union[int, float], height: Union[int, float]) -> float:
    """
    Calculate the area of a triangle given its base and height.

    Parameters:
    base (Union[int, float]): The length of the base of the triangle.
    height (Union[int, float]): The height of the triangle.

    Returns:
    float: The area of the triangle.
    """
    if base < 0 or height < 0:
        raise ValueError("Base and height cannot be negative.")
    
    # Calculate area using formula: A = ½ × base × height
    return 0.5 * base * height