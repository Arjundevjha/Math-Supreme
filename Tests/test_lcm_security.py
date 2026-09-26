import unittest
from Math.Discrete_Math.Number_Theory.lcm import compute_lcm


class TestLcmSecurity(unittest.TestCase):
    def test_compute_lcm_boolean_rejection(self):
        # Booleans inherit from int in Python, but must be rejected with TypeError
        with self.assertRaisesRegex(TypeError, "Both a and b must be integers."):
            compute_lcm(True, 5)
        with self.assertRaisesRegex(TypeError, "Both a and b must be integers."):
            compute_lcm(5, False)
        with self.assertRaisesRegex(TypeError, "Both a and b must be integers."):
            compute_lcm(True, False)

    def test_compute_lcm_invalid_types(self):
        # Non-integer types should raise TypeError
        with self.assertRaisesRegex(TypeError, "Both a and b must be integers."):
            compute_lcm("10", 5)
        with self.assertRaisesRegex(TypeError, "Both a and b must be integers."):
            compute_lcm(10, "5")
        with self.assertRaisesRegex(TypeError, "Both a and b must be integers."):
            compute_lcm(10.5, 2)
        with self.assertRaisesRegex(TypeError, "Both a and b must be integers."):
            compute_lcm(None, 5)


if __name__ == "__main__":
    unittest.main()
