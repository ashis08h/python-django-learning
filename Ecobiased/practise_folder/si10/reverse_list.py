a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
reversed_list = a_list[::-1]
print("reversed_list", reversed_list)

reversed_list1 = a_list[:-1]
print("reversed_list1", reversed_list1)

reverse_list2 = list(reversed(a_list))
print("reverse_list2", reverse_list2)

a_str = "Ashish Kumar"
rev_str = a_str[::-1]
print("rev_str", rev_str)
rev_str_list = list(reversed(a_str))
print("rev_str_list", rev_str_list)
rev_str = "".join(rev_str_list)
print("rev_str", rev_str)