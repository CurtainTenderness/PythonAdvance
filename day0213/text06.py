# """
# 生成器的第二种写法，常见一种函数写法
# 通过yield
# """
# def fun():
#     yield 10
#     yield 20
#     yield 30
#     return "hello"
# s1=fun()
# print(s1)
# print(type(s1))
# print(next(s1))
# print(next(s1))
# print(next(s1))
# # 如果想要在生成器中输出原始数据，需要用try
# try:
#     print(next(s1))
# except StopIteration as e:
#     print(e)



# a, b=0, 1
# print(a,b)
# a, b=b, a+b
# print(a,b)
# a, b=b, a+b
# print(a,b)
# a, b=b, a+b
# print(a,b)
# a, b=b, a+b
# print(a,b)

# 裴波那契算法
def fun(n):
    a, b=0, 1
    count=0
    yield a
    yield b
    while count<n:
        a, b=b, a+b
        yield b
        count+=1
    return "结束"
gend=fun(10)
# print(next(gend))
# print(next(gend))
# print(next(gend))
# print(next(gend))
while True:
    try:
        print(next(gend))
    except StopIteration as e:
        print(e)
        break






