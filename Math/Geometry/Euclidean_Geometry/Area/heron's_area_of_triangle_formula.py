# Area of triangle using Heron's formula
from typing import Union


def herons_area_of_triangle(a: Union[int, float], b: Union[int, float], c: Union[int, float]) -> float:
    """
    Calculate the area of a triangle using Heron's formula.

    Parameters:
    a (Union[int, float]): Length of side a.
    b (Union[int, float]): Length of side b.
    c (Union[int, float]): Length of side c.

    Returns:
    float: Area of the triangle.
    """
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("All sides must be positive.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid triangle: the sum of any two sides must be greater than the third side.")
    
    # Calculate semi-perimeter
    s = (a + b + c) / 2
    
    # Calculate area using Heron's formula: A = √(s(s-a)(s-b)(s-c))
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    
    return area