import unittest
from Math.Discrete_Math.Number_Theory.lcm import compute_lcm


class TestLCMSecurity(unittest.TestCase):
    def test_lcm_boolean_rejection(self):
        # Booleans inherit from int in Python, but must be rejected with TypeError
        with self.assertRaises(TypeError):
            compute_lcm(True, 5)
        with self.assertRaises(TypeError):
            compute_lcm(5, False)
        with self.assertRaises(TypeError):
            compute_lcm(True, False)

    def test_lcm_invalid_types(self):
        # Non-integer types should raise TypeError
        with self.assertRaises(TypeError):
            compute_lcm("10", 5)
        with self.assertRaises(TypeError):
            compute_lcm(10, "5")
        with self.assertRaises(TypeError):
            compute_lcm(10.5, 2)
        with self.assertRaises(TypeError):
            compute_lcm(None, 5)

    def test_lcm_upper_bound_limit(self):
        # Test that inputs > 10**100 raise ValueError to prevent DoS via CPU/memory resource exhaustion
        with self.assertRaisesRegex(ValueError, r"Inputs exceed maximum limit of 10\^100\."):
            compute_lcm(10**100 + 1, 5)
        with self.assertRaisesRegex(ValueError, r"Inputs exceed maximum limit of 10\^100\."):
            compute_lcm(5, 10**100 + 1)

    def test_lcm_boundary_value(self):
        # Boundary value 10**100 should pass without raising limit error
        val = compute_lcm(10**100, 10**100)
        self.assertEqual(val, 10**100)

    def test_lcm_non_positive_inputs(self):
        # Non-positive numbers should raise ValueError
        with self.assertRaisesRegex(ValueError, "Both numbers must be positive."):
            compute_lcm(0, 5)
        with self.assertRaisesRegex(ValueError, "Both numbers must be positive."):
            compute_lcm(-5, 5)


if __name__ == "__main__":
    unittest.main()
