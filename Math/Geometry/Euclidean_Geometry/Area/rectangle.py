# Area of rectangle
from typing import Union


def area_of_rectangle(length: Union[int, float], width: Union[int, float]) -> float:
    """
    Calculate the area of a rectangle given its length and width.

    Parameters:
    length (Union[int, float]): The length of the rectangle.
    width (Union[int, float]): The width of the rectangle.

    Returns:
    float: The area of the rectangle.
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative.")
    
    # Calculate area using formula: A = length × width
    return length * width