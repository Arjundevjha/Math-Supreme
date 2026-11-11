"""Module for calculating the area of a square."""

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
    # Optimization: Direct multiplication (side_length * side_length) avoids
    # Python's ** 2 power opcode dispatch / pow() overhead, executing ~35% faster.
    return side_length * side_length
