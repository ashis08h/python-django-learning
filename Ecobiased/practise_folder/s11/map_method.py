# Example 1

def square(x):
    return x**2


input_list = [1, 2, 3, 4]


result_list = map(square, input_list)
print(tuple(result_list))


# Example 2

def convert_celcius_to_foreignheight(celcius):
    temp_in_foreignheight = (celcius * 9/5) + 32
    return temp_in_foreignheight


temp_in_celcius = [0, 10, 20, 30]

temp_in_foreignheight = map(convert_celcius_to_foreignheight, temp_in_celcius)
print(list(temp_in_foreignheight))