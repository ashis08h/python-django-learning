import threading
import time


def func(n):
    print(n)
    time.sleep(n)


t1 = threading.Thread(target=func, args=[2])
t2 = threading.Thread(target=func, args=[3])
t3 = threading.Thread(target=func, args=[4])

t1.start()
t2.start()
t3.start()
