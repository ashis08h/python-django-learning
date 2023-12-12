def generate_sequence(input_list):
    for item in input_list:
        yield(item)


seq = generate_sequence([1, 8, 9, 2, 7, 3, 4, 0])
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
