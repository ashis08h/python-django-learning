num = 123

sum_of_digit = sum(list(map(int, str(num))))
print("sum_of_digit", sum_of_digit)


sum = 0

for digit in str(num):
    sum += int(digit)

print(sum)

dict1 = {'name': 'Ashish', 'dob':'20-12-2023'}
print("Ashish" in dict1.values())

print("ashish" in dict1.values())
print("ashish" in dict1.keys())
print("name" in dict1.keys())


