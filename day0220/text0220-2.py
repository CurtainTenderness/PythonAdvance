from socket import *
sc=socket(AF_INET,SOCK_DGRAM)
addr=("192.168.15.9",9000)
while True:
    datastr=input("请输入要发送的内容")
    if datastr.__eq__("exit"):
        break
    dataencode=datastr.encode(encoding="utf-8")
    sc.sendto(dataencode,addr)
    receivecode,saddr=sc.recvfrom(1024)
    recevidata=receivecode.decode(encoding="utf-8")
    print(recevidata,saddr)
sc.close()
print("finish")