import math


class Shape:
    def __init__(self, x: int | float, y: int | float):
        self.x = x
        self.y = y

    def square(self):
        return 0


class Point:
    def __init__(self, x: int | float, y: int | float):
        self.x = x
        self.y = y


class Circle(Shape):
    def __init__(self, x: int | float, y: int | float, radius: int | float):
        super().__init__(x, y)
        self.radius = radius

    def square(self):
        return round(math.pi * self.radius**2, 2)

    def __contains__(self, point: Point) -> bool:
        distance = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
        return distance <= self.radius


class Rectangle(Shape):
    def __init__(
        self, x: int | float, y: int | float, width: int | float, height: int | float
    ):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def square(self):
        return round(self.width * self.height, 2)


class Parallelogram(Rectangle):
    def __init__(
        self,
        x: int | float,
        y: int | float,
        width: int | float,
        height: int | float,
        angle: int | float,
    ):
        super().__init__(x, y, width, height)
        self.angle = angle

    def square(self):
        return round(self.width * self.height * math.sin(math.radians(self.angle)), 2)


class Triangle(Shape):
    def __init__(
        self,
        x: int | float,
        y: int | float,
        side_a: int | float,
        side_b: int | float,
        side_c: int | float,
    ):
        super().__init__(x, y)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c


def square(self):
    semi_perimeter = (self.side_a + self.side_b + self.side_c) / 2
    return round(
        math.sqrt(
            semi_perimeter
            * (semi_perimeter - self.side_a)
            * (semi_perimeter - self.side_b)
            * (semi_perimeter - self.side_c)
        ),
        2,
    )
