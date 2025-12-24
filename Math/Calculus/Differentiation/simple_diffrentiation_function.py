# Simple differentiation function
from typing import List, Union, Tuple


def differentiate_polynomial(coeffs: List[Union[int, float]], powers: List[Union[int, float]]) -> List[Tuple[float, float]]:
    """
    Differentiate a polynomial using the power rule.

    Parameters:
    coeffs (List[Union[int, float]]): Coefficients of the polynomial terms.
    powers (List[Union[int, float]]): Powers of the polynomial terms.

    Returns:
    List[Tuple[float, float]]: List of tuples (coefficient, power) for the derivative.
    """
    derivative = []
    
    # Apply power rule: d/dx(ax^n) = n×a×x^(n-1)
    for coeff, power in zip(coeffs, powers):
        if power > 0:
            new_coeff = coeff * power
            new_power = power - 1
            derivative.append((new_coeff, new_power))
    
    return derivative