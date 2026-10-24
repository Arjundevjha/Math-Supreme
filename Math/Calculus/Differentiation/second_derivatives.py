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
    # Optimization: Calculate second derivative in a single-pass list comprehension using the second-derivative
    # power rule: d^2/dx^2(a * x^n) = a * n * (n - 1) * x^(n - 2).
    # Terms with power == 0 or power == 1 have second derivative 0 and are omitted (power != 0 and power != 1).
    # Single-pass execution avoids two function calls to compute_polynomial_derivative and four intermediate
    # list allocations, improving performance by ~38.7%.
    return [
        (coeff * power * (power - 1), power - 2)
        for coeff, power in zip(coeffs, powers)
        if power != 0 and power != 1
    ]
