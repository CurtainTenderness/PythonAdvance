#
# def checkaccess(fun):
#     def check():
#         name=input("请输入姓名")
#         if name=="ljk":
#             fun()
#         else:
#             print("验证不通过")
#     return check
#
# @checkaccess
# def getAge():
#     print("你猜——————")
# getAge()
#
# @checkaccess
# def goodsShop():
#     print("你要买啥")
# goodsShop()
#
# @checkaccess
# def playgame():
#     print("玩游戏")
# playgame()
# @checkaccess
# def aaa():
#     print("aaa")
# aaa()


"""
检测到需要执行的函数如：playgame等拥有@checkaccess
不执行playgame而是将playgame函数作为一个参数传入到
checkaccess方法，并执行checkaccess方法，将checkaccess
的执行结果返回，即将check的方法的引用返回，即实际执行的是
check方法
"""
# def checkuser(fun):
#     def check():
#         name=input("请输入你的姓名")
#         if name=="ljk":
#             print("验证通过")
#         else:
#             print("验证失败")
#     return check
# @checkuser
# def showList():
#     print("成功输出列表")
# showList()

def checkuser(fun):
    def check(*arge,**kwargs):
        name = input("请输入你的姓名")
        if name=="ljk":
            # print("正确")
            return fun(*arge,**kwargs)
        else:
            print("错误")
    return check
# *arge任意位数字显示
@checkuser
def showlist(n):
    print("显示成功第"+str(n)+"页")
@checkuser
def showlist1(n,m):
    print("显示成功第"+str(n)+"页,总共"+str(m)+"页")
# **kwargs显示任意字典
# 有返回值return的
@checkuser
def showgoods():
    return "hello"
showlist(3)
showlist1(5,15)
print(showgoods())

