# Volume of sphere
from typing import Union

from Math.utils.math_utils import PI


def volume_of_sphere(radius: Union[int, float]) -> float:
    """
    Calculate the volume of a sphere given its radius.

    Parameters:
    radius (Union[int, float]): The radius of the sphere.

    Returns:
    float: The volume of the sphere.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative.")

    # Calculate volume using formula: V = (4/3)πr³
    return (4 / 3) * PI * (radius**3)