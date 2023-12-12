add = lambda x, y: x + y
print(add(3, 4))

a_list = [1, 2, 3, 4]

square_list = list(map(lambda x:x**2, a_list))
print("square_list", square_list)

even_element_list = list(filter(lambda x:x%2 == 0, a_list))
print("even_element_list", even_element_list)
