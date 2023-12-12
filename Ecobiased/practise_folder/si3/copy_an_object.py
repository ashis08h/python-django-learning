from copy import copy, deepcopy

original_list = [1, 2, [0, 3, 4], 7]

shallow_copied = original_list.copy()
shallow_copied[1] = 5
print("shallow_copied1", shallow_copied)
print("original_list1", original_list)

shallow_copied[2][1] = 11
print("shallow_copied2", shallow_copied)
print("original_list2", original_list)

shallow_copied[2] = [15, 16, 17]
print("shallow_copied3", shallow_copied)
print("original_list3", original_list)

original_list1 = [1, 2, [0, 3, 4], 7]
shallow_copied1 = deepcopy(original_list1)
shallow_copied1[1] = 5
print("shallow_copied4", shallow_copied1)
print("original_list4", original_list1)
shallow_copied1[2][1] = 11
print("shallow_copied5", shallow_copied1)
print("original_list5", original_list1)
shallow_copied1[2] = [15, 16, 17]
print("shallow_copied6", shallow_copied1)
print("original_list6", original_list1)