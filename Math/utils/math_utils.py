# Mathematical utilities and shared constants
from decimal import Decimal
from typing import List, Union

# Mathematical constants
PI = 3.14159265358979323846


def factorial(n: int) -> int:
    """
    Calculate the factorial of a number.

    Parameters:
    n (int): The number to calculate factorial for.

    Returns:
    int: The factorial of n (n!).
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1

    # Calculate factorial using iterative approach
    result = 1
    for i in range(2, n + 1):
        result *= i

    return result


def factorial_decimal(n: int) -> Decimal:
    """
    Calculate factorial as a Decimal for high precision.

    Parameters:
    n (int): The number to calculate factorial for.

    Returns:
    Decimal: The factorial of n as a Decimal.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    result = Decimal(1)
    for i in range(1, n + 1):
        result *= i
    return result


def format_polynomial(
    coefficients: List[Union[int, float]], powers: List[Union[int, float]]
) -> str:
    """
    Format a polynomial as a string.

    Parameters:
    coefficients (List[Union[int, float]]): List of coefficients.
    powers (List[Union[int, float]]): List of powers.

    Returns:
    str: String representation of the polynomial.
    """
    terms = []
    for coeff, power in zip(coefficients, powers):
        term = f"{coeff}x^{int(power)}"
        terms.append(term)
    return " + ".join(terms)
