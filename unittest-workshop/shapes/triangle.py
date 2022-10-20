import math
from .shape import Shape


class Triangle(Shape):
    def __init__(self, a, b, C: float) -> None:
        '''
        Define a triangle by providing the length of two
        sides, and the angle between them
        
        Constructor arguments:
            a : Length of side a
            b : Length of side b
            C : Angle between side a and b
        Attributes:
            self._a : Length of side a
            self._b : Length of side b
            self._c : Length of side c (Calculated during constuction)
            self._A : Angle between sides _b and _c
            self._B : Angle between sides _a and _c
            self._C : Angle between sides _a and _b
        Methods:
            self.area
            self.perimeter
            self.isRight
            self.isEquilateral
            
        '''
        if any(n < 0 for n in [a, b]):
            raise ValueError('The lengths cannot be negative')
        if (0 >= C) or (C >= 180):
            raise ValueError('Angle must be between 0 and 180')

        self._a = float(a)
        self._b = float(b)
        self._C = float(C)

        # a^2 = b^2 + c^2 − 2bccosA
        self._c = round(
            math.sqrt(
                self._a*self._a + self._b * self._b -
                2 * self._a * self._b * math.cos(
                    math.radians(self._C)
                )
            ), 15
        )

        self._A = math.degrees(
            math.acos(
                (self._b ** 2 + self._c ** 2 -
                 self._a ** 2) / (2 * self._b * self._c)
            ))

        self._B = 180 - self._A - self._C

    def area(self) -> float:
        '''
        Returns the area of two triangle.

                Parameters: -
                Returns:
                        area (float): Area of the triangle
        '''        
        s = (self._a + self._b + self._c) / 2
        return math.sqrt(s*(s-self._a)*(s-self._b)*(s-self._c))

    def perimeter(self) -> float:
        '''
        Returns the sum the anles of the triangle.

                Parameters: -
                Returns:
                        perimeter (float): Sum of all the sides of the triangle
        '''        
        return self._a + self._b + self._c

    def isRight(self):
        return True in [round(x, 4) == 90 for x in [self._A, self._B, self._C]]

    def isEquilateral(self):
        angles = [round(x, 4)
                  for x in (self._A, self._B, self._C)]
        return angles[0] == angles[1] == angles[2] == 60
