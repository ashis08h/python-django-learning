import time
from functools import lru_cache


@lru_cache
def func(n):
    time.sleep(n)
    return 5*n


print(func(5))
print(func(5))
print(func(5))
print(func(4))
print(func(4))
print(func(4))
print(func(5))