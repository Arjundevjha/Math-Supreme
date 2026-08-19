import math



from Math.Geometry.Analytic_Geometry.distance_formula import distance_formula

class TestDistanceFormula:
    def test_same_point(self):
        assert math.isclose(distance_formula(1, 1, 1, 1), 0.0)
        assert math.isclose(distance_formula(0, 0, 0, 0), 0.0)
        assert math.isclose(distance_formula(-5, 3.5, -5, 3.5), 0.0)

    def test_horizontal_line(self):
        assert math.isclose(distance_formula(1, 2, 5, 2), 4.0)
        assert math.isclose(distance_formula(5, 2, 1, 2), 4.0)
        assert math.isclose(distance_formula(-3, 0, 2, 0), 5.0)

    def test_vertical_line(self):
        assert math.isclose(distance_formula(3, 1, 3, 4), 3.0)
        assert math.isclose(distance_formula(3, 4, 3, 1), 3.0)
        assert math.isclose(distance_formula(0, -2, 0, 5), 7.0)

    def test_pythagorean_triples(self):
        assert math.isclose(distance_formula(0, 0, 3, 4), 5.0)
        assert math.isclose(distance_formula(0, 0, 5, 12), 13.0)
        assert math.isclose(distance_formula(1, 1, 4, 5), 5.0)
        assert math.isclose(distance_formula(-1, -1, -4, -5), 5.0)
        assert math.isclose(distance_formula(2, 3, -4, 11), 10.0)

    def test_floating_points(self):
        assert math.isclose(distance_formula(1.5, 2.5, 4.5, 6.5), 5.0)
        assert math.isclose(distance_formula(0.1, 0.2, 0.4, 0.6), 0.5)

    def test_negative_coordinates(self):
        assert math.isclose(distance_formula(-3, -4, 0, 0), 5.0)
        assert math.isclose(distance_formula(-1, 2, 2, -2), 5.0)
