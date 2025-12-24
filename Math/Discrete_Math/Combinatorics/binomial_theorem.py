# Binomial theorem expansion
import sys
sys.path.append('..')
from combination import factorial, n_choose_r
from typing import List


def binomial_coefficient(n: int, r: int) -> int:
    """
    Calculate the binomial coefficient C(n, r).

    Parameters:
    n (int): The power to which the binomial is raised.
    r (int): The term index.

    Returns:
    int: The binomial coefficient.
    """
    return n_choose_r(n, r)


def expand_binomial(a: str, b: str, n: int) -> str:
    """
    Expand the binomial (a + b)^n using the binomial theorem.

    Parameters:
    a (str): The first term of the binomial.
    b (str): The second term of the binomial.
    n (int): The power to which the binomial is raised.

    Returns:
    str: The expanded form of the binomial.
    """
    if n < 0:
        raise ValueError("Power n must be non-negative.")
    
    result = []
    # Expand using binomial theorem: (a+b)ⁿ = Σ C(n,r) × aⁿ⁻ʳ × bʳ
    for r in range(n + 1):
        coeff = binomial_coefficient(n, r)
        term = f"{coeff}*{a}^{n - r}*{b}^{r}"
        result.append(term)
    
    return " + ".join(result)