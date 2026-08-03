# AGENTS.md - AI Agent Operational Guide for Math-Supreme

Welcome to **Math-Supreme**! This document provides operational guidelines, repository architecture, coding standards, and workflow instructions for AI agents working in this codebase.

---

## 1. Core Principles & Non-Negotiable Rules

1. **No Standard `math` Module Usage**:
   - Using Python's built-in `math` module is **prohibited**, unless strictly necessary for an algorithm whose internal implementation in `Math/` has not yet been built.
   - Example: `math.sqrt()` is forbidden if custom square root / power functions are available or implemented within `Math/`.

2. **Internal Imports First**:
   - Always import internal custom implementations from the `Math/` directory whenever available.
   - Example: Reuse internal polynomial, calculus, trig, or discrete math functions rather than third-party or standard library helpers.

3. **Strict Test Verification**:
   - After making any code changes or adding new math modules, always run `pytest` to ensure 100% test suite pass rate across all existing module tests.

---

## 2. Repository Architecture

```text
Math-Supreme/
├── Math/                          # Primary source code package
│   ├── Algebra/                   # Polynomials, Linear Equations, etc.
│   ├── Calculus/                  # Differentiation, Integration, Limits, etc.
│   ├── DiscreteMath/              # Combinatorics, Number Theory, Sequences, etc.
│   ├── Geometry/                  # Euclidean, Analytic, Trigonometry, etc.
│   ├── LinearAlgebra/             # Vectors, Matrices, Transformations
│   ├── NumericalMethods/          # Pi Algorithms, Euler's number, Root Finding, etc.
│   ├── ProbabilityandStatistics/ # Descriptive Stats, Distributions, Axioms
│   └── AppliedMath/               # Physics, Finance, Engineering
├── Tests/                         # Comprehensive pytest test suite
│   ├── test_Algebra.py
│   ├── test_Calculus.py
│   ├── test_DiscreteMath.py
│   └── ...
├── Style_Guide.MD                 # Repository style guide and coding standards
├── README.md                      # Feature expansion roadmap & progress tracker
└── AGENTS.md                      # AI Agent Operational Guide (this file)
```

---

## 3. Coding Standards & Conventions

- **File & Function Naming**: Use `snake_case` for filenames and functions (e.g., `linear_eqn.py`, `calculate_area()`).
- **Header Comment**: Every script must start with a top-level header comment describing its purpose (e.g., `# Calculating slope of a line`).
- **Type Annotations**:
  - All function signatures **must** include type hints for parameters and return types.
  - Use `typing.Union[int, float]` for numeric inputs accepting both integers and floating point numbers.
- **Docstrings**:
  - Multi-line triple-quoted docstrings.
  - Must include `Parameters:` and `Returns:` sections.
  - Include usage `Examples:` where applicable.
- **PEP 8**: Follow PEP 8 guidelines (79-character line limit, clean spacing, clear error messages with `ValueError`).

---

## 4. Example Function Template

```python
# Calculating equation of a line given two points
from typing import Union


def linear_eqn(
    x1: Union[int, float],
    y1: Union[int, float],
    x2: Union[int, float],
    y2: Union[int, float]
) -> str:
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

---

## 5. Development & Testing Workflow

1. **Check Roadmap**: Consult `README.md` to identify implemented vs. pending features.
2. **Implement Feature**: Place code in the appropriate `Math/<Category>/` subfolder adhering to `Style_Guide.MD`.
3. **Add Tests**: Create or update matching test files in `Tests/` directory (`test_<feature>.py`).
4. **Run Verification**: Execute `pytest` in terminal to confirm all tests pass cleanly.
