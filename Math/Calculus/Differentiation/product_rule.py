"""Product rule for differentiation using dense polynomial lists."""
from typing import List, Sequence, Union

from Math.Algebra.Polynomials.polynomial import (
    add_polynomials,
    multiply_polynomials,
    validate_polynomial,
)
from .simple_diffrentiation_function import differentiate_polynomial


def product_rule_derivative(
    u: Sequence[Union[int, float]],
    v: Sequence[Union[int, float]],
) -> List[Union[int, float]]:
    """
    Apply the product rule (u * v)' = u' * v + u * v' on dense polynomials.

    Parameters:
    u (Sequence[Union[int, float]]): First polynomial [c0, c1, ...].
    v (Sequence[Union[int, float]]): Second polynomial [c0, c1, ...].

    Returns:
    List[Union[int, float]]: Dense coefficient list of (u * v)'.
    """
    u_list = validate_polynomial(u)
    v_list = validate_polynomial(v)

    u_prime = differentiate_polynomial(u_list)
    v_prime = differentiate_polynomial(v_list)

    term1 = multiply_polynomials(u_prime, v_list)
    term2 = multiply_polynomials(u_list, v_prime)
    return add_polynomials(term1, term2)
