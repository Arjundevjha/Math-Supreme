# Style Guide for how to code in the repository

This style guide outlines the coding conventions and best practices to be followed when contributing to this repository. Adhering to these guidelines will help maintain code quality, readability, and consistency across all contributions.

# Number One Principle

- Usage of the math module is not allowed, unless it is necessary for the implementation of the algorithm, and theat section has not been implemented yet. Example: math.sqrt() is not allowed, unless squareroot has not been implemented.
- Import internally whereever possible.

## General Principles
- **File Name**: Use descriptive and concise names for files and directories. Use underscores (_) to separate words (e.g., `polynomial_solver.py`).
- **Documentation**: Each script should include a header comment at the top that briefly describes its purpose (e.g., `# Finding an equation of a line given two points`). Additionally, use docstrings for functions and classes to explain their functionality.
- **Modularity**: Break down code into functions and classes to promote reusability and maintainability.
- **Version Control**: Use meaningful commit messages that describe the changes made. Follow the repository's branching strategy for feature development and bug fixes.
- **Testing**: Include tests for new features and bug fixes to ensure code reliability.
- **Code Reviews**: Collaborators must participate in code reviews to provide feedback on contributions.
- **PRs**: Use pull requests to merge code into the main branch. Ensure that PRs are well-documented and include a description of the changes made.
- **Branching**: Use feature branches for new features and bug fixes. Merge feature branches into the main branch using pull requests.

## Python Coding Conventions
- **PEP 8 Compliance**: Follow the PEP 8 style guide for Python code. This includes indentation, line length (maximum 79 characters), and spacing.
- **Imports**: Group imports into three sections: standard library imports, related third-party imports, and local application/library-specific imports. Each group should be separated by a blank line.
- **Type Hints**: Always use type hints for function parameters and return values. Use `Union[int, float]` for numeric parameters that can accept both integers and floats. Import `Union` from the `typing` module.
- **Variable Naming**: Use lowercase words separated by underscores for variable names (e.g., `total_sum`).
- **Function Naming**: Use lowercase with underscores for function names (e.g., `calculate_area`).
- **Comments**: Use inline comments to explain calculations and complex logic (e.g., `# Calculate slope (m)`). Avoid obvious comments that do not add value.
- **Error Handling**: Use exceptions to handle errors gracefully. Provide informative error messages using `ValueError` or appropriate exception types.
- **String Formatting**: Use f-strings for string formatting and interpolation (e.g., `f"y = {m}x + {b}"`).

## Class and Function Documentation
- **Docstrings**: Use triple quotes for docstrings. The first line should be a brief summary, followed by a more detailed description if necessary.
- **Parameters and Returns**: Use the following format for documenting parameters and return values:
  - `Parameters:` section listing each parameter with its description
  - `Returns:` section describing the return value with its type
- **Examples**: Include usage examples in docstrings where applicable.
- **Indentation**: Maintain consistent indentation within docstrings (use 8 spaces or 2 tabs for content within the docstring).

## Example of a Well-Documented Function

```python
from typing import Union


def linear_eqn(x1: Union[int, float], y1: Union[int, float], x2: Union[int, float], y2: Union[int, float]) -> str:
    """
    Calculate the equation of a line given two points (x1, y1) and (x2, y2).

    Parameters:
    x1, y1: Coordinates of the first point.
    x2, y2: Coordinates of the second point.

    Returns:
    str: The equation of the line in the form "y = mx + b".
    """
    if x1 == x2:
        raise ValueError("The x-coordinates cannot be the same (vertical line).")

    # Calculate slope (m)
    m = (y2 - y1) / (x2 - x1)

    # Calculate y-intercept (b)
    b = y1 - m * x1

    return f"y = {m}x + {b}"
```


## Math Implementation Guidelines
- **Clarity**: Ensure that mathematical operations are clearly defined and easy to follow.
- **Efficiency**: Optimize algorithms for performance, especially for large datasets or complex calculations.
- **Precision**: Be mindful of numerical precision and rounding errors in calculations.

## How to implement math symbols
- Use standard mathematical notation where possible. For example:
  - Addition: `+`
  - Subtraction: `-`
  - Multiplication: `*` or `·`
  - Division: `/` or `÷`
  - Exponents: `**` for power operations (e.g., `x**2')
- Use parentheses to clarify the order of operations when necessary.
- For complex mathematical expressions, consider breaking them down into smaller, manageable parts for better readability.
###Example

Implementation of Sigma Function(Summation)

```python
def sigma(n: int) -> int:
    """
    Calculate the sum of the first n natural numbers.

    Parameters:
    n (int): The upper limit of the summation.

    Returns:
    int: The sum of the first n natural numbers.
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
```

## Acknowledgments
This style guide is inspired by widely accepted coding standards and best practices in the software development community. We encourage contributors to stay updated with the latest developments in coding standards and continuously improve their coding practices.

# Conclusion
By following this style guide, we can ensure that our codebase remains clean, efficient, and easy to navigate for all contributors. Thank you for your commitment to maintaining high coding standards in this repository
