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
    if number <= 0:
        raise ValueError("Number must be positive.")
    if number == 1:
        return []
    
    factors = []
    n = number
    
    # Find all prime factors by trial division

    # Check for factor 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    factor = 3
    # Check for odd factors
    while n > 1:
        while n % factor == 0:
            factors.append(factor)
            n //= factor
        factor += 2
    
    return factors