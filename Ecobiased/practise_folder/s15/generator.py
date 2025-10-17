def generate_element(input_list):
    for element in input_list:
        yield element


seq = generate_element([1, 2, 3, 4, 5, 6])

print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
# print(seq.__next__()) this line gives stopIteration error.