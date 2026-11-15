"""Remainder theorem: find remainder when polynomial is divided by (x - a)."""
from typing import Sequence, Union

from .polynomial import evaluate_polynomial


def remainder_theorem(
    poly: Sequence[Union[int, float]], x: Union[int, float]
) -> float:
    """
    Find the remainder when a polynomial is divided by (x - a).

    Parameters:
    poly (Sequence[Union[int, float]]): Dense coefficient list [c0, c1, ...].
    x (Union[int, float]): The value a in (x - a).

    Returns:
    float: The remainder when the polynomial is divided by (x - a).
    """
    return evaluate_polynomial(poly, x)
