add_number = lambda a, b:a+b
print(add_number(3, 4))

a_list = [1, 2, 3, 4, 5]

sq_list = list(map(lambda x: x**2, a_list))
print("sq_list", sq_list)

even_filter = list(filter(lambda x: x%2==0, a_list))
print("even_filter", even_filter)

num_list = [1, 2, 3]
alphabet_list = ["a", "b", "c"]

mappling_dict = dict(zip(num_list, alphabet_list))
print("mapping_dict", mappling_dict)

result_dict = lambda l1, l2: dict(zip(l1, l2))
print("result_dict", result_dict(num_list, alphabet_list))

result_list2 = lambda l1, l2: {l1[x]: l2[x] for x in range(len(l1))}
print(result_list2(alphabet_list, num_list))

print('************************')

add_number = lambda a, b: a+b
print(add_number(3, 4))

a_list = [1, 2, 3, 4, 5]

sq_list = list(map(lambda x: x**2, a_list))
print("sq_list", sq_list)

even_filter = list(filter(lambda x: x%2==0, a_list))
print("even_list", even_filter)

n_l = [1, 2, 3]
a_l = ["a", "b", "c"]

mapp_dict = dict(zip(n_l, a_l))
print("mapp_dict", mapp_dict)

result_dict = lambda l1, l2: dict(zip(l1, l2))
print(result_dict(n_l, a_l))

result_dict_2 = lambda l1, l2: {l1[x]: l2[x] for x in range(len(l1))}
print(result_dict_2(a_l, n_l))

