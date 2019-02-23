"""
TCP客户端
"""
import socket
from threading import Thread

# 线程
# 接收信息
def recvThread():
    SERREVRADDR=(1024*1024)
    while True:
        databety=client.recv(SERREVRADDR)
        if len(databety)==0:
            client.close()
            break
        else:
            datastr=databety.decode("gbk")
            print(datastr)


# 发送信息
def sendThread():
    while True:
        if client._closed:
            break
        else:
            sendname=input("发送对象为")
            sendstr = input("请输入你要发送的内容")
            sendall=sendname+"|"+sendstr
            sendbety = sendall.encode("gbk")
            client.send(sendbety)



# 常见套字链接
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 链接服务器
serverIP=("192.168.15.9",9999)
client.connect(serverIP)

# 传输姓名
cliname=input("请输入你的姓名")
clinamestr=cliname.encode(encoding="gbk")
client.send(clinamestr)
#通过线程 收发与服务器之间的信息
terecv=Thread(target=recvThread)
terecv.start()
tesend=Thread(target=sendThread)
tesend.start()
