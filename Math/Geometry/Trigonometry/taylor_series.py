from typing import Union

def sine_taylor(radians: Union[int, float], terms: int = 50) -> float:
    """
    Calculate the sine of an angle using Taylor series expansion.

    Parameters:
    radians (Union[int, float]): The angle in radians.
    terms (int): Number of terms to use in the series. Default is 50.

    Returns:
    float: The sine of the angle.
    """
    sine_value = float(radians)
    term = float(radians)
    radians_sq = float(radians * radians)

    # Calculate sine using Taylor series iteratively:
    # Next term = Previous term * (-x^2) / ((idx - 1) * idx)
    for idx in range(3, terms * 2, 2):
        term *= -radians_sq / ((idx - 1) * idx)
        sine_value += term

    return sine_value

def cosine_taylor(radians: Union[int, float], terms: int = 50) -> float:
    """
    Calculate the cosine of an angle using Taylor series expansion.

    Parameters:
    radians (Union[int, float]): The angle in radians.
    terms (int): Number of terms to use in the series. Default is 50.

    Returns:
    float: The cosine of the angle.
    """
    cos_value = 1.0
    term = 1.0
    radians_sq = float(radians * radians)

    for idx in range(2, terms * 2, 2):
        term *= -radians_sq / (idx * (idx - 1))
        cos_value += term

    return cos_value
