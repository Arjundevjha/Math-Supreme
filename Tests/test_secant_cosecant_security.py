import unittest
import pytest
from Math.Geometry.Trigonometry.Trig_Functions.cosecant import cosecant
from Math.Geometry.Trigonometry.Trig_Functions.secant import secant


class TestSecantCosecantSecurity(unittest.TestCase):
    def test_secant_invalid_types(self):
        # Non-numeric types should raise TypeError
        with pytest.raises(TypeError, match=r"radians must be a numeric int or float\."):
            secant("1.57")
        with pytest.raises(TypeError, match=r"radians must be a numeric int or float\."):
            secant(None)
        with pytest.raises(TypeError, match=r"radians must be a numeric int or float\."):
            secant([1.57])

        # Booleans should raise TypeError
        with pytest.raises(TypeError, match=r"radians must be a numeric int or float\."):
            secant(True)
        with pytest.raises(TypeError, match=r"radians must be a numeric int or float\."):
            secant(False)

    def test_cosecant_invalid_types(self):
        # Non-numeric types should raise TypeError
        with pytest.raises(TypeError, match=r"radians must be a numeric int or float\."):
            cosecant("1.57")
        with pytest.raises(TypeError, match=r"radians must be a numeric int or float\."):
            cosecant(None)
        with pytest.raises(TypeError, match=r"radians must be a numeric int or float\."):
            cosecant([1.57])

        # Booleans should raise TypeError
        with pytest.raises(TypeError, match=r"radians must be a numeric int or float\."):
            cosecant(True)
        with pytest.raises(TypeError, match=r"radians must be a numeric int or float\."):
            cosecant(False)


if __name__ == "__main__":
    unittest.main()
