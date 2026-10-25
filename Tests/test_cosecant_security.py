import unittest
from unittest.mock import patch
from Math.Geometry.Trigonometry.Trig_Functions.cosecant import cosecant


class TestCosecantSecurity(unittest.TestCase):
    def test_cosecant_invalid_types(self):
        # Non-numeric types should raise TypeError
        with self.assertRaises(TypeError):
            cosecant("1.0")
        with self.assertRaises(TypeError):
            cosecant(None)
        with self.assertRaises(TypeError):
            cosecant([1.0])

        # Booleans should raise TypeError
        with self.assertRaises(TypeError):
            cosecant(True)
        with self.assertRaises(TypeError):
            cosecant(False)

    @patch(
        "Math.Geometry.Trigonometry.Trig_Functions.cosecant.sine_taylor",
        return_value=0.0,
    )
    def test_cosecant_division_by_zero(self, mock_sine):
        # When sin(x) = 0, cosecant should raise ValueError
        with self.assertRaisesRegex(
            ValueError, r"Cosecant is undefined for angles where sin\(x\) = 0\."
        ):
            cosecant(0.0)


if __name__ == "__main__":
    unittest.main()
