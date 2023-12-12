import threading
import time


def get_delay(seconds):
    print(f"This method delayed to {seconds}")
    time.sleep(seconds)


thread1 = threading.Thread(target=get_delay, args=[4])
thread2 = threading.Thread(target=get_delay, args=[5])
thread3 = threading.Thread(target=get_delay, args=[6])

thread1.start()
thread2.start()
thread3.start()
