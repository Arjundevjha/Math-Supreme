"""Classic related rates problems in differential calculus."""
from typing import Union

from Math.Numerical_Methods.Functions.nth_root.nth_root import nth_root
from Math.utils.math_utils import PI

Number = Union[int, float]


def _validate_num(name: str, val: Number) -> float:
    """Validate that val is a finite int or float (excluding bool)."""
    if isinstance(val, bool) or not isinstance(val, (int, float)):
        raise TypeError(f"{name} must be a numeric int or float.")
    if not -float("inf") < val < float("inf"):
        raise ValueError(f"{name} must be a finite number.")
    return float(val)


def circle_area_rate(radius: Number, dr_dt: Number) -> float:
    """
    Calculate rate of change of circle area: dA/dt = 2 * pi * r * (dr/dt).

    Parameters:
    radius (Number): Current radius r (>= 0).
    dr_dt (Number): Rate of change of radius.

    Returns:
    float: Rate of change of area dA/dt.
    """
    r = _validate_num("radius", radius)
    rate_r = _validate_num("dr_dt", dr_dt)
    if r < 0:
        raise ValueError("radius must be non-negative.")
    return 2.0 * PI * r * rate_r


def sphere_volume_rate(radius: Number, dr_dt: Number) -> float:
    """
    Calculate rate of change of sphere volume: dV/dt = 4 * pi * r^2 * dr/dt.

    Parameters:
    radius (Number): Current radius r (>= 0).
    dr_dt (Number): Rate of change of radius.

    Returns:
    float: Rate of change of volume dV/dt.
    """
    r = _validate_num("radius", radius)
    rate_r = _validate_num("dr_dt", dr_dt)
    if r < 0:
        raise ValueError("radius must be non-negative.")
    return 4.0 * PI * r * r * rate_r


def ladder_sliding_rate(
    ladder_length: Number, base_dist: Number, dx_dt: Number
) -> float:
    """
    Calculate dy/dt for a sliding ladder: dy/dt = -(x / y) * (dx/dt).

    Parameters:
    ladder_length (Number): Fixed ladder length L (> 0).
    base_dist (Number): Distance of ladder base from wall x (0 <= x < L).
    dx_dt (Number): Horizontal speed of base away from wall.

    Returns:
    float: Vertical speed dy/dt of the top of the ladder.
    """
    length = _validate_num("ladder_length", ladder_length)
    x = _validate_num("base_dist", base_dist)
    rate_x = _validate_num("dx_dt", dx_dt)
    if length <= 0:
        raise ValueError("ladder_length must be positive.")
    if x < 0 or x >= length:
        raise ValueError("base_dist must satisfy 0 <= base_dist < length.")

    y = float(nth_root(length * length - x * x, 2))
    return -(x / y) * rate_x


def cone_volume_rate(
    radius: Number, height: Number, dr_dt: Number, dh_dt: Number
) -> float:
    """
    Calculate dV/dt for a right circular cone V = (1/3) * pi * r^2 * h.

    Parameters:
    radius (Number): Current radius r (>= 0).
    height (Number): Current height h (>= 0).
    dr_dt (Number): Rate of change of radius.
    dh_dt (Number): Rate of change of height.

    Returns:
    float: Rate of change of cone volume dV/dt.
    """
    r = _validate_num("radius", radius)
    h = _validate_num("height", height)
    rate_r = _validate_num("dr_dt", dr_dt)
    rate_h = _validate_num("dh_dt", dh_dt)
    if r < 0 or h < 0:
        raise ValueError("radius and height must be non-negative.")
    return (PI / 3.0) * (2.0 * r * h * rate_r + r * r * rate_h)
