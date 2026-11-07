"""Quotient rule for differentiation."""

from typing import List, Union

from Math.utils.math_utils import format_polynomial
from .utils import compute_polynomial_derivative_str


def _validate_polynomial_inputs(
    u_coeffs: List[Union[int, float]],
    u_powers: List[Union[int, float]],
    v_coeffs: List[Union[int, float]],
    v_powers: List[Union[int, float]],
) -> None:
    """Validate polynomial inputs and prevent denial of service."""
    if not all(
        isinstance(seq, (list, tuple))
        for seq in (u_coeffs, u_powers, v_coeffs, v_powers)
    ):
        raise TypeError("Coefficients and powers must be lists or tuples.")

    for coeffs in (u_coeffs, v_coeffs):
        for coeff in coeffs:
            if isinstance(coeff, bool) or not isinstance(coeff, (int, float)):
                raise TypeError("Coefficients must be numeric values (int or float).")

    for powers in (u_powers, v_powers):
        for power in powers:
            if isinstance(power, bool) or not isinstance(power, (int, float)):
                raise TypeError("Powers must be numeric values (int or float).")
            if abs(power) > 10000:
                raise ValueError("Power exceeds maximum limit of 10000.")


def quotient_rule_derivative(
    u_coeffs: List[Union[int, float]],
    u_powers: List[Union[int, float]],
    v_coeffs: List[Union[int, float]],
    v_powers: List[Union[int, float]],
) -> str:
    """
    Apply the quotient rule to find the derivative of u(x) / v(x).

    Parameters:
    u_coeffs (List[Union[int, float]]): Coefficients of the numerator polynomial u(x).
    u_powers (List[Union[int, float]]): Powers of the numerator polynomial u(x).
    v_coeffs (List[Union[int, float]]): Coefficients of the denominator polynomial v(x).
    v_powers (List[Union[int, float]]): Powers of the denominator polynomial v(x).

    Returns:
    str: A string representation of the derivative using quotient rule.
    """
    # Security: Input validation & DoS prevention
    _validate_polynomial_inputs(u_coeffs, u_powers, v_coeffs, v_powers)

    # Format polynomials
    poly1 = format_polynomial(u_coeffs, u_powers)
    poly2 = format_polynomial(v_coeffs, v_powers)

    # Compute derivatives
    u_prime = compute_polynomial_derivative_str(u_coeffs, u_powers)
    v_prime = compute_polynomial_derivative_str(v_coeffs, v_powers)

    # Apply quotient rule: (u/v)' = (u'×v - u×v') / v²
    numerator = f"({u_prime}) * ({poly2}) - ({poly1}) * ({v_prime})"
    denominator = f"({poly2})^2"
    result = f"({numerator}) / {denominator}"

    return result
