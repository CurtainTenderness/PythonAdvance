# # 1.自定义元类：
# # 实现功能：能够将所有属性更名为小写类名+小写属性名,
# # 如果存在属性名以temp开头的则删除该属性
# def mydesignclass(curentclass,parentclassname,attrdict):
#     newname={}
#     for k,v in attrdict.items():
#         if not k.startswith("temp") and not k.startswith("__"):
#             newname[curentclass.lower()+k.lower()]=v
#     print(newname)
#     return type(curentclass,(),newname)
# class stu(metaclass=mydesignclass):
#     Name="weg"
#     Age=15

# 2.总结垃圾回收的三种机制
"""
垃圾回收
1，引用计数
2，标记清除（就是为了解决引用计数的循环引用问题）
    标记清除：在进行清除变量之后对每一个删除的对象引用计数-1
    如果引用计数变为0 就暂时放入死亡容器
    如果引用计数部位0 检测是否引用到了死亡容器容器中对象
    如果引用到了死亡容器对象，将死亡容器对象拿出来放入存活容器
标记清除:
    第一步查看删除对象后对象所在内存的引用计数，都减去1
    【1,2】 计数为 0 死亡容器
    【3,4】 计数为 0 死亡容器
     【5,6】 计数 为0  死亡容器
     【7,8 ，【5,6】】计数为1 存活容器

    第二步 遍历存活容器对象 查看是否引用到了死亡容器对象
    需要将【5,6】 从死亡容器中拿出放入存活容器

    分代收集: 目的是为了确定 对哪些对象进行标记清除
    每标记清除一次 称为1代 代数越高 证明存活能力强，执行标记清除频率低

    小整数对象与intern机制
    某些特定的对象引用计数为0 也不回收，而是放入对象池（用来存储小整数的池子）
    有了对象池：系统载频帆的使用小整数时 不需要每次开辟空间和回收空间
"""



# 4.
import hashlib
password=input("请输入密码：")
md5=hashlib.md5()
md5.update(password.encode("utf-8"))
print(md5.hexdigest())




#5. os.fork方法 os.getpid() os.getppid()方法使用案例
"""
import os 
pid =os.fork()
print("do")
if pid==0:
    print("child process pid %d"% os.getpid())
else:
    print("parent pid %d"% pid)
"""



# # 6，封装进程类MyProcess
# # 要求进程执行后输出“（进程名..执行了）”
# from multiprocessing import Process
# import os
# class MyProcess(Process):
#     def __init__(self):
#         Process.__init__(self)
#     def run(self):
#         print("pid %d ,processpid %d" % (os.getpid(),os.getppid()))
# if __name__=="__main__":
#     p = MyProcess()
#     p.start()
#     p.join()
#     print("进程"+"MyProcess"+"实现了")

# 7.使用进程池制作阻塞、非阻塞创建进程案例
# 阻塞
# from multiprocessing import Pool
# import os
# import time
# def fun(i):
#     print("pid %d,run %d"% (os.getpid(),i))
#     time.sleep(1)
# if __name__=="__main__":
#     pool=Pool(5)
#     start=time.time()
#     for i in range(100):
#         pool.apply(fun,(i,))
#     end=time.time()
#     print(end-start)
#     pool.close()
#     pool.join()
#     print("finish")

#非阻塞
# from multiprocessing import Pool
# import os
# import time
# def fun(i):
#     print("pid %d,run %d"% (os.getpid(),i))
#     time.sleep(1)
# if __name__=="__main__":
#     pool=Pool(5)
#     start=time.time()
#     for i in range(100):
#         pool.apply_async(fun,(i,))
#     end=time.time()
#     print(end-start)
#     pool.close()
#     pool.join()
#     print("finish")
