# Sine trigonometric function using Taylor series
from typing import Union

from Math.Geometry.Trigonometry.taylor_series import sine_taylor



def sine(radians: Union[int, float]) -> float:
    """
    Calculate the sine of an angle using Taylor series expansion.

    Parameters:
    radians (Union[int, float]): The angle in radians.

    Returns:
    float: The sine of the angle.
    """
    return sine_taylor(radians)
