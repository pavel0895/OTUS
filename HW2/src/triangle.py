from HW2.src.figure import Figure

import math


class Triangle(Figure):
    def __init__(self, name, a, b, c):
        super().__init__(name)
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Заданы некорректные значения длин треугольника")
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            raise ValueError("Нельзя создать треугольник")

        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = 0.5 * (self.a + self.b + self.c)
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self):
        return self.a + self.b + self.c
