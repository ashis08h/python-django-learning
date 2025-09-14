def square_list(n):
    return n**2


numbers = [1, 2, 3, 4, 5]

sq_list = list(map(square_list, numbers))
print("sq_list", sq_list)


sq_list1 = tuple(map(lambda x:x**2, numbers))
print("sq_list1", sq_list1)