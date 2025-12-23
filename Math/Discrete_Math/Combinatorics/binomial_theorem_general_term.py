# General term of the binomial expansion of (a + b)^n is given by:
# T_n+1 = nCr * a^(n-r) * b^r
from typing import Union
from Discrete_Math.Combinatorics import Combination

    """
    Class to calculate the general term in the binomial expansion of (a + b)^n.
    The general term T_(r+1) is given by:
    T_(r+1) = nCr * a^(n-r) * b^r
    where n is the exponent, r is the term index, and nCr is the combination formula.
    """

def general_term(n: Union[int, float], r: Union[int, float], a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Calculate the general term in the binomial expansion."""
    if r < 0 or r > n:
        raise ValueError("Invalid values for n and r.")

    nCr = Combination.nCr(n, r)
    return nCr * (a ** (n - r)) * (b ** r)
    

 