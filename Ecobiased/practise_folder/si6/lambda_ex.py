add_num = lambda a, b: a+b
print(add_num(4, 5))

a_list = [1, 2, 3, 4, 5, 6]

square_list = list(map(lambda x: x**2, a_list))
print("square_list", square_list)

even_list = list(filter(lambda x: x%2==0, a_list))
print("even_list", even_list)

a_list = [1, 2, 3]
b_list = ['a', 'b', 'c']

a_dict = zip(a_list,b_list)
print('a_dict', dict(a_dict))

new_dict = lambda l1, l2: dict(zip(l1, l2))
print("new_dict", new_dict(a_list, b_list))

new_dict1 = lambda  l1, l2: {l1[x]:l2[x] for x in range(len(a_list)) if l1[x] and l2[x]}
print("new_dict1", new_dict1(a_list, b_list))