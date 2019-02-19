from multiprocessing import Queue
from multiprocessing import ProcessError
q=Queue(3)
q.put(1)
q.put(2)
q.put(3)
# 空间内多少数据
print(q.qsize())
# 空间是否填充满
print(q.full())
print(q.empty())
