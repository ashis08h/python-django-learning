add_number = lambda a,b: a+b
print(add_number(2, 3))

a_list = [0, 1, 2, 3, 4, 5, 6]
square_list = list(map(lambda x:x**2, a_list))
print(square_list)

even_list = list(filter(lambda x:x%2==0, a_list))
print(even_list)

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

result = dict(zip(list1, list2))
print(result)

result1 = lambda l1, l2:dict(zip(l1, l2))
print(result1(list1, list2))

result3 = lambda l1, l2:{l1[x]:l2[x] for x in range(len(l1))}
print(result3(list2, list1))