"""Calculate vector magnitude (Euclidean norm) and validate vectors."""
from typing import List, Sequence, Union

from Math.Numerical_Methods.Functions.nth_root.nth_root import nth_root

Number = Union[int, float]


def validate_vector(name: str, vector: Sequence[Number]) -> List[float]:
    """
    Validate a numeric vector sequence and return a list of floats.

    Parameters:
    name (str): Parameter name for error messages.
    vector (Sequence[Number]): Sequence of finite numeric elements.

    Returns:
    List[float]: Validated vector as a list of floats.
    """
    if not isinstance(vector, (list, tuple)):
        raise TypeError(f"{name} must be a list or tuple.")
    if not vector:
        raise ValueError(f"{name} must not be empty.")
    if len(vector) > 10000:
        raise ValueError(f"{name} length exceeds maximum limit of 10000.")

    result: List[float] = []
    for val in vector:
        if isinstance(val, bool) or not isinstance(val, (int, float)):
            raise TypeError(f"All elements in {name} must be int or float.")
        if not -float("inf") < val < float("inf"):
            raise ValueError(f"All elements in {name} must be finite.")
        result.append(float(val))
    return result


def vector_magnitude(vector: Sequence[Number]) -> float:
    """
    Calculate the Euclidean magnitude (L2 norm) of a vector.

    Parameters:
    vector (Sequence[Number]): Non-empty numeric vector.

    Returns:
    float: Magnitude ||v|| >= 0.
    """
    vec = validate_vector("vector", vector)
    sq_sum = sum(x * x for x in vec)
    if sq_sum == 0.0:
        return 0.0
    return float(nth_root(sq_sum, 2))
