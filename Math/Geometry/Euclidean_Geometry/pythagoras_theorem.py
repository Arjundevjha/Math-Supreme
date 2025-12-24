# Pythagorean theorem for calculating the hypotenuse of a right triangle
from typing import Union


def pythagorean_theorem(a: Union[int, float], b: Union[int, float]) -> float:
    """
    Calculate the length of the hypotenuse of a right triangle using the Pythagorean theorem.

    Parameters:
    a (Union[int, float]): Length of one leg of the triangle.
    b (Union[int, float]): Length of the other leg of the triangle.

    Returns:
    float: Length of the hypotenuse.
    """
    if a <= 0 or b <= 0:
        raise ValueError("Both legs must be positive.")
    
    # Calculate hypotenuse using formula: c = √(a² + b²)
    return (a ** 2 + b ** 2) ** 0.5
