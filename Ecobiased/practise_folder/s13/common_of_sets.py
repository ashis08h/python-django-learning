set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

common_of_set = set1 & set2
print("common_of_set", common_of_set)

union_of_set = set1 | set2
print("union_of_set", union_of_set)

common_of_set1 = set1.intersection(set2)
print("common_of_set1", common_of_set1)

union_of_set1 = set1.union(set2)
print("union_of_set", union_of_set1)
