# Calculate the number of partitions of a positive integer


def partition(n: int) -> int:
    """
    Calculate the number of partitions of a positive integer n.

    Parameters:
    n (int): The positive integer to partition.

    Returns:
    int: The number of partitions of n.
    """
    if n < 0:
        return 0
    if n == 0:
        return 1


    # Optimization: Use Euler's pentagonal number theorem to calculate
    # partitions in O(n sqrt(n)) time instead of O(n^2) dynamic programming.
    # Recurrence: p(n) = sum_{k != 0} (-1)^(k-1) * p(n - g_k), where
    # g_k = k(3k - 1)/2 for k = 1, -1, 2, -2, 3, -3, ...
    pentagonals = []
    k = 1
    while True:
        g1 = (k * (3 * k - 1)) // 2
        g2 = (k * (3 * k + 1)) // 2
        sign = 1 if (k % 2 == 1) else -1
        if g1 > n:
            break
        pentagonals.append((g1, sign))
        if g2 <= n:
            pentagonals.append((g2, sign))
        k += 1

    partitions = [0] * (n + 1)
    partitions[0] = 1

    for i in range(1, n + 1):
        total = 0
        for g, sign in pentagonals:
            if g > i:
                break
            total += sign * partitions[i - g]
        partitions[i] = total

    return partitions[n]
