import os
import sys
import unittest
import math

# Fix imports
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
math_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Math"))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)
if math_dir not in sys.path:
    sys.path.insert(0, math_dir)

from Math.Geometry.Analytic_Geometry.line_equations.intersection import find_intersection

class TestFindIntersection(unittest.TestCase):
    def test_basic_intersection(self):
        # y = 2x + 1 and y = x - 1
        # 2x + 1 = x - 1 => x = -2
        # y = 2(-2) + 1 = -3
        result = find_intersection(2, 1, 1, -1)
        self.assertEqual(result, (-2, -3))

    def test_intersection_at_origin(self):
        # y = x and y = -x
        # x = -x => x = 0, y = 0
        result = find_intersection(1, 0, -1, 0)
        self.assertEqual(result, (0, 0))

    def test_parallel_lines(self):
        # y = 2x + 1 and y = 2x - 3
        result = find_intersection(2, 1, 2, -3)
        self.assertIsNone(result)

    def test_identical_lines(self):
        # y = 2x + 1 and y = 2x + 1
        # Since m1 == m2, it returns None by the current logic
        result = find_intersection(2, 1, 2, 1)
        self.assertIsNone(result)

    def test_horizontal_line_intersection(self):
        # y = 2 and y = x
        # m1=0, b1=2, m2=1, b2=0
        result = find_intersection(0, 2, 1, 0)
        self.assertEqual(result, (2, 2))

    def test_floating_point_inputs(self):
        # y = 1.5x + 2.0 and y = 0.5x + 4.0
        # 1.5x + 2.0 = 0.5x + 4.0 => 1.0x = 2.0 => x = 2.0, y = 5.0
        result = find_intersection(1.5, 2.0, 0.5, 4.0)
        self.assertIsNotNone(result)
        x, y = result
        self.assertTrue(math.isclose(x, 2.0, rel_tol=1e-9))
        self.assertTrue(math.isclose(y, 5.0, rel_tol=1e-9))

if __name__ == '__main__':
    unittest.main()
