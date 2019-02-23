"""
UDP Client
"""
import socket
# 常见UDP客户端
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 2发送数据到指定对象
SERVERADDRESS=("192.168.15.9",9000)
client.sendto("你好客户端".encode(encoding="utf-8"),SERVERADDRESS)
# 3,客户端
BUFFERSIZE=1024
while True:
    recvdata,recvaddr=client.recvfrom(BUFFERSIZE)
