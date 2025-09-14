a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

sq_list = list(x**2 for x in a_list)
print("sq_list", sq_list)

even_list = list(x for x in a_list if x%2==0)
print("even_list", even_list)

b_list = ['ashi', 'as', 'ashish', 'ash', 'a', 'a']

dict_result = {len(x): x for x in b_list}
print("dict_result", dict_result)

# sort a dictionary by key
sorted_dict = sorted(dict_result.items())
print("sorted_dict", dict(sorted_dict))

# sort a dictionary by value

sorted_dict = sorted(dict_result.items(), key=lambda items: items[1])
print("sorted_dict", dict(sorted_dict))

# sort a dictionary by key in reverse order
rev_sorted_dict = sorted(dict_result.items(), reverse=True)
print("rev_sorted_dict", dict(rev_sorted_dict))

# sort a dictionary by value in reverse order
rev_sorted_dict = sorted(dict_result.items(), key=lambda items:items[1], reverse=True)
print("rev_sorted_dict", dict(rev_sorted_dict))

l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result_dict = {x: x**2 if x%2==0 else x**3 for x in l1}
print("result_dict", result_dict)