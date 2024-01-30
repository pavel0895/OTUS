from HW2.src.figure import Figure


class Rectangle(Figure):
    def __init__(self, a, b):
        super().__init__(name="rectangle")
        if a <= 0 or b <= 0:
            raise ValueError("Нельзя создать прямоугольник со стороной <= 0")
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return (self.a + self.b) * 2
