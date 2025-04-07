# example to sort a list with sorted function


a_list = [1, 2, 8, 7, 0, 1, 0, 0, 9, 9, 8]
sorted_list = sorted(a_list)
print(sorted_list)

# example of sorting a list without sorted method

a_list = [1, 2, 8, 7, 0, 1, 0, 0, 9, 9, 8]
result_list = []
len_of_input_list = len(a_list)
for item in range(len_of_input_list):
    min_of_a_list = min(a_list)
    result_list.append(min_of_a_list)
    a_list.remove(min_of_a_list)
print(result_list)


# example to sort a list without any builtin function
a_list = [1, 2, 8, 7, 0, 1, 0, 0, 9, 9, 8]
len_of_a_list = len(a_list)

for iter in range(len(a_list)):
    for num in range(len_of_a_list - iter - 1):
        if a_list[num] > a_list[num + 1]:
            a_list[num], a_list[num + 1] = a_list[num + 1], a_list[num]

print(a_list)

