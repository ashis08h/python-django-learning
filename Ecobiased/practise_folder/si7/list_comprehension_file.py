a_list = [0, 1, 2, 3, 4, 5, 6]

sq_list = list(x**2 for x in a_list if x)
print("sq_list", sq_list)

even_list = list(item for item in a_list if item%2 == 0)
print("even_list", even_list)

b_list = ['a', 'as', 'ash', 'ashi', 'ashis', 'ashish']
result = {len(x): x for x in b_list if x}

print("result", result)