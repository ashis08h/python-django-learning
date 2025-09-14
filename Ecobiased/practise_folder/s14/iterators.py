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


myiter = MyIterator([1, 2, 3, 6, 3])
#print(tuple(myiter.__iter__()))

print(myiter.__next__())
print(myiter.__next__())
print(myiter.__next__())
print(myiter.__next__())
print(myiter.__next__())
#print(myiter.__next__())