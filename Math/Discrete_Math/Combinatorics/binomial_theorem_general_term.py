# General term of the binomial expansion
import sys
sys.path.append('..')
from combination import nCr
from typing import Union


def binomial_general_term(n: int, r: int, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Calculate the general term in the binomial expansion of (a + b)^n.

    Parameters:
    n (int): The exponent in the binomial expansion.
    r (int): The term index (0-indexed).
    a (Union[int, float]): The first term in the binomial.
    b (Union[int, float]): The second term in the binomial.

    Returns:
    Union[int, float]: The (r+1)th term in the expansion.
    """
    if r < 0 or r > n:
        raise ValueError("Invalid values for n and r. r must be between 0 and n.")
    
    # Calculate general term using formula: T_(r+1) = C(n,r) × a^(n-r) × b^r
    nCr = nCr(n, r)
    return nCr * (a ** (n - r)) * (b ** r)