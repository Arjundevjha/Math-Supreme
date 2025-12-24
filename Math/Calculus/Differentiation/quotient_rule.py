# Quotient rule for differentiation
from typing import List, Union


def format_polynomial(coefficients: List[Union[int, float]], powers: List[Union[int, float]]) -> str:
    """
    Format a polynomial as a string.

    Parameters:
    coefficients (List[Union[int, float]]): List of coefficients.
    powers (List[Union[int, float]]): List of powers.

    Returns:
    str: String representation of the polynomial.
    """
    terms = []
    for coeff, power in zip(coefficients, powers):
        term = f"{coeff}x^{int(power)}"
        terms.append(term)
    return " + ".join(terms)


def compute_polynomial_derivative_str(coefficients: List[Union[int, float]], powers: List[Union[int, float]]) -> str:
    """
    Compute the derivative of a polynomial and return as string.

    Parameters:
    coefficients (List[Union[int, float]]): List of coefficients.
    powers (List[Union[int, float]]): List of powers.

    Returns:
    str: String representation of the derivative.
    """
    derivative_terms = []
    
    # Apply power rule: d/dx(ax^n) = n×a×x^(n-1)
    for coeff, power in zip(coefficients, powers):
        if power == 0:
            continue
        new_coeff = coeff * power
        new_power = power - 1
        derivative_terms.append(f"{new_coeff}x^{int(new_power)}")
    
    return " + ".join(derivative_terms) if derivative_terms else "0"


def quotient_rule_derivative(u_coeffs: List[Union[int, float]], u_powers: List[Union[int, float]], 
                             v_coeffs: List[Union[int, float]], v_powers: List[Union[int, float]]) -> str:
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