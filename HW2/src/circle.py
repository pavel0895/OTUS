from HW2.src.figure import Figure

class Circle(Figure):
    def __init__(self, radius):
        super().__init__(name="Circle")
        if radius <= 0:
            raise ValueError("Нельзя создать круг с радиусом <= 0")
        self.radius = radius

    def area(self):
        area_value = 3.14 * self.radius * self.radius
        return int(area_value)

    def perimeter(self):
        perimeter_value = 2 * 3.14 * self.radius
        return int(perimeter_value)