# # 1，实现基础闭包语法
# def checkuser():
#     a=1
#     def check():
#         b=3
#         return a+b
#     return check
# s1=checkuser()()
# print(s1)

# # 2，实现需求：
# # 给订单列表，用户余额两个函数添加装饰函数，能够完成权限验证功能
#
# def checkuser(fun):
#     def check():
#         name=input("请输入你的姓名")
#         if name=="wrg":
#             fun()
#         else:
#             print("验证失败")
#     return check
# @checkuser
# def showlist():
#     print("订单列表")
# @checkuser
# def showmoney():
#     print("余额")
#
# showlist()
# showmoney()


# # 3，编写可以实现任意多个参数的万能装饰器
# def checkuser(fun):
#     def check(*args,**kwargs):
#         name=input("请输入你的名字")
#         if name=="wrg":
#             return fun(*args,**kwargs)
#     return check
# @checkuser
# def showlist(n,m):
#     print("这本书一共"+str(n)+"页，我看到了"+str(m)+"页")
# @checkuser
# def showpay():
#     return "这本书价钱为20元"
# @checkuser
# def showdict(pirct=20):
#     print("价钱为：",pirct)
# showlist(200,30)
# print(showpay())
# showdict(pirct=30)



# # 4，实现一个装饰器能够统计多个函数的性能消耗
# import time
# def checkuser(fun):
#     a=time.time()
#     time.sleep(1)
#     def check():
#         fun()
#         b=time.time()
#         print(b-a)
#     return check
# @checkuser
# def showlist():
#     print("程序运行时间为")
# showlist()




# # 5，结合flask模块完成能够显示多个页面的基本后端
# from flask import Flask,render_template
# app=Flask(__name__)
# @app.route("/")
# def theFirst():
#     return "首页"
# @app.route("/wrg")
# def wrg():
#     return "wrg的个人材料"
# @app.route("/wrg/day")
# def wrgday():
#     return "wrg的生日"
# @app.route("/wrg/info")
# def wrginfo():
#     return render_template("pay.html")
# app.run()

