"""
Flask:使用装饰器
1.pip install flask
2.from flask import Flask
3.创建一个应用
4。注册路由（URL）
5.启动服务
"""
from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def index():
    return "首页"
@app.route("/ljk")
def ljkinfo():
    return "江坤的主页"
@app.route("/ljk/pay")
def ljkpay():
    return "每天都困"
@app.route("/ljk/num")
def ljkunm():
    return render_template("pay.html",name="ljk1")

app.run()
