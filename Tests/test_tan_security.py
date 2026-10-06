import unittest
from unittest.mock import patch
from Math.Geometry.Trigonometry.Trig_Functions.tan import tangent


class TestTangentSecurity(unittest.TestCase):
    def test_tangent_invalid_types(self):
        # Non-numeric types should raise TypeError
        with self.assertRaises(TypeError):
            tangent("1.57")
        with self.assertRaises(TypeError):
            tangent(None)
        with self.assertRaises(TypeError):
            tangent([1.57])

        # Booleans should raise TypeError
        with self.assertRaises(TypeError):
            tangent(True)
        with self.assertRaises(TypeError):
            tangent(False)

    @patch("Math.Geometry.Trigonometry.Trig_Functions.tan.cosine_taylor", return_value=0.0)
    def test_tangent_division_by_zero(self, mock_cosine):
        # When cos(x) = 0, tangent should raise ValueError instead of unhandled ZeroDivisionError
        with self.assertRaisesRegex(ValueError, r"Tangent is undefined for angles where cos\(x\) = 0\."):
            tangent(1.5707963267948966)


if __name__ == "__main__":
    unittest.main()
