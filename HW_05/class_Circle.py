
from HW_05.class_Point import Point


class Circle:
    def __init__(self, x: int | float, y: int | float, radius: int | float):
        self.x = x
        self.y = y
        self.radius = radius

    def contains(self, point: Point) -> bool:
        distance = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
        return distance <= self.radius


def main():
    point = Point(10, 7)
    circle = Circle(3, 4, 6)
    print(circle.contains(point))


if __name__ == '__main__':
    main()
