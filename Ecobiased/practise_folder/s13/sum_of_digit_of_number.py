num = 123

sum_of_digit = sum(map(int, str(num)))
print("sum_of_digit", sum_of_digit)


sod = 0
for char in str(num):
    sod += int(char)

print(sod)

dict1 = {'name': 'Ashish', 'dob':'20-12-2023'}
print('ashish' in dict1.values())
print("Ashish" in dict1.values())

print('name' in dict1.keys())