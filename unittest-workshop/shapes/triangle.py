import math
from .shape import Shape
from decimal import Decimal


class Triangle(Shape):
    def __init__(self, a, b, C: float) -> None:
        '''
        Define a triangle by providing the length of two
        sides, and the angle between them
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
        s = (self._a + self._b + self._c) / 2
        return math.sqrt(s*(s-self._a)*(s-self._b)*(s-self._c))

    def length_a(self):
        return self._a

    def length_b(self):
        return self._b

    def length_c(self):
        return self._c

    def angle_A(self):
        return self._A

    def angle_B(self):
        return self._B

    def angle_C(self):
        return self._C

    def perimeter(self) -> float:
        return self._a + self._b + self._c

    def isRight(self):
        return (round(x, 4) == 90 for x in [self.angle_A(), self.angle_B(), self.angle_C()])

    def isEquilateral(self):
        angles = [round(x, 4)
                  for x in (self.angle_A(), self.angle_B(), self.angle_C())]
        return angles[0] == angles[1] == angles[2] == 60

    def isIsosceles(self):
        return len({self._a, self._b, self._c}) < 3

    def isScalene(self):
        return not self.isIsosceles()
