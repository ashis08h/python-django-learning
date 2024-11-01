import threading
import time


def add_delay(n):
    print(n)
    time.sleep(n)


t1 = threading.Thread(target=add_delay, args=[2])
t2 = threading.Thread(target=add_delay, args=[3])
t3 = threading.Thread(target=add_delay, args=[4])

t1.start()
t2.start()
t3.start()