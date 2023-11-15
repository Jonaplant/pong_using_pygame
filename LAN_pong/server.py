import socket
from _thread import *
import pickle
from game import Game

server = "10.192.137.195"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print("waiting for a connection, server started")


def threaded_client(conn, player):
    conn.send(str.encode(str(player)))
    reply = ""

    while True:
        try:
            data = pickle.load(conn.recv(1024))

            if not data:
                print("no data received")
                break
            else:
                reply = data
                conn.sendall(pickle.dumps(reply))

        except error as err:
            print(err)
            break

    player -= 1
    conn.close()


player = 0
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    player += 1
    game = Game()
    if not player > 1:
        start_new_thread(threaded_client, (conn, player))
