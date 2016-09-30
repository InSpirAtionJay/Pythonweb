from socket import *

HOST = "localhost"
PORT = 21567
ADDR = (HOST, PORT)
BUFSIZE = 1024

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)                 # ipv4 面向连接的流套接字
    tcpCliSock.connect(ADDR)
    data = input()
    if not data:
        break
    tcpCliSock.send((data + "\n\r").encode("utf-8"))          # 添加文件结束符\n\r
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print(data.strip().decode("utf-8"))
    tcpCliSock.close()
