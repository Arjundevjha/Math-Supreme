# Chain rule for differentiation of composite functions
from typing import List, Union, Tuple


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


def compute_polynomial_derivative(coefficients: List[Union[int, float]], powers: List[Union[int, float]]) -> Tuple[List[float], List[float]]:
    """
    Compute the derivative of a polynomial.

    Parameters:
    coefficients (List[Union[int, float]]): List of coefficients.
    powers (List[Union[int, float]]): List of powers.

    Returns:
    Tuple[List[float], List[float]]: Lists of derivative coefficients and powers.
    """
    derivative_coeffs = []
    derivative_powers = []
    
    # Apply power rule: d/dx(ax^n) = n×a×x^(n-1)
    for coeff, power in zip(coefficients, powers):
        if power == 0:
            continue
        derivative_coeffs.append(coeff * power)
        derivative_powers.append(power - 1)
    
    return derivative_coeffs, derivative_powers


def chain_rule_derivative(inner_coeffs: List[Union[int, float]], inner_powers: List[Union[int, float]], exponent: int) -> str:
    """
    Apply the chain rule to find the derivative of [g(x)]^n.

    Parameters:
    inner_coeffs (List[Union[int, float]]): Coefficients of the inner function g(x).
    inner_powers (List[Union[int, float]]): Powers of the inner function g(x).
    exponent (int): The power n to which g(x) is raised.

    Returns:
    str: A string representation of the derivative.
    """
    if exponent < 0:
        raise ValueError("Exponent must be non-negative.")
    
    # Format inner polynomial g(x)
    g_x = format_polynomial(inner_coeffs, inner_powers)
    
    # Compute derivative of inner function g'(x)
    g_prime_coeffs, g_prime_powers = compute_polynomial_derivative(inner_coeffs, inner_powers)
    
    derivative_terms = []
    for coeff, power in zip(g_prime_coeffs, g_prime_powers):
        derivative_terms.append(f"{coeff}x^{int(power)}")
    g_prime = " + ".join(derivative_terms)
    
    # Apply chain rule: d/dx[g(x)]^n = n×[g(x)]^(n-1) × g'(x)
    result = f"{exponent}({g_x})^{exponent - 1} * ({g_prime})"
    
    return result