num = 123

sum_of_num = sum(map(int, str(num)))
print("num", sum_of_num)

som = 0
for char in str(num):
    som += int(char)

print(som)


dict1 = {'name': 'Ashish', 'dob':'20-12-2023'}
print("ashish" in dict1.values())
print("Ashish" in dict1.values())

print("Ashish" in dict1.keys())