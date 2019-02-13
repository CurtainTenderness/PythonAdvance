# 可以直接作用于for 循环的数据类型有以下几种：
# 一类是集合数据类型，如list、tuple、dict、set、str
# 一类是generator，包括生成器和带yield的generator function
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable


# 判断是否可以迭代
from collections.abc import Iterable
# True 说明可以迭代，False 说明不能迭代
# print(isinstance([], Iterable))
# print(isinstance({}, Iterable))
# print(isinstance("asd", Iterable))
# print(isinstance((x for x in range(10)), Iterable))
# print(isinstance(100,Iterable))



# 迭代器
# 可以被next()函数调用并不断返回下一个值的对象
# 称为迭代器：Iterator
# 可以使用isinstance()判断一个对象是否是Tterator对象
from collections.abc import Iterator

print(isinstance((x for x in range(10)), Iterator))