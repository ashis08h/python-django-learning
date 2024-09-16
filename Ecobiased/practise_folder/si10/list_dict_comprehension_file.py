a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


sq_list = list(x**2 for x in a_list)
print("sq_list", sq_list)

even_list = list(x for x in a_list if x%2==0)
print("even_list", even_list)

# example of dict comprehension
b_list = ['a', 'as', 'a', 'ash', 'ashish', 'ashi']

result_dict = {b_list[x]: len(b_list[x]) for x in range(len(b_list))}
print("result_list", result_dict)

# short a dictionary by keys

sorted_by_keys = dict(sorted(result_dict.items()))
print("sorted by keys", sorted_by_keys)

# short a dictionary by values

sorted_by_values = dict(sorted(result_dict.items(), key=lambda item: item[1]))
print("sorted by values", sorted_by_values)

l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


mapped_dict = {x: x**2 if x%2==0 else x**3 for x in l1}
print("mapped_dict", mapped_dict)

