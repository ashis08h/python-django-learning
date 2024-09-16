from copy import copy, deepcopy

original_list = [1, 2, 3, [1, 2, 3], 9]
copied_list = original_list.copy()

copied_list[-1] = 100

print("original_list1", original_list)
print('copied_list1', copied_list)

copied_list[3][1] = 12
print("original_list2", original_list)
print('copied_list2', copied_list)

original_list = [1, 2, 3, [1, 2, 3], 9]
copied_list = deepcopy(original_list)

copied_list[3][2] = 12
print("original_list3", original_list)
print('copied_list3', copied_list)
