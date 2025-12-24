# Volume of cuboid
from typing import Union


def volume_of_cuboid(length: Union[int, float], width: Union[int, float], height: Union[int, float]) -> float:
    """
    Calculate the volume of a cuboid given its length, width, and height.

    Parameters:
    length (Union[int, float]): The length of the cuboid.
    width (Union[int, float]): The width of the cuboid.
    height (Union[int, float]): The height of the cuboid.

    Returns:
    float: The volume of the cuboid.
    """
    if length < 0 or width < 0 or height < 0:
        raise ValueError("Length, width, and height cannot be negative.")
    
    # Calculate volume using formula: V = length × width × height
    return length * width * height