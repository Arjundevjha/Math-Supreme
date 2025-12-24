# Quadratic formula solver for equations of the form ax² + bx + c = 0
from typing import Union, Tuple, Optional


def solve_quadratic(a: Union[int, float], b: Union[int, float], c: Union[int, float]) -> Tuple[Optional[float], Optional[float]]:
    """
    Return the real roots of ax² + bx + c = 0.

    Parameters:
    a (Union[int, float]): Coefficient of x².
    b (Union[int, float]): Coefficient of x.
    c (Union[int, float]): Constant term.

    Returns:
    Tuple[Optional[float], Optional[float]]: The two roots. Returns (None, None) if discriminant is negative.
    """
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero for a quadratic equation.")
    
    # Calculate discriminant: Δ = b² - 4ac
    discriminant = b ** 2 - 4 * a * c
    
    if discriminant < 0:
        return None, None
    
    # Calculate roots using quadratic formula: x = (-b ± √Δ) / 2a
    root1 = (-b + discriminant ** 0.5) / (2 * a)
    root2 = (-b - discriminant ** 0.5) / (2 * a)
    
    return root1, root2