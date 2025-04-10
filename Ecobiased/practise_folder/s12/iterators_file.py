class MyIteration:

    def __init__(self, number_list):
        self.number_list = number_list
        self.index = 0

    def __iter__(self):
        return self # return the iterator object itself.

    def __next__(self):
        if self.index < len(self.number_list):
            value = self.number_list[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration


mi = MyIteration([1, 2, 3, 4])
print(mi.__iter__())
print(mi.__next__())
print(mi.__next__())
print(mi.__next__())
print(mi.__next__())