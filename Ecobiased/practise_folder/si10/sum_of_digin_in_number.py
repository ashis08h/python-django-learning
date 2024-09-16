# method 1
num1 = 123
sum_pf_digit = sum(map(int, str(num1)))
print(sum_pf_digit)

# method 2

num_str = str(num1)
print(num_str)


def sum_of_digit():
    total = 0
    for digit in num_str:
        print(digit)
        total += int(digit)
    return total


print(sum_of_digit())

# method 3

num2 = 123
digit_sum_list = list(map(int, str(num2)))
print("digit_sum_list", digit_sum_list)
print("digit_sum", sum(digit_sum_list))

# repeat method 1

num3 = 123
digit_sum = sum(map(int, str(num3)))
print("digit_sum", digit_sum)