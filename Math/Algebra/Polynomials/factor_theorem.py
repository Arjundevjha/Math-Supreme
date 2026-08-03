# Factor theorem: check if (x - a) is a factor of a polynomial
from typing import List, Union
from .polynomial import evaluate_polynomial


def check_factor(coefficients: List[Union[int, float]], powers: List[Union[int, float]], x: Union[int, float]) -> bool:
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
    
    # Check absolute difference to account for floating-point precision issues
    return abs(result) <= 1e-9
