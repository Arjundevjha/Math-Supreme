"""Product rule for differentiation."""
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
    # Security: Input validation & DoS prevention
    sequences = (u_coeffs, u_powers, v_coeffs, v_powers)
    if not all(isinstance(seq, (list, tuple)) for seq in sequences):
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
