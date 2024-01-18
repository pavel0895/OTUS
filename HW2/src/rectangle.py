from HW2.src.figure import Figure


class Rectangle(Figure):
    def __init__(self, name, a, b):
        super().__init__(name)
        self.a = a
        self.b = b


    def area(self):
        return self.a * self.b


    def perimeter(self):
        return (self.a + self.b) * 2
