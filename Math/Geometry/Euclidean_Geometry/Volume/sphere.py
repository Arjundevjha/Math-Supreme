# Volume of sphere
from typing import Union


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

    # Use pi approximation: π ≈ 3.14159265358979323846
    pi = 3.14159265358979323846
    
    # Calculate volume using formula: V = (4/3)πr³
    return (4 / 3) * pi * (radius ** 3)