from HW_06.wh_with_shape.class_Rectangle import Rectangle


class Parallelogram(Rectangle):
    def __init__(self, x, y, width, height, angle):
        super().__init__(x, y, width, height)
        self.angle = angle


