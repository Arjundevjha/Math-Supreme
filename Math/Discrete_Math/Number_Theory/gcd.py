# Greatest Common Divisor (GCD) calculation
from typing import List

from Math.Discrete_Math.Number_Theory.prime_factorisation import (
    prime_factorization,
)


def prime_factorization_for_gcd(n: int) -> List[int]:
    """
    Get prime factors of a number for GCD calculation.

    Parameters:
    n (int): The number to factorize.

    Returns:
    List[int]: List of prime factors.
    """
    if n <= 1:
        return []
    return prime_factorization(n)



def compute_gcd(a: int, b: int) -> int:
    """
    Compute the Greatest Common Divisor (GCD) of two numbers using the Euclidean algorithm.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The GCD of a and b.
    """
    if a <= 0 or b <= 0:
        raise ValueError("Both numbers must be positive.")

    while b != 0:
        a, b = b, a % b

    return a
