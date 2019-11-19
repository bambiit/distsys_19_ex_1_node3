from socket import *
import threading

HOST = ''
PORT = 8003
fraud_db = ["111122223333444455", "987698769876987698"]

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
            res = "THIS BANK ACCOUNT IS IN THE DATABASE OF FRAUD" if data.decode() in fraud_db else "OK"
            self.conn.send(bytes(res, "utf-8"))


print("Server is running...")
while True:
    (connection, addr) = s.accept()
    print("Connection from {} has been established!".format(addr))
    newThread = ThreadedServer(connection)
    newThread.start()
