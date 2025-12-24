# Factorial calculation


def factorial(num: int) -> int:
    """
    Calculate the factorial of a number.

    Parameters:
    num (int): The number to calculate factorial for.

    Returns:
    int: The factorial of num (num!).
    """
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    # Calculate factorial using iterative approach
    result = 1
    for idx in range(1, num + 1):
        result *= idx
    
    return result