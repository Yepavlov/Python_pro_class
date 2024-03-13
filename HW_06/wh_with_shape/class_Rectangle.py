from HW_06.wh_with_shape.class_Shape import Shape


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def square(self):
        return round(self.width * self.height, 2)
