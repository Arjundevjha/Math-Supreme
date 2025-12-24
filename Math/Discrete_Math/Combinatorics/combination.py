# Combination formula: for nCr where n and r are non-negative integers


def factorial(n: int) -> int:
    """
    Calculate factorial of n.

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


def n_choose_r(n: int, r: int) -> int:
    """
    Calculate combinations (nCr) using the formula: nCr = n! / (r! * (n - r)!).

    Parameters:
    n (int): The total number of items.
    r (int): The number of items to choose.

    Returns:
    int: The number of combinations (n choose r).
    """
    if r < 0 or r > n:
        raise ValueError("Invalid values for n and r.")
    
    # Calculate combinations using factorial formula
    return factorial(n) // (factorial(r) * factorial(n - r))