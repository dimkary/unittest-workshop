from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area() -> float:
        pass
