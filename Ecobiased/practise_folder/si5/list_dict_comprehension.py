a_list = [0, 1, 2, 3, 4, 5, 6]

square_list = [item**2 for item in a_list if item]
print("square_list", square_list)

even_list = [item for item in a_list if item%2==0]
print("even_list", even_list)

b_list = ['a', 'as', 'ash', 'ashi', 'ashis', 'ashish']

result = {key: len(key) for key in b_list if key}
print("result", result)