"""
多线程
"""
import time
from threading import Thread
def prt():
    "模拟耗时操作，比如下载资源"
    time.sleep(1)
    print("+")
def singspendtime():
    "单线程耗时"
    start = time.time()
    for i in range(5):
        prt()
    end = time.time()
    print("时间消耗", end - start)
def threadmain():
    prt()
def multithread():
    treadlist=[]
    "创建线程"
    start=time.time()
    for r in range(5):
        t1 = Thread(name="multithread", target=threadmain)
        t1.start()
        treadlist.append(t1)
        print(t1.name)
    # 主进程执行完毕，子进程还没有执行完
    # 如果想要统计时间消耗需要等待五个子进程执行完毕
    # 确保每个子线程都join才能统计结束时间

    # 阻塞主进程（需要的子线程都已经创建成功）
    for t in treadlist:
        t.join()
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





