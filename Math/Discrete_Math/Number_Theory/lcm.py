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
    if a <= 0 or b <= 0:
        raise ValueError("Both numbers must be positive.")

    # Calculate LCM using GCD to avoid slow prime factorization and prevent DoS for large numbers
    return (a * b) // compute_gcd(a, b)
