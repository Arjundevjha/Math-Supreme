import unittest
from Math.Geometry.Euclidean_Geometry.pythagoras_theorem import pythagorean_theorem


class TestPythagorasSecurity(unittest.TestCase):
    def test_pythagorean_theorem_boolean_type_rejection(self):
        # Booleans inherit from int in Python, but must be rejected with TypeError
        with self.assertRaises(TypeError):
            pythagorean_theorem(True, 4)
        with self.assertRaises(TypeError):
            pythagorean_theorem(3, False)
        with self.assertRaises(TypeError):
            pythagorean_theorem(True, False)

    def test_pythagorean_theorem_invalid_types(self):
        # Non-numeric types should raise TypeError
        with self.assertRaises(TypeError):
            pythagorean_theorem("3", 4)
        with self.assertRaises(TypeError):
            pythagorean_theorem(3, "4")
        with self.assertRaises(TypeError):
            pythagorean_theorem([3], 4)
        with self.assertRaises(TypeError):
            pythagorean_theorem(3, None)


if __name__ == "__main__":
    unittest.main()
