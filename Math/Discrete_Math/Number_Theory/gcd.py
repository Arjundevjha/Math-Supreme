# Greatest Common Divisor (GCD) calculation


def compute_gcd(a: int, b: int) -> int:
    """
    Compute the Greatest Common Divisor (GCD) of two numbers using the Euclidean algorithm.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The GCD of a and b.
    """
    # Security: Validate input parameter types and upper bound limit to prevent DoS via CPU resource exhaustion
    if not isinstance(a, int) or isinstance(a, bool) or not isinstance(b, int) or isinstance(b, bool):
        raise TypeError("Both a and b must be integers.")

    if a <= 0 or b <= 0:
        raise ValueError("Both numbers must be positive.")

    if a > 10**100 or b > 10**100:
        raise ValueError("Inputs exceed maximum limit of 10^100.")

    while b != 0:
        a, b = b, a % b

    return a
