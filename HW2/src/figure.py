class Figure:
    @property
    def area(self):
        raise NotImplementedError()

    def add_area(self, figure):
        if not isinstance (figure, Figure):
            raise ValueError("Фигура не является геометрической")
        return self.area + figure.area
