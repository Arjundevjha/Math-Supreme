"""Calculate the dot product (inner product) of two vectors."""
from typing import Sequence, Union

from Math.Linear_Algebra.Vectors.magnitude import validate_vector


def dot_product(
    u: Sequence[Union[int, float]], v: Sequence[Union[int, float]]
) -> float:
    """
    Calculate the dot product of two equal-length vectors u and v.

    Parameters:
    u (Sequence[Union[int, float]]): First vector.
    v (Sequence[Union[int, float]]): Second vector.

    Returns:
    float: Scalar dot product u . v.
    """
    u_vec = validate_vector("u", u)
    v_vec = validate_vector("v", v)
    if len(u_vec) != len(v_vec):
        raise ValueError("Vectors must have the same dimension.")
    return sum(a * b for a, b in zip(u_vec, v_vec))
