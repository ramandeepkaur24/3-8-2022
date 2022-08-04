from threading import *
from threading import Thread
class A(Thread):
    def run(self):
        for x in range(5):
            print(x)
ob=A()
ob.start()