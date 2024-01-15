class FigureMeta(type):
    def __new__(cls, name, bases, dct):
        if "area" not in dct or not isinstance(dct["area"], property):
            raise ValueError("Класс должен иметь свойство 'area'")
        return super().__new__(cls, name, bases, dct)


class Figure():
    @property
    def area(self):
        raise NotImplementedError()

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("Фигура не является геометрической")
        return self.area + figure.area
