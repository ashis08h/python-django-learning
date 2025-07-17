from copy import copy, deepcopy


# example of shallow copy
original_list = [1, 2, 3, [1, 2, 3], 9]
copied_list = original_list.copy()

copied_list[3][1] = 123
print("copied_list1", copied_list)
print("original_list1", original_list)

original_list = [1, 2, 3, [1, 2, 3], 9]
copied_list = deepcopy(original_list)
copied_list[3][1] = 123
print("copied_list1", copied_list)
print("original_list1", original_list)
