# coding=utf-8
import threading
import time


class SingletonData:

    def __init__(self):
        self.i = 0

    def inc(self, worker):
        print("%s:inc from %d" % (worker, self.i))
        time.sleep(3)
        self.i = self.i + 1
        print("%s:inc to %d" % (worker, self.i))


singleton = SingletonData()
