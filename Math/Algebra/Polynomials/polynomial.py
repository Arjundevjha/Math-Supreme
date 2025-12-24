# Polynomial representation (simplified version)
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


def format_polynomial(coefficients: List[Union[int, float]], powers: List[Union[int, float]]) -> str:
    """
    Format a polynomial as a string.

    Parameters:
    coefficients (List[Union[int, float]]): List of coefficients for each term.
    powers (List[Union[int, float]]): List of powers for each term.

    Returns:
    str: String representation of the polynomial.
    """
    terms = []
    for coeff, power in zip(coefficients, powers):
        if power == 0:
            terms.append(f"{coeff}")
        elif power == 1:
            terms.append(f"{coeff}x")
        else:
            terms.append(f"{coeff}x^{power}")
    
    return " + ".join(terms)
