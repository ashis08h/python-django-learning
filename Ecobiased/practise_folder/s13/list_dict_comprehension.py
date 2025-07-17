a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

sq_list = list(x**2 for x in a_list)
print("sq_list", sq_list)

even_list = list(x for x in a_list if x%2 == 0)
print("even_list", even_list)

b_list = ['a', 'as', 'a', 'ash', 'ashish', 'ashi']

result_dict = {len(x): x for x in b_list}
print("b_list", result_dict)

# sort a dictionary by its key

sorted_dict = sorted(result_dict.items())
print("sorted_dict", dict(sorted_dict))

# sorted a dictonary by values
sorted_dict = sorted(result_dict.items(), key=lambda items:items[1])
print("sorted_dict", dict(sorted_dict))

# sort a dictionary by its key in reverse order

reverse_sorted_dict = dict(sorted(result_dict.items(), reverse=True))
print("reverse_sorted_dict", reverse_sorted_dict)

reverse_sorted_dict = dict(sorted(result_dict.items(), key=lambda items:items[1], reverse=True))
print("reverse_sorted_dict", reverse_sorted_dict)

l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result_dict = {x: x**2 if x%2 == 0 else x**3 for x in l1}
print("result_dict", result_dict)