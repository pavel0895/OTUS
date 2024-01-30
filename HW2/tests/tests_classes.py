from HW2.src.rectangle import Rectangle
from HW2.src.triangle import Triangle
from HW2.src.circle import Circle
from HW2.src.square import Square
import pytest


@pytest.mark.parametrize(("a", "b", "area", "perimeter"),
                         [(3, 5, 15, 16),
                          (2.5, 2.5, 6.25, 10)],
                         ids=["int", "float"])
def test_positive_rectangle(a, b, area, perimeter):
    r = Rectangle(a, b)
    assert r.area() == area
    assert r.perimeter() == perimeter


@pytest.mark.parametrize(("a", "b"),
                         [(-1, 2),
                          (0, 20.5)],
                         ids=["int", "float"])
def test_negative_rectangle(a, b):
    with pytest.raises(ValueError):
        Rectangle(a, b)


@pytest.mark.parametrize(("a", "b", "c", "area", "perimeter"),
                         [(13, 15, 12, 74, 40),
                          (5.5, 3.7, 5.5, 9, 14.7)],
                         ids=["int", "float"])
def test_positive_triangle(a, b, c, area, perimeter):
    t = Triangle(a, b, c)
    assert t.area() == area
    assert t.perimeter() == perimeter


@pytest.mark.parametrize(("a", "b", "c"),
                         [(-2, 2, 5),
                          (0, 5, 1.5)],
                         ids=["int", "float"])
def test_negative_triangle(a, b, c):
    with pytest.raises(ValueError):
        Triangle(a, b, c)


@pytest.mark.parametrize(("radius", "area", "perimeter"),
                         [(5, 78, 31),
                          (2.5, 19, 15)],
                         ids=["int", "float"])
def test_positive_circle(radius, area, perimeter):
    c = Circle(radius)
    assert c.area() == area
    assert c.perimeter() == perimeter


@pytest.mark.parametrize(("radius"),
                         [(-2),
                          (0)],
                         ids=["int", "float"])
def test_negative_circle(radius):
    with pytest.raises(ValueError):
        Circle(radius)


@pytest.mark.parametrize(("a", "area", "perimeter"),
                         [(5, 25, 20),
                          (2.5, 6.25, 10.0)],
                         ids=["int", "float"])
def test_positive_square(a, area, perimeter):
    s = Square(a)
    assert s.area() == area
    assert s.perimeter() == perimeter


@pytest.mark.parametrize(("a"),
                         [(-2),
                          (0)],
                         ids=["int", "float"])
def test_negative_square(a):
    with pytest.raises(ValueError):
        Square(a)

def test_figure_add_area():
    triangle = Triangle(5, 5,4)
    square = Square(4)
    circle = Circle(2)
    rectangle = Rectangle(8,6)

    assert triangle.add_area(square)
    assert triangle.add_area(circle)
    assert triangle.add_area(rectangle)

    assert square.add_area(triangle)
    assert square.add_area(circle)
    assert square.add_area(rectangle)

    assert circle.add_area(square)
    assert circle.add_area(triangle)
    assert circle.add_area(rectangle)

    assert rectangle.add_area(square)
    assert rectangle.add_area(circle)
    assert rectangle.add_area(triangle)

