from socket import *

HOST = '127.0.0.1'
PORT = 8003

s = socket(AF_INET, SOCK_STREAM)

s.connect((HOST, PORT))
s.send(bytes("111122223333444455", "utf-8"))
data = s.recv(1024)
print(data.decode())
s.close()
