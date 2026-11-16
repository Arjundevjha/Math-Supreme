"""Evaluate limits of rational polynomial functions as x -> +/-infinity."""
from typing import Sequence, Union

from Math.Algebra.Polynomials.polynomial import (
    trim_polynomial,
    validate_polynomial,
)

Number = Union[int, float]


def limit_at_infinity(
    numerator: Sequence[Number],
    denominator: Sequence[Number],
    positive: bool = True,
) -> float:
    """
    Evaluate lim_{x -> +inf/-inf} P(x) / Q(x) for dense-list polynomials.

    Parameters:
    numerator (Sequence[Number]): Numerator polynomial [c0, c1, ...].
    denominator (Sequence[Number]): Denominator polynomial [d0, d1, ...].
    positive (bool): If True, evaluate as x -> +inf; else x -> -inf.

    Returns:
    float: The limit value (0.0, ratio of leading coeffs, +inf, or -inf).
    """
    if not isinstance(positive, bool):
        raise TypeError("positive must be a boolean.")

    num = trim_polynomial(validate_polynomial(numerator))
    den = trim_polynomial(validate_polynomial(denominator))
    if not den:
        raise ValueError("Denominator polynomial cannot be identically zero.")
    if not num:
        return 0.0

    deg_p = len(num) - 1
    deg_q = len(den) - 1

    if deg_p < deg_q:
        return 0.0
    if deg_p == deg_q:
        return float(num[-1]) / float(den[-1])

    # deg_p > deg_q: diverges to +inf or -inf
    lead_ratio = float(num[-1]) / float(den[-1])
    diff_deg = deg_p - deg_q
    sign = 1.0 if lead_ratio > 0 else -1.0
    if not positive and diff_deg % 2 == 1:
        sign = -sign
    return float("inf") if sign > 0 else float("-inf")
