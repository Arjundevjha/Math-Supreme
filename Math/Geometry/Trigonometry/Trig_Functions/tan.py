"""Module for calculating the tangent trigonometric function."""
from typing import Union

from Math.Geometry.Trigonometry.taylor_series import (
    cosine_taylor,
    sine_taylor,
)


def tangent(radians: Union[int, float]) -> float:
    """
    Calculate the tangent of an angle.

    Parameters:
    radians (Union[int, float]): The angle in radians.

    Returns:
    float: The tangent of the angle.
    """
    # Security: Validate input type to prevent type confusion / unexpected behavior
    if isinstance(radians, bool) or not isinstance(radians, (int, float)):
        raise TypeError("radians must be a numeric int or float.")

    cos_val = cosine_taylor(radians)
    if cos_val == 0:
        raise ValueError("Tangent is undefined for angles where cos(x) = 0.")

    # Calculate tangent using formula: tan(x) = sin(x) / cos(x)
    return sine_taylor(radians) / cos_val
