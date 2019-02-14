"""
类修饰器
类修饰器通过构造方法以及call 方法实现
当程序检测到函数有类修饰器是没有直接执行函数，将函数作为参数传递给类的构造函数
当函数调用时执行类的call函数
"""
class checkuser():
    def __init__(self,fun):
        print("构造方法")
        self.f=fun
    def __call__(self, *args, **kwargs):
        print("__call方法")
        self.f()
# cu=checkuser()
"使用实例名（）会执行类内部call方法"
# cu()

@checkuser
def showlist():
    print("战士")
showlist()