# Second derivatives
from typing import List, Union
from Math.Calculus.Differentiation.utils import compute_polynomial_derivative

def second_derivative(
    coeffs: List[Union[int, float]], powers: List[Union[int, float]]
) -> List[tuple]:
    """
    Calculate the second derivative of a polynomial.

    Parameters:
    coeffs (List[Union[int, float]]): Coefficients of the polynomial.
    powers (List[Union[int, float]]): Powers of the polynomial.

    Returns:
    List[tuple]: List of tuples (coefficient, power) for the second derivative.
    """
    first_deriv_coeffs, first_deriv_powers = compute_polynomial_derivative(coeffs, powers)
    second_deriv_coeffs, second_deriv_powers = compute_polynomial_derivative(first_deriv_coeffs, first_deriv_powers)

    return list(zip(second_deriv_coeffs, second_deriv_powers))
