def create_seq():
    for i in [1, 2, 3, 4]:
        yield i


seq = create_seq()
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
