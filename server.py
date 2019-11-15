from socket import *
import threading
import time

HOST = '127.0.0.1'
PORT = 8003

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)


class ThreadedServer(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.conn = conn

    def run(self):
        while True:
            data = self.conn.recv(1024)
            if not data:
                break
            time.sleep(5)
            if "13" in data.decode():
                self.conn.send(bytes("Not OK", "utf-8"))
            else:
                self.conn.send(bytes("OK", "utf-8"))


while True:
    (connection, addr) = s.accept()
    print("Connection: ", connection)
    newThread = ThreadedServer(connection)
    newThread.start()
