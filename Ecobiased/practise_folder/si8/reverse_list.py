a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

reverse_list = a_list[::-1]
print('reversed_list1', reverse_list)

reverse_list1 = list(reversed(a_list))
print('reversed_list1', reverse_list1)

a_string = 'Ashish Kumar'

reverse_string = a_string[::-1]
print('reverse_string', reverse_string)

reverse_string1_list = list(reversed(a_string))
reversed_string1 = "".join(reverse_string1_list)

print('reversed_string1', reversed_string1)