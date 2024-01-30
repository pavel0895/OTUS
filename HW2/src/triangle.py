from HW2.src.figure import Figure

import math


class Triangle(Figure):
    def __init__(self, a, b, c):
        super().__init__(name="triangle")
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Заданы некорректные значения длин треугольника")
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            raise ValueError("Сумма длин двух сторон больше длины третьей стороны.")

        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = 0.5 * (self.a + self.b + self.c)
        area_value = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return int(area_value)

    def perimeter(self):
        return self.a + self.b + self.c

t =Triangle(5.5, 3.7, 5.5)
print(t.perimeter())
