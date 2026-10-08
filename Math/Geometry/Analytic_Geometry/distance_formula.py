# Distance formula for calculating distance between two points
from typing import Union


def distance_formula(x1: Union[int, float], y1: Union[int, float], x2: Union[int, float], y2: Union[int, float]) -> float:
    """
    Calculate the distance between two points (x1, y1) and (x2, y2) using the distance formula.

    Parameters:
    x1 (Union[int, float]): x-coordinate of the first point.
    y1 (Union[int, float]): y-coordinate of the first point.
    x2 (Union[int, float]): x-coordinate of the second point.
    y2 (Union[int, float]): y-coordinate of the second point.

    Returns:
    float: Distance between the two points.
    """
    # Security: Validate parameter types and magnitude limits to prevent DoS via OverflowError
    coords = (x1, y1, x2, y2)
    for coord in coords:
        if isinstance(coord, bool) or not isinstance(coord, (int, float)):
            raise TypeError("Coordinates must be numeric values (int or float).")
        if abs(coord) > 1e300:
            raise ValueError("Coordinates exceed maximum allowed magnitude limit of 1e300.")

    # Calculate distance using formula: d = √((x₂-x₁)² + (y₂-y₁)²)
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
