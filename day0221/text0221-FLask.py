"""
使用Flask 进行HTTP编程
"""
from flask import Flask,render_template

app=Flask(__name__)
@app.route("/")
@app.route("/list")
def list():
    return render_template("list.html")
@app.route("/detail")
def deail():
    return render_template("detail.html")
@app.route("/index")
def index():
    return render_template("index.html")



app.run()