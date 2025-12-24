# Calculate the slope of a line given two points
from typing import Union


def calculate_slope(x1: Union[int, float], y1: Union[int, float], x2: Union[int, float], y2: Union[int, float]) -> float:
    """
    Calculate the slope of the line connecting two points.

    Parameters:
    x1 (Union[int, float]): x-coordinate of the first point.
    y1 (Union[int, float]): y-coordinate of the first point.
    x2 (Union[int, float]): x-coordinate of the second point.
    y2 (Union[int, float]): y-coordinate of the second point.

    Returns:
    float: The slope of the line.
    """
    if x2 - x1 == 0:
        raise ValueError("Slope is undefined for vertical lines (x1 cannot equal x2).")

    # Calculate slope using formula: m = (y₂ - y₁) / (x₂ - x₁)
    return (y2 - y1) / (x2 - x1)