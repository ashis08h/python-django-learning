from copy import copy, deepcopy

original_list = [1, 2, [0, 1, 2, 3], 5]
copied_list = original_list.copy()

copied_list[3] = 9
print("original_list", original_list)
print("copied_list", copied_list)

copied_list[2][1] = 12
print("original_list1", original_list)
print("copied_list1", copied_list)

original_list1 = [1, 2, [0, 1, 2, 3], 5]
copied_list1 = deepcopy(original_list1)

copied_list1[3] = 9
print("original_list2", original_list1)
print("copied_list2", copied_list1)
copied_list1[2][1] = 12
print("original_list3", original_list1)
print("copied_list3", copied_list1)