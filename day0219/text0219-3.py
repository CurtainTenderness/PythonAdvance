"""
使用Queue(队列)完成多进程共享数据（）
"""
from multiprocessing import Queue,Process
import time
q=Queue(5)
# block代表是否阻塞，timeout代表多久后放入
q.put(-3,block=True,timeout=3)
q.put(-2)
q.put(-1)
def read(q):
    while True:
        time.sleep(1)
        #q.get中的 timeout，当内存中没有内容是无法取出，规定时间后报错
        print("队列中取出数据",q.get(timeout=3))
def write(q):
    for i in range(10):
        q.put(i)

if __name__=="__main__":
    pr = Process(target=read,args=(q,))
    pw = Process(target=write,args=(q,))
    pr.start()
    pw.start()
    pr.join()
    pw.join()
    print("finish")

"""
进程执行后q放入-2，-1
写进程放入0 1 2此时队列中有-2 -1 0 1 2
之后一秒取出一个-2，添加一个3
之后每一秒回取出一个首位数据，在末未添加一个数据
"""