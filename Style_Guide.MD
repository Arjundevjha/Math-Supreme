# Style Guide for how to code in the repository

This style guide outlines the coding conventions and best practices to be followed when contributing to this repository. Adhering to these guidelines will help maintain code quality, readability, and consistency across all contributions.

## General Principles
- **File Name**: Use descriptive and concise names for files and directories. Use underscores (_) to separate words (e.g., `polynomial_solver.py`).
- **Documentation**: Each script should include a header comment that describes its purpose, author, and date of creation. Additionally, use docstrings for functions and classes to explain their functionality.
- **Modularity**: Break down code into functions and classes to promote reusability and maintainability.
- **Version Control**: Use meaningful commit messages that describe the changes made. Follow the repository's branching strategy for feature development and bug fixes.
- **Testing**: Include tests for new features and bug fixes to ensure code reliability.
- **Code Reviews**: Collaborators must participate in code reviews to provide feedback on contributions.

## Python Coding Conventions
- **PEP 8 Compliance**: Follow the PEP 8 style guide for Python code. This includes indentation, line length (maximum 79 characters), and spacing.
- **Imports**: Group imports into three sections: standard library imports, related third-party imports, and local application/library-specific imports. Each group should be separated by a blank line.
- **Variable Naming**: Use lowercase words separated by underscores for variable names (e.g., `total_sum`).
- **Function and Class Naming**: Use lowercase with underscores for function names (e.g., `calculate_area`) and CapitalizedWords for class names (e.g., `PolynomialSolver`).
- **Comments**: Use comments to explain complex logic. Avoid obvious comments that do not add value.
- **Error Handling**: Use exceptions to handle errors gracefully. Provide informative error messages.

## Class and Function Documentation
- **Docstrings**: Use triple quotes for docstrings. The first line should be a brief summary, followed by a more detailed description if necessary.
- **Parameters and Returns**: Clearly document function parameters and return values in the docstring.
- **Examples**: Include usage examples in docstrings where applicable.

## Example of a Well-Documented class and function

```python

class Factorial:
    """Class to compute factorials.

    Usage:
        - `Factorial.factorial(n)` for a direct static call
        - `Factorial()(n)` via an instance (calls `__call__`)
    """

    @staticmethod
    def factorial(num: int) -> int:
        if num < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        result = 1
        for idx in range(1, num + 1):
            result *= idx
        return result

    def __call__(self, num: int) -> int:
        return self.factorial(num)
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

Implementation of Sigma Function(Sumation)

```python
def sigma(n: int) -> int:
    """Calculate the sum of the first n natural numbers.
    return sum(range(1, n + 1))

    Args:
        n (int): The upper limit of the summation.
    Returns:
        int: The sum of the first n natural numbers.

    """
    just use a for loop to calculate the sum, its not worth to make a brand new function for it
    """

    total = 0
    for i in range(1, n + 1):
        total += i
    return total
```
```python
# Example implementation of factorial


class Factorial:
    """Class to compute factorials.

    Usage:
        - `Factorial.factorial(n)` for a direct static call
        - `Factorial()(n)` via an instance (calls `__call__`)
    """

    @staticmethod
    def factorial(num: int) -> int:
        if num < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        result = 1
        for idx in range(1, num + 1):
            result *= idx
        return result

    def __call__(self, num: int) -> int:
        return self.factorial(num)


```



## Acknowledgments
This style guide is inspired by widely accepted coding standards and best practices in the software development community. We encourage contributors to stay updated with the latest developments in coding standards and continuously improve their coding practices.

# Conclusion
By following this style guide, we can ensure that our codebase remains clean, efficient, and easy to navigate for all contributors. Thank you for your commitment to maintaining high coding standards in this repository
