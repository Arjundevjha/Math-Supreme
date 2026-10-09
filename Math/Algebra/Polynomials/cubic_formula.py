"""Cubic formula solver for equations of the form ax³ + bx² + cx + d = 0."""
from typing import Union, Tuple

# Precompute sqrt(3) constant to avoid calling 100-iteration Newton-Raphson loop
# in nth_root(3, 2) on every function call.
SQRT_3 = 3.0 ** 0.5


# pylint: disable=too-many-locals
def cubic_formula(
    a: Union[float, int],
    b: Union[float, int],
    c: Union[float, int],
    d: Union[float, int],
) -> Tuple[complex, complex, complex]:
    """
    Solve cubic equations of the form ax³ + bx² + cx + d = 0 using the cubic formula.

    Parameters:
    a (Union[float, int]): Coefficient of x³.
    b (Union[float, int]): Coefficient of x².
    c (Union[float, int]): Coefficient of x.
    d (Union[float, int]): Constant term.

    Returns:
    Tuple[complex, complex, complex]: The three roots of the cubic equation.
    """
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero for a cubic equation.")

    # Optimization: Precompute reciprocal term 1 / (3a) and 1 / (6a)
    # to avoid repeated divisions across intermediate and multiplier steps.
    inv_3a = 1.0 / (3.0 * a)
    term_1 = complex(-b * inv_3a)

    b2 = b * b
    a2 = a * a
    inner_term_1 = 2.0 * (b2 * b) - (9.0 * a * b * c) + (27.0 * a2 * d)
    inner_term_2 = inner_term_1 * inner_term_1 - 4.0 * ((b2 - 3.0 * a * c) ** 3)

    # Optimization: Direct IEEE 754 float square root (inner_term_2 ** 0.5) avoids
    # running nth_root's 100-iteration Newton-Raphson loop, yielding a ~2x speedup.
    if inner_term_2 >= 0:
        sqrt_val = complex(inner_term_2 ** 0.5)
    else:
        sqrt_val = 1j * complex((-inner_term_2) ** 0.5)

    inner_term_1_cmplx = complex(inner_term_1)

    # Calculate cube roots
    cubed_value_1 = 0.5 * (inner_term_1_cmplx + sqrt_val)
    cubed_value_2 = 0.5 * (inner_term_1_cmplx - sqrt_val)

    # Optimization: Precompute complex cube roots (cb1, cb2) once instead of
    # recomputing complex exponentiations 3 times each across x1, x2, x3.
    cb1 = cubed_value_1 ** (1.0 / 3.0)
    cb2 = cubed_value_2 ** (1.0 / 3.0)

    # Calculate multipliers
    normal_multiplier = complex(-inv_3a)
    inv_6a = 0.5 * inv_3a
    complex_multiplier_1 = complex((1.0 + (1j * SQRT_3)) * inv_6a)
    complex_multiplier_2 = complex((1.0 + (-1j * SQRT_3)) * inv_6a)

    # Calculate the three roots using the cubic formula
    x1 = term_1 + (cb1 * normal_multiplier) + (cb2 * normal_multiplier)
    x2 = term_1 + (cb1 * complex_multiplier_1) + (cb2 * complex_multiplier_2)
    x3 = term_1 + (cb1 * complex_multiplier_2) + (cb2 * complex_multiplier_1)

    return (x1, x2, x3)
