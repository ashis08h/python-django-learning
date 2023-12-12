def generate_sequence():
    for i in range(5):
        yield(i)


seq = generate_sequence()
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))


def generate_items1():
    for item in range(8):
        yield(item)


seq = generate_items1()
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
