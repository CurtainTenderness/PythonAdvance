import types
class Person(object):
    """
    添加类方法
    """
    isopen=True
    def __init__(self,_hp):
        self.hp=_hp

s1=Person(100)
# 动态添加实例方法，需要引入types模块，用types.MothodType添加
def setname(self):
    return "ljk"
s1.setname=types.MethodType(setname,s1)
print(s1.setname())

# 动态添加类方法
@classmethod
def getn(cls):
    return cls.__doc__
Person.getl=getn
print(Person.getl())