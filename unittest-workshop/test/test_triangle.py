from email.policy import default
import unittest

from shapes.triangle import Triangle
from shapes.shape import Shape


class TestTriangle(unittest.TestCase):

    default_Triangle = Triangle(1, 2, 60)  # also right, scalene
    equilateral_Triangle = Triangle(1, 1, 60)
    isosceles_Triangle = Triangle(1, 1, 30)

    def test_square_instance_of_shape(self):
        self.assertIsInstance(Triangle(1, 1, 1), Shape)

    def test_create_square_negative_length(self):
        with self.assertRaises(ValueError):
            Triangle(-1, 1, 40)

    def test_create_square_negative_angle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 1, -40)

    def test_create_square_exceed_angle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 1, 181)

    def test_create_square_zero_angle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 1, 0)

    def test_positive_length_c(self):
        self.assertAlmostEqual(
            self.default_Triangle.length_c(), 1.7320, places=3
        )

    def test_area(self):
        self.assertAlmostEqual(
            self.default_Triangle.area(), 0.8660, places=3
        )

    def test_angle_B(self):
        self.assertAlmostEqual(
            self.default_Triangle.angle_B(), 90, places=3
        )

    def test_angle_A(self):
        self.assertAlmostEqual(
            self.default_Triangle.angle_A(), 30, places=3
        )

    def test_right(self):
        self.assertTrue(
            self.default_Triangle.isRight()
        )

    def test_equilateral(self):
        self.assertTrue(
            self.equilateral_Triangle.isEquilateral()
        )

    def test_isosceles_1(self):
        self.assertTrue(
            self.isosceles_Triangle.isIsosceles()
        )

    def test_isosceles_2(self):
        self.assertTrue(self.equilateral_Triangle.isIsosceles())

    def test_scalene(self):
        self.assertTrue(self.default_Triangle.isScalene())
