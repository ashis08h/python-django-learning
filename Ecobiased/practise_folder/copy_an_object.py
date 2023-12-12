from copy import copy, deepcopy


original_list = [1, 2, [0, 1, 3], 4]

# shallow copy
shallow_copy_list = original_list.copy()
shallow_copy_list[3] = 7
shallow_copy_list[2][1] = 100
print(shallow_copy_list)
print(original_list)

deep_copy_list = deepcopy(original_list)
deep_copy_list[3] = 8
deep_copy_list[2][1] = 1000
print(deep_copy_list)
print(original_list)



