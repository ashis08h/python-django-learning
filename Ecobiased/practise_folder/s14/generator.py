def generate_element(input_list):
    for item in input_list:
        yield item


seq = generate_element([1, 2, 3, 4, 5, 6])
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
# print(seq.__next__()) # raise stopIteration