import unittest
from shapes.triangle import Triangle


class TestTriangle(unittest.TestCase):
    
    # Sample triangles from the document
    right_Triangle = Triangle(1, 2, 60)  # length c ~ 1.73205, area ~0.86603
    equilateral_Triangle = Triangle(1, 1, 60) # length c ~ 1, area ~0.43301

    '''
    Define all the tests you wish to write below

    Think about:
        - Have I covered all the lines that need to be covered ?
        - Are my tests thorough enough to cover all edge cases ?
        - What kind of assertions are needed to cover my tests ?
        Does that make sense? If not what is the reason behind that?

        Feel free to copy and amend tests from test_square or test_circle :-)

        Triangle calculator for cross reference: https://www.calculator.net/triangle-calculator.html
    '''
    def test_line_30(self):
        # Hint: Test that the code fails for negative lengths:
        # Check the assertRaises example from the README.
        # To create a Triangle with side lengths 2,1 and an angle of 45 between them use the following
        # my_triangle = Triangle(2, 1, 45)
        pass
    
    def test_line_32(self): 
        # Hint: Test that the code fails for invalid angles:
        # Check the assertRaises example from the README.
        # To create a Triangle with side lengths 2,1 and an angle of 45 between them use the following
        # my_triangle = Triangle(2, 1, 45)
        pass
    
    def test_triangle_area(self):
        # Hint: To use the area method from the right triangle try the following example:
        # self.right_Triangle.area()
        # Hint: Check the assertAlmostEqual example from the README
        pass
    
    def test_triangle_perimeter(self):
        # Hint: Check the assertAlmostEqual or assertEqual examples from the README
        pass
    
    def test_triangle_isRight(self):
        # Hint: Check the assertTrue example from the README
        pass
    
    def test_triangle_isEquilateral(self):
        # Hint: Check the assertTrue example from the README
        pass
