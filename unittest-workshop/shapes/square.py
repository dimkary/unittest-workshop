import math
from .shape import Shape


class Square(Shape):
    def __init__(self, length: float) -> None:
        if length < 0:
            raise ValueError('The length cannot be negative')
        self._length = length

    def area(self) -> float:
        return math.pow(self._length, 2)

    def perimeter(self) -> float:
        return self._length * 4

    def diagonal(self) -> float:
        return math.sqrt(2*self._length*self._length)
