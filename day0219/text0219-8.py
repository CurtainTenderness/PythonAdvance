"""
多线程共享全部对象产生的问题
GIL锁：全局解释锁
互斥锁：资源互斥锁：线程想要访问某个资源前给资源加锁，加锁成功就可以访问
加锁失败，需要陷入等待直到加锁成功
"""


from threading import Thread,Lock
# 得到一把锁
lock=Lock()
num=0
def fun():
    global num
    for i in range(1000000):
        "添加互斥锁"
        lock.acquire()
        num+=1
        "解除互斥锁"
        lock.release()
def main():
    t1=Thread(target=fun)
    t1.start()
    t1.join()
    print(num)
    t2=Thread(target=fun)
    t2.start()

    t2.join()
    print(num)
if __name__=="__main__":
    main()

"""
多进程：内存独立，需要共享数据就是用Queue
多线程：内存不独立本身就是共享数据但产生线程不安全数据
"""