"""Factor theorem: check if (x - a) is a factor of a polynomial."""
from typing import Sequence, Union

from .polynomial import evaluate_polynomial


def check_factor(
    poly: Sequence[Union[int, float]], x: Union[int, float]
) -> bool:
    """
    Check if (x - a) is a factor of a polynomial using the Factor Theorem.

    Parameters:
    poly (Sequence[Union[int, float]]): Dense coefficient list [c0, c1, ...].
    x (Union[int, float]): The value a to test whether (x - a) is a factor.

    Returns:
    bool: True if (x - a) is a factor, False otherwise.
    """
    result = evaluate_polynomial(poly, x)
    return abs(result) <= 1e-9
