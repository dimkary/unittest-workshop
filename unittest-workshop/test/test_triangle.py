import unittest
from shapes.triangle import Triangle


class TestTriangle(unittest.TestCase):
    
    # Sample triangles from the document
    right_Triangle = Triangle(1, 2, 60)  # third length ~ 1.73205
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
