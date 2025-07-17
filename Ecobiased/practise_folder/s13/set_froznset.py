# example of set

set1 = {1, 2, 3, 4}
print("set1", set1)
print("type", type(set1))

set1.add(5)
print("set1", set1)

set1.remove(4)
print("set1", set1)

# example of froznset

frznset1 = frozenset({1, 2, 3, 4})
print("frznset", frznset1)
print("type", type(frznset1))