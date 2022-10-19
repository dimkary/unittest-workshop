import unittest
from shapes.circle import Circle


class TestCircle(unittest.TestCase):

    def test_create_circle_negative_radius(self):
        with self.assertRaises(ValueError):
            circle = Circle(-1)

    def test_area(self):
        circle = Circle(2.5)
        self.assertAlmostEqual(circle.area(), 19.6349, places=3)

    def test_diameter(self):
        circle = Circle(2.5)
        self.assertEqual(circle.diameter(), 5)

    def test_circumference(self):
        circle = Circle(2.5)
        self.assertAlmostEqual(circle.circumference(), 15.7079, places=3)
