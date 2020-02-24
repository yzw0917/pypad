from multiprocessing import Process
from threading import Thread
import os

def func():
    print('hello',os.getpid())

if __name__ == '__main__':
    # 在主进程开启多个线程，每个线程都跟主进程pid一样
    t1 = Thread(target=func)
    t2 = Thread(target=func)
    t1.start()
    t2.start()
    print('thread主线程/主进程pid:',os.getpid())

    # 开个多个子进程，每个进程都有不同的pid：
    p1 = Process(target=func)
    p2 = Process(target=func)
    p1.start()
    p2.start()
    print('Process主线程/主进程pid:', os.getpid())