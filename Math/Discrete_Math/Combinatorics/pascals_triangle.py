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
    if num_rows > 1000:
        raise ValueError("Number of rows cannot exceed 1000 to prevent excessive resource consumption.")
    if num_rows == 0:
        return []
    
    triangle = []
    # Generate each row of Pascal's triangle
    for i in range(num_rows):
        row = [1] * (i + 1)
        for j in range(1, i):
            # Each element is the sum of the two elements above it
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
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
