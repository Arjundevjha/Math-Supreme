# Combination formula: for nCr where n and r are non-negative integers

import math


def nCr(n: int, r: int) -> int:
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

    return math.comb(n, r)
