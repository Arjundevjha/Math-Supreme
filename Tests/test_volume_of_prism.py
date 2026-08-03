import unittest
from Math.Geometry.Euclidean_Geometry.Volume.prism import volume_of_prism

class TestVolumeOfPrism(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(volume_of_prism(10, 5), 50.0)

    def test_positive_floats(self):
        self.assertAlmostEqual(volume_of_prism(2.5, 4.2), 10.5, places=7)

    def test_mixed_types(self):
        self.assertAlmostEqual(volume_of_prism(2, 4.5), 9.0, places=7)
        self.assertAlmostEqual(volume_of_prism(2.5, 4), 10.0, places=7)

    def test_zero_dimensions(self):
        self.assertEqual(volume_of_prism(0, 5), 0)
        self.assertEqual(volume_of_prism(5, 0), 0)
        self.assertEqual(volume_of_prism(0, 0), 0)

    def test_negative_dimensions_raise_value_error(self):
        with self.assertRaises(ValueError):
            volume_of_prism(-1, 5)
        with self.assertRaises(ValueError):
            volume_of_prism(5, -1)
        with self.assertRaises(ValueError):
            volume_of_prism(-1, -1)

if __name__ == '__main__':
    unittest.main()
