add_number = lambda a, b: a+b
print(add_number(3, 4))


a_list = [1, 2, 3, 4, 5, 6]
sq_list = list(map(lambda x:x**2, a_list))
print("sq_list", sq_list)

even_list = list(filter(lambda x:x%2==0, a_list))
print("even_list", even_list)

num_list = [1, 2, 3]
alpha_list = ["a", "b", "c"]

result = lambda x, y:zip(x,y)
print(dict(result(num_list, alpha_list)))

result_dict = dict(zip(num_list, alpha_list))
print("result_dict", result_dict)

result_dict2 = lambda left_list, right_list:{left_list[x]:right_list[x] for x in range(len(left_list))}
print(result_dict2(num_list, alpha_list))