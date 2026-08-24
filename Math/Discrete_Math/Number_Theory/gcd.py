# Greatest Common Divisor (GCD) calculation
from typing import List
from collections import Counter


def prime_factorization_for_gcd(n: int) -> List[int]:
    """
    Get prime factors of a number for GCD calculation.

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


def compute_gcd(a: int, b: int) -> int:
    """
    Compute the Greatest Common Divisor (GCD) of two numbers using prime factorization.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The GCD of a and b.
    """
    if a <= 0 or b <= 0:
        raise ValueError("Both numbers must be positive.")

    # Get prime factors for both numbers
    factors_a = prime_factorization_for_gcd(a)
    factors_b = prime_factorization_for_gcd(b)

    # Find common factors
    common_factors = set(factors_a) & set(factors_b)

    # Calculate GCD by taking minimum power of each common prime factor
    count_a = Counter(factors_a)
    count_b = Counter(factors_b)

    gcd = 1
    for factor in common_factors:
        gcd *= factor ** min(count_a[factor], count_b[factor])

    return gcd