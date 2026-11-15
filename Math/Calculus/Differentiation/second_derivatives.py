"""Module for calculating second derivatives of dense-list polynomials."""
from typing import List, Sequence, Union

from Math.Algebra.Polynomials.polynomial import (
    trim_polynomial,
    validate_polynomial,
)


def second_derivative(
    poly: Sequence[Union[int, float]],
) -> List[Union[int, float]]:
    """
    Calculate the second derivative of a dense polynomial [c0, c1, c2, ...].

    Parameters:
    poly (Sequence[Union[int, float]]): Dense coefficient list where
        index i corresponds to x^i.

    Returns:
    List[Union[int, float]]: Dense coefficient list of the second derivative.
    """
    coeffs = validate_polynomial(poly)
    if len(coeffs) <= 2:
        return []
    return trim_polynomial(
        [c * i * (i - 1) for i, c in enumerate(coeffs)][2:]
    )
