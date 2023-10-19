import socket
from _thread import *
import pickle
from player import Player
import random

port = 5555
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


class Server:
    added_players = 0
    player_count = 0
    players = []
    current_player = 0


def threaded_client(conn, ip):
    while True:  # Send and Receive Data
        try:
            data = pickle.loads(conn.recv(2048))
            if not data:
                print(ip[0] + " Disconnected")
                break
            else:  # Update Players, Update Card Piles, Update Board Squares, Card Actions
                if data == "?":  # Check if Game is Starting
                    if Server.added_players == Server.player_count:
                        data = Server.players  # Sends the Player List
                        print("Sending " + str(data) + " to " + ip[0])
                    else:
                        data = False
                elif data[0] == "Name":  # Creates a Player
                    print("From " + str(ip[0]) + ", Received Player Name: " + str(data[1]))
                    Server.players.append(Player(Server.added_players, data[1]))
                    data = Server.added_players  # Sends Player Number
                    Server.added_players += 1
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


def start_server(count, server):
    Server.player_count = count
    sock.listen(Server.player_count)
    print("Waiting for Connection, Server Started at " + server)
    while True:
        connect, addr = sock.accept()
        print(addr[0] + " has Connected")
        start_new_thread(threaded_client, (connect, addr))
