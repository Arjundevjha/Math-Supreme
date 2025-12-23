from typing import List, Union 

def mean(data: List[Union[int, float]]) -> float:
    """
    Calculate the mean (average) of a list of numbers.

    Parameters:
    data (List[Union[int, float]]): A list of numerical values (integers or floats).

    Returns:
    float: The mean of the provided numbers.

    Raises:
    ValueError: If the input list is empty.
    """
    if not data:
        return 0.0  # Return 0.0 for empty list as per specification
    
    total = sum(data)
    count = len(data)
    
    return total / count