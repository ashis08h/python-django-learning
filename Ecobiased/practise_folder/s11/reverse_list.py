a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

reversed_list = a_list[::-1]
print("reversed_list", reversed_list)

reversed_list2 = list(reversed(a_list))
print("reversed_list2", reversed_list2)

a_string = 'Ashish Kumar'
reversed_str = a_string[::-1]
print("reversed_str", reversed_str)

reversed_str2 = list(reversed(a_string))
print("reversed_str2", "".join(reversed_str2))