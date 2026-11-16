"""Calculate 2D projectile motion trajectories under uniform gravity."""
from typing import Tuple, Union

from Math.Geometry.Trigonometry.Trig_Functions.cosine import cosine
from Math.Geometry.Trigonometry.Trig_Functions.sine import sine
from Math.Numerical_Methods.Functions.nth_root.nth_root import nth_root
from Math.utils.math_utils import PI

_STANDARD_GRAVITY = 9.80665


def _validate_projectile_inputs(
    initial_velocity: Union[int, float],
    angle_degrees: Union[int, float],
    gravity: Union[int, float],
    initial_height: Union[int, float],
) -> Tuple[float, float, float, float]:
    """Validate common projectile motion parameters."""
    for name, val in [
        ("initial_velocity", initial_velocity),
        ("angle_degrees", angle_degrees),
        ("gravity", gravity),
        ("initial_height", initial_height),
    ]:
        if isinstance(val, bool) or not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be a numeric int or float.")
        if not -float("inf") < val < float("inf"):
            raise ValueError(f"{name} must be a finite number.")

    v0 = float(initial_velocity)
    angle = float(angle_degrees)
    g = float(gravity)
    y0 = float(initial_height)
    if v0 < 0:
        raise ValueError("initial_velocity must be non-negative.")
    if angle < 0 or angle > 90:
        raise ValueError("angle_degrees must be between 0 and 90.")
    if g <= 0:
        raise ValueError("gravity must be greater than zero.")
    if y0 < 0:
        raise ValueError("initial_height must be non-negative.")
    return v0, angle * PI / 180.0, g, y0


def time_of_flight(
    initial_velocity: Union[int, float],
    angle_degrees: Union[int, float],
    gravity: Union[int, float] = _STANDARD_GRAVITY,
    initial_height: Union[int, float] = 0.0,
) -> float:
    """
    Calculate total time of flight until the projectile hits y = 0.

    Parameters:
    initial_velocity (Union[int, float]): Launch speed v0 (m/s >= 0).
    angle_degrees (Union[int, float]): Launch angle in degrees [0, 90].
    gravity (Union[int, float]): Gravitational acceleration g (m/s^2 > 0).
    initial_height (Union[int, float]): Initial launch height y0 (m >= 0).

    Returns:
    float: Total time of flight (s).
    """
    v0, rad, g, y0 = _validate_projectile_inputs(
        initial_velocity, angle_degrees, gravity, initial_height
    )
    vy = v0 * sine(rad)
    disc = vy * vy + 2.0 * g * y0
    return (vy + float(nth_root(disc, 2))) / g


def max_height(
    initial_velocity: Union[int, float],
    angle_degrees: Union[int, float],
    gravity: Union[int, float] = _STANDARD_GRAVITY,
    initial_height: Union[int, float] = 0.0,
) -> float:
    """
    Calculate maximum vertical height reached by the projectile.

    Parameters:
    initial_velocity (Union[int, float]): Launch speed v0 (m/s >= 0).
    angle_degrees (Union[int, float]): Launch angle in degrees [0, 90].
    gravity (Union[int, float]): Gravitational acceleration g (m/s^2 > 0).
    initial_height (Union[int, float]): Initial launch height y0 (m >= 0).

    Returns:
    float: Maximum height above y = 0 (m).
    """
    v0, rad, g, y0 = _validate_projectile_inputs(
        initial_velocity, angle_degrees, gravity, initial_height
    )
    vy = v0 * sine(rad)
    return y0 + (vy * vy) / (2.0 * g)


def horizontal_range(
    initial_velocity: Union[int, float],
    angle_degrees: Union[int, float],
    gravity: Union[int, float] = _STANDARD_GRAVITY,
    initial_height: Union[int, float] = 0.0,
) -> float:
    """
    Calculate horizontal range covered before landing at y = 0.

    Parameters:
    initial_velocity (Union[int, float]): Launch speed v0 (m/s >= 0).
    angle_degrees (Union[int, float]): Launch angle in degrees [0, 90].
    gravity (Union[int, float]): Gravitational acceleration g (m/s^2 > 0).
    initial_height (Union[int, float]): Initial launch height y0 (m >= 0).

    Returns:
    float: Horizontal range (m).
    """
    v0, rad, _, _ = _validate_projectile_inputs(
        initial_velocity, angle_degrees, gravity, initial_height
    )
    vx = v0 * cosine(rad)
    t_flight = time_of_flight(
        initial_velocity, angle_degrees, gravity, initial_height
    )
    return vx * t_flight


def projectile_position(
    initial_velocity: Union[int, float],
    angle_degrees: Union[int, float],
    time: Union[int, float],
    gravity: Union[int, float] = _STANDARD_GRAVITY,
    initial_height: Union[int, float] = 0.0,
) -> Tuple[float, float]:
    """
    Calculate (x, y) position of a projectile at a given time t.

    Parameters:
    initial_velocity (Union[int, float]): Launch speed v0 (m/s >= 0).
    angle_degrees (Union[int, float]): Launch angle in degrees [0, 90].
    time (Union[int, float]): Elapsed time t (s >= 0).
    gravity (Union[int, float]): Gravitational acceleration g (m/s^2 > 0).
    initial_height (Union[int, float]): Initial launch height y0 (m >= 0).

    Returns:
    Tuple[float, float]: (x, y) coordinates in meters.
    """
    if isinstance(time, bool) or not isinstance(time, (int, float)):
        raise TypeError("time must be a numeric int or float.")
    if not -float("inf") < time < float("inf"):
        raise ValueError("time must be a finite number.")
    if time < 0:
        raise ValueError("time must be non-negative.")

    v0, rad, g, y0 = _validate_projectile_inputs(
        initial_velocity, angle_degrees, gravity, initial_height
    )
    t = float(time)
    x = v0 * cosine(rad) * t
    y = y0 + v0 * sine(rad) * t - 0.5 * g * t * t
    return x, y
