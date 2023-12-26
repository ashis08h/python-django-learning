add_number = lambda a, b: a+b
print("add_number", add_number(3, 5))

a_list = [1, 3, 4, 2, 5, 6]

square_list = list(map(lambda x: x**2, a_list))
print('square_list', square_list)

filtered_list = list(filter(lambda x: x % 2 == 0, a_list))
print("filtered_list", filtered_list)


square_list = list(map(lambda x:x**2, [1,2,3]))
print("square_list", square_list)

sq_list = [x**2 for x in [1, 2, 3] if x]
print("sq_list", sq_list)