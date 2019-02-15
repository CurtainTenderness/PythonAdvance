import time
def fun(f):
    def cost():
        start=time.time()
        f()
        end=time.time()
        print("耗时为"+str(end-start))
    return cost
# TODO 有利于以后找到自己没完善的地方利于修改，并且TODO后边一定要有空格，并且在git提交时会提醒有未完善的地方，但依旧可以提交
@fun
def costlist():
    n=[x for x in range(100000)]
    for r in n:
        print(r)
@fun
def costlist1():
    n=(x for x in range(100000))
    for r in n:
        print(r)
# costlist()
costlist1()