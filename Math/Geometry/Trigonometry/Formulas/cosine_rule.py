# Cosine rule (Law of Cosines) for finding sides and angles of triangles
from typing import Union


def factorial(n: int) -> int:
    """Calculate factorial of n."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def cosine_taylor(radians: Union[int, float]) -> float:
    """Calculate cosine using Taylor series."""
    cos_value = 1
    sign = 1
    for idx in range(2, 100, 2):
        fact = factorial(idx)
        if sign % 2 == 0:
            cos_value += radians**idx / fact
        else:
            cos_value -= radians**idx / fact
        sign += 1
    return cos_value


def sqrt_newton(x: Union[int, float], precision: float = 0.000001) -> float:
    """Calculate square root using Newton's method."""
    if x < 0:
        raise ValueError("Cannot calculate square root of negative number.")
    if x == 0:
        return 0
    
    guess = x / 2
    while abs(guess * guess - x) > precision:
        guess = (guess + x / guess) / 2
    return guess


def arccos_series(x: Union[int, float]) -> float:
    """Calculate arccos using series approximation."""
    if x < -1 or x > 1:
        raise ValueError("arccos is only defined for values between -1 and 1.")
    
    # Use arccos(x) = π/2 - arcsin(x) approximation
    # For simplicity, use polynomial approximation
    pi = 3.14159265358979323846
    
    if x == 1:
        return 0
    if x == -1:
        return pi
    
    # Polynomial approximation for arccos
    result = pi / 2 - x - (x**3) / 6 - (3 * x**5) / 40
    return result


def cosine_rule_for_side(a: Union[int, float], b: Union[int, float], angle_C_radians: Union[int, float]) -> float:
    """
    Calculate the length of side c using the cosine rule: c² = a² + b² - 2ab×cos(C).

    Parameters:
    a (Union[int, float]): Length of side a.
    b (Union[int, float]): Length of side b.
    angle_C_radians (Union[int, float]): Angle C in radians (opposite to side c).

    Returns:
    float: The length of side c.
    """
    if a <= 0 or b <= 0:
        raise ValueError("Side lengths must be positive.")
    
    # Calculate side using cosine rule: c = √(a² + b² - 2ab×cos(C))
    c_squared = a**2 + b**2 - 2 * a * b * cosine_taylor(angle_C_radians)
    return sqrt_newton(c_squared)


def cosine_rule_for_angle(a: Union[int, float], b: Union[int, float], c: Union[int, float]) -> float:
    """
    Calculate angle C using the cosine rule: cos(C) = (a² + b² - c²) / (2ab).

    Parameters:
    a (Union[int, float]): Length of side a.
    b (Union[int, float]): Length of side b.
    c (Union[int, float]): Length of side c (opposite to angle C).

    Returns:
    float: Angle C in radians.
    """
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("All side lengths must be positive.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid triangle: the sum of any two sides must be greater than the third side.")
    
    # Calculate angle using cosine rule: C = arccos((a² + b² - c²) / (2ab))
    cos_C = (a**2 + b**2 - c**2) / (2 * a * b)
    return arccos_series(cos_C)
