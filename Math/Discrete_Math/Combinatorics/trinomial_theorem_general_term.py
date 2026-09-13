# General term of the trinomial expansion
from typing import Union

from Math.Discrete_Math.Combinatorics.trinomial_theorem import (
    trinomial_coefficient,
)


def trinomial_general_term(
    n: int,
    i: int,
    j: int,
    a: Union[int, float],
    b: Union[int, float],
    c: Union[int, float],
) -> Union[int, float]:
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
    # Security: Validate input parameter types and upper bound limit to prevent DoS via CPU/memory resource exhaustion
    if (
        not isinstance(n, int)
        or isinstance(n, bool)
        or not isinstance(i, int)
        or isinstance(i, bool)
        or not isinstance(j, int)
        or isinstance(j, bool)
    ):
        raise TypeError("Power n, i, and j must be integers.")

    if (
        not isinstance(a, (int, float))
        or isinstance(a, bool)
        or not isinstance(b, (int, float))
        or isinstance(b, bool)
        or not isinstance(c, (int, float))
        or isinstance(c, bool)
    ):
        raise TypeError("Terms a, b, and c must be numeric (int or float).")

    if n < 0 or i < 0 or j < 0 or i + j > n:
        raise ValueError("Invalid values for n, i, and j.")

    if n > 1000:
        raise ValueError("Power n exceeds maximum limit of 1000.")

    k = n - i - j

    # Calculate general term using formula: T_(i,j,k) = C(n,i)×C(n-i,j) × aⁱ × bʲ × cᵏ
    coefficient = trinomial_coefficient(n, i, j)
    return coefficient * (a**i) * (b**j) * (c**k)
