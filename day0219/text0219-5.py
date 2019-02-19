"""
多线程
"""
import time
from threading import Thread
def prt():
    "模拟耗时操作"
    time.sleep(1)
    print("+")
def singspendtime():
    "单线程耗时"
    start = time.time()
    for i in range(5):
        prt()
    end = time.time()
    print("时间消耗", end - start)
def threadmain(num):
    print(num)
def multithread():
    treadlist=[]
    "创建线程"
    start=time.time()
    for r in range(5):
        t1 = Thread(name="multithread", target=threadmain,args=(10,))
        t1.start()
        print(t1.name)
        treadlist.append(t1)
    end=time.time()

    print(end-start)
if __name__=="__main__":
    # singspendtime()
    multithread()

"""
结果
在单进程单线程情况下开启五次下载耗时为5秒钟
在单进程5个线程的情况下开启五次下载因为线程是并发的，所以只需要1秒钟就可以完成
"""





