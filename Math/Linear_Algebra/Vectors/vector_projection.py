"""Calculate the orthogonal projection of one vector onto another."""
from typing import List, Sequence, Union

from Math.Linear_Algebra.Vectors.dot_product import dot_product
from Math.Linear_Algebra.Vectors.magnitude import validate_vector


def vector_projection(
    u: Sequence[Union[int, float]], v: Sequence[Union[int, float]]
) -> List[float]:
    """
    Project vector u orthogonally onto non-zero vector v.

    Parameters:
    u (Sequence[Union[int, float]]): Vector to project.
    v (Sequence[Union[int, float]]): Target direction vector (non-zero).

    Returns:
    List[float]: Projection vector proj_v(u) = ((u . v) / (v . v)) * v.
    """
    u_vec = validate_vector("u", u)
    v_vec = validate_vector("v", v)
    if len(u_vec) != len(v_vec):
        raise ValueError("Vectors must have the same dimension.")

    v_dot_v = dot_product(v_vec, v_vec)
    if v_dot_v == 0.0:
        raise ValueError("Cannot project onto the zero vector.")

    scale = dot_product(u_vec, v_vec) / v_dot_v
    return [scale * x for x in v_vec]
