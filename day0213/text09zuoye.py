# 1，新建1.py文件
# 使用yield得到生成器
# 创建列表，元组，字典，字符串，整形
# 判断以上类型是否可以迭代，是否是迭代器
# 如果是迭代器则使用next得到所有内容



def fun():
    yield 10
    yield 20
s1=fun()
print(next(s1))
print(next(s1))
from collections.abc import Iterable

print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance({"字典":"用法"}, Iterable))
print(isinstance("asd", Iterable))
print(isinstance(100, Iterable))
print(isinstance((x for x in range(10)), Iterable))

from  collections.abc import Iterator

print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance({"字典":"用法"}, Iterator))
print(isinstance("asd", Iterator))
print(isinstance(100, Iterator))
print(isinstance((x for x in range(10)), Iterator))
s1=(x for x in range(10))
while True:
    try:
        print(next(s1))
    except StopIteration as e:
        print(e)
        break