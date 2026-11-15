"""Chain rule for differentiation of [g(x)]^n using dense lists."""
from typing import List, Sequence, Union

from Math.Algebra.Polynomials.polynomial import (
    multiply_polynomials,
    power_polynomial,
    trim_polynomial,
    validate_polynomial,
)
from .simple_diffrentiation_function import differentiate_polynomial


def chain_rule_derivative(
    inner: Sequence[Union[int, float]],
    exponent: int,
) -> List[Union[int, float]]:
    """
    Apply the chain rule to compute d/dx [g(x)]^n as a dense polynomial list.

    Parameters:
    inner (Sequence[Union[int, float]]): Inner polynomial g(x) [c0, c1, ...].
    exponent (int): Non-negative integer power n.

    Returns:
    List[Union[int, float]]: Dense coefficient list of n * g(x)^(n-1) * g'(x).
    """
    g_list = validate_polynomial(inner)
    if isinstance(exponent, bool) or not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer.")
    if exponent < 0:
        raise ValueError("Exponent must be non-negative.")
    if exponent > 10000:
        raise ValueError("Exponent exceeds maximum limit of 10000.")

    if exponent == 0:
        return []

    g_prime = differentiate_polynomial(g_list)
    if not g_prime:
        return []

    if exponent == 1:
        return g_prime

    outer_part = power_polynomial(g_list, exponent - 1)
    scaled_outer = [c * exponent for c in outer_part]
    return trim_polynomial(multiply_polynomials(scaled_outer, g_prime))
