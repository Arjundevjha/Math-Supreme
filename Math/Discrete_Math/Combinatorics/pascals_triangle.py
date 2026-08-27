# Pascal's triangle generator
from typing import List


def generate_pascals_triangle(num_rows: int) -> List[List[int]]:
    """
    Generate Pascal's triangle with num_rows rows.

    Parameters:
    num_rows (int): The number of rows to generate.

    Returns:
    List[List[int]]: A list of lists representing Pascal's triangle.
    """
    if num_rows < 0:
        raise ValueError("Number of rows cannot be negative.")
    if num_rows == 0:
        return []

    
    triangle = []
    # Generate each row of Pascal's triangle.
    # Optimization: Leverage bilateral symmetry of Pascal's triangle (row[j] == row[i - j]).
    # We only compute values up to the midpoint (i // 2) and assign symmetrical entries,
    # reducing additions by ~50%.
    for i in range(num_rows):
        row = [1] * (i + 1)
        if i > 1:
            prev = triangle[-1]
            for j in range(1, (i // 2) + 1):
                val = prev[j - 1] + prev[j]
                row[j] = val
                row[i - j] = val
        triangle.append(row)
    
    return triangle


def print_pascals_triangle(triangle: List[List[int]]) -> None:
    """
    Print Pascal's triangle in a formatted way.

    Parameters:
    triangle (List[List[int]]): Pascal's triangle as a list of lists.

    Returns:
    None
    """
    if not triangle:
        return
    max_length = len(" ".join(map(str, triangle[-1])))
    for row in triangle:
        print(" ".join(map(str, row)).center(max_length))
