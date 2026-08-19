# Cosine trigonometric function using Taylor series
from typing import Union

from Math.Geometry.Trigonometry.taylor_series import cosine_taylor



def cosine(radians: Union[int, float]) -> float:
    """
    Calculate the cosine of an angle using Taylor series expansion.

    Parameters:
    radians (Union[int, float]): The angle in radians.

    Returns:
    float: The cosine of the angle.
    """
    return cosine_taylor(radians)
