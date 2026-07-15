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
    if n > 1000:
        raise ValueError("Number too large, maximum allowed is 1000 to prevent uncontrolled resource consumption.")

    # Use dynamic programming to calculate partitions
    partitions = [0] * (n + 1)
    partitions[0] = 1

    # Build partition table: p(n) = number of ways to write n as sum of positive integers
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            partitions[j] += partitions[j - i]

    return partitions[n]