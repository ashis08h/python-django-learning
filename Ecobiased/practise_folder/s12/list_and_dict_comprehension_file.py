a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

sq_list = list(x**2 for x in a_list)
print(sq_list)

even_list = list(x for x in a_list if x%2==0)
print(even_list)

b_list = ['a', 'as', 'a', 'ash', 'ashish', 'ashi']

result_dict = {x: len(x) for x in b_list}
print(result_dict)

# example of sort a dict by it's key

sorted_by_key = sorted(result_dict.items())
print(dict(sorted_by_key))

# example of sort a dict by it's value

sorted_by_value = sorted(result_dict.items(), key=lambda items:items[1])
print(dict(sorted_by_value))

l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result_dict = {x: x**2 if x%2==0 else x**3 for x in l1}
print(result_dict)