"""Gram-Schmidt orthogonalization and orthonormalization."""
from typing import List, Sequence, Union

from Math.Linear_Algebra.Vectors.dot_product import dot_product
from Math.Linear_Algebra.Vectors.magnitude import (
    validate_vector,
    vector_magnitude,
)


def gram_schmidt(
    vectors: Sequence[Sequence[Union[int, float]]],
    normalize: bool = False,
) -> List[List[float]]:
    """
    Apply Gram-Schmidt orthogonalization to a list of linearly independent
    vectors.

    Parameters:
    vectors (Sequence[Sequence[Union[int, float]]]): Basis vectors.
    normalize (bool): If True, return orthonormal vectors.

    Returns:
    List[List[float]]: Orthogonal (or orthonormal) basis vectors.
    """
    if not isinstance(vectors, (list, tuple)) or not vectors:
        raise TypeError("vectors must be a non-empty list or tuple.")
    if not isinstance(normalize, bool):
        raise TypeError("normalize must be a boolean.")

    basis = [validate_vector(f"vectors[{i}]", v) for i, v in enumerate(vectors)]
    dim = len(basis[0])
    if any(len(v) != dim for v in basis):
        raise ValueError("All vectors must have the same dimension.")

    orthogonal: List[List[float]] = []
    for vec in basis:
        w = list(vec)
        for u in orthogonal:
            u_dot_u = dot_product(u, u)
            if u_dot_u > 1e-12:
                proj_scale = dot_product(w, u) / u_dot_u
                w = [wi - proj_scale * ui for wi, ui in zip(w, u)]
        if vector_magnitude(w) <= 1e-12:
            raise ValueError("Input vectors are linearly dependent.")
        if normalize:
            mag = vector_magnitude(w)
            w = [wi / mag for wi in w]
        orthogonal.append(w)

    return orthogonal
