import socket
from time import ctime

HOST=""
PORT=9999
ADDR=(HOST,PORT)
BUFSIZE=1024

udpSerSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpSerSocket.bind(ADDR)
print('Bind UDP on 9999...')
while True:
    data,addr=udpSerSocket.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    udpSerSocket.sendto(b'[%s] Hello, %s!' % (ctime().encode("utf-8"),data), addr)

