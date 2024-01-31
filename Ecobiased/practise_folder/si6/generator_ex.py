def create_seq():
    for i in range(5):
        yield i


seq = create_seq()
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())