# coding=utf-8
from worker import Worker

if __name__ == '__main__':
    max_thread = 3  # 测试线程数量

    threads = [lambda: [Worker("t" + str(i)) for i in range(max_thread)]][0]()  # 线程列表

    [t.start() for t in threads]    # 启动线程

    [t.join() for t in threads]     # 等待子线程结束 但是子线程里面是死循环 所以你懂的
