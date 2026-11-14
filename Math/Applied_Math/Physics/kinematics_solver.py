"""Solve 1D constant-acceleration kinematics (SUVAT) equations."""
# pylint: disable=too-many-locals,too-many-branches,too-many-statements
from typing import Dict, Optional, Union

from Math.Numerical_Methods.Functions.nth_root.nth_root import nth_root


def _validate_num(name: str, value: Union[int, float]) -> float:
    """
    Validate that a value is a finite numeric int or float (not bool).

    Parameters:
    name (str): Parameter name for error messages.
    value (Union[int, float]): Numeric value to validate.

    Returns:
    float: Validated value as a float.
    """
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a numeric int or float.")
    if not -float("inf") < value < float("inf"):
        raise ValueError(f"{name} must be a finite number.")
    if abs(value) > 1e12:
        raise ValueError(f"{name} exceeds maximum allowed magnitude of 1e12.")
    return float(value)


def final_velocity(
    initial_velocity: Union[int, float],
    acceleration: Union[int, float],
    time: Union[int, float],
) -> float:
    """
    Calculate final velocity using v = u + a * t.

    Parameters:
    initial_velocity (Union[int, float]): Initial velocity u (m/s).
    acceleration (Union[int, float]): Constant acceleration a (m/s^2).
    time (Union[int, float]): Elapsed time t (s), must be non-negative.

    Returns:
    float: Final velocity v (m/s).

    Examples:
    >>> final_velocity(10, 2, 5)
    20.0
    """
    u = _validate_num("initial_velocity", initial_velocity)
    a = _validate_num("acceleration", acceleration)
    t = _validate_num("time", time)
    if t < 0:
        raise ValueError("time must be non-negative.")
    return u + a * t


def displacement(
    initial_velocity: Union[int, float],
    acceleration: Union[int, float],
    time: Union[int, float],
) -> float:
    """
    Calculate displacement using s = u * t + 0.5 * a * t^2.

    Parameters:
    initial_velocity (Union[int, float]): Initial velocity u (m/s).
    acceleration (Union[int, float]): Constant acceleration a (m/s^2).
    time (Union[int, float]): Elapsed time t (s), must be non-negative.

    Returns:
    float: Displacement s (m).

    Examples:
    >>> displacement(0, 9.8, 2)
    19.6
    """
    u = _validate_num("initial_velocity", initial_velocity)
    a = _validate_num("acceleration", acceleration)
    t = _validate_num("time", time)
    if t < 0:
        raise ValueError("time must be non-negative.")
    return u * t + 0.5 * a * t * t


def displacement_avg_velocity(
    initial_velocity: Union[int, float],
    final_velocity_val: Union[int, float],
    time: Union[int, float],
) -> float:
    """
    Calculate displacement using s = 0.5 * (u + v) * t.

    Parameters:
    initial_velocity (Union[int, float]): Initial velocity u (m/s).
    final_velocity_val (Union[int, float]): Final velocity v (m/s).
    time (Union[int, float]): Elapsed time t (s), must be non-negative.

    Returns:
    float: Displacement s (m).
    """
    u = _validate_num("initial_velocity", initial_velocity)
    v = _validate_num("final_velocity_val", final_velocity_val)
    t = _validate_num("time", time)
    if t < 0:
        raise ValueError("time must be non-negative.")
    return 0.5 * (u + v) * t


def final_velocity_squared(
    initial_velocity: Union[int, float],
    acceleration: Union[int, float],
    displacement_val: Union[int, float],
) -> float:
    """
    Calculate squared final velocity using v^2 = u^2 + 2 * a * s.

    Parameters:
    initial_velocity (Union[int, float]): Initial velocity u (m/s).
    acceleration (Union[int, float]): Constant acceleration a (m/s^2).
    displacement_val (Union[int, float]): Displacement s (m).

    Returns:
    float: Squared final velocity v^2 (m^2/s^2).
    """
    u = _validate_num("initial_velocity", initial_velocity)
    a = _validate_num("acceleration", acceleration)
    s = _validate_num("displacement_val", displacement_val)
    return u * u + 2.0 * a * s


def solve_kinematics(
    displacement_val: Optional[Union[int, float]] = None,
    initial_velocity: Optional[Union[int, float]] = None,
    final_velocity_val: Optional[Union[int, float]] = None,
    acceleration: Optional[Union[int, float]] = None,
    time: Optional[Union[int, float]] = None,
) -> Dict[str, float]:
    """
    Solve for all five 1D kinematics (SUVAT) variables given any three.

    Parameters:
    displacement_val (Optional[Union[int, float]]): Displacement s (m).
    initial_velocity (Optional[Union[int, float]]): Initial velocity u (m/s).
    final_velocity_val (Optional[Union[int, float]]): Final velocity v (m/s).
    acceleration (Optional[Union[int, float]]): Acceleration a (m/s^2).
    time (Optional[Union[int, float]]): Elapsed time t (s, >= 0).

    Returns:
    Dict[str, float]: Dictionary containing displacement, initial_velocity,
                      final_velocity, acceleration, and time.
    """
    s = (
        _validate_num("displacement_val", displacement_val)
        if displacement_val is not None
        else None
    )
    u = (
        _validate_num("initial_velocity", initial_velocity)
        if initial_velocity is not None
        else None
    )
    v = (
        _validate_num("final_velocity_val", final_velocity_val)
        if final_velocity_val is not None
        else None
    )
    a = (
        _validate_num("acceleration", acceleration)
        if acceleration is not None
        else None
    )
    t = _validate_num("time", time) if time is not None else None

    if t is not None and t < 0:
        raise ValueError("time must be non-negative.")

    known_count = sum(x is not None for x in (s, u, v, a, t))
    if known_count != 3:
        raise ValueError(
            "Exactly three of the five kinematics variables must be provided."
        )

    # Case 1: u, a, t known -> solve v, s
    if u is not None and a is not None and t is not None:
        v = u + a * t
        s = u * t + 0.5 * a * t * t
    # Case 2: v, a, t known -> solve u, s
    elif v is not None and a is not None and t is not None:
        u = v - a * t
        s = v * t - 0.5 * a * t * t
    # Case 3: u, v, t known -> solve a, s
    elif u is not None and v is not None and t is not None:
        if t == 0:
            if u != v:
                raise ValueError(
                    "When time is 0, initial and final velocity must match."
                )
            a = 0.0
            s = 0.0
        else:
            a = (v - u) / t
            s = 0.5 * (u + v) * t
    # Case 4: u, v, a known -> solve t, s
    elif u is not None and v is not None and a is not None:
        if a == 0:
            if u != v:
                raise ValueError(
                    "Zero acceleration requires equal initial/final velocity."
                )
            raise ValueError(
                "Time is indeterminate when a = 0 and u = v."
            )
        t = (v - u) / a
        if t < 0:
            raise ValueError("Computed time is negative for given u, v, a.")
        s = 0.5 * (u + v) * t
    # Case 5: s, u, t known -> solve a, v
    elif s is not None and u is not None and t is not None:
        if t == 0:
            if s != 0:
                raise ValueError("Non-zero displacement impossible at t = 0.")
            raise ValueError(
                "Acceleration and final velocity indeterminate at t = 0."
            )
        a = 2.0 * (s - u * t) / (t * t)
        v = u + a * t
    # Case 6: s, v, t known -> solve a, u
    elif s is not None and v is not None and t is not None:
        if t == 0:
            if s != 0:
                raise ValueError("Non-zero displacement impossible at t = 0.")
            raise ValueError(
                "Acceleration and initial velocity indeterminate at t = 0."
            )
        a = 2.0 * (v * t - s) / (t * t)
        u = v - a * t
    # Case 7: s, u, v known -> solve t, a
    elif s is not None and u is not None and v is not None:
        avg_v = 0.5 * (u + v)
        if avg_v == 0:
            if s != 0:
                raise ValueError(
                    "Non-zero displacement impossible with zero avg velocity."
                )
            raise ValueError(
                "Time and acceleration indeterminate when s = 0 and u = -v."
            )
        t = s / avg_v
        if t < 0:
            raise ValueError("Computed time is negative for given s, u, v.")
        a = (v - u) / t
    # Case 8: s, u, a known -> solve v, t
    elif s is not None and u is not None and a is not None:
        v_sq = u * u + 2.0 * a * s
        if v_sq < 0:
            raise ValueError("No real solution: u^2 + 2as < 0.")
        sqrt_v_sq = float(nth_root(v_sq, 2)) if v_sq > 0 else 0.0
        if a == 0:
            if u == 0:
                if s != 0:
                    raise ValueError("No motion possible when u = 0, a = 0.")
                raise ValueError(
                    "Time is indeterminate when s = 0, u = 0, a = 0."
                )
            t = s / u
            if t < 0:
                raise ValueError("Computed time is negative.")
            v = u
        else:
            t1 = (-u + sqrt_v_sq) / a
            t2 = (-u - sqrt_v_sq) / a
            valid_times = [cand for cand in (t1, t2) if cand >= 0]
            if not valid_times:
                raise ValueError("No non-negative time solution exists.")
            t = min(valid_times)
            v = u + a * t
    # Case 9: s, v, a known -> solve u, t
    elif s is not None and v is not None and a is not None:
        u_sq = v * v - 2.0 * a * s
        if u_sq < 0:
            raise ValueError("No real solution: v^2 - 2as < 0.")
        sqrt_u_sq = float(nth_root(u_sq, 2)) if u_sq > 0 else 0.0
        if a == 0:
            if v == 0:
                if s != 0:
                    raise ValueError("No motion possible when v = 0, a = 0.")
                raise ValueError(
                    "Time is indeterminate when s = 0, v = 0, a = 0."
                )
            t = s / v
            if t < 0:
                raise ValueError("Computed time is negative.")
            u = v
        else:
            t1 = (v - sqrt_u_sq) / a
            t2 = (v + sqrt_u_sq) / a
            valid_times = [cand for cand in (t1, t2) if cand >= 0]
            if not valid_times:
                raise ValueError("No non-negative time solution exists.")
            t = min(valid_times)
            u = v - a * t
    # Case 10: s, a, t known -> solve u, v
    elif s is not None and a is not None and t is not None:
        if t == 0:
            if s != 0:
                raise ValueError("Non-zero displacement impossible at t = 0.")
            raise ValueError(
                "Velocities are indeterminate when t = 0 and s = 0."
            )
        u = (s - 0.5 * a * t * t) / t
        v = u + a * t

    return {
        "displacement": float(s),
        "initial_velocity": float(u),
        "final_velocity": float(v),
        "acceleration": float(a),
        "time": float(t),
    }
