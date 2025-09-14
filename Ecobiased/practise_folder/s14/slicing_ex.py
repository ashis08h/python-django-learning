a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

sliced_list = a_list[1:4:1]
print("sliced_list", sliced_list)

double_sliced_list = a_list[1:5:2]
print("double_list", double_sliced_list)

negative_sliced_list = a_list[-2::-1]
print("negative_sliced_list", negative_sliced_list)

negative_doubled_sliced_list = a_list[-2:2:-2]
print("negative_doubled_sliced_list", negative_doubled_sliced_list)