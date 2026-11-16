"""Calculate mechanical work, kinetic/potential energy, and power."""
from typing import Union

from Math.Applied_Math.Physics.newton_laws_force import (
    _validate_finite,
)
from Math.Geometry.Trigonometry.Trig_Functions.cosine import cosine
from Math.utils.math_utils import PI

_STANDARD_GRAVITY = 9.80665


def work_done(
    force_val: Union[int, float],
    displacement: Union[int, float],
    angle_degrees: Union[int, float] = 0.0,
) -> float:
    """
    Calculate mechanical work W = F * d * cos(theta).

    Parameters:
    force_val (Union[int, float]): Applied force magnitude (N).
    displacement (Union[int, float]): Displacement magnitude (m).
    angle_degrees (Union[int, float]): Angle between force and motion (deg).

    Returns:
    float: Work done (J).
    """
    f_val = _validate_finite("force_val", force_val)
    d = _validate_finite("displacement", displacement)
    theta = _validate_finite("angle_degrees", angle_degrees)
    radians = theta * PI / 180.0
    return f_val * d * cosine(radians)


def kinetic_energy(
    mass: Union[int, float], velocity: Union[int, float]
) -> float:
    """
    Calculate translational kinetic energy KE = 0.5 * m * v^2.

    Parameters:
    mass (Union[int, float]): Mass (kg), must be non-negative.
    velocity (Union[int, float]): Velocity (m/s).

    Returns:
    float: Kinetic energy (J).
    """
    m = _validate_finite("mass", mass)
    v = _validate_finite("velocity", velocity)
    if m < 0:
        raise ValueError("mass must be non-negative.")
    return 0.5 * m * v * v


def potential_energy(
    mass: Union[int, float],
    height: Union[int, float],
    gravity: Union[int, float] = _STANDARD_GRAVITY,
) -> float:
    """
    Calculate gravitational potential energy PE = m * g * h.

    Parameters:
    mass (Union[int, float]): Mass (kg), must be non-negative.
    height (Union[int, float]): Height relative to reference (m).
    gravity (Union[int, float]): Gravitational acceleration (m/s^2).

    Returns:
    float: Gravitational potential energy (J).
    """
    m = _validate_finite("mass", mass)
    h = _validate_finite("height", height)
    g = _validate_finite("gravity", gravity)
    if m < 0 or g < 0:
        raise ValueError("mass and gravity must be non-negative.")
    return m * g * h


def elastic_potential_energy(
    spring_constant: Union[int, float], displacement: Union[int, float]
) -> float:
    """
    Calculate elastic potential energy stored in a spring U = 0.5 * k * x^2.

    Parameters:
    spring_constant (Union[int, float]): Spring stiffness k (N/m >= 0).
    displacement (Union[int, float]): Displacement from equilibrium (m).

    Returns:
    float: Elastic potential energy (J).
    """
    k = _validate_finite("spring_constant", spring_constant)
    x = _validate_finite("displacement", displacement)
    if k < 0:
        raise ValueError("spring_constant must be non-negative.")
    return 0.5 * k * x * x


def power_from_work(
    work: Union[int, float], time: Union[int, float]
) -> float:
    """
    Calculate average power P = W / t.

    Parameters:
    work (Union[int, float]): Work done (J).
    time (Union[int, float]): Elapsed time (s), must be positive.

    Returns:
    float: Average power (W).
    """
    w = _validate_finite("work", work)
    t = _validate_finite("time", time)
    if t <= 0:
        raise ValueError("time must be greater than zero.")
    return w / t


def power_from_force_velocity(
    force_val: Union[int, float],
    velocity: Union[int, float],
    angle_degrees: Union[int, float] = 0.0,
) -> float:
    """
    Calculate instantaneous power P = F * v * cos(theta).

    Parameters:
    force_val (Union[int, float]): Force magnitude (N).
    velocity (Union[int, float]): Velocity magnitude (m/s).
    angle_degrees (Union[int, float]): Angle between force and velocity (deg).

    Returns:
    float: Instantaneous power (W).
    """
    f_val = _validate_finite("force_val", force_val)
    v = _validate_finite("velocity", velocity)
    theta = _validate_finite("angle_degrees", angle_degrees)
    radians = theta * PI / 180.0
    return f_val * v * cosine(radians)
