from HW2.src.figure import Figure


class Square(Figure):
    def __init__(self, name, a):
        super().__init__(name)
        self.a = a

    def area(self):
        return self.a * self.a

    def perimeter(self):
        return self.a * 4
