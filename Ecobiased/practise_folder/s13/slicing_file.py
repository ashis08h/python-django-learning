a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

sliced_list = a_list[1:4:1]
print("sliced_list", sliced_list)

double_list = a_list[1:5:2]
print("double_list", double_list)

negative_sliced = a_list[-2::-1]
print("negative_sliced", negative_sliced)

negative_double_list = a_list[-2:2:-2]
print("negative_double_sliced", negative_double_list)