# Secant function
from typing import Union


from Math.Geometry.Trigonometry.taylor_series import cosine_taylor


def secant(radians: Union[int, float]) -> float:
    """
    Calculate the secant of an angle.

    Parameters:
    radians (Union[int, float]): The angle in radians.

    Returns:
    float: The secant of the angle.
    """
    cos_value = cosine_taylor(radians)
    if cos_value == 0:
        raise ValueError("Secant is undefined for angles where cos(x) = 0.")
    
    # Calculate secant using formula: sec(x) = 1 / cos(x)
    return 1 / cos_value
