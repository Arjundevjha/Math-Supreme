# Calculate the equation of a line from two points
from typing import Union


def line_from_points(x1: Union[int, float], y1: Union[int, float], x2: Union[int, float], y2: Union[int, float]) -> str:
    """
    Return the equation of the line passing through two points in slope-intercept form.

    Parameters:
    x1 (Union[int, float]): x-coordinate of the first point.
    y1 (Union[int, float]): y-coordinate of the first point.
    x2 (Union[int, float]): x-coordinate of the second point.
    y2 (Union[int, float]): y-coordinate of the second point.

    Returns:
    str: The equation of the line in the form "y = mx + b".
    """
    if x2 - x1 == 0:
        raise ValueError("Slope is undefined for vertical lines.")
    
    # Calculate slope: m = (y₂ - y₁) / (x₂ - x₁)
    m = (y2 - y1) / (x2 - x1)
    
    # Calculate y-intercept: b = y₁ - mx₁
    b = y1 - m * x1
    
    return f"y = {m}x + {b}"