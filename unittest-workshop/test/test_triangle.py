from email.policy import default
import unittest

from shapes.triangle import Triangle
from shapes.shape import Shape


class TestTriangle(unittest.TestCase):

    default_Triangle = Triangle(1, 2, 60)  # also right,third length ~ 1.73205
    equilateral_Triangle = Triangle(1, 1, 60)

    '''
    Define all the tests you wish to write below

    Functions:

    Think about:
        - Have I covered all the lines that need to be covered ?
        - Are my tests thorough enough to cover all edge cases ?
        - What kind of assertions are needed to cover my tests ?
        - My initial coverage is too high for not having done nothing (61%!).
        Does that make sense? If not what is the reason behind that?

        Feel free to copy and amend tests from test_square or test_circle :-)

        Triangle calculator for cross reference: https://www.calculator.net/triangle-calculator.html
    '''

    def test_area(self):
        self.assertAlmostEqual(
            self.default_Triangle.area(), 0.8660, places=3
        )

    def test_perimeter(self):
        self.assertAlmostEqual(
            self.default_Triangle.perimeter(), 4.73205, places=3
        )

    def test_right(self):
        self.assertTrue(
            self.default_Triangle.isRight()
        )

    def test_equilateral(self):
        self.assertTrue(
            self.equilateral_Triangle.isEquilateral()
        )

    def test_create_square_negative_length(self):
        with self.assertRaises(ValueError):
            Triangle(-1, 1, 40)

    def test_create_square_negative_angle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 1, -40)
