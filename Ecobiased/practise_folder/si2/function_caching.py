from functools import lru_cache
import time


@lru_cache(maxsize=None)
def add_delay(sec):
    time.sleep(5)
    return f"It is {sec}"


print(add_delay(5))
print(add_delay(5))
print(add_delay(5))
print(add_delay(5))
print(add_delay(5))

