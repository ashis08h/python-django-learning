from functools import lru_cache
import time


@lru_cache
def func(n):
    time.sleep(2)
    return 5*n


print(func(5))
print(func(5))
print(func(5))