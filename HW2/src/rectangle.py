from HW2.src.figure import Figure

class Rectangle(Figure):
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @property
    def area(self):
        return self.__a * self.__b

    @property
    def perimeter(self):
        return (self.__a + self.__b) * 2
