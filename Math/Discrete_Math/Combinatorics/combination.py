# Combination formula: for nCr where n and r are non-negative integers
from functools import lru_cache


@lru_cache(maxsize=None)
def nCr(n: int, r: int) -> int:
    """
    Calculate combinations (nCr) using the formula: nCr = n! / (r! * (n - r)!).

    Parameters:
    n (int): The total number of items.
    r (int): The number of items to choose.

    Returns:
    int: The number of combinations (n choose r).
    """
    if not (isinstance(n, int) and isinstance(r, int)) or isinstance(n, bool) or isinstance(r, bool):
        raise TypeError("Inputs must be integers.")
    if n < 0 or r < 0 or r > n:
        raise ValueError("Invalid values for n and r.")

    # Optimization: Compute product iteratively over r terms instead of calculating 3 full factorials.
    # Symmetry property nCr(n, r) == nCr(n, n - r) reduces iterations to min(r, n - r).
    # This reduces time complexity from O(n) large integer multiplications to O(min(r, n - r)).
    r = min(r, n - r)
    if r == 0:
        return 1

    num = 1
    den = 1
    for i in range(1, r + 1):
        num *= (n - r + i)
        den *= i

    return num // den
