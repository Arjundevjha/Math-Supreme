import pytest



from Math.Geometry.Euclidean_Geometry.Area.rectangle import area_of_rectangle

class TestAreaOfRectangle:
    def test_positive_integers(self):
        assert area_of_rectangle(5, 10) == 50.0

    def test_positive_floats(self):
        assert area_of_rectangle(5.5, 2.0) == 11.0

    def test_mixed_types(self):
        assert area_of_rectangle(4, 2.5) == 10.0

    def test_zero_dimensions(self):
        assert area_of_rectangle(0, 5) == 0.0
        assert area_of_rectangle(5, 0) == 0.0
        assert area_of_rectangle(0, 0) == 0.0

    def test_negative_length(self):
        with pytest.raises(ValueError, match="Length and width cannot be negative."):
            area_of_rectangle(-1, 5)

    def test_negative_width(self):
        with pytest.raises(ValueError, match="Length and width cannot be negative."):
            area_of_rectangle(5, -1)

    def test_negative_both(self):
        with pytest.raises(ValueError, match="Length and width cannot be negative."):
            area_of_rectangle(-5, -5)
