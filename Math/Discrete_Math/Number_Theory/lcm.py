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
    # Security: Validate input parameter types and upper bound limit to prevent DoS via CPU/memory resource exhaustion
    if not isinstance(a, int) or isinstance(a, bool) or not isinstance(b, int) or isinstance(b, bool):
        raise TypeError("Both a and b must be integers.")

    if a <= 0 or b <= 0:
        raise ValueError("Both numbers must be positive.")

    if a > 10**100 or b > 10**100:
        raise ValueError("Inputs exceed maximum limit of 10^100.")

    # Calculate LCM using GCD to avoid slow prime factorization and prevent DoS for large numbers
    return (a * b) // compute_gcd(a, b)
