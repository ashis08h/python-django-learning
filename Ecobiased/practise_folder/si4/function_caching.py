from functools import lru_cache
import time


@lru_cache()
def func(n):
    time.sleep(5)
    return n*5


print(func(5))
print(func(5))
print(func(5))
print(func(5))
