from functools import lru_cache
import time


@lru_cache()
def fx(n):
    time.sleep(5)
    return 20*n


print(fx(5))
print(fx(15))
print(fx(25))
print(fx(35))
print(fx(45))
