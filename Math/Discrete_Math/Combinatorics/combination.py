# Combination formula: for nCr where n and r are non-negative integers


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
        raise TypeError("n and r must be integers.")

    if r < 0 or r > n or n < 0:
        raise ValueError("Invalid values for n and r.")

    # Performance Optimization: Avoid calculating full factorials (3x expensive factorial calls).
    # Use symmetry property nCr(n, r) == nCr(n, n - r) to minimize loop iterations.
    r = min(r, n - r)

    numerator = 1
    denominator = 1
    for i in range(1, r + 1):
        numerator *= (n - i + 1)
        denominator *= i

    return numerator // denominator
