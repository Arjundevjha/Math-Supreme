"""Optimization problems: closed-interval extrema and Newton-Raphson."""
from typing import Dict, Sequence, Union

from Math.Algebra.Polynomials.polynomial import (
    evaluate_polynomial,
    validate_polynomial,
)
from Math.Calculus.Applications_of_Derivatives.curve_sketching import (
    critical_points,
)
from Math.Calculus.Differentiation.simple_diffrentiation_function import (
    differentiate_polynomial,
)

Number = Union[int, float]


def find_extrema_on_interval(
    poly: Sequence[Number], a: Number, b: Number
) -> Dict[str, float]:
    """
    Find the global minimum and maximum of polynomial P(x) on [a, b].

    Parameters:
    poly (Sequence[Number]): Dense polynomial coefficient list [c0, c1, ...].
    a (Number): Left endpoint of closed interval.
    b (Number): Right endpoint of closed interval.

    Returns:
    Dict[str, float]: Dictionary with 'min_x', 'min_val', 'max_x', 'max_val'.
    """
    coeffs = validate_polynomial(poly)
    for name, val in [("a", a), ("b", b)]:
        if isinstance(val, bool) or not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be a numeric int or float.")
        if not -float("inf") < val < float("inf"):
            raise ValueError(f"{name} must be a finite number.")
    if a >= b:
        raise ValueError("Interval requires a < b.")

    candidates = [float(a), float(b)] + critical_points(
        coeffs, float(a), float(b)
    )
    evaluated = [(x, evaluate_polynomial(coeffs, x)) for x in candidates]
    min_x, min_val = min(evaluated, key=lambda item: item[1])
    max_x, max_val = max(evaluated, key=lambda item: item[1])
    return {
        "min_x": min_x,
        "min_val": min_val,
        "max_x": max_x,
        "max_val": max_val,
    }


def newton_raphson_root(
    poly: Sequence[Number],
    initial_guess: Number,
    tol: float = 1e-9,
    max_iter: int = 100,
) -> float:
    """
    Find a real root of polynomial P(x) = 0 using Newton-Raphson iteration.

    Parameters:
    poly (Sequence[Number]): Dense polynomial coefficient list [c0, c1, ...].
    initial_guess (Number): Starting x0 value.
    tol (float): Convergence tolerance (> 0).
    max_iter (int): Maximum iterations (1 to 10000).

    Returns:
    float: Approximate root x such that P(x) ~= 0.
    """
    coeffs = validate_polynomial(poly)
    if isinstance(initial_guess, bool) or not isinstance(
        initial_guess, (int, float)
    ):
        raise TypeError("initial_guess must be a numeric int or float.")
    if not -float("inf") < initial_guess < float("inf"):
        raise ValueError("initial_guess must be finite.")
    if isinstance(tol, bool) or not isinstance(tol, (int, float)) or tol <= 0:
        raise ValueError("tol must be a positive number.")
    if (
        isinstance(max_iter, bool)
        or not isinstance(max_iter, int)
        or max_iter < 1
        or max_iter > 10000
    ):
        raise ValueError("max_iter must be an integer between 1 and 10000.")

    deriv = differentiate_polynomial(coeffs)
    x = float(initial_guess)

    for _ in range(max_iter):
        fx = evaluate_polynomial(coeffs, x)
        if abs(fx) <= tol:
            return x
        dfx = evaluate_polynomial(deriv, x)
        if abs(dfx) <= 1e-14:
            raise ValueError("Derivative is zero; Newton-Raphson stalled.")
        next_x = x - fx / dfx
        if abs(next_x - x) <= tol:
            return next_x
        x = next_x

    raise ValueError("Newton-Raphson did not converge within max_iter.")
