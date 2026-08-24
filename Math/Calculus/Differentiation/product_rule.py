# Product rule for differentiation
from typing import List, Union

from Math.utils.math_utils import format_polynomial
from .utils import compute_polynomial_derivative_str


def product_rule_derivative(
    u_coeffs: List[Union[int, float]],
    u_powers: List[Union[int, float]],
    v_coeffs: List[Union[int, float]],
    v_powers: List[Union[int, float]],
) -> str:
    """
    Apply the product rule to find the derivative of u(x) * v(x).

    Parameters:
    u_coeffs (List[Union[int, float]]): Coefficients of the first polynomial u(x).
    u_powers (List[Union[int, float]]): Powers of the first polynomial u(x).
    v_coeffs (List[Union[int, float]]): Coefficients of the second polynomial v(x).
    v_powers (List[Union[int, float]]): Powers of the second polynomial v(x).

    Returns:
    str: A string representation of the derivative using product rule.
    """
    # Format polynomials
    poly1 = format_polynomial(u_coeffs, u_powers)
    poly2 = format_polynomial(v_coeffs, v_powers)

    # Compute derivatives
    u_prime = compute_polynomial_derivative_str(u_coeffs, u_powers)
    v_prime = compute_polynomial_derivative_str(v_coeffs, v_powers)

    # Apply product rule: (u×v)' = u'×v + u×v'
    if not u_coeffs and not v_coeffs:
        return "0"
    result = f"({u_prime}) * ({poly2}) + ({poly1}) * ({v_prime})"

    return result
