# S. Ramanujan's formula for calculating Pi
from decimal import Decimal, getcontext


def factorial_decimal(n: int) -> Decimal:
    """
    Calculate factorial as a Decimal for high precision.

    Parameters:
    n (int): The number to calculate factorial for.

    Returns:
    Decimal: The factorial of n.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    result = Decimal(1)
    for i in range(1, n + 1):
        result *= i
    return result


def calculate_pi_ramanujan(num_decimal_places: int = 50, num_terms: int = 10) -> Decimal:
    """
    Calculate Pi using S. Ramanujan's formula.
    
    Formula: 1/π = (2√2/9801) × Σ[(4k)! × (1103 + 26390k)] / [(k!)⁴ × 396^(4k)]

    Parameters:
    num_decimal_places (int): The desired number of decimal places for pi (default: 50).
    num_terms (int): The number of terms to use in the series summation (default: 10).

    Returns:
    Decimal: The calculated value of pi.
    """
    if num_decimal_places < 0:
        raise ValueError("Number of decimal places cannot be negative.")
    if num_terms < 1:
        raise ValueError("Number of terms must be at least 1.")

    # Set precision for Decimal calculations with extra buffer
    getcontext().prec = num_decimal_places + 20

    total_sum = Decimal(0)
    # Calculate constant: (2√2)/9801
    constant = (Decimal(2) * Decimal(2).sqrt()) / Decimal(9801)

    # Apply Ramanujan's series
    for k in range(num_terms):
        # Calculate numerator: (4k)! × (1103 + 26390k)
        numerator_factorial = factorial_decimal(4 * k)
        numerator_expression = Decimal(1103 + 26390 * k)
        numerator = numerator_factorial * numerator_expression

        # Calculate denominator: (k!)⁴ × 396^(4k)
        denominator_factorial = (factorial_decimal(k)) ** 4
        denominator_power = Decimal(396) ** (4 * k)
        denominator = denominator_factorial * denominator_power

        term = numerator / denominator
        total_sum += term

    # Calculate 1/π
    one_over_pi = constant * total_sum

    # Calculate π = 1 / (1/π)
    pi_value = Decimal(1) / one_over_pi

    return pi_value