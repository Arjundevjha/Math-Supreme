"""Curve sketching tools: tangent lines, critical points, and concavity."""
# pylint: disable=too-many-locals,too-many-branches
from typing import List, Sequence, Tuple, Union

from Math.Algebra.Polynomials.polynomial import (
    evaluate_polynomial,
    trim_polynomial,
    validate_polynomial,
)
from Math.Calculus.Differentiation.second_derivatives import second_derivative
from Math.Calculus.Differentiation.simple_diffrentiation_function import (
    differentiate_polynomial,
)
from Math.Numerical_Methods.Functions.nth_root.nth_root import nth_root

Number = Union[int, float]


def tangent_line(
    poly: Sequence[Number], x0: Number
) -> Tuple[float, float]:
    """
    Compute the tangent line y = m*x + b to polynomial P(x) at x = x0.

    Parameters:
    poly (Sequence[Number]): Dense polynomial coefficient list [c0, c1, ...].
    x0 (Number): Point of tangency.

    Returns:
    Tuple[float, float]: (slope, y_intercept).
    """
    coeffs = validate_polynomial(poly)
    if isinstance(x0, bool) or not isinstance(x0, (int, float)):
        raise TypeError("x0 must be a numeric int or float.")
    if not -float("inf") < x0 < float("inf"):
        raise ValueError("x0 must be a finite number.")

    deriv = differentiate_polynomial(coeffs)
    slope = evaluate_polynomial(deriv, x0)
    y0 = evaluate_polynomial(coeffs, x0)
    intercept = y0 - slope * float(x0)
    return slope, intercept


def _find_roots_on_interval(
    poly: List[Number], x_min: float, x_max: float, steps: int = 400
) -> List[float]:
    """Find real roots of a polynomial on [x_min, x_max] via scan + bisection."""
    trimmed = trim_polynomial(poly)
    if not trimmed or len(trimmed) == 1:
        return []
    if len(trimmed) == 2:
        root = -float(trimmed[0]) / float(trimmed[1])
        return [root] if x_min <= root <= x_max else []
    if len(trimmed) == 3:
        c, b, a = float(trimmed[0]), float(trimmed[1]), float(trimmed[2])
        disc = b * b - 4.0 * a * c
        if disc < -1e-12:
            return []
        if abs(disc) <= 1e-12:
            r = -b / (2.0 * a)
            return [r] if x_min <= r <= x_max else []
        sq = float(nth_root(disc, 2))
        roots = sorted([(-b - sq) / (2.0 * a), (-b + sq) / (2.0 * a)])
        return [r for r in roots if x_min <= r <= x_max]

    # General degree >= 3: sample grid + bisection
    roots = []
    step = (x_max - x_min) / steps
    prev_x = x_min
    prev_y = evaluate_polynomial(trimmed, prev_x)
    if abs(prev_y) <= 1e-9:
        roots.append(prev_x)

    for i in range(1, steps + 1):
        cur_x = x_min + i * step
        cur_y = evaluate_polynomial(trimmed, cur_x)
        if abs(cur_y) <= 1e-9:
            if not roots or abs(cur_x - roots[-1]) > 1e-5:
                roots.append(cur_x)
        elif prev_y * cur_y < 0:
            lo, hi = prev_x, cur_x
            f_lo = prev_y
            for _ in range(60):
                mid = 0.5 * (lo + hi)
                f_mid = evaluate_polynomial(trimmed, mid)
                if abs(f_mid) <= 1e-12:
                    lo = hi = mid
                    break
                if f_lo * f_mid <= 0:
                    hi = mid
                else:
                    lo = mid
                    f_lo = f_mid
            cand = 0.5 * (lo + hi)
            if not roots or abs(cand - roots[-1]) > 1e-5:
                roots.append(cand)
        prev_x, prev_y = cur_x, cur_y
    return roots


def critical_points(
    poly: Sequence[Number],
    x_min: Number = -100.0,
    x_max: Number = 100.0,
) -> List[float]:
    """
    Find critical points of a polynomial (where P'(x) = 0) on [x_min, x_max].

    Parameters:
    poly (Sequence[Number]): Dense polynomial coefficient list [c0, c1, ...].
    x_min (Number): Lower search bound.
    x_max (Number): Upper search bound.

    Returns:
    List[float]: Sorted list of critical points x in [x_min, x_max].
    """
    coeffs = validate_polynomial(poly)
    for name, val in [("x_min", x_min), ("x_max", x_max)]:
        if isinstance(val, bool) or not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be a numeric int or float.")
        if not -float("inf") < val < float("inf"):
            raise ValueError(f"{name} must be a finite number.")
    if x_min >= x_max:
        raise ValueError("x_min must be strictly less than x_max.")

    deriv = differentiate_polynomial(coeffs)
    return _find_roots_on_interval(deriv, float(x_min), float(x_max))


def classify_critical_point(poly: Sequence[Number], x0: Number) -> str:
    """
    Classify a critical point using the second derivative test.

    Parameters:
    poly (Sequence[Number]): Dense polynomial coefficient list [c0, c1, ...].
    x0 (Number): Critical point to classify.

    Returns:
    str: 'local_minimum', 'local_maximum', or 'inconclusive'.
    """
    coeffs = validate_polynomial(poly)
    if isinstance(x0, bool) or not isinstance(x0, (int, float)):
        raise TypeError("x0 must be a numeric int or float.")
    if not -float("inf") < x0 < float("inf"):
        raise ValueError("x0 must be a finite number.")

    deriv2 = second_derivative(coeffs)
    val = evaluate_polynomial(deriv2, float(x0))
    if val > 1e-9:
        return "local_minimum"
    if val < -1e-9:
        return "local_maximum"
    return "inconclusive"
