import socket

class Client():
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def send(self):
        add = (self.host, self.port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(add)

        msg = "hello world"
        sock.sendall(msg)
        data = sock.recv(2048)
        res = "client receive msg: {}".format(data)
        print(res)

if __name__ == '__main__':
    client = Client("127.0.0.1", 8100)
    client.send()
