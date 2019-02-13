# 新建2.py文件编码验证迭代器与可迭代的区别


from collections.abc import Iterable
from  collections.abc import Iterator
s1=["a","s","d"]
print(isinstance(s1, Iterable))
print(isinstance(s1, Iterator))
s2=iter(s1)
print(isinstance(s2, Iterator))


