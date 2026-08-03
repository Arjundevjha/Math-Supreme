# Remainder theorem: find the remainder when a polynomial is divided by (x - a)
from typing import List, Union
from .polynomial import evaluate_polynomial


def remainder_theorem(coefficients: List[Union[int, float]], powers: List[Union[int, float]], x: Union[int, float]) -> float:
    """
    Find the remainder when a polynomial is divided by (x - a) using the Remainder Theorem.

    Parameters:
    coefficients (List[Union[int, float]]): List of coefficients for each term.
    powers (List[Union[int, float]]): List of powers for each term.
    x (Union[int, float]): The value a in (x - a).

    Returns:
    float: The remainder when the polynomial is divided by (x - a).
    """
    # According to Remainder Theorem: remainder = P(a)
    return evaluate_polynomial(coefficients, powers, x)
