import unittest
from Math.Geometry.Analytic_Geometry.distance_formula import distance_formula


class TestDistanceFormulaSecurity(unittest.TestCase):
    def test_distance_formula_boolean_type_rejection(self):
        # Booleans inherit from int in Python, but must be rejected with TypeError
        with self.assertRaises(TypeError):
            distance_formula(True, 0, 0, 0)
        with self.assertRaises(TypeError):
            distance_formula(0, False, 0, 0)
        with self.assertRaises(TypeError):
            distance_formula(0, 0, True, 0)
        with self.assertRaises(TypeError):
            distance_formula(0, 0, 0, False)

    def test_distance_formula_invalid_types(self):
        # Non-numeric types should raise TypeError
        with self.assertRaises(TypeError):
            distance_formula("1", 0, 0, 0)
        with self.assertRaises(TypeError):
            distance_formula(0, [2], 0, 0)
        with self.assertRaises(TypeError):
            distance_formula(0, 0, None, 0)
        with self.assertRaises(TypeError):
            distance_formula(0, 0, 0, "4")

    def test_distance_formula_upper_bound_limit(self):
        # Coordinates with magnitude > 1e300 should raise ValueError to prevent DoS/OverflowError
        with self.assertRaisesRegex(ValueError, "Coordinates exceed maximum allowed magnitude limit of 1e300."):
            distance_formula(1e301, 0, 0, 0)
        with self.assertRaisesRegex(ValueError, "Coordinates exceed maximum allowed magnitude limit of 1e300."):
            distance_formula(0, -1e301, 0, 0)
        with self.assertRaisesRegex(ValueError, "Coordinates exceed maximum allowed magnitude limit of 1e300."):
            distance_formula(0, 0, 1e301, 0)
        with self.assertRaisesRegex(ValueError, "Coordinates exceed maximum allowed magnitude limit of 1e300."):
            distance_formula(0, 0, 0, -1e301)


if __name__ == "__main__":
    unittest.main()
