import os
import sys
import pytest
import cmath

# Add root directory to path
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from Math.Algebra.Polynomials.cubic_formula import cubic_formula

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
    assert_roots_match(expected_roots, roots)

def test_cubic_formula_zero_roots():
    # Equation: x^3 = 0
    # Roots: 0, 0, 0
    roots = cubic_formula(1, 0, 0, 0)
    expected_roots = [0, 0, 0]
    assert_roots_match(expected_roots, roots)

def test_cubic_formula_value_error():
    # a = 0 should raise ValueError
    with pytest.raises(ValueError, match="Coefficient 'a' cannot be zero for a cubic equation."):
        cubic_formula(0, 1, 1, 1)

if __name__ == '__main__':
    pytest.main([__file__])
