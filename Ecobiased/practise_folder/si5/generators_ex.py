def create_sequence():
    for i in range(5):
        yield(i)


seq = create_sequence()
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())