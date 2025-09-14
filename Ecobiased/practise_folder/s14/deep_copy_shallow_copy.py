from copy import copy, deepcopy


# example of shallow copy
original_list = [1, 2, 3, [1, 2, 3], 9]
copied_list = original_list.copy()

copied_list[3][1] = 12

print("original_list", original_list)
print("copied_list", copied_list)

# example of deep copy
original_list = [1, 2, 3, [1, 2, 3], 9]
copied_list = deepcopy(original_list)

copied_list[3][1] = 15
print("original_list", original_list)
print("copied_list", copied_list)