def square(x):
    return x**2


numbers = [1, 2, 3, 4]
sq_list = map(square, numbers)
print(list(sq_list))


def celcius_to_forenheight(temp):
    return (temp*(9/5)) + 32


temp_in_celcius = [0, 10, 20, 30]

temp_in_foreignheight = map(celcius_to_forenheight, temp_in_celcius)
print(list(temp_in_foreignheight))