
from threading import *
from threading import Thread
import time
start=time.time()
def f1():
  #  start=time.time()
    for x in range(10):

        time.sleep(5)
        print(x)

t1=Thread(target=f1,name="thread1")
t1.start()
end=time.time()
print('time taken',end-start)