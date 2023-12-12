from copy import copy, deepcopy

original_list = [1, 2, [0, 1, 3], 4]
original_list1 = [1, 2, [0, 1, 3], 4]

# shallow copy example

copied_list = original_list.copy()
print("copied_list11", copied_list)

copied_list[3] = 7
print("original_list12", original_list)
print("shallow_copy12", copied_list)
copied_list[2][1] = 100
print("original_list13", original_list)
print("shallow_copy13", copied_list)

# deep copy example

copied_list2 = deepcopy(original_list1)
print("shallow_copy21", copied_list2)
copied_list2[3] = 19
print("original_list22", original_list1)
print("shallow_copy22", copied_list2)
copied_list2[2][1] = 34
print("original_list23", original_list1)
print("shallow_copy23", copied_list2)


a_list = [1, [0, 2, 3], 5]
b_list = [1, [0, 2, 3], 5]

c_a_list = a_list.copy()
c_a_list[1][1] = 45
print("a_list", a_list)
print("c_a_list", c_a_list)

c_b_list = deepcopy(b_list)
c_b_list[1][1] = 60

print("b_list", b_list)
print("c_b_list", c_b_list)
