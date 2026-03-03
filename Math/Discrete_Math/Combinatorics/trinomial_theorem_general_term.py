# General term of the trinomial expansion
import sys
sys.path.append('../..')
from Numerical_Methods.Functions.Factorial import factorial
from typing import Union


def trinomial_general_term(n: int, i: int, j: int, a: Union[int, float], b: Union[int, float], c: Union[int, float]) -> Union[int, float]:
    """
    Calculate the general term in the trinomial expansion of (a + b + c)^n.

    Parameters:
    n (int): The exponent in the trinomial expansion.
    i (int): The power of the first term (a).
    j (int): The power of the second term (b).
    a (Union[int, float]): The first term in the trinomial.
    b (Union[int, float]): The second term in the trinomial.
    c (Union[int, float]): The third term in the trinomial.

    Returns:
    Union[int, float]: The term T_(i,j,k) in the expansion where k = n - i - j.
    """
    if i < 0 or j < 0 or i + j > n:
        raise ValueError("Invalid values for n, i, and j.")
    
    k = n - i - j
    if k < 0:
        raise ValueError("Invalid value for k.")
    
    # Calculate general term using formula: T_(i,j,k) = n!/(i!×j!×k!) × aⁱ × bʲ × cᵏ
    n_factorial = factorial(n)
    i_factorial = factorial(i)
    j_factorial = factorial(j)
    k_factorial = factorial(k)
    
    coefficient = n_factorial // (i_factorial * j_factorial * k_factorial)
    return coefficient * (a ** i) * (b ** j) * (c ** k)