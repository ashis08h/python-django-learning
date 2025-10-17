# example of sort a list with builtin method

a_list = [1, 2, 8, 7, 0, 1, 0, 0, 9, 9, 8]

sorted_list = sorted(a_list)
print("sorted_list", sorted_list)

a_list.sort()
print("a_list", a_list)

# example of sort a list without sorting method

a_list = [1, 2, 8, 7, 0, 1, 0, 0, 9, 9, 8]
result_list = []
len_of_input_list = len(a_list)

for index in range(len_of_input_list):
    for num in range(len_of_input_list - index - 1):
        if a_list[num] > a_list[num + 1]:
            a_list[num], a_list[num + 1] = a_list[num + 1], a_list[num]

print("a_list", a_list)