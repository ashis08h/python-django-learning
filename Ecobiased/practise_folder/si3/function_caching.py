from functools import lru_cache
import time


@lru_cache(maxsize=None)
def fun(n):
    time.sleep(5)
    return 5*n


print(fun(5))
print(fun(15))
print(fun(5))
print(fun(25))
print(fun(5))
