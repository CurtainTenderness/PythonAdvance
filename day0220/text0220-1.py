"""
UDP Server
"""
import socket
# 1.创建UDP服务器
server =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 2绑定服务端的IP端口
SERVERADDRESS=("192.168.15.9",9000)
server.bind(SERVERADDRESS)
# 3开始使用阻塞方法接收信息
BUFFERSIZE  =1024
recvtdata,recvaddr=server.recvfrom(BUFFERSIZE)
print("收到了",recvaddr,"信息",recvtdata.decode("utf-8"))
server.sendto("我收到了你的消息".encode(encoding="utf-8"),recvaddr)
print("服务器收到了小溪并做出了响应")