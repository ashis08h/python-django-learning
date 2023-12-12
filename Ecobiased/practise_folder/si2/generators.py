def generate_sequence():
    for i in range(5):
        yield i


seq = generate_sequence()
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
