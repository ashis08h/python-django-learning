number = 123
sum_of_digit = sum(map(int, str(number)))
print(sum_of_digit)

num_to_str = str(number)

sum_of_digit = 0
for num in num_to_str:
    sum_of_digit += int(num)

print(sum_of_digit)

# how to check if a key present in dict or not?

dict1 = {'name': 'Ashish', 'dob': '30-12-1995'}
print('Ashish' in dict1.values())

