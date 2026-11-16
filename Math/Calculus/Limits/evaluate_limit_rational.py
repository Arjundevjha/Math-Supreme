"""Evaluate limits of rational polynomial functions at finite points."""
from typing import Sequence, Union

from Math.Algebra.Polynomials.polynomial import (
    evaluate_polynomial,
    trim_polynomial,
    validate_polynomial,
)
from Math.Calculus.Differentiation.simple_diffrentiation_function import (
    differentiate_polynomial,
)

Number = Union[int, float]


def evaluate_limit_rational(
    numerator: Sequence[Number],
    denominator: Sequence[Number],
    x0: Number,
) -> float:
    """
    Evaluate lim_{x -> x0} P(x) / Q(x) for dense-list polynomials P and Q.

    Applies repeated L'Hopital's rule on 0/0 indeterminate forms, and inspects
    left/right signs near x0 when Q(x0) == 0 and P(x0) != 0.

    Parameters:
    numerator (Sequence[Number]): Numerator polynomial [c0, c1, ...].
    denominator (Sequence[Number]): Denominator polynomial [d0, d1, ...].
    x0 (Number): Finite point at which to evaluate the limit.

    Returns:
    float: The limit value (or +/-inf if both sides diverge identically).
    """
    num = trim_polynomial(validate_polynomial(numerator))
    den = trim_polynomial(validate_polynomial(denominator))
    if isinstance(x0, bool) or not isinstance(x0, (int, float)):
        raise TypeError("x0 must be a numeric int or float.")
    if not -float("inf") < x0 < float("inf"):
        raise ValueError("x0 must be a finite number.")
    if not den:
        raise ValueError("Denominator polynomial cannot be identically zero.")

    x_val = float(x0)
    cur_num = num
    cur_den = den

    for _ in range(max(len(num), len(den)) + 1):
        p_val = evaluate_polynomial(cur_num, x_val)
        q_val = evaluate_polynomial(cur_den, x_val)

        if abs(q_val) > 1e-12:
            return p_val / q_val
        if abs(p_val) > 1e-12:
            # Non-zero / 0 -> check left and right asymptotic behavior
            eps = 1e-6
            left = evaluate_polynomial(cur_num, x_val - eps) / (
                evaluate_polynomial(cur_den, x_val - eps)
            )
            right = evaluate_polynomial(cur_num, x_val + eps) / (
                evaluate_polynomial(cur_den, x_val + eps)
            )
            if left > 0 and right > 0:
                return float("inf")
            if left < 0 and right < 0:
                return float("-inf")
            raise ValueError(
                f"Two-sided limit does not exist at x = {x_val} "
                "(opposite-sign vertical asymptote)."
            )

        # 0/0 indeterminate form -> apply L'Hopital's rule via list diff
        cur_num = differentiate_polynomial(cur_num)
        cur_den = differentiate_polynomial(cur_den)
        if not cur_den:
            break

    return 0.0
