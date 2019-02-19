from multiprocessing import Pool
import time
def processmain(num,l2):
    # print(num,l2222)
    time.sleep(1)
    print("begin")
    num=200
    l2.append(5)
    print("子进程执行完毕，子进程中num值为",num )
    print("子进程执行完毕，子进程中l2222值为",l2)
def main():
    num = 100
    l2 = [1, 2, 3]
    pool = Pool(5)
    # 将num传入需要添加：args=(num,)
    pool.apply_async(func=processmain, args=(num,l2))
    pool.close()
    pool.join()
    print("finish")
    print("主进程执行完毕，主进程中num值为", num)
    # 两个进程之间数据相互独立，相当于操作系统给两个进程分配了两个独立的内存
if __name__=="__main__":
    main()