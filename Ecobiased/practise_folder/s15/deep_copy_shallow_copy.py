from copy import copy, deepcopy


original_list = [1, 2, 3, [1, 2, 3], 9]

# example of shallow copy.
copied_list = original_list.copy()

copied_list[3][1] = 99

print("coppied_list", copied_list)
print("original_list", original_list)


# example of deepcopy

original_list = [1, 2, 3, [1, 2, 3], 9]

copied_list = deepcopy(original_list)

copied_list[3][1] = 88

print("coppied_list", copied_list)
print("original_list", original_list)
