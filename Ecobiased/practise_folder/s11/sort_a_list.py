# example to sort a list with sorted method

a_list = [1, 2, 8, 7, 0, 1, 0, 0, 9, 9, 8]
sorted_list = sorted(a_list)
print(sorted_list)

# example to sort a list without sorted method
a_list = [1, 2, 8, 7, 0, 1, 0, 0, 9, 9, 8]
length_of_a_list = len(a_list)
result_set = []
for x in range(length_of_a_list):
    minimun_element = min(a_list)
    result_set.append(minimun_element)
    a_list.remove(minimun_element)

print(result_set)

# example to sort a list without any builtin function
a_list = [1, 2, 8, 7, 0, 1, 0, 0, 9, 9, 8]
length_of_a_list = len(a_list)

for iter in range(length_of_a_list):
    for num in range(0, length_of_a_list - iter -1):
        if a_list[num] > a_list[num + 1]:
            a_list[num], a_list[num+1] = a_list[num + 1], a_list[num]
print(a_list)


