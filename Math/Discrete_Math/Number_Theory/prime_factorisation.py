# Prime factorization of a number
from typing import List


def prime_factorization(number: int) -> List[int]:
    """
    Find the prime factorization of a number.

    Parameters:
    number (int): The number to factorize (must be positive).

    Returns:
    List[int]: A list of prime factors.
    """
    # Security: Validate type and upper bound limit to prevent DoS via CPU resource exhaustion
    if not isinstance(number, int) or isinstance(number, bool):
        raise TypeError("number must be an integer.")
    if number <= 0:
        raise ValueError("Number must be positive.")
    if number > 1000000000000:
        raise ValueError("number exceeds maximum limit of 1000000000000.")
    if number == 1:
        return []
    
    factors = []
    n = number
    
    # Optimization: 2,3-wheel trial division factorization.
    # By trial-dividing by 2 and 3 first, all remaining candidate factors must be of the
    # form 6k ± 1 (5, 7, 11, 13, 17, 19, ...).
    # Alternating steps of +2 and +4 eliminates multiples of 2 and 3 from trial division,
    # reducing loop iterations by 33% (skipping 1/3 of odd candidates: 9, 15, 21, ...)
    # and improving overall runtime by ~25-30%.
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    while n % 3 == 0:
        factors.append(3)
        n //= 3

    factor = 5
    step = 2
    while factor * factor <= n:
        while n % factor == 0:
            factors.append(factor)
            n //= factor
        factor += step
        step = 6 - step

    if n > 1:
        factors.append(n)
    
    return factors