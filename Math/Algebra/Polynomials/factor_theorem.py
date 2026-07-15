# Factor theorem: check if (x - a) is a factor of a polynomial
import math
from typing import List, Union


def evaluate_polynomial(
    coefficients: List[Union[int, float]],
    powers: List[Union[int, float]],
    x: Union[int, float],
) -> float:
    """
    Evaluate a polynomial at a given value of x.

    Parameters:
    coefficients (List[Union[int, float]]): List of coefficients for each term.
    powers (List[Union[int, float]]): List of powers for each term.
    x (Union[int, float]): The value at which to evaluate the polynomial.

    Returns:
    float: The value of the polynomial at x.
    """
    # Calculate polynomial value: P(x) = Σ(coefficient × x^power)
    result = sum(coeff * (x**power) for coeff, power in zip(coefficients, powers))
    return result


def check_factor(
    coefficients: List[Union[int, float]],
    powers: List[Union[int, float]],
    x: Union[int, float],
) -> bool:
    """
    Check if (x - a) is a factor of a polynomial using the Factor Theorem.

    Parameters:
    coefficients (List[Union[int, float]]): List of coefficients for each term.
    powers (List[Union[int, float]]): List of powers for each term.
    x (Union[int, float]): The value to check if (x - value) is a factor.

    Returns:
    bool: True if (x - value) is a factor, False otherwise.
    """
    # According to Factor Theorem: (x - a) is a factor if P(a) = 0
    result = evaluate_polynomial(coefficients, powers, x)

    # Use math.isclose to handle potential floating-point inaccuracies
    return math.isclose(result, 0.0, abs_tol=1e-9)
