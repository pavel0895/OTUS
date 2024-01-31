from HW2.src.figure import Figure


class Square(Figure):
    def __init__(self, a):
        super().__init__(name="square")
        if a <= 0:
            raise ValueError("Нельзя создать квадрат со стороной <= 0")
        self.a = a

    def area(self):
        return self.a * self.a

    def perimeter(self):
        return self.a * 4

s = Square(2.5)
print(s.area())