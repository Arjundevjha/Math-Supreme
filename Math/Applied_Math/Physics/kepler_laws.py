"""Kepler's laws of planetary motion and orbital mechanics."""
from typing import Union

from Math.Applied_Math.Physics.newton_laws_force import (
    _validate_finite,
)
from Math.Numerical_Methods.Functions.nth_root.nth_root import nth_root
from Math.utils.math_utils import PI

_G_CONST = 6.67430e-11


def _validate_positive(name: str, value: Union[int, float]) -> float:
    """Validate that a value is a finite positive int or float."""
    val = _validate_finite(name, value)
    if val <= 0:
        raise ValueError(f"{name} must be greater than zero.")
    return val


def orbital_period(
    semi_major_axis: Union[int, float],
    central_mass: Union[int, float],
    g_const: Union[int, float] = _G_CONST,
) -> float:
    """
    Calculate orbital period using Kepler's third law: T = 2*pi*sqrt(a^3/GM).

    Parameters:
    semi_major_axis (Union[int, float]): Semi-major axis a (m > 0).
    central_mass (Union[int, float]): Mass of central body M (kg > 0).
    g_const (Union[int, float]): Gravitational constant G (> 0).

    Returns:
    float: Orbital period T (s).
    """
    a = _validate_positive("semi_major_axis", semi_major_axis)
    m = _validate_positive("central_mass", central_mass)
    g = _validate_positive("g_const", g_const)
    return 2.0 * PI * float(nth_root((a * a * a) / (g * m), 2))


def semi_major_axis_from_period(
    period: Union[int, float],
    central_mass: Union[int, float],
    g_const: Union[int, float] = _G_CONST,
) -> float:
    """
    Calculate semi-major axis from orbital period: a = (G*M*T^2 / 4pi^2)^(1/3).

    Parameters:
    period (Union[int, float]): Orbital period T (s > 0).
    central_mass (Union[int, float]): Mass of central body M (kg > 0).
    g_const (Union[int, float]): Gravitational constant G (> 0).

    Returns:
    float: Semi-major axis a (m).
    """
    t = _validate_positive("period", period)
    m = _validate_positive("central_mass", central_mass)
    g = _validate_positive("g_const", g_const)
    a_cubed = (g * m * t * t) / (4.0 * PI * PI)
    return float(nth_root(a_cubed, 3))


def vis_viva_speed(
    radius: Union[int, float],
    semi_major_axis: Union[int, float],
    central_mass: Union[int, float],
    g_const: Union[int, float] = _G_CONST,
) -> float:
    """
    Calculate orbital speed via vis-viva equation: v = sqrt(GM*(2/r - 1/a)).

    Parameters:
    radius (Union[int, float]): Current orbital radius r (m > 0).
    semi_major_axis (Union[int, float]): Semi-major axis a (m > 0).
    central_mass (Union[int, float]): Mass of central body M (kg > 0).
    g_const (Union[int, float]): Gravitational constant G (> 0).

    Returns:
    float: Orbital speed v (m/s).
    """
    r = _validate_positive("radius", radius)
    a = _validate_positive("semi_major_axis", semi_major_axis)
    m = _validate_positive("central_mass", central_mass)
    g = _validate_positive("g_const", g_const)
    term = 2.0 / r - 1.0 / a
    if term < 0:
        raise ValueError("Invalid elliptical orbit: radius exceeds 2 * a.")
    if term == 0:
        return 0.0
    return float(nth_root(g * m * term, 2))


def areal_velocity(
    angular_momentum: Union[int, float], mass: Union[int, float]
) -> float:
    """
    Calculate areal velocity dA/dt = L / (2 * m) (Kepler's second law).

    Parameters:
    angular_momentum (Union[int, float]): Orbital angular momentum L.
    mass (Union[int, float]): Orbiting body mass m (kg > 0).

    Returns:
    float: Constant areal velocity (m^2/s).
    """
    if isinstance(angular_momentum, bool) or not isinstance(
        angular_momentum, (int, float)
    ):
        raise TypeError("angular_momentum must be a numeric int or float.")
    if not -float("inf") < angular_momentum < float("inf"):
        raise ValueError("angular_momentum must be a finite number.")
    m = _validate_positive("mass", mass)
    return float(angular_momentum) / (2.0 * m)
