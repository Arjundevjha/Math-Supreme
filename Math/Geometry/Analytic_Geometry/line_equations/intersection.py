# Find the intersection point of two lines
from typing import Union, Optional, Tuple


def find_intersection(m1: Union[int, float], b1: Union[int, float], m2: Union[int, float], b2: Union[int, float]) -> Optional[Tuple[float, float]]:
    """
    Find the intersection point of two lines given their equations in the form y = mx + b.

    Parameters:
    m1 (Union[int, float]): Slope of the first line.
    b1 (Union[int, float]): Y-intercept of the first line.
    m2 (Union[int, float]): Slope of the second line.
    b2 (Union[int, float]): Y-intercept of the second line.

    Returns:
    Optional[Tuple[float, float]]: A tuple (x, y) representing the coordinates of the intersection point.
                                     Returns None if the lines are parallel.
    """
    if m1 == m2:
        return None  # Lines are parallel and do not intersect

    # Calculate intersection point by solving: m₁x + b₁ = m₂x + b₂
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    
    return (x, y)