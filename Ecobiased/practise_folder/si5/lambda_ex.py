add_num = lambda a, b:a+b
print(add_num(2, 4))

a_list = [1, 2, 3, 4, 5, 6]

square_list = list(map(lambda x: x**2, a_list))
print("square_list", square_list)

even_element_list = list(filter(lambda x:x%2 == 0, a_list))
print("even_element_list", even_element_list)

l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']
a_dict = zip(l1, l2)

print(dict(a_dict))

a_dict = lambda l1, l2 : dict(zip(l1, l2))
print(a_dict(l1, l2))

b_dict = lambda l1, l2 : {l1[x]: l2[x] for x in range(0,len(l2)) if l1[x] and l2[x]}
print(b_dict(l1, l2))