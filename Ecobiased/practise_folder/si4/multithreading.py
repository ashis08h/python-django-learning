import threading
import time


def get_delay(n):
    print(n)
    time.sleep(n)


t1 = threading.Thread(target=get_delay, args=[5])
t2 = threading.Thread(target=get_delay, args=[6])
t3 = threading.Thread(target=get_delay, args=[4])

t1.start()
t2.start()
t3.start()