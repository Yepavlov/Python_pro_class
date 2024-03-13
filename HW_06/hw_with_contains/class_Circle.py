from HW_06.hw_with_contains.class_Point import Point


class Circle:
    def __init__(self, x: int | float, y: int | float, radius: int | float):
        self.x = x
        self.y = y
        self.radius = radius

    def __contains__(self, point: Point) -> bool:
        distance = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
        return distance <= self.radius


def main():
    point_out = Point(10, 7)
    point_in = Point(2, 3)
    circle = Circle(3, 4, 6)
    print(point_out in circle)
    print(point_in in circle)


if __name__ == '__main__':
    main()
