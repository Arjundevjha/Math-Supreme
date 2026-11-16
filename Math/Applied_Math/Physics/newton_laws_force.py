"""Calculate forces, weight, normal force, friction, and gravity."""
from typing import Union

from Math.Geometry.Trigonometry.Trig_Functions.cosine import cosine
from Math.utils.math_utils import PI

_STANDARD_GRAVITY = 9.80665
_G_CONST = 6.67430e-11


def _validate_finite(name: str, value: Union[int, float]) -> float:
    """Validate that a value is a finite int or float (excluding bool)."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a numeric int or float.")
    if not -float("inf") < value < float("inf"):
        raise ValueError(f"{name} must be a finite number.")
    return float(value)


def force(
    mass: Union[int, float], acceleration: Union[int, float]
) -> float:
    """
    Calculate net force using Newton's second law (F = m * a).

    Parameters:
    mass (Union[int, float]): Mass of the object (kg), must be non-negative.
    acceleration (Union[int, float]): Acceleration (m/s^2).

    Returns:
    float: Net force (N).
    """
    m = _validate_finite("mass", mass)
    a = _validate_finite("acceleration", acceleration)
    if m < 0:
        raise ValueError("mass must be non-negative.")
    return m * a


def acceleration_from_force(
    force_val: Union[int, float], mass: Union[int, float]
) -> float:
    """
    Calculate acceleration from net force and mass (a = F / m).

    Parameters:
    force_val (Union[int, float]): Net force (N).
    mass (Union[int, float]): Mass of the object (kg), must be positive.

    Returns:
    float: Acceleration (m/s^2).
    """
    f_val = _validate_finite("force_val", force_val)
    m = _validate_finite("mass", mass)
    if m <= 0:
        raise ValueError("mass must be greater than zero.")
    return f_val / m


def weight(
    mass: Union[int, float], gravity: Union[int, float] = _STANDARD_GRAVITY
) -> float:
    """
    Calculate gravitational weight (W = m * g).

    Parameters:
    mass (Union[int, float]): Mass (kg), must be non-negative.
    gravity (Union[int, float]): Gravitational acceleration (m/s^2).

    Returns:
    float: Weight (N).
    """
    m = _validate_finite("mass", mass)
    g = _validate_finite("gravity", gravity)
    if m < 0 or g < 0:
        raise ValueError("mass and gravity must be non-negative.")
    return m * g


def normal_force_incline(
    mass: Union[int, float],
    angle_degrees: Union[int, float],
    gravity: Union[int, float] = _STANDARD_GRAVITY,
) -> float:
    """
    Calculate normal force on an inclined plane (N = m * g * cos(theta)).

    Parameters:
    mass (Union[int, float]): Mass (kg), must be non-negative.
    angle_degrees (Union[int, float]): Incline angle in degrees [0, 90].
    gravity (Union[int, float]): Gravitational acceleration (m/s^2).

    Returns:
    float: Normal force (N).
    """
    m = _validate_finite("mass", mass)
    theta = _validate_finite("angle_degrees", angle_degrees)
    g = _validate_finite("gravity", gravity)
    if m < 0 or g < 0:
        raise ValueError("mass and gravity must be non-negative.")
    if theta < 0 or theta > 90:
        raise ValueError("angle_degrees must be between 0 and 90.")
    radians = theta * PI / 180.0
    return m * g * cosine(radians)


def friction_force(
    coefficient: Union[int, float], normal_force: Union[int, float]
) -> float:
    """
    Calculate friction force (f = mu * N).

    Parameters:
    coefficient (Union[int, float]): Coefficient of friction (mu >= 0).
    normal_force (Union[int, float]): Normal force (N >= 0).

    Returns:
    float: Friction force (N).
    """
    mu = _validate_finite("coefficient", coefficient)
    n_val = _validate_finite("normal_force", normal_force)
    if mu < 0 or n_val < 0:
        raise ValueError("coefficient and normal_force must be non-negative.")
    return mu * n_val


def gravitational_force(
    mass1: Union[int, float],
    mass2: Union[int, float],
    distance: Union[int, float],
    g_const: Union[int, float] = _G_CONST,
) -> float:
    """
    Calculate universal gravitational force F = G * m1 * m2 / r^2.

    Parameters:
    mass1 (Union[int, float]): First mass (kg), non-negative.
    mass2 (Union[int, float]): Second mass (kg), non-negative.
    distance (Union[int, float]): Separation distance r (m), positive.
    g_const (Union[int, float]): Gravitational constant G.

    Returns:
    float: Gravitational attraction force (N).
    """
    m1 = _validate_finite("mass1", mass1)
    m2 = _validate_finite("mass2", mass2)
    r = _validate_finite("distance", distance)
    g = _validate_finite("g_const", g_const)
    if m1 < 0 or m2 < 0 or g < 0:
        raise ValueError("masses and g_const must be non-negative.")
    if r <= 0:
        raise ValueError("distance must be greater than zero.")
    return g * m1 * m2 / (r * r)
