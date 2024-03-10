from typing import Union

from HW_05.class_Point import Point


class Circle:
    def __init__(self, x: Union[int, float], y: Union[int, float], radius: Union[int, float]):
        self.x = x
        self.y = y
        self.radius = radius

    def include(self, point: Point) -> bool:
        distance = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
        return distance <= self.radius


def main():
    point = Point(2.3, 4.3)
    circle = Circle(6.1, 6.5, 1.2)
    print(circle.include(point))


if __name__ == '__main__':
    main()
