import socket

HOST = "222.20.35.137"
PORT = 9997
BUFSIZE = 1024
ADDR = (HOST, PORT)

# 建立套接字
tcpCliSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
tcpCliSocket.connect(ADDR)

# 接收欢迎消息:
print(tcpCliSocket.recv(BUFSIZE).decode('utf-8'))
for data in ['Michael'.encode("utf-8"), '小明Dylan'.encode("utf-8"), 'Sarah'.encode("utf-8")]:
    # 发送数据:
    tcpCliSocket.send(data)
    print(tcpCliSocket.recv(BUFSIZE).decode('utf-8'))
tcpCliSocket.send(b'exit')
tcpCliSocket.close()
