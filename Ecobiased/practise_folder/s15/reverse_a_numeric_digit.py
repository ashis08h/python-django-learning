num = 4560001
rev_num = 0
while num > 0:
    last_digit = num % 10 # get the last digit from number
    rev_num = rev_num * 10 + last_digit
    num = num // 10 # remove last digit from the number

print(rev_num)

