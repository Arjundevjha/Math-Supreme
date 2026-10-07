# Calculate the mean (average) of a list of numbers
from typing import List, Union


def mean(data: List[Union[int, float]]) -> float:
    """
    Calculate the mean (average) of a list of numbers.

    Parameters:
    data (List[Union[int, float]]): A list of numerical values (integers or floats).

    Returns:
    float: The mean of the provided numbers.
    """
    if not isinstance(data, (list, tuple)):
        raise TypeError("Input data must be a list or tuple.")
    if len(data) > 1000000:
        raise ValueError("Input data length exceeds maximum limit of 1,000,000.")
    for x in data:
        if isinstance(x, bool) or not isinstance(x, (int, float)):
            raise TypeError("All elements in data must be integers or floats.")

    if not data:
        return 0.0
    
    # Calculate mean using formula: mean = sum / count
    total = sum(data)
    count = len(data)
    
    return total / count
