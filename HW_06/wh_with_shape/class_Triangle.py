import math

from HW_06.wh_with_shape.class_Shape import Shape


class Triangle(Shape):
    def __init__(self, x, y, side_a, side_b, side_c):
        super().__init__(x, y)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def square(self):
        semi_perimeter = (self.side_a + self.side_b + self.side_c) / 2
        return round(math.sqrt(semi_perimeter * (semi_perimeter - self.side_a) * (semi_perimeter - self.side_b) *
                               (semi_perimeter - self.side_c)), 2)
