a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

reversed_list = a_list[::-1]
print(reversed_list)

reversed_list = list(reversed(a_list))
print(reversed_list)

a_string = 'Ashish Kumar'
reversed_string = a_string[::-1]
print(reversed_string)

reversed_list = list(reversed(a_string))
print(reversed_list)

reverse_string = "".join(reversed_list)
print(reverse_string)