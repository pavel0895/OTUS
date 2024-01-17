from HW2.src.figure import Figure

class Circle(Figure):
    def __init__(self, radius, name):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius
