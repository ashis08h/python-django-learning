from functools import reduce


numbers = [1, 2, 3, 4, 5]

result = reduce(lambda x, y:x+y, numbers)
print("result", result)

result = reduce(lambda x, y:x*y, numbers)
print("result", result)

result = reduce(lambda x, y:x if x>y else y, numbers)
print("result", result)

result = reduce(lambda x, y:x+y, numbers, 10)
print("result", result)