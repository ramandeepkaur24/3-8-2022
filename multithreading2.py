from threading import *
from threading import Thread
import time
#start=time.time()
def f1():

    for x in range(10):
        print(x)
        time.sleep(5)

def f2():
    for y in range(10,15):
        print(y)
        time.sleep(4)
t1=Thread(target=f1,name="thread1")
t1.start()
t2=Thread(target=f2,name="thread2")
t2.start()
#end=time.time()
#print('time taken',end-start)