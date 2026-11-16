"""Calculate the 3D cross product of two vectors."""
from typing import List, Sequence, Union

from Math.Linear_Algebra.Vectors.magnitude import validate_vector


def cross_product(
    u: Sequence[Union[int, float]], v: Sequence[Union[int, float]]
) -> List[float]:
    """
    Calculate the cross product u x v of two 3-dimensional vectors.

    Parameters:
    u (Sequence[Union[int, float]]): First 3D vector.
    v (Sequence[Union[int, float]]): Second 3D vector.

    Returns:
    List[float]: 3D vector orthogonal to both u and v.
    """
    u_vec = validate_vector("u", u)
    v_vec = validate_vector("v", v)
    if len(u_vec) != 3 or len(v_vec) != 3:
        raise ValueError("Cross product is only defined for 3D vectors.")

    return [
        u_vec[1] * v_vec[2] - u_vec[2] * v_vec[1],
        u_vec[2] * v_vec[0] - u_vec[0] * v_vec[2],
        u_vec[0] * v_vec[1] - u_vec[1] * v_vec[0],
    ]
