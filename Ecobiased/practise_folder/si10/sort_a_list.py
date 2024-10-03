# Method - 1 using sorted method

a_list = [1, 2, 8, 7, 0, 1, 0, 0, 9, 9, 8]
print(sorted(a_list))

# Method - 2 using min method

result_list = []
# calculate length of a_list
length_of_list = len(a_list)
# Iterate the list as much their length
for x in range(length_of_list):
    # take minimum element
    minimum_element = min(a_list)
    # append to result list one by one and removing that element from source list.
    result_list.append(minimum_element)
    a_list.remove(minimum_element)
print(result_list)

# Method - 3 without any builtin method using swaping two numbers mechanism.

a_list = [1, 2, 8, 7, 0, 1, 0, 0, 9, 9, 8]
# calculate the length of source list
length_of_list = len(a_list)
# Iterate the list as much their length
for iter in range(length_of_list):
    # Last element is already sorted no need to check them so doing - 1 at the last.
    for num in range(0, length_of_list - iter - 1):
        # comparing an element with next element and spawing the numbers if previous element is larger
        # than the next number
        if a_list[num] > a_list[num + 1]:
            a_list[num], a_list[num + 1] = a_list[num + 1], a_list[num]

print(a_list)
