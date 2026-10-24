import unittest
import pytest
from Math.Discrete_Math.Combinatorics.trinomial_theorem import trinomial_coefficient


class TestTrinomialTheoremSecurity(unittest.TestCase):
    def test_trinomial_coefficient_boolean_type_rejection(self):
        # Booleans inherit from int in Python, but must be rejected with TypeError
        with pytest.raises(TypeError, match=r"Inputs n, i, and j must be integers\."):
            trinomial_coefficient(True, 1, 1)
        with pytest.raises(TypeError, match=r"Inputs n, i, and j must be integers\."):
            trinomial_coefficient(5, False, 1)
        with pytest.raises(TypeError, match=r"Inputs n, i, and j must be integers\."):
            trinomial_coefficient(5, 1, True)

    def test_trinomial_coefficient_invalid_types(self):
        # Non-integer types should raise TypeError
        with pytest.raises(TypeError, match=r"Inputs n, i, and j must be integers\."):
            trinomial_coefficient("5", 1, 1)
        with pytest.raises(TypeError, match=r"Inputs n, i, and j must be integers\."):
            trinomial_coefficient(5.5, 1, 1)
        with pytest.raises(TypeError, match=r"Inputs n, i, and j must be integers\."):
            trinomial_coefficient(5, "1", 1)
        with pytest.raises(TypeError, match=r"Inputs n, i, and j must be integers\."):
            trinomial_coefficient(5, 1, None)

    def test_trinomial_coefficient_negative_n(self):
        # Negative n should raise ValueError
        with pytest.raises(ValueError, match=r"Power n must be non-negative\."):
            trinomial_coefficient(-1, 0, 0)

    def test_trinomial_coefficient_upper_bound_limit(self):
        # n > 100000 should raise ValueError to prevent DoS via CPU and memory resource exhaustion
        with pytest.raises(ValueError, match=r"n exceeds maximum limit of 100000\."):
            trinomial_coefficient(100001, 1, 1)

    def test_trinomial_coefficient_valid_boundary_value(self):
        # Boundary value n = 100000 should pass without raising limit error
        self.assertEqual(trinomial_coefficient(100000, 0, 0), 1)


if __name__ == "__main__":
    unittest.main()
