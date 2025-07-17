a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

reversed_list = a_list[::-1]
print("reversed_list", reversed_list)

reversed_list1 = list(reversed(a_list))
print("reversed_list1", reversed_list1)

a_string = "Ashish"
reverse_string = a_string[::-1]
print("reverse_string", reverse_string)

reverse_list = list(reversed(a_string))
print("reverse_list", reverse_list)

reverse_string = "".join(reverse_list)
print("reverse_string", reverse_string)
