import socket
from _thread import *
import pickle
from player import Player

port = 5555
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


class Server:
    added_players = 0
    player_count = 0
    players = []


def threaded_client(conn, ip):
    while True:  # Send and Receive Data
        try:
            data = pickle.loads(conn.recv(2048))
            if not data:
                print(ip[0] + " Disconnected")
                break
            else:  # Update Players, Update Card Piles, Update Board Squares, Card Actions
                print("From " + str(ip[0]) + ", Received: " + str(data))
                if data == "?":
                    data = Server.added_players == Server.player_count - 1
                elif data[0] == "Name":
                    Server.players.append(Player(Server.player_count + 1, data[1]))
                    Server.player_count += 1
                    data = Server.players[-1]
                print("Sending " + str(data) + " to " + ip[0])
                conn.sendall(pickle.dumps(data))
        except error:
            break
    print(ip[0] + " Lost Connection")
    conn.close()


def check_server(server):
    try:
        sock.bind((server, port))
        return True
    except socket.error:
        return False


def start_server(count):
    Server.player_count = count
    sock.listen(Server.player_count)
    print("Waiting for Connection, Server Started")
    while True:
        connect, addr = sock.accept()
        print(addr[0] + " has Connected")
        start_new_thread(threaded_client, (connect, addr))