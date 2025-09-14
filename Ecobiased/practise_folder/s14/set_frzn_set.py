# example of set

set1 = {1, 2, 3, 4}
print("set1", set1)

print("type", type(set1))

set1.add(5)
print("set1", set1)

set1.remove(4)
print("set1", set1)

# example of frznset

fr_set1 = frozenset({1, 2, 3, 5})
print("frznset", fr_set1)
print("type", type(fr_set1))

set2 = {4, 5, 6, 2}

common = set1 & set2
print("common", common)
common1 = set1.intersection(set2)
print("common1", common1)

union = set1 | set2
print("union", union)
union1 = set1.union(set2)
print("union1", union1)