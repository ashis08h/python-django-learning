from copy import copy, deepcopy

# example of shallow copy.
original_list = [1, 2, [0, 1, 2, 3], 5]
copied_list = original_list.copy()

print('original_list1', original_list)
print('copied_list1', copied_list)

copied_list[3] = 12
print("***********")
print('original_list2', original_list)
print('copied_list2', copied_list)

copied_list[2][1] = 9
print("***********")
print('original_list3', original_list)
print('copied_list3', copied_list)

# example of deep copy.
deep_original_list = [1, 2, [0, 1, 2, 3], 5]
deep_copied_list = deepcopy(deep_original_list)
print("***********")
print('deep_original_list', deep_original_list)
print('deep_copied_list', deep_copied_list)

deep_copied_list[3] = 19
print("***********")
print('deep_original_list1', deep_original_list)
print('deep_copied_list1', deep_copied_list)

deep_copied_list[2][1] = 9
print("***********")
print('deep_original_list2', deep_original_list)
print('deep_copied_list2', deep_copied_list)