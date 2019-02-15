"""
'='    简单的拷贝引用，拷贝内存地址，列表外层拷贝引用，内层也拷贝引用
'浅拷贝'   外层是拷贝的是值，创建新的内存，内层引用
'深拷贝'   外层，内层都是拷贝的值,并且创建一个新的内存
id()   打印对象内存地址
"""
# # 1. "="
# l=[1,2,[3,4]]
# l2=[1,2,[3,4]]
# l3=l
# l3.append(5)
# # l与l2内容相同，但地址不同
# # l与l3内容相同，地址也相同
# print(id(l))
# print(id(l2))
# print(id(l3))
# # 由于l与l3的地址相同，在l3 中添加一个数即是想这个地址添加了一个数，
# # 相同的地址，所以输出的内容是相同的
# print(l)
# print(l3)

# # 2."浅拷贝"
# import copy
# l=[1,2,[3,4]]
# l2=copy.copy(l)
# # l2是由l拷贝过来的，内容相同，但创建了一个新的地址，所以地址不同
# print(id(l))
# print(id(l2))
# # 由于l与l2外层地址不同，所以l外层中添加一个数，l2中不添加
# l.append(5)
# print(l)
# print(l2)
# #浅拷贝情况下 l与l2 内层地址相同，
# print(id(l[2]))
# print(id(l2[2]))
# l2[2].append(3.5)
# print(l)
# print(l2)

# 3.深拷贝
import copy
l=[1,2,[3,4]]
l2=copy.deepcopy(l)
# 深拷贝，外层拷贝值，创建一个新的内存
print(id(l),id(l2))
l.append(5)
print(l)
print(l2)
# 深拷贝，内层也拷贝值，创建一个新的内存
print(id(l[2]),id(l2[2]))
l2[2].append(3.5)
print(l)
print(l2)
