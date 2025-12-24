# Remainder theorem: find the remainder when a polynomial is divided by (x - a)
from typing import List, Union


def evaluate_polynomial(coefficients: List[Union[int, float]], powers: List[Union[int, float]], x: Union[int, float]) -> float:
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
    result = sum(coeff * (x ** power) for coeff, power in zip(coefficients, powers))
    return result


def remainder_theorem(coefficients: List[Union[int, float]], powers: List[Union[int, float]], x: Union[int, float]) -> float:
    """
    Find the remainder when a polynomial is divided by (x - a) using the Remainder Theorem.

    Parameters:
    coefficients (List[Union[int, float]]): List of coefficients for each term.
    powers (List[Union[int, float]]): List of powers for each term.
    x (Union[int, float]): The value a in (x - a).

    Returns:
    float: The remainder when the polynomial is divided by (x - a).
    """
    # According to Remainder Theorem: remainder = P(a)
    return evaluate_polynomial(coefficients, powers, x)
