import unittest

from shapes.square import Square
from shapes.shape import Shape


class TestSquare(unittest.TestCase):

    def test_create_square_negative_length(self):
        with self.assertRaises(ValueError):
            square = Square(-1)

    def test_square_instance_of_shape(self):
        square = Square(10)
        self.assertIsInstance(square, Shape)

    def test_area(self):
        square = Square(10)
        area = square.area()
        self.assertEqual(area, 100)

    def test_perimeter(self):
        square = Square(10)
        perimeter = square.perimeter()
        self.assertEqual(perimeter, 40)

    def test_diagonal_negative(self):
        square = Square(10)
        diagonal = square.diagonal()
        self.assertNotEqual(diagonal, 14.142135623731)

    def test_diagonal_positive(self):
        square = Square(10)
        diagonal = square.diagonal()
        self.assertAlmostEqual(diagonal, 14.1421, places=4)
