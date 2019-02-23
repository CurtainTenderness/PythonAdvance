"""
TCP服务端
"""
import socket
# 创建服务端通信对象
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# p配置IP端口
SERRVERADDR=("192.168.15.9",9999)
server.bind(SERRVERADDR)
# 开始监听
server.listen()
print("服务端启动")

# 获取客户端accept
while True:
    client, clientaddr = server.accept()
    print("客户端", clientaddr, "链接上了")
