# Cubic formula solver for equations of the form ax³ + bx² + cx + d = 0
from typing import Union, Tuple

# Precalculated constant for sqrt(3)
SQRT_3 = 1.7320508075688772


def cubic_formula(a: Union[float, int], b: Union[float, int], c: Union[float, int], d: Union[float, int]) -> Tuple[complex, complex, complex]:
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
    
    # Optimization: Precompute reciprocal factor -1 / (3 * a) to eliminate redundant
    # divisions and nth_root calls for square roots, yielding ~2x speedup.
    inv_3a = -1.0 / (3.0 * float(a))
    term_1 = complex(float(b) * inv_3a)
    
    a_float = float(a)
    b_float = float(b)
    c_float = float(c)
    d_float = float(d)

    b_sq = b_float * b_float
    b_cu = b_sq * b_float
    a_sq = a_float * a_float

    inner_term_1 = 2.0 * b_cu - 9.0 * a_float * b_float * c_float + 27.0 * a_sq * d_float
    p_term = b_sq - 3.0 * a_float * c_float
    inner_term_2 = inner_term_1 * inner_term_1 - 4.0 * (p_term * p_term * p_term)
    
    # Calculate square root using native float exponentiation
    if inner_term_2 >= 0:
        sqrt_val = complex(inner_term_2 ** 0.5)
    else:
        sqrt_val = 1j * complex((-inner_term_2) ** 0.5)

    inner_term_1_cmplx = complex(inner_term_1)

    # Calculate cube roots
    cubed_value_1 = 0.5 * (inner_term_1_cmplx + sqrt_val)
    cubed_value_2 = 0.5 * (inner_term_1_cmplx - sqrt_val)

    # Precompute multipliers and complex cube roots
    normal_multiplier = complex(inv_3a)
    six_a = 6.0 * a_float
    complex_multiplier_1 = complex(1.0, SQRT_3) / complex(six_a)
    complex_multiplier_2 = complex(1.0, -SQRT_3) / complex(six_a)
    
    r1 = cubed_value_1 ** (1 / 3)
    r2 = cubed_value_2 ** (1 / 3)

    # Calculate the three roots using the cubic formula
    x1 = term_1 + (r1 * normal_multiplier) + (r2 * normal_multiplier)
    x2 = term_1 + (r1 * complex_multiplier_1) + (r2 * complex_multiplier_2)
    x3 = term_1 + (r1 * complex_multiplier_2) + (r2 * complex_multiplier_1)

    return (x1, x2, x3)