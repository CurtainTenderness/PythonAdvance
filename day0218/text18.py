"""
元类用来创建类
type (类名字符串，父类列表，类中属性)
元类的用法：
私有属性：_name
不可访问实行：__name__
"""

# def move(self,_speed):
#     print("AI速度为",str(_speed))
#
# AI=type("AI",(object,),{"name":"ail","move":move})
# print(dir(AI))
# print(AI.__dict__)
#
# NPC=type("NPC",(AI,),{})
# print(NPC.__dict__)
# print(NPC.__bases__)
# python是动态语言，动态添加属性
"""
Python在创建NPC类时先不在内存中创建、 首先查看NPC中有__metaclass__这个属性吗
如果有， Python会通过__metaclass__创建一个名字为NPC的类(对象)
如果Python没有找到__metaclass__， 它会继续在AI（父类） 中寻找__metaclass__属性， 并尝试做和前面同样的操作。
如果Python在任何父类中都找不到__metaclass__， 它就会在模块层次中去寻找__metaclass__， 并尝试做同样的操作。
如果还是找不到__metaclass__,Python就会用内置的type来创建这个类对象
"""



"""
要求：所有的属性均要以小写类名+小写属性名
"""

"""
metaclass存储的方法才是真正类的创建过程
"""
def mydesignclass(curterclass,parentclassname,attridict):
    "使用这个方法去创建真正的NPC类"
    # print((curterclass,parentclassname,attridict))
    # # 将curterclass中的字母转换为小写字母
    # print(curterclass.lower())
    newclassattrdict={}
    for k,v in attridict.items():
        if not k.startswith("__"):
            newclassattrdict[curterclass.lower()+k.lower()]=v
    print(newclassattrdict)
    "在使用type创建类之前需要对原始类进行修改  比如属性重命名"
    return  type(curterclass,(),newclassattrdict)


class NPC(metaclass=mydesignclass):
    "npcspeed  npcname"
    Speed=10
    name="ail"

print(hasattr(NPC,"Speed"))
print(hasattr(NPC,"npcspeed"))