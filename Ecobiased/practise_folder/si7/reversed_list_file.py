a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
reversed_list = a_list[::-1]
reversed_list1 = list(reversed(a_list))
print("reversed_list", reversed_list)
print("reversed_list1", reversed_list1)

a_string = 'Ashish'
reversed_str = a_string[::-1]
print('reversed_str', reversed_str)
reversed_str1 = list(reversed(a_string))
print('reversed_str1', ''.join(reversed_str1))