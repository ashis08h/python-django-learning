a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

sq_list = [x**2 for x in a_list]
print("sq_list", sq_list)

even_list = [x for x in a_list if x%2 == 0]
print(even_list)

b_list = ['ashi', 'as', 'ashish', 'ash', 'a', 'a']

result_dict = {len(x): x for x in b_list}
print(result_dict)

# sort a dictionary with key

sorted_dict = sorted(result_dict.items())
print("sorted_dict", dict(sorted_dict))

# sort a dictionary with value

sorted_dict = sorted(result_dict.items(), key=lambda x:x[1])
print("sorted_dict", dict(sorted_dict))

# sort a dictionary with key in reverse order
rev_sorted = sorted(result_dict.items(), reverse=True)
print("rev_sorted", dict(rev_sorted))

# sort a dictionary with value in reverse order
rev_sorted_with_value = sorted(result_dict.items(), key=lambda x:x[1], reverse=True)
print("rev_sorted_with_value", dict(rev_sorted_with_value))

l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result_list = [x**2 if x%2 == 0 else x**3 for x in l1]
print("result_list", result_list)