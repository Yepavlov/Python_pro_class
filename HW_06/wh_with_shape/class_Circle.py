import math

from HW_06.wh_with_shape.class_Shape import Shape


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def square(self):
        return round(math.pi * self.radius ** 2, 2)
