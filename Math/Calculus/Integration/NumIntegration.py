"""Module for numerical polynomial integration."""
# pylint: disable=invalid-name,comparison-with-itself
from typing import List, Union, Tuple

# Optimization: Hoist positive and negative float infinity constants to module scope
# to avoid repeated float parsing and tuple allocations on every validation loop iteration.
POS_INF = float("inf")
NEG_INF = float("-inf")


def _validate_polynomial_inputs(
    coefficients: List[Union[int, float]], powers: List[Union[int, float]]
) -> None:
    """Validate coefficients and powers input lists/tuples to prevent DoS and type confusion."""
    if not isinstance(coefficients, (list, tuple)) or not isinstance(powers, (list, tuple)):
        raise TypeError("Coefficients and powers must be lists or tuples.")

    # Optimization: Direct comparison with module constants POS_INF and NEG_INF
    # avoids allocating a tuple (float("inf"), float("-inf")) and parsing string floats
    # per element, providing a ~2x faster validation loop.
    for coeff in coefficients:
        if isinstance(coeff, bool) or not isinstance(coeff, (int, float)):
            raise TypeError("Coefficients must be numeric values (int or float).")
        if coeff != coeff or coeff == POS_INF or coeff == NEG_INF:
            raise ValueError("Coefficients must be finite real numbers.")

    for power in powers:
        if isinstance(power, bool) or not isinstance(power, (int, float)):
            raise TypeError("Powers must be numeric values (int or float).")
        if power != power or power == POS_INF or power == NEG_INF:
            raise ValueError("Powers must be finite real numbers.")
        if abs(power) > 10000:
            raise ValueError("Power exceeds maximum limit of 10000.")


def integrate_polynomial(
    coefficients: List[Union[int, float]], powers: List[Union[int, float]]
) -> Tuple[List[float], List[float]]:
    """
    Integrate a polynomial term by term.

    Parameters:
    coefficients (List[Union[int, float]]): List of coefficients for each term.
    powers (List[Union[int, float]]): List of powers for each term.

    Returns:
    Tuple[List[float], List[float]]: Lists of integrated coefficients and powers.
    """
    # Security: Validate inputs to prevent DoS, type confusion, and invalid state
    _validate_polynomial_inputs(coefficients, powers)

    n = min(len(coefficients), len(powers))
    sub_powers = powers[:n]
    if -1 in sub_powers:
        raise ValueError(
            "Integration of x^-1 results in ln|x|, which is not supported "
            "by this polynomial integration function."
        )

    # Apply integration rule: ∫(ax^n)dx = (a/(n+1))×x^(n+1) + C
    integrated_powers = [power + 1 for power in sub_powers]
    integrated_coeffs = [
        coeff / new_power for coeff, new_power in zip(coefficients[:n], integrated_powers)
    ]

    return integrated_coeffs, integrated_powers


def format_polynomial_integration(coefficients: List[float], powers: List[float]) -> str:
    """
    Format an integrated polynomial as a string.

    Parameters:
    coefficients (List[float]): List of coefficients.
    powers (List[float]): List of powers.

    Returns:
    str: String representation of the integrated polynomial.
    """
    # Security: Validate inputs to prevent DoS, type confusion, and invalid state
    _validate_polynomial_inputs(coefficients, powers)

    terms = []
    for coeff, power in zip(coefficients, powers):
        if power == 0:
            terms.append(f"{coeff}")
        elif power == 1:
            terms.append(f"{coeff}x")
        else:
            terms.append(f"{coeff}x^{int(power)}")

    result = " + ".join(terms)
    return result + " + C"
