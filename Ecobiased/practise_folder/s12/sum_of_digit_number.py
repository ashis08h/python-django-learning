number = 123

sum_of_digit = sum(map(int, str(number)))
print(sum_of_digit)

sum_of_digit = 0

for num in str(number):
    sum_of_digit += int(num)

print(sum_of_digit)

dict1 = {'name': 'Ashish', 'dob':'20-12-2023'}
print('Ashish' in dict1.values())
print('ashish' in dict1.values())