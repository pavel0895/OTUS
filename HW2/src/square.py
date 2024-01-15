from HW2.src.figure import Figure

class Square(Figure):
    def __init__(self, a):
        self.__a = a

    @property
    def area(self):
        return self.__a * self.__a

    @property
    def perimeter(self):
        return self.__a * 4


