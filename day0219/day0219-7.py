"""
在函数内部赋值的局部变量，不能使用global访问到
多个线程可以共享主线程数据
"""

from threading import Thread

def threadmain():
    global num
    num=20
    print("子线程",num)



if __name__=="__main__":
    num = 10
    thread = Thread(target=threadmain)
    thread.start()
    thread.join()
    print("finish")
    print(num)

"""
多线程：内存独立，共享数据需要用queue
多进程：内存不独立，本身就能共享数据
"""