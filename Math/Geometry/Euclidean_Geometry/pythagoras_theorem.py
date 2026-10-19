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
    # Security: Validate input parameter types to prevent unexpected behavior and boolean type confusion
    for param_name, param_val in [("a", a), ("b", b)]:
        if isinstance(param_val, bool) or not isinstance(param_val, (int, float)):
            raise TypeError(f"Leg '{param_name}' must be a numeric int or float.")

    if a <= 0 or b <= 0:
        raise ValueError("Both legs must be positive.")

    # Calculate hypotenuse using formula: c = √(a² + b²)
    return (a ** 2 + b ** 2) ** 0.5
