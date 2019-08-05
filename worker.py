# coding=utf-8

import threading

from context import singleton

l = threading.Lock()


class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        try:
            self.loop()
        finally:
            print("%s:thread error" % self.name)

    def loop(self):
        while True:
            print("%s:start" % self.name)
            l.acquire()
            try:
                print("%s:lock" % self.name)
                singleton.inc(self.name)
                print("%s:unlock" % self.name)
            finally:
                l.release()
            print("%s:over" % self.name)
