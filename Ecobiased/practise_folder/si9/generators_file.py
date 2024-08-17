def create_seq(a_list):
    for element in a_list:
        yield element


seq = create_seq([1, 2, 3, 4, 5])
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
# print(seq.__next__())