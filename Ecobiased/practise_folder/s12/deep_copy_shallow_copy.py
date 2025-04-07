from copy import copy, deepcopy


# example for shallow copy
original_list = [1, 2, 3, [1, 2, 3], 9]
copied_list = original_list.copy()


print("original_list1", original_list)
print("copied_list1", copied_list)

copied_list[-1] = 100

print("original_list2", original_list)
print("copied_list2", copied_list)

copied_list[3][2] = 120

print("original_list3", original_list)
print("copied_list3", copied_list)


# example of deepcopy


original_list = [1, 2, 3, [1, 2, 3], 9]
copied_list = deepcopy(original_list)

print("original_list4", original_list)
print("copied_list4", copied_list)

copied_list[-1] = 100

print("original_list5", original_list)
print("copied_list5", copied_list)

copied_list[3][2] = 120

print("original_list6", original_list)
print("copied_list6", copied_list)
