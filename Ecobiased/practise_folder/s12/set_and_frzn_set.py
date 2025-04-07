# example of set

set1 = {1, 2, 3, 4}
print(set1)
print(type(set1))

set1.add(6)
print(set1)
set1.remove(4)
print(set1)

frzn_set = frozenset({1, 2, 3, 4})
print(frzn_set)
print(type(frzn_set))