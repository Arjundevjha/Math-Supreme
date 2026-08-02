from typing import Union

def factorial(n: int) -> int:
    """Calculate factorial of n."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers.")
    if n > 1000:
        raise ValueError(
            "Factorial calculation limit exceeded (maximum allowed is 1000)."
        )
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def cosine_taylor(radians: Union[int, float]) -> float:
    """Calculate cosine using Taylor series iteratively."""
    cos_value = 1.0
    term = 1.0
    radians_sq = radians * radians

    for idx in range(2, 100, 2):
        term *= -radians_sq / (idx * (idx - 1))
        cos_value += term

    return cos_value

def sine_taylor(radians: Union[int, float]) -> float:
    """Calculate sine using Taylor series iteratively."""
    sine_value = float(radians)
    term = float(radians)
    radians_sq = float(radians * radians)

    for idx in range(3, 100, 2):
        term *= -radians_sq / ((idx - 1) * idx)
        sine_value += term

    return sine_value
