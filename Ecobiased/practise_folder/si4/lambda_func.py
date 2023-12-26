add_num = lambda x, y: x+y
print(add_num(2, 7))

a_list = [1, 2, 3, 4, 5, 6]

square_list = list(map(lambda x:x**2, a_list))
print(square_list)
even_number_list = list(filter(lambda x: x%2 == 0, a_list))
print(even_number_list)