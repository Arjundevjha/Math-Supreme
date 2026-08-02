from typing import List, Union

def format_polynomial(coefficients: List[Union[int, float]], powers: List[Union[int, float]]) -> str:
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
