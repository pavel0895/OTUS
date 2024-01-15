from HW2.src.figure import Figure

class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @property
    def area(self):
        return 3.14 * self.__radius * self.__radius

    def perimeter(self):
        return 2 * 3.14 * self.__radius
