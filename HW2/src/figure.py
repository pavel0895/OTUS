from abc import ABC, abstractmethod

class Figure(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("other_figure должно быть фигурой")
        return self.area() + other_figure.area()

