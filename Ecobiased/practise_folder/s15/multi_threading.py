import threading
import time


def func(n):
    print(n)
    time.sleep(n)


task1 = threading.Thread(target=func, args=[2])
task2 = threading.Thread(target=func, args=[3])
task3 = threading.Thread(target=func, args=[4])

task1.start()
task2.start()
task3.start()
