# example to sort a list with builtin sorted method

a_list = [1, 2, 8, 7, 0, 1, 0, 0, 9, 9, 8]
sorted_list = sorted(a_list)
print("a_list", sorted_list)

a_list.sort()
print(a_list)

# example of sorting a list without sorted method

a_list = [1, 2, 8, 7, 0, 1, 0, 0, 9, 9, 8]

result_list = []

length_of_list = len(a_list)

for item in range(length_of_list):
    result_list.append(min(a_list))
    a_list.remove(min(a_list))
print("result_list", result_list)

a_list = [1, 2, 8, 7, 0, 1, 0, 0, 9, 9, 8]
for index in range(length_of_list):
    for iter in range(length_of_list - index - 1):
        if a_list[iter] > a_list[iter + 1]:
            a_list[iter], a_list[iter + 1] = a_list[iter+1], a_list[iter]
print(a_list)