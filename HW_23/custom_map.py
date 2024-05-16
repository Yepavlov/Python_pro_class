class CustomMap:
    class CustomIterator:
        def __init__(self, some_dict: dict, func1, func2):
            self.some_dict = some_dict
            self.func1 = func1
            self.func2 = func2
            self.index = 0

        def __next__(self):
            if self.index == len(self.some_dict):
                raise StopIteration
            key = list(self.some_dict.keys())[self.index]
            value = list(self.some_dict.values())[self.index]
            self.index += 1
            return self.func1(key), self.func2(value)

    def __init__(self, some_dict: dict, func1, func2):
        self.some_dict = some_dict
        self.func1 = func1
        self.func2 = func2

    def __iter__(self):
        return self.CustomIterator(self.some_dict, self.func1, self.func2)


my_dict = {'a': 1, 'b': 2, 'c': 3}


def add_prefix(text):
    return text + "+my_prefix"


def multiple_on_two(digit):
    return digit ** 2


iterator = CustomMap(my_dict, add_prefix, multiple_on_two)
for k, v in iterator:
    print(k, v)
print(my_dict)
