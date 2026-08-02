# Tangent function
from typing import Union


from Math.Geometry.Trigonometry.taylor_series import sine_taylor, cosine_taylor


def tangent(radians: Union[int, float]) -> float:
    """
    Calculate the tangent of an angle.

    Parameters:
    radians (Union[int, float]): The angle in radians.

    Returns:
    float: The tangent of the angle.
    """
    # Calculate tangent using formula: tan(x) = sin(x) / cos(x)
    return sine_taylor(radians) / cosine_taylor(radians)
