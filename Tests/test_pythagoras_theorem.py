import math
import pytest



from Math.Geometry.Euclidean_Geometry.pythagoras_theorem import pythagorean_theorem

class TestPythagoreanTheorem:
    def test_pythagorean_triples(self):
        assert math.isclose(pythagorean_theorem(3, 4), 5.0)
        assert math.isclose(pythagorean_theorem(5, 12), 13.0)
        assert math.isclose(pythagorean_theorem(8, 15), 17.0)
        assert math.isclose(pythagorean_theorem(7, 24), 25.0)

    def test_floats(self):
        assert math.isclose(pythagorean_theorem(1.5, 2.0), 2.5)
        assert math.isclose(pythagorean_theorem(2.5, 6.0), 6.5)

    def test_non_perfect_squares(self):
        assert math.isclose(pythagorean_theorem(2, 2), math.sqrt(8))
        assert math.isclose(pythagorean_theorem(1, 1), math.sqrt(2))

    def test_zero_legs(self):
        with pytest.raises(ValueError, match="Both legs must be positive."):
            pythagorean_theorem(0, 5)
        with pytest.raises(ValueError, match="Both legs must be positive."):
            pythagorean_theorem(5, 0)
        with pytest.raises(ValueError, match="Both legs must be positive."):
            pythagorean_theorem(0, 0)

    def test_negative_legs(self):
        with pytest.raises(ValueError, match="Both legs must be positive."):
            pythagorean_theorem(-3, 4)
        with pytest.raises(ValueError, match="Both legs must be positive."):
            pythagorean_theorem(3, -4)
        with pytest.raises(ValueError, match="Both legs must be positive."):
            pythagorean_theorem(-3, -4)

if __name__ == '__main__':
    pytest.main([__file__])
