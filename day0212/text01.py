"""
类方法： 需要使用@classmethod方法声明 第一个参数为cls 可以访问类相关比如 类说明
实例方法： 方法的第一个参数为self , 用来操作实例属性
静态方法：需要使用@staticmethod声明，和类无关
"""
class Person(object):
    """
    学习python高级，前边的基本忘完了
    """
    "实例方法"
    def __init__(self,_name):
        self.name=_name
    "类方法"
    @classmethod
    def printclassinfo(cls):
        print(cls.__doc__)
    "静态方法"
    @staticmethod
    def end():
        print("假期已经结束了")
s1=Person("王二狗")
print(s1.name)
s1.printclassinfo()
s1.end()
