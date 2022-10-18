import unittest
import math

from shapes.circle import Circle
from shapes.shape import Shape


class TestCircle(unittest.TestCase):
    def test_circle_instance_of_shape(self):
        circle = Circle(10)
        self.assertIsInstance(circle, Shape)

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
