"""Quotient rule for differentiation using dense polynomial lists."""
from typing import List, Sequence, Tuple, Union

from Math.Algebra.Polynomials.polynomial import (
    multiply_polynomials,
    subtract_polynomials,
    trim_polynomial,
    validate_polynomial,
)
from .simple_diffrentiation_function import differentiate_polynomial


def quotient_rule_derivative(
    u: Sequence[Union[int, float]],
    v: Sequence[Union[int, float]],
) -> Tuple[List[Union[int, float]], List[Union[int, float]]]:
    """
    Apply the quotient rule (u / v)' = (u' * v - u * v') / v^2.

    Parameters:
    u (Sequence[Union[int, float]]): Numerator polynomial [c0, c1, ...].
    v (Sequence[Union[int, float]]): Denominator polynomial [c0, c1, ...].

    Returns:
    Tuple[List[Union[int, float]], List[Union[int, float]]]:
        A tuple (numerator_poly, denominator_poly) as dense coefficient lists.
    """
    u_list = validate_polynomial(u)
    v_list = trim_polynomial(validate_polynomial(v))
    if not v_list:
        raise ValueError("Denominator polynomial v(x) cannot be zero.")

    u_prime = differentiate_polynomial(u_list)
    v_prime = differentiate_polynomial(v_list)

    numerator = subtract_polynomials(
        multiply_polynomials(u_prime, v_list),
        multiply_polynomials(u_list, v_prime),
    )
    denominator = multiply_polynomials(v_list, v_list)
    return numerator, denominator
