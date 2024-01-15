from HW2.src.figure import Figure

import math


class Triangle(Figure):
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Заданы некорректные значения длин треугольника")
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            raise ValueError("Нельзя создать треугольник")

        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def area(self):
        p = 0.5 * (self.__a + self.__b + self.__c)
        return int(math.isqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c)))

    @property
    def perimeter(self):
        return self.__a + self.__b + self.__c
