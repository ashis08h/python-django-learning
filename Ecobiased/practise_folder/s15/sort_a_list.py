a_list = [1, 2, 8, 7, 0, 1, 0, 0, 9, 9, 8]

# sort a list by builtin method

sorted_list = sorted(a_list)
print("sorted_list", sorted_list)

a_list.sort()
print(sorted_list)

# example of sort without sorting method

a_list = [1, 2, 8, 7, 0, 1, 0, 0, 9, 9, 8]

len_of_a_list = len(a_list)

for index in range(len_of_a_list):
    for element in range(len_of_a_list - index - 1):

        if a_list[element] > a_list[element + 1]:
            a_list[element], a_list[element + 1] = a_list[element + 1], a_list[element]
print(a_list)