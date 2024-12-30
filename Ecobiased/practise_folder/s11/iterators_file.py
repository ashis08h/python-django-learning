class MyIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self # Return the iterator object itself.

    def __next__(self):
        if self.index < len(self.numbers):
            value = self.numbers[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration


nums = MyIterator([10, 20, 30])
print(nums.__next__())
print(nums.__next__())
print(nums.__next__())
# print(nums.__next__())
print(nums.__iter__())
