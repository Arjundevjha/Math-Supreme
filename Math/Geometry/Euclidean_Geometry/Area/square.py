# Area of a square
from typing import Union


def area_of_square(side_length: Union[int, float]) -> float:
    """
    Calculate the area of a square given the length of its side.

    Parameters:
    side_length (Union[int, float]): The length of one side of the square.

    Returns:
    float: The area of the square.
    """
    if side_length < 0:
        raise ValueError("Side length cannot be negative.")
    
    # Calculate area using formula: A = side²
    return side_length ** 2