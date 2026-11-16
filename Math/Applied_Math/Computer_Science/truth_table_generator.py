"""Truth table generator for boolean functions."""
from typing import Callable, Dict, List, Sequence


def generate_truth_table(
    variables: Sequence[str], expr_func: Callable[..., bool]
) -> List[Dict[str, bool]]:
    """
    Generate all rows of a truth table for a boolean callable.

    Parameters:
    variables (Sequence[str]): Variable names (1 to 12).
    expr_func (Callable[..., bool]): Function taking len(variables) booleans.

    Returns:
    List[Dict[str, bool]]: List of row dictionaries mapping each variable
        name and 'result' to boolean values.
    """
    if not isinstance(variables, (list, tuple)):
        raise TypeError("variables must be a list or tuple of strings.")
    if not variables:
        raise ValueError("variables must not be empty.")
    if len(variables) > 12:
        raise ValueError("Maximum of 12 variables supported.")
    if not callable(expr_func):
        raise TypeError("expr_func must be callable.")

    for var in variables:
        if not isinstance(var, str) or not var.strip():
            raise ValueError("Each variable name must be a non-empty string.")
    if len(set(variables)) != len(variables):
        raise ValueError("Variable names must be unique.")

    n = len(variables)
    rows: List[Dict[str, bool]] = []
    for mask in range(1 << n):
        values = [bool((mask >> (n - 1 - i)) & 1) for i in range(n)]
        res = bool(expr_func(*values))
        row = dict(zip(variables, values))
        row["result"] = res
        rows.append(row)
    return rows


def format_truth_table(
    variables: Sequence[str], expr_func: Callable[..., bool]
) -> str:
    """
    Format a truth table as a human-readable ASCII table.

    Parameters:
    variables (Sequence[str]): Variable names (1 to 12).
    expr_func (Callable[..., bool]): Function taking len(variables) booleans.

    Returns:
    str: Formatted truth table string.
    """
    rows = generate_truth_table(variables, expr_func)
    headers = list(variables) + ["result"]
    lines = [" | ".join(headers), " | ".join("-" * len(h) for h in headers)]
    for row in rows:
        lines.append(
            " | ".join(str(int(row[h])).ljust(len(h)) for h in headers)
        )
    return "\n".join(lines)
