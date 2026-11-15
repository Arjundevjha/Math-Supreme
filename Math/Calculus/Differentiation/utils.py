"""Polynomial differentiation and formatting utilities."""
from typing import List, Sequence, Union

from Math.Algebra.Polynomials.polynomial import format_polynomial
from .simple_diffrentiation_function import differentiate_polynomial


def compute_polynomial_derivative(
    poly: Sequence[Union[int, float]],
) -> List[Union[int, float]]:
    """
    Compute the derivative of a dense polynomial [c0, c1, c2, ...].

    Parameters:
    poly (Sequence[Union[int, float]]): Dense coefficient list.

    Returns:
    List[Union[int, float]]: Dense coefficient list of the derivative.
    """
    return differentiate_polynomial(poly)


def compute_polynomial_derivative_str(
    poly: Sequence[Union[int, float]],
) -> str:
    """
    Compute the derivative of a dense polynomial and format as a string.

    Parameters:
    poly (Sequence[Union[int, float]]): Dense coefficient list.

    Returns:
    str: String representation of the derivative.
    """
    return format_polynomial(differentiate_polynomial(poly))
