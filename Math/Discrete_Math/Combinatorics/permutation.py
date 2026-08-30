# Permutation formula: for nPr where n and r are non-negative integers
import math
from typing import Union


def n_permute_r(n: int, r: int) -> int:
    """
    Calculate permutations (nPr) using the formula: nPr = n! / (n - r)!.

    Parameters:
    n (int): The total number of items.
    r (int): The number of items to arrange.

    Returns:
    int: The number of permutations (n permute r).
    """
    if r < 0 or n < 0 or n < r:
        raise ValueError(
            "n should be greater than or equal to r for permutations to be valid."
        )

    return math.perm(n, r)
