def generate_seq(input_list):
    for char in input_list:
        yield char


seq = generate_seq([1, 2, 3, 4, 5])
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
# print(seq.__next__())