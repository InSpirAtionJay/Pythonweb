#!/usr/bin/bin python

from socketserver import TCPServer as TCP, StreamRequestHandler as SRH
from time import ctime

HOST = ""
PORT = 21567
ADDR = (HOST, PORT)


class MyRequestHandler(SRH):
    def handle(self):
        print("...connected from:", self.client_address)
        data = self.rfile.readline().decode("utf-8")
        if data.strip():                                    # 判断是否全为空（空串）
            try:
                answer = eval(data)
                self.wfile.write((ctime() + "\n" + data.strip() + "=" + str(answer)).encode("utf-8"))
            except Exception as e:
                self.wfile.write((ctime() + "\n" + "expression error").encode("utf-8"))
        else:
            self.wfile.write((ctime() + "\n" + "None:表达式为空").encode("utf-8"))


tcpServer = TCP(ADDR, MyRequestHandler)
print("waiting for connection")
tcpServer.serve_forever()
