import os
import sys
import pytest
import cmath

# Add root directory to path
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from Math.Algebra.Polynomials.cubic_formula import cubic_formula  # noqa: E402

def verify_roots(expected_roots, actual_roots):
    """
    Helper function to verify roots, accounting for multiplicity and floating point inaccuracies.
    Ensures that each expected root has exactly one corresponding actual root.
    """
    roots_list = list(actual_roots)
    for expected in expected_roots:
        matched = False
        for i, root in enumerate(roots_list):
            if cmath.isclose(expected, root, rel_tol=1e-9, abs_tol=1e-9):
                roots_list.pop(i)
                matched = True
                break
        assert matched, f"Expected root {expected} not found. Remaining unmatched actual roots: {roots_list}"
    assert len(roots_list) == 0, f"Unexpected extra roots found: {roots_list}"
def assert_roots_match(expected_roots, actual_roots):
    assert len(expected_roots) == len(actual_roots), f"Expected {len(expected_roots)} roots, got {len(actual_roots)}"

    # Check that each expected root is matched exactly once by an actual root
    matched_indices = set()
    for expected in expected_roots:
        found_match = False
        for i, actual in enumerate(actual_roots):
            if i not in matched_indices and cmath.isclose(expected, actual, rel_tol=1e-9, abs_tol=1e-9):
                matched_indices.add(i)
                found_match = True
                break
        assert found_match, f"Expected root {expected} not found in {actual_roots}"

def test_cubic_formula_real_roots():
    # Equation: x^3 - 6x^2 + 11x - 6 = 0
    # Roots: 1, 2, 3
    roots = cubic_formula(1, -6, 11, -6)
    expected_roots = [1, 2, 3]

    verify_roots(expected_roots, roots)
    assert_roots_match(expected_roots, roots)

def test_cubic_formula_complex_roots():
    # Equation: x^3 - 1 = 0
    # Roots: 1, -1/2 + sqrt(3)i/2, -1/2 - sqrt(3)i/2
    roots = cubic_formula(1, 0, 0, -1)

    expected_roots = [
        1,
        complex(-0.5, cmath.sqrt(3).real / 2),
        complex(-0.5, -cmath.sqrt(3).real / 2)
    ]

    verify_roots(expected_roots, roots)
    assert_roots_match(expected_roots, roots)

def test_cubic_formula_zero_roots():
    # Equation: x^3 = 0
    # Roots: 0, 0, 0
    roots = cubic_formula(1, 0, 0, 0)
    expected_roots = [0, 0, 0]

    verify_roots(expected_roots, roots)
    assert_roots_match(expected_roots, roots)

def test_cubic_formula_value_error():
    # a = 0 should raise ValueError
    with pytest.raises(ValueError, match="Coefficient 'a' cannot be zero for a cubic equation."):
        cubic_formula(0, 1, 1, 1)


def test_cubic_formula_floats():
    # Equation: 2.5x^3 - 7.5x^2 + 2.5x + 2.5 = 0
    # Equivalent to x^3 - 3x^2 + x + 1 = 0
    # Roots: 1, 1+sqrt(2), 1-sqrt(2)
    roots = cubic_formula(2.5, -7.5, 2.5, 2.5)
    expected_roots = [
        1,
        1 + cmath.sqrt(2).real,
        1 - cmath.sqrt(2).real
    ]

    for expected in expected_roots:
        assert any(cmath.isclose(expected, root, rel_tol=1e-9, abs_tol=1e-9) for root in roots)

def test_cubic_formula_negative_a():
    # Equation: -x^3 + 6x^2 - 11x + 6 = 0
    # Roots: 1, 2, 3
    roots = cubic_formula(-1, 6, -11, 6)
    expected_roots = [1, 2, 3]

    for expected in expected_roots:
        assert any(cmath.isclose(expected, root, rel_tol=1e-9, abs_tol=1e-9) for root in roots)

def test_cubic_formula_triple_root():
    # Equation: x^3 - 3x^2 + 3x - 1 = 0
    # Root: 1, 1, 1
    roots = cubic_formula(1, -3, 3, -1)

    # We should have exactly 3 roots close to 1
    assert len(roots) == 3
    for root in roots:
        assert cmath.isclose(1, root, rel_tol=1e-9, abs_tol=1e-9)
def test_cubic_formula_double_root():
    # Equation: x^3 - 3x + 2 = 0
    # Roots: 1, 1, -2
    roots = cubic_formula(1, 0, -3, 2)
    expected_roots = [1, 1, -2]

    verify_roots(expected_roots, roots)

def test_cubic_formula_float_coefficients():
    # Equation: 2.5x^3 - 7.5x^2 + 7.5x - 2.5 = 0
    # Roots: 1, 1, 1
    roots = cubic_formula(2.5, -7.5, 7.5, -2.5)
    expected_roots = [1, 1, 1]

    verify_roots(expected_roots, roots)

if __name__ == '__main__':
    pytest.main([__file__])
