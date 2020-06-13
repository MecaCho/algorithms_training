import socket

class Server():
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def start_server(self):
        add = (self.host, self.port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(add)
        sock.listen(5)


        while True:
            con, addr = sock.accept()

            while True:
                data = con.recv(2048)
                if len(data) > 0:
                    msg = "server recv data: {}.".format(data)
                    print(msg)
                    con.sendall("i have received: {}".format(data).encode("utf-8"))
                else:
                    print("received None")
                    break
            con.close()


class Client():
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def send(self):
        add = (self.host, self.port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(add)

        msg = "hello world"
        sock.sendall(msg.encode('utf-8'))

        data = sock.recv(32)
        res = "client receive msg: {}".format(data)
        print(res)
        while len(data) > 0:
            data = sock.recv(32)
            res = "client receive msg: {}".format(data)
            print(res)
        sock.close()


if __name__ == '__main__':
    server = Server("127.0.0.1", 8100)
    server.start_server()