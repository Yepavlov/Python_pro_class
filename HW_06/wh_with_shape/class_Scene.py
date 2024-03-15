from typing import Union, List

from HW_06.wh_with_shape.class_Figures import (
    Triangle,
    Circle,
    Parallelogram,
    Rectangle,
    Point,
)


class Scene:
    def __init__(self):
        self._figures = []

    def add_figure(
        self,
        figure: Union[
            Triangle,
            Circle,
            Parallelogram,
            Rectangle,
            List[Union[Circle, Parallelogram, Rectangle, Triangle]],
        ],
    ):
        if isinstance(figure, list):
            self._figures.extend(figure)
        else:
            self._figures.append(figure)

    def total_square(self):
        return sum(f.square() for f in self._figures)


def main():
    t = Triangle(0, 0, 10, 15, 12)
    square_triangle = t.square()
    c = Circle(0, 0, 10)
    square_circle = c.square()
    r = Rectangle(0, 0, 5, 10)
    square_rectangle = r.square()
    p = Parallelogram(0, 0, 12, 15, 65)
    square_parallelogram = p.square()
    print(
        f"{square_triangle=}, {square_circle=}, {square_rectangle=}, {square_parallelogram=} and "
        f"{sum([square_circle, square_triangle, square_rectangle, square_parallelogram])}"
    )
    scene = Scene()
    scene.add_figure([t, c, r, p])
    print(scene.total_square())
    print(
        "---------------------------------------HW_06_task_2---------------------------------------------"
    )
    point_out = Point(10, 7)
    point_in = Point(2, 3)
    circle = Circle(3, 4, 6)
    print(point_out in circle)
    print(point_in in circle)


if __name__ == "__main__":
    main()
