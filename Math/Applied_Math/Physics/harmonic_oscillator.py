"""Simple harmonic oscillator equations for springs and pendulums."""
from typing import Union

from Math.Applied_Math.Physics.newton_laws_force import (
    _validate_finite,
)
from Math.Geometry.Trigonometry.Trig_Functions.cosine import cosine
from Math.Geometry.Trigonometry.Trig_Functions.sine import sine
from Math.Numerical_Methods.Functions.nth_root.nth_root import nth_root
from Math.utils.math_utils import PI

_STANDARD_GRAVITY = 9.80665


def angular_frequency(
    spring_constant: Union[int, float], mass: Union[int, float]
) -> float:
    """
    Calculate angular frequency omega = sqrt(k / m) for a mass-spring system.

    Parameters:
    spring_constant (Union[int, float]): Spring stiffness k (N/m > 0).
    mass (Union[int, float]): Mass m (kg > 0).

    Returns:
    float: Angular frequency (rad/s).
    """
    k = _validate_finite("spring_constant", spring_constant)
    m = _validate_finite("mass", mass)
    if k <= 0 or m <= 0:
        raise ValueError("spring_constant and mass must be positive.")
    return float(nth_root(k / m, 2))


def period_spring(
    mass: Union[int, float], spring_constant: Union[int, float]
) -> float:
    """
    Calculate oscillation period T = 2 * pi * sqrt(m / k) for a spring.

    Parameters:
    mass (Union[int, float]): Mass m (kg > 0).
    spring_constant (Union[int, float]): Spring stiffness k (N/m > 0).

    Returns:
    float: Oscillation period (s).
    """
    m = _validate_finite("mass", mass)
    k = _validate_finite("spring_constant", spring_constant)
    if m <= 0 or k <= 0:
        raise ValueError("mass and spring_constant must be positive.")
    return 2.0 * PI * float(nth_root(m / k, 2))


def period_pendulum(
    length: Union[int, float], gravity: Union[int, float] = _STANDARD_GRAVITY
) -> float:
    """
    Calculate small-angle simple pendulum period T = 2 * pi * sqrt(L / g).

    Parameters:
    length (Union[int, float]): Pendulum length L (m > 0).
    gravity (Union[int, float]): Gravitational acceleration g (m/s^2 > 0).

    Returns:
    float: Pendulum period (s).
    """
    length_val = _validate_finite("length", length)
    g = _validate_finite("gravity", gravity)
    if length_val <= 0 or g <= 0:
        raise ValueError("length and gravity must be positive.")
    return 2.0 * PI * float(nth_root(length_val / g, 2))


def shm_displacement(
    amplitude: Union[int, float],
    angular_freq: Union[int, float],
    time: Union[int, float],
    phase: Union[int, float] = 0.0,
) -> float:
    """
    Calculate SHM displacement x(t) = A * cos(omega * t + phi).

    Parameters:
    amplitude (Union[int, float]): Oscillation amplitude A (m >= 0).
    angular_freq (Union[int, float]): Angular frequency omega (rad/s >= 0).
    time (Union[int, float]): Time t (s >= 0).
    phase (Union[int, float]): Phase constant phi (rad).

    Returns:
    float: Displacement x(t) (m).
    """
    amp = _validate_finite("amplitude", amplitude)
    omega = _validate_finite("angular_freq", angular_freq)
    t = _validate_finite("time", time)
    phi = _validate_finite("phase", phase)
    if amp < 0 or omega < 0 or t < 0:
        raise ValueError("amplitude, angular_freq, and time must be >= 0.")
    return amp * cosine(omega * t + phi)


def shm_velocity(
    amplitude: Union[int, float],
    angular_freq: Union[int, float],
    time: Union[int, float],
    phase: Union[int, float] = 0.0,
) -> float:
    """
    Calculate SHM velocity v(t) = -A * omega * sin(omega * t + phi).

    Parameters:
    amplitude (Union[int, float]): Oscillation amplitude A (m >= 0).
    angular_freq (Union[int, float]): Angular frequency omega (rad/s >= 0).
    time (Union[int, float]): Time t (s >= 0).
    phase (Union[int, float]): Phase constant phi (rad).

    Returns:
    float: Velocity v(t) (m/s).
    """
    amp = _validate_finite("amplitude", amplitude)
    omega = _validate_finite("angular_freq", angular_freq)
    t = _validate_finite("time", time)
    phi = _validate_finite("phase", phase)
    if amp < 0 or omega < 0 or t < 0:
        raise ValueError("amplitude, angular_freq, and time must be >= 0.")
    return -amp * omega * sine(omega * t + phi)


def shm_acceleration(
    amplitude: Union[int, float],
    angular_freq: Union[int, float],
    time: Union[int, float],
    phase: Union[int, float] = 0.0,
) -> float:
    """
    Calculate SHM acceleration a(t) = -A * omega^2 * cos(omega * t + phi).

    Parameters:
    amplitude (Union[int, float]): Oscillation amplitude A (m >= 0).
    angular_freq (Union[int, float]): Angular frequency omega (rad/s >= 0).
    time (Union[int, float]): Time t (s >= 0).
    phase (Union[int, float]): Phase constant phi (rad).

    Returns:
    float: Acceleration a(t) (m/s^2).
    """
    amp = _validate_finite("amplitude", amplitude)
    omega = _validate_finite("angular_freq", angular_freq)
    t = _validate_finite("time", time)
    phi = _validate_finite("phase", phase)
    if amp < 0 or omega < 0 or t < 0:
        raise ValueError("amplitude, angular_freq, and time must be >= 0.")
    return -amp * omega * omega * cosine(omega * t + phi)


def shm_total_energy(
    spring_constant: Union[int, float], amplitude: Union[int, float]
) -> float:
    """
    Calculate total mechanical energy of a harmonic oscillator E = 0.5*k*A^2.

    Parameters:
    spring_constant (Union[int, float]): Spring stiffness k (N/m >= 0).
    amplitude (Union[int, float]): Oscillation amplitude A (m >= 0).

    Returns:
    float: Total mechanical energy (J).
    """
    k = _validate_finite("spring_constant", spring_constant)
    amp = _validate_finite("amplitude", amplitude)
    if k < 0 or amp < 0:
        raise ValueError("spring_constant and amplitude must be >= 0.")
    return 0.5 * k * amp * amp
