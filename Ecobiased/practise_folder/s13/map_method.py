def sq_num(x):
    return x**2


numbers = [1, 2, 3, 4]
sq_list = map(sq_num, numbers)
print("sq_list", list(sq_list))