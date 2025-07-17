add_number = lambda a, b: a+b
print(add_number(3, 4))

a_list = [1, 2, 3, 4, 5, 6]
sq_list = list(map(lambda x:x**2, a_list))
print("sq_list", sq_list)

even_list = list(filter(lambda x:x%2, a_list))
print("even_list", even_list)

num_list = [1, 2, 3]
alpha_list = ["a", "b", "c"]

result_dict = lambda num_list, alpha_list: zip(num_list, alpha_list)
print("result_dict", dict(result_dict(num_list, alpha_list)))

result_dict = zip(num_list, alpha_list)
print("result_dict1", dict(result_dict))

result_dict = lambda num_list, alpha_list: {num_list[x]: alpha_list[x] for x in range(len(num_list))}
print("result_dict", dict(result_dict(num_list, alpha_list)))