from multiprocessing import Pool,Manager,Queue
import time

# 从队列中取数据
def read(q):
    while True:
        time.sleep(2)
        r=q.get()
        print("取到",r,"剩余",q.qsize())
# 向对列中添加数据
def write(q):

    while True:
        time.sleep(1)
        q.put(0)

if __name__=="__main__":
    q=Manager().Queue(500)
    pool=Pool(2)
    pool.apply_async(func=write,args=(q,))
    pool.apply_async(func=read, args=(q,))
    pool.close()
    pool.join()
    print("finish")
