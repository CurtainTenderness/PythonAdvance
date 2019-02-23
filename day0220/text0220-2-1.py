from socket import *
ss=socket(AF_INET,SOCK_DGRAM)
saddr=("192.168.15.9",9000)
ss.bind(saddr)
while True:
    detaenconde,caddr=ss.recvfrom(1024)
    datastr=detaenconde.decode(encoding="utf-8")
    print(datastr)
    str=input("输入发送内容")
    if str.__eq__("exit"):
        break
    strcode=str.encode(encoding="utf-8")
    ss.sendto(strcode,caddr)
ss.close()
print("finish")