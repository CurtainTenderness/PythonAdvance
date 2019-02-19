"""
多线程共享全部对象产生的问题
"""


from threading import Thread,Lock
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