from copy import copy, deepcopy

# example of shallow copy
orig_list = [1, 2, 3, [1, 2, 3], 9]
copied_list = orig_list.copy()

copied_list[3][1] = 11

print("original_list", orig_list)
print("copied_list", copied_list)

copied_list[-1] = 12
print("original_list1", orig_list)
print("copied_list1", copied_list)

# example of deepcopy

orig_list = [0, 1, 2, [1, 2, 3], 9]
copied_list = deepcopy(orig_list)

copied_list[3][1] = 11

print("original_list2", orig_list)
print("copied_list2", copied_list)

copied_list[-1] = 12

print("original_list3", orig_list)
print("copied_list3", copied_list)