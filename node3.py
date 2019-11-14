from socket import *

HOST = '127.0.0.1'
PORT = 8003

s = socket(AF_INET, SOCK_STREAM)

s.bind((HOST, PORT))
s.listen(1)

while True:
    (conn, addr) = s.accept()
    data = conn.recv(1024)
    if not data:
        break
    if "13" in data.decode():
        conn.send(bytes("Not OK", "utf-8"))
    else:
        conn.send(bytes("OK", "utf-8"))
conn.close()
