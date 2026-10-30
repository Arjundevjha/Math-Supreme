"""Module for differentiating polynomials using the power rule."""
from typing import List, Union, Tuple


def differentiate_polynomial(
    coeffs: List[Union[int, float]], powers: List[Union[int, float]]
) -> List[Tuple[float, float]]:
    """
    Differentiate a polynomial using the power rule.

    Parameters:
    coeffs (List[Union[int, float]]): Coefficients of the polynomial terms.
    powers (List[Union[int, float]]): Powers of the polynomial terms.

    Returns:
    List[Tuple[float, float]]: List of tuples (coefficient, power) for the derivative.
    """
    # Security: Validate input types and power bounds to prevent DoS and unexpected behavior
    if not isinstance(coeffs, (list, tuple)) or not isinstance(powers, (list, tuple)):
        raise TypeError("Coefficients and powers must be lists or tuples.")

    for coeff in coeffs:
        if isinstance(coeff, bool) or not isinstance(coeff, (int, float)):
            raise TypeError("Coefficients must be numeric values (int or float).")

    for power in powers:
        if isinstance(power, bool) or not isinstance(power, (int, float)):
            raise TypeError("Powers must be numeric values (int or float).")
        if abs(power) > 10000:
            raise ValueError("Power exceeds maximum limit of 10000.")

    # Optimization: Use list comprehension to eliminate loop method lookup
    # and dynamic list allocations
    return [
        (coeff * power, power - 1)
        for coeff, power in zip(coeffs, powers)
        if power > 0
    ]
