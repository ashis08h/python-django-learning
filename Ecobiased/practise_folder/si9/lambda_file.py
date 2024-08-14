add_number = lambda a, b: a+b
print(add_number(3, 4))

a_list = [1, 2, 3, 4, 5]
sq_list = list(map(lambda x: x**2, a_list))
print("sq_list", sq_list)

even_filter = list(filter(lambda x:x%2==0, a_list))
print("even_filter", even_filter)


num_list = [1, 2, 3]
a_list = ["a", "b", "c"]

result_dict = dict(zip(num_list, a_list))
print(result_dict)


result_list2 = lambda l1, l2:dict(zip(l1, l2))
print(result_list2(a_list, num_list))


result_list3 = lambda l1, l2:{l1[x]: l2[x] for x in range(len(l1))}
print(result_list3(a_list, num_list))