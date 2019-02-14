
def checkaccess(fun):
    def check():
        name=input("请输入姓名")
        if name=="ljk":
            fun()
        else:
            print("验证不通过")
    return check

@checkaccess
def getAge():
    print("你猜——————")
getAge()

@checkaccess
def goodsShop():
    print("你要买啥")
goodsShop()

@checkaccess
def playgame():
    print("玩游戏")
playgame()


"""
检测到需要执行的函数如：playgame等拥有@checkaccess
不执行playgame而是将playgame函数作为一个参数传入到
checkaccess方法，并执行checkaccess方法，将checkaccess
的执行结果返回，即将check的方法的引用返回，即实际执行的是
check方法
"""