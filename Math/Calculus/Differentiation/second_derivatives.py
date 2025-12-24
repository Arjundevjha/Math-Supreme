# Second derivatives
from typing import List, Union


def second_derivative(coeffs: List[Union[int, float]], powers: List[Union[int, float]]) -> List[tuple]:
    """
    Calculate the second derivative of a polynomial.

    Parameters:
    coeffs (List[Union[int, float]]): Coefficients of the polynomial.
    powers (List[Union[int, float]]): Powers of the polynomial.

    Returns:
    List[tuple]: List of tuples (coefficient, power) for the second derivative.
    """
    # First derivative: d/dx(ax^n) = n×a×x^(n-1)
    first_deriv_coeffs = []
    first_deriv_powers = []
    
    for coeff, power in zip(coeffs, powers):
        if power > 0:
            first_deriv_coeffs.append(coeff * power)
            first_deriv_powers.append(power - 1)
    
    # Second derivative: apply derivative again
    second_deriv = []
    for coeff, power in zip(first_deriv_coeffs, first_deriv_powers):
        if power > 0:
            second_deriv.append((coeff * power, power - 1))
    
    return second_deriv