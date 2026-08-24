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
    if a <= 0 or b <= 0:
        raise ValueError("Both numbers must be positive.")

    while b != 0:
        a, b = b, a % b

    return a
