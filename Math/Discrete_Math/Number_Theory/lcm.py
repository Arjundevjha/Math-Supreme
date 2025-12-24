# Least Common Multiple (LCM) calculation
from typing import List


def prime_factorization_simple(n: int) -> List[int]:
    """
    Get prime factors of a number.

    Parameters:
    n (int): The number to factorize.

    Returns:
    List[int]: List of prime factors.
    """
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


def compute_lcm(a: int, b: int) -> int:
    """
    Compute the Least Common Multiple (LCM) of two numbers.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The LCM of a and b.
    """
    if a <= 0 or b <= 0:
        raise ValueError("Both numbers must be positive.")
    
    # Get prime factors for both numbers
    factors_a = prime_factorization_simple(a)
    factors_b = prime_factorization_simple(b)

    # Find all unique factors
    all_factors = set(factors_a) | set(factors_b)
    
    # Calculate LCM by taking maximum power of each prime factor
    lcm = 1
    for factor in all_factors:
        lcm *= factor ** max(factors_a.count(factor), factors_b.count(factor))
    
    return lcm