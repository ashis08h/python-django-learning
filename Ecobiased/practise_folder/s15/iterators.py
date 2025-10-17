class MyIterator:

    def __init__(self, number_list):
        self.number_list = number_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.number_list):
            value = self.number_list[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration


my_iter = MyIterator([1, 2, 3, 4])
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
#print(my_iter.__next__())