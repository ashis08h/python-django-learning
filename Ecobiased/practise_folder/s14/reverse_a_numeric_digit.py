num = 4567
rev_num = 0

while num > 0:
    last_digit = num % 10
    rev_num = rev_num *10 + last_digit
    num = num // 10

print(rev_num)