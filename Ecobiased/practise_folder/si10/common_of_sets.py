set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

common_of_both_sets = set1 & set2
print(common_of_both_sets)

union_of_sets = set1 | set2
print(union_of_sets)

# method 2

common_of_both_sets = set1.intersection(set2)
print(common_of_both_sets)

union_of_sets = set1.union(set2)
print(union_of_sets)