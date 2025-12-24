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
    if not data:
        return 0.0
    
    # Calculate mean using formula: mean = sum / count
    total = sum(data)
    count = len(data)
    
    return total / count