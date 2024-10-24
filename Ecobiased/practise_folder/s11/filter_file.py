def is_even(a):
    return a % 2 == 0


def is_even1(a):
    if a % 2 == 0:
        return True
    else:
        return False


numbers = [1, 2, 3, 4, 5, 0]


# we can use both the methods result will not change.
even_list = filter(is_even1, numbers)
print(list(even_list))
