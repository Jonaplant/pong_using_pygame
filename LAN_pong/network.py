import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "10.192.137.195"
        self.server = " 192.168.1.121"
        self.port = 5555
        self.addr = (self.host, self.port)
        self.player_data = self.connect()

    def get_player_data(self):
        return self.player_data

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            print("failed to connect client")

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)

