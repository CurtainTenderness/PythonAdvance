"""
闭包：
    1.函数内部嵌套函数
    2.函数内部可以访问外部函数局部变量，并且保存变量
    3.外部函数将内部函数返回
"""
def fun1(a):
    def fun2(b):
        return a+b
    return fun2
f1=fun1(10)
f2=fun1(20)
print(f1(1))
print(f2(1))