from HW2.src.figure import Figure

import math

class Triangle(Figure):
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Заданы некорректные значения длин треугольника")

        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @property
    def c(self):
        return self.__c

    @property
    def area(self):
        p = 0.5 * (self.__a + self.__b + self.__c)
        return math.isqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c))

    @property
    def perimeter(self):
        return self.__a + self.__b + self.__c