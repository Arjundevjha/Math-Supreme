# Second derivatives
from typing import List, Union
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
    # Optimization: Apply second-derivative power rule d^2/dx^2(ax^n) = n(n-1)ax^(n-2)
    # in a single-pass list comprehension, avoiding two compute_polynomial_derivative
    # function calls, intermediate list allocations, and zip/list conversions.
    return [
        (coeff * power * (power - 1), power - 2)
        for coeff, power in zip(coeffs, powers)
        if power != 0 and power != 1
    ]
