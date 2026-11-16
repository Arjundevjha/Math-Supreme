"""Module for polynomial integration using dense coefficient lists."""
# pylint: disable=invalid-name
from typing import List, Sequence, Union

from Math.Algebra.Polynomials.polynomial import (
    format_polynomial,
    trim_polynomial,
    validate_polynomial,
)


def integrate_polynomial(
    poly: Sequence[Union[int, float]],
) -> List[float]:
    """
    Integrate a dense polynomial [c0, c1, c2, ...] term by term.

    Parameters:
    poly (Sequence[Union[int, float]]): Dense coefficient list where
        index i corresponds to x^i.

    Returns:
    List[float]: Dense coefficient list of the antiderivative (constant
        term set to 0.0; + C is implicit).
    """
    coeffs = trim_polynomial(validate_polynomial(poly))
    if not coeffs:
        return []

    return [0.0] + [coeff / (power + 1) for power, coeff in enumerate(coeffs)]


def format_polynomial_integration(
    poly: Sequence[Union[int, float]],
) -> str:
    """
    Format an integrated dense polynomial as a string with '+ C'.

    Parameters:
    poly (Sequence[Union[int, float]]): Dense coefficient list.

    Returns:
    str: String representation of the integrated polynomial.
    """
    trimmed = trim_polynomial(validate_polynomial(poly))
    if not trimmed:
        return "C"
    return f"{format_polynomial(trimmed)} + C"
