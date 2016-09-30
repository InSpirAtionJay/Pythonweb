import socket
import threading

import time

HOST = ""                                     # 主机ip为空表示任何可用的客户端ip地址
PORT = 9997                                   # 端口号
BUFSIZE = 1024                                # 传输最大字节
ADDR = (HOST, PORT)                           # ip+端口号构成通信地址

tcpServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 建立套接字
tcpServerSocket.bind(ADDR)                    # 绑定套接字和
tcpServerSocket.listen(5)                     # 最大并发客户端数


def tcp_link(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(BUFSIZE)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('%s Hello, %s!' % (time.ctime(),data.decode('utf-8'))).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


while True:
    print('Waiting for connection...')
    # 接受一个新连接:
    tcpClientSocket, addr = tcpServerSocket.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcp_link, args=(tcpClientSocket, addr))
    t.start()
