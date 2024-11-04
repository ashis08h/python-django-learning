num = 4567
reversed_num = 0
while num > 0:
    # get the last digit of num by modulous division
    last_digit = num % 10
    reversed_num = reversed_num * 10 + last_digit
    # remove the last digit from num by integer division.
    num = num // 10


print(reversed_num)