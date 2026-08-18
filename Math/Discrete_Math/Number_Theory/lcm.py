# Least Common Multiple (LCM) calculation
from typing import List

from Math.Discrete_Math.Number_Theory.gcd import compute_gcd


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

    return abs(a * b) // compute_gcd(a, b)
