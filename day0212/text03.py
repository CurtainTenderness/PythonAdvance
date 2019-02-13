# 1，编写代码验证
# 类可以操作类属性，不可以操作实例属性
# 实例可以操作实例属性，可以操作类属性
# 2，新建Shop类
# 编写类说明
# 编写类属性isopen（是否开张）
# 编写实例属性shoplist（ 商品列表）
# 编写类方法 返回字符串为类说明
# 编写实例方法添加商品方法
# 编写实例方法获取商品列表方法
# 编写静态方法功能随意
# 3，编写代码验证
# 动态的添加类属性
# 动态的添加实例属性
# 说明类与实例以及类属性实例属性相互调用关系




# # 第一题
# class person(object):
#     name="ljk"
#     def years(self,_age):
#         self.age=_age
# q1=person()
# print(q1.name)
# q1.old=18
# person.name="ljk1"
# print(q1.name)
# person.old=20
# print(q1.old)
# q1.old=23
# print(q1.old)
# q1.name="ljk2"
# print(q1.name)


# 第二题
# class Shop(object):
#     """
# 商店是每个城市的，方便了人们的生活
#
#     """
#     isopen=True
#     def shoplist(self,_name,_price):
#         self.name=_name
#         self.price=_price
#
#     @classmethod
#     def printclassinfo(cls):
#         print(cls.__doc__)
#     @staticmethod
#     def information():
#         print("这是一个商店")
#
# s1=Shop()
# print(s1.isopen)
# s1.shoplist("苹果","10元")
# print(s1.name)
# s1.printclassinfo()
# s1.time="3个月"
# print(s1.time)
# print(s1.name,s1.price,s1.time)
# s1.information()



# 第三题
class Person(object):
    isOpen=True
    def getname(self,_name):
        self.name=_name
s1=Person()
# 动态添加类属性
Person.age=15
print(s1.age)
s1.getname("ljk")
print(s1.name)

# 动态添加实例属性
s1.classname="三年级"
print(s1.classname)







