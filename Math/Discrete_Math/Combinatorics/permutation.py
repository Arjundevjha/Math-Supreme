# Permutation formula: for nPr where n and r are non-negative integers
from typing import Union


def factorial(n: int) -> int:
    """
    Calculate factorial of n using recursion.

    Parameters:
    n (int): The number to calculate factorial for.

    Returns:
    int: The factorial of n (n!).
    """
    if n == 0:
        return 1
    else:
        # Calculate factorial recursively
        return n * factorial(n - 1)


def n_permute_r(n: int, r: int) -> Union[int, float]:
    """
    Calculate permutations (nPr) using the formula: nPr = n! / (n - r)!.

    Parameters:
    n (int): The total number of items.
    r (int): The number of items to arrange.

    Returns:
    Union[int, float]: The number of permutations (n permute r).
    """
    if n < r:
        raise ValueError("n should be greater than or equal to r for permutations to be valid.")
    
    # Calculate permutations using factorial formula
    return factorial(n) / factorial(n - r)