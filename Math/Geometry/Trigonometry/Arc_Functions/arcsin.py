# Arcsine calculation using numerical approximation
from typing import Union

from Math.Geometry.Trigonometry.taylor_series import sine_taylor


def arcsin_numerical(
    sin_value: Union[int, float], precision: float = 0.0001
) -> Union[float, None]:
    """
    Calculate arcsine using numerical approximation by finding angle where sin(angle) = sin_value.

    Parameters:
    sin_value (Union[int, float]): The sine value to find the arcsine for (must be between -1 and 1).
    precision (float): The precision for the approximation (default: 0.0001).

    Returns:
    Union[float, None]: The angle in radians, or None if not found.
    """
    if sin_value < -1 or sin_value > 1:
        raise ValueError("Sine value must be between -1 and 1.")

    pi_approx = 3.14159265358979323846

    # Range searched is [0, π/2].
    # For negative sin_value where abs(0 - sin_value) >= precision,
    # sin(angle) >= 0 for angle in [0, π/2], so no angle can match within precision.
    if sin_value < 0 and abs(0.0 - float(sin_value)) >= precision:
        return None

    # Optimization: Use binary search (bisection method) over domain [0, π/2]
    # instead of linear incremental stepping (0.0001 step size).
    # Since sin(x) is strictly increasing on [0, π/2], binary search achieves
    # high-precision convergence in ~30 iterations vs ~15,700 linear iterations (~1,300x faster).
    low = 0.0
    high = pi_approx / 2.0

    # 30 iterations of bisection reduces search interval to (π/2) * (1/2)^30 ≈ 1.4e-9
    for _ in range(30):
        mid = (low + high) / 2.0
        val = sine_taylor(mid, terms=20)
        if val < sin_value:
            low = mid
        else:
            high = mid

    best_angle = (low + high) / 2.0
    calculated_sin = sine_taylor(best_angle, terms=20)

    if abs(calculated_sin - sin_value) < precision:
        return best_angle

    return None
