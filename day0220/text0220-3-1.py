"""
TCP的客户端
"""
import socket
# 创建客户端socket对象
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 连接到服务端
SERVERADDR = ("192.168.15.9", 9999)
client.connect(SERVERADDR)
while True:
    data = input("请输入发送的内容")
    client.send(data.encode(encoding="utf-8"))
    data1=client.recv(1024)
    print(data1.decode(encoding="utf-8"))