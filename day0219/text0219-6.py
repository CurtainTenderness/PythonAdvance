"""
线程
多个线程之间执行没有固定的先后顺序，需要抢占CPU资源
其实python多线程伪多线程，本质并不是并行的
"""
from threading import Thread
import time
def threadmain(name):
    while True:
        time.sleep(1)
        print(name,"执行了")
def main():
    tread1 = Thread(target=threadmain, args=("线程1",))
    tread2 = Thread(target=threadmain, args=("线程2",))
    tread1.start()
    tread2.start()

if __name__=="__main__":
    main()