# Cubic formula solver for equations of the form ax³ + bx² + cx + d = 0
from typing import Union, Tuple
from Math.Numerical_Methods.Functions.nth_root.nth_root import nth_root


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
    
    # Calculate intermediate terms
    term_1 = complex(-(b / (3 * a)))
    
    inner_term_1 = 2 * (b**3) - (9 * a * b * c) + (27 * (a**2) * d)
    inner_term_2 = inner_term_1**2 - 4 * ((b**2 - 3 * a * c)**3)
    
    # Calculate square root of inner_term_2
    if inner_term_2 >= 0:
        sqrt_val = complex(nth_root(inner_term_2, 2))
    else:
        sqrt_val = 1j * complex(nth_root(-inner_term_2, 2))

    inner_term_1 = complex(inner_term_1)

    # Calculate cube roots
    cubed_value_1 = 0.5 * (inner_term_1 + sqrt_val)
    cubed_value_2 = 0.5 * (inner_term_1 - sqrt_val)

    # Calculate multipliers
    normal_multiplier = complex(-1 / (3 * a))
    sqrt_3 = complex(nth_root(3, 2))
    complex_multiplier_1 = (1 + (1j * sqrt_3)) / complex(6 * a)
    complex_multiplier_2 = (1 + (-1j * sqrt_3)) / complex(6 * a)
    
    # Calculate the three roots using the cubic formula
    x1 = term_1 + ((cubed_value_1**(1/3)) * normal_multiplier) + ((cubed_value_2**(1/3)) * normal_multiplier)
    x2 = term_1 + ((cubed_value_1**(1/3)) * complex_multiplier_1) + ((cubed_value_2**(1/3)) * complex_multiplier_2)
    x3 = term_1 + ((cubed_value_1**(1/3)) * complex_multiplier_2) + ((cubed_value_2**(1/3)) * complex_multiplier_1)

    return (x1, x2, x3)