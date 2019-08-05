# coding=utf-8
from worker import Worker

if __name__ == '__main__':
    _ = [th for th in [t for t in [lambda: [Worker("t_" + str(i)) for i in range(3)]][0]() if
                       not t.setDaemon(True) and not t.start()] if
         not th.join()]
