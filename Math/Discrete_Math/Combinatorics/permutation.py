# Permutation formula: for nPr where n and r are non-negative integers
from Math.utils.math_utils import _product_tree, factorial


def n_permute_r(n: int, r: int) -> int:
    """
    Calculate permutations (nPr) using the formula: nPr = n! / (n - r)!.

    Parameters:
    n (int): The total number of items.
    r (int): The number of items to arrange.

    Returns:
    int: The number of permutations (n permute r).
    """
    if (
        not (isinstance(n, int) and isinstance(r, int))
        or isinstance(n, bool)
        or isinstance(r, bool)
    ):
        raise TypeError("Inputs must be integers.")
    if r < 0 or n < 0 or n < r:
        raise ValueError(
            "n should be greater than or equal to r for permutations to be valid."
        )

    if r == 0:
        return 1

    # Optimization: Compute product over range [n - r + 1, n] using
    # divide-and-conquer tree multiplication instead of calculating full n!
    # and (n - r)! factorials and performing large integer division.
    # This reduces work from 2 * O(n) multiplications + big integer division
    # to O(r) balanced tree multiplications.
    return _product_tree(n - r + 1, n)


