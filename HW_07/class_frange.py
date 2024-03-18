class frange:
    def __init__(self, *args: float | int):
        if len(args) == 1:
            self.start = 0
            self.stop = float(args[0])
            self.step = 1
        if len(args) == 2:
            self.start = args[0]
            self.stop = args[1]
            self.step = 1
        if len(args) == 3:
            self.start = float(args[0])
            self.stop = float(args[1])
            self.step = float(args[2])

    def __iter__(self):
        return self

    def __next__(self):
        if (self.step > 0 and self.start >= self.stop) or (self.step < 0 and self.start <= self.stop):
            raise StopIteration
        result = self.start
        self.start += self.step
        return result


assert (list(frange(5)) == [0, 1, 2, 3, 4])
assert (list(frange(2, 5)) == [2, 3, 4])
assert (list(frange(2, 10, 2)) == [2, 4, 6, 8])
assert (list(frange(10, 2, -2)) == [10, 8, 6, 4])
assert (list(frange(2, 5.5, 1.5)) == [2, 3.5, 5])
assert (list(frange(1, 5)) == [1, 2, 3, 4])
assert (list(frange(0, 5)) == [0, 1, 2, 3, 4])
assert (list(frange(0, 0)) == [])
assert (list(frange(100, 0)) == [])
assert (list(frange(-2, 10, 2)) == [-2, 0, 2, 4, 6, 8])
