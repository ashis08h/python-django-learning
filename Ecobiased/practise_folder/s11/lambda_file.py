add_number = lambda a, b: a+b
print(add_number(3, 4))

a_list = [1, 2, 3, 4, 5, 6]
sq_list = list(map(lambda x: x**2, a_list))
print("sq_list", sq_list)

even_list = list(filter(lambda x: x%2==0, a_list))
print("even_list", even_list)

num_list = [1, 2, 3]
alphabet_list = ["a", "b", "c"]

result = lambda list1, list2: zip(list1, list2)
print(dict(result(num_list, alphabet_list)))

result_dict = zip(num_list, alphabet_list)
print(dict(result_dict))

result = lambda num1, alpha1 :{num_list[x]: alphabet_list[x] for x in range(len(num1))}
print(dict(result(num_list, alphabet_list)))


def add_extra(num1):
    return num1 + 8

a_list = [1, 2, 3, 4]

result_list = map(add_extra, a_list)
print(list(result_list))