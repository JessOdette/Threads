import threading
import time
import random

def blue_car():
    for i in range(3):
        print("Blue Car is running")
        time.sleep(1) 


def red_car():
    for i in range(3):
        print("Red Car is running")
        time.sleep(1)

flag = 1
while flag:
      t1 = threading.Thread(target=blue_car)
      t2 = threading.Thread(target=red_car)
      t1.start()
      t2.start()
      t1.join()
      t2.join()
      flag = 0