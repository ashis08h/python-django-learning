def is_even(num):
    return num % 2 == 0


def is_even1(num):
    if num % 2 == 0:
        return True
    else:
        return False


numbers = [1, 2, 3, 4, 5, 0]

even_list = filter(is_even, numbers)
print(list(even_list))

even_list2 = filter(is_even1, numbers)
print(list(even_list2))