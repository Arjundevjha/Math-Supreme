# Volume of prism
from typing import Union


def volume_of_prism(base_area: Union[int, float], height: Union[int, float]) -> float:
    """
    Calculate the volume of a prism given its base area and height.

    Parameters:
    base_area (Union[int, float]): The area of the base of the prism.
    height (Union[int, float]): The height of the prism.

    Returns:
    float: The volume of the prism.
    """
    if base_area < 0 or height < 0:
        raise ValueError("Base area and height cannot be negative.")
    
    # Calculate volume using formula: V = base area × height
    return base_area * height