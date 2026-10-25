import unittest
from unittest.mock import patch
from Math.Geometry.Trigonometry.Trig_Functions.secant import secant


class TestSecantSecurity(unittest.TestCase):
    def test_secant_invalid_types(self):
        # Non-numeric types should raise TypeError
        with self.assertRaises(TypeError):
            secant("1.0")
        with self.assertRaises(TypeError):
            secant(None)
        with self.assertRaises(TypeError):
            secant([1.0])

        # Booleans should raise TypeError
        with self.assertRaises(TypeError):
            secant(True)
        with self.assertRaises(TypeError):
            secant(False)

    @patch(
        "Math.Geometry.Trigonometry.Trig_Functions.secant.cosine_taylor",
        return_value=0.0,
    )
    def test_secant_division_by_zero(self, mock_cosine):
        # When cos(x) = 0, secant should raise ValueError
        with self.assertRaisesRegex(
            ValueError, r"Secant is undefined for angles where cos\(x\) = 0\."
        ):
            secant(1.5707963267948966)


if __name__ == "__main__":
    unittest.main()
