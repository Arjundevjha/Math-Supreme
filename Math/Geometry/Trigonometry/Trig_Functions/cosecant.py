# Cosecant trigonometric function
from typing import Union

from Math.Geometry.Trigonometry.taylor_series import sine_taylor



def cosecant(radians: Union[int, float]) -> float:
    """
    Calculate the cosecant of an angle.

    Parameters:
    radians (Union[int, float]): The angle in radians.

    Returns:
    float: The cosecant of the angle.
    """
    sin_value = sine_taylor(radians)
    if sin_value == 0:
        raise ValueError("Cosecant is undefined for angles where sin(x) = 0.")

    # Calculate cosecant using formula: csc(x) = 1 / sin(x)
    return 1 / sin_value
