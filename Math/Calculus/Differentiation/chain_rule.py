# Chain rule for differentiation of composite functions
from typing import List, Union

from Math.utils.math_utils import format_polynomial
from .utils import compute_polynomial_derivative


def chain_rule_derivative(
    inner_coeffs: List[Union[int, float]],
    inner_powers: List[Union[int, float]],
    exponent: int,
) -> str:
    """
    Apply the chain rule to find the derivative of [g(x)]^n.

    Parameters:
    inner_coeffs (List[Union[int, float]]): Coefficients of the inner function g(x).
    inner_powers (List[Union[int, float]]): Powers of the inner function g(x).
    exponent (int): The power n to which g(x) is raised.

    Returns:
    str: A string representation of the derivative.
    """
    # Security: Input validation & DoS prevention
    if not isinstance(inner_coeffs, (list, tuple)) or not isinstance(inner_powers, (list, tuple)):
        raise TypeError("Coefficients and powers must be lists or tuples.")

    for coeff in inner_coeffs:
        if isinstance(coeff, bool) or not isinstance(coeff, (int, float)):
            raise TypeError("Coefficients must be numeric values (int or float).")

    for power in inner_powers:
        if isinstance(power, bool) or not isinstance(power, (int, float)):
            raise TypeError("Powers must be numeric values (int or float).")
        if abs(power) > 10000:
            raise ValueError("Power exceeds maximum limit of 10000.")

    if isinstance(exponent, bool) or not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer.")

    if exponent < 0:
        raise ValueError("Exponent must be non-negative.")
    if exponent > 10000:
        raise ValueError("Exponent exceeds maximum limit of 10000.")

    # Format inner polynomial g(x)
    g_x = format_polynomial(inner_coeffs, inner_powers)

    # Compute derivative of inner function g'(x)
    g_prime_coeffs, g_prime_powers = compute_polynomial_derivative(
        inner_coeffs, inner_powers
    )

    derivative_terms = []
    for coeff, power in zip(g_prime_coeffs, g_prime_powers):
        derivative_terms.append(f"{coeff}x^{int(power)}")
    g_prime = " + ".join(derivative_terms)

    # Apply chain rule: d/dx[g(x)]^n = n×[g(x)]^(n-1) × g'(x)
    result = f"{exponent}({g_x})^{exponent - 1} * ({g_prime})"

    return result
