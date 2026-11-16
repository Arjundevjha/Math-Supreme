"""Calculate the angle between two non-zero vectors."""
from typing import Sequence, Union

from Math.Geometry.Trigonometry.Arc_Functions.arcsin import arcsin_numerical
from Math.Linear_Algebra.Vectors.dot_product import dot_product
from Math.Linear_Algebra.Vectors.magnitude import vector_magnitude
from Math.utils.math_utils import PI


def angle_between_vectors(
    u: Sequence[Union[int, float]],
    v: Sequence[Union[int, float]],
    degrees: bool = False,
) -> float:
    """
    Calculate the angle between two non-zero vectors u and v.

    Parameters:
    u (Sequence[Union[int, float]]): First vector.
    v (Sequence[Union[int, float]]): Second vector.
    degrees (bool): If True, return angle in degrees; otherwise radians.

    Returns:
    float: Angle in [0, pi] radians (or [0, 180] degrees).
    """
    if not isinstance(degrees, bool):
        raise TypeError("degrees must be a boolean.")

    mag_u = vector_magnitude(u)
    mag_v = vector_magnitude(v)
    if mag_u == 0.0 or mag_v == 0.0:
        raise ValueError("Angle is undefined for zero-magnitude vectors.")

    cos_theta = dot_product(u, v) / (mag_u * mag_v)
    cos_theta = max(-1.0, min(1.0, cos_theta))
    radians = (PI / 2.0) - arcsin_numerical(cos_theta)
    if degrees:
        return radians * 180.0 / PI
    return radians
