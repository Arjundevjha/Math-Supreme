import sys
import os
import pytest

# Add both the project root and the Math/ directory to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
math_dir = os.path.join(project_root, 'Math')

if project_root not in sys.path:
    sys.path.insert(0, project_root)
if math_dir not in sys.path:
    sys.path.insert(0, math_dir)

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
