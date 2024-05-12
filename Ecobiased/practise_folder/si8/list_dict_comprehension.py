a_list = [0, 1, 2, 3, 4, 5, 6]

sq_list = list(x**2 for x in a_list if x)
print(sq_list)

even_list = list(x for x in a_list if x%2==0)
print(even_list)

b_list = ['a', 'ash', 'as', 'ashish', 'ashi', 'ash']
name_value_pair = {x:len(x) for x in b_list if x}
print(name_value_pair)