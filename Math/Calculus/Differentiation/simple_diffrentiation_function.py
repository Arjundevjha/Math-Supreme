"""Module for differentiating dense-list polynomials using the power rule."""
from typing import List, Sequence, Union

from Math.Algebra.Polynomials.polynomial import (
    trim_polynomial,
    validate_polynomial,
)


def differentiate_polynomial(
    poly: Sequence[Union[int, float]],
) -> List[Union[int, float]]:
    """
    Differentiate a polynomial [c0, c1, c2, ...] via list manipulation.

    Parameters:
    poly (Sequence[Union[int, float]]): Dense coefficient list where
        index i corresponds to x^i.

    Returns:
    List[Union[int, float]]: Dense coefficient list of the derivative.
    """
    coeffs = validate_polynomial(poly)
    if len(coeffs) <= 1:
        return []
    return trim_polynomial([i * c for i, c in enumerate(coeffs)][1:])
