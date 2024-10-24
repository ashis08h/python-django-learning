def generate_seq(input_list):
    for item in input_list:
        yield item


seq = generate_seq([1, 2, 3, 4, 5])
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
# print(seq.__next__())