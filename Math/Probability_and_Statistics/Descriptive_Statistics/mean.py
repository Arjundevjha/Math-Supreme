# Calculate the mean (average) of a list of numbers
from typing import List, Sequence, Union


def mean(data: Sequence[Union[int, float]]) -> float:
    """
    Calculate the mean (average) of a list of numbers.

    Parameters:
    data (Sequence[Union[int, float]]): A list or tuple of numerical values (integers or floats).

    Returns:
    float: The mean of the provided numbers.
    """
    # Security: Validate input sequence type and element types
    if not isinstance(data, (list, tuple)):
        raise TypeError("Data must be a list or tuple of numbers.")
    if any(isinstance(x, bool) or not isinstance(x, (int, float)) for x in data):
        raise TypeError("All elements in data must be integers or floats.")

    if not data:
        return 0.0

    # Calculate mean using formula: mean = sum / count
    total = sum(data)
    count = len(data)

    return total / count
