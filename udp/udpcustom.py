import socket

HOST="localhost"
PORT=9999
ADDR=(HOST,PORT)
BUFSIZE=1024
udpCliSocket= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    udpCliSocket.sendto(data,ADDR)
    # 接收数据:
    print(udpCliSocket.recv(BUFSIZE).decode('utf-8'))
udpCliSocket.close()