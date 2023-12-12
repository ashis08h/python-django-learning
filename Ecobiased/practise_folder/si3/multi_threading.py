import threading
import time


def func(n):
    print(f"The sleep time is {n} seconds.")
    time.sleep(n)


t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[5])
t3 = threading.Thread(target=func, args=[6])

t1.start()
t2.start()
t3.start()