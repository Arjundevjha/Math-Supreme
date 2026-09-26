# Least Common Multiple (LCM) calculation
from Math.Discrete_Math.Number_Theory.gcd import compute_gcd


def compute_lcm(a: int, b: int) -> int:
    """
    Compute the Least Common Multiple (LCM) of two numbers.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The LCM of a and b.
    """
    # Security: Validate input parameter types to prevent type confusion
    if not isinstance(a, int) or isinstance(a, bool) or not isinstance(b, int) or isinstance(b, bool):
        raise TypeError("Both a and b must be integers.")

    if a <= 0 or b <= 0:
        raise ValueError("Both numbers must be positive.")

    # Calculate LCM using GCD: compute GCD first to avoid large intermediate products
    gcd_val = compute_gcd(a, b)
    return (a // gcd_val) * b
