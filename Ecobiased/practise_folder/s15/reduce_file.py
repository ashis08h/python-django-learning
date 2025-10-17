from functools import reduce


numbers = [1, 4, 3, 2]

result = reduce(lambda x, y:x+y, numbers)
print(result)

result1 = reduce(lambda x, y:x*y, numbers)
print(result1)

result2 = reduce(lambda x, y: x if x>y else y, numbers)
print(result2)

result3 = reduce(lambda x, y: x+y, numbers, 10)
print(result3)