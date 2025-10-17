def sq_number(num):
    return num **2


numbers = [1, 2, 3, 4, 5]


sq_numbers = list(map(sq_number, numbers))
print(sq_numbers)

sq_list2 = list(map(lambda x:x**2, numbers))
print(sq_list2)