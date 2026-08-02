from decimal import Decimal


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
    if n > 1000:
        raise ValueError(
            "Factorial calculation limit exceeded (maximum allowed is 1000)."
        )
    if n == 0 or n == 1:
        return 1

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
    Decimal: The factorial of n.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n > 1000:
        raise ValueError(
            "Factorial calculation limit exceeded (maximum allowed is 1000)."
        )

    result = Decimal(1)
    for i in range(1, n + 1):
        result *= i
    return result
