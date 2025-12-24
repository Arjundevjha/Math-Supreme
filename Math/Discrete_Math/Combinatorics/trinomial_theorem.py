# Trinomial theorem expansion
import sys
sys.path.append('..')
from combination import n_choose_r
from typing import List


def trinomial_coefficient(n: int, i: int, j: int) -> int:
    """
    Calculate the coefficient for a term in the trinomial expansion.

    Parameters:
    n (int): The exponent in the trinomial expansion.
    i (int): The power of the first term.
    j (int): The power of the second term.

    Returns:
    int: The coefficient for the term.
    """
    if i < 0 or j < 0 or i + j > n:
        return 0
    
    # Calculate coefficient using formula: C(n,i) × C(n-i,j)
    k = n - i - j
    return n_choose_r(n, i) * n_choose_r(n - i, j)


def expand_trinomial(a: str, b: str, c: str, n: int) -> str:
    """
    Expand the trinomial (a + b + c)^n using the trinomial theorem.

    Parameters:
    a (str): The first term of the trinomial.
    b (str): The second term of the trinomial.
    c (str): The third term of the trinomial.
    n (int): The power to which the trinomial is raised.

    Returns:
    str: The expanded form of the trinomial.
    """
    if n < 0:
        raise ValueError("Power n must be non-negative.")
    
    result = []
    # Expand using trinomial theorem: (a+b+c)ⁿ = Σ C(n,i)×C(n-i,j) × aⁱ × bʲ × cᵏ
    for i in range(n + 1):
        for j in range(n - i + 1):
            k = n - i - j
            coeff = trinomial_coefficient(n, i, j)
            term = f"{coeff}*{a}^{i}*{b}^{j}*{c}^{k}"
            result.append(term)
    
    return " + ".join(result)