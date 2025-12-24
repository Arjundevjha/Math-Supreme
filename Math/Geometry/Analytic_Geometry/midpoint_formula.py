# Midpoint formula for finding the midpoint of a line segment
from typing import Union, Tuple


def midpoint_formula(x1: Union[int, float], y1: Union[int, float], x2: Union[int, float], y2: Union[int, float]) -> Tuple[float, float]:
    """
    Calculate the midpoint of a line segment in a 2D plane.

    Parameters:
    x1 (Union[int, float]): x-coordinate of the first point.
    y1 (Union[int, float]): y-coordinate of the first point.
    x2 (Union[int, float]): x-coordinate of the second point.
    y2 (Union[int, float]): y-coordinate of the second point.

    Returns:
    Tuple[float, float]: A tuple representing the coordinates of the midpoint (mx, my).
    """
    # Calculate midpoint using formula: M = ((x₁+x₂)/2, (y₁+y₂)/2)
    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2
    return (mx, my)