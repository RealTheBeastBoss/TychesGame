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
    current_player = 0
    current_player_to_update = 0
    players_to_update = 0
    board_to_update = 0
    card_piles_to_update = 0
    board_squares = []
    discard_pile = []
    red_cards = []
    blue_cards = []
    event_to_send = []


def threaded_client(conn, ip):
    while True:  # Send and Receive Data
        try:
            data = pickle.loads(conn.recv(2048*10))
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
                elif data == "!":  # Check for Updates
                    data = {}
                    if Server.current_player_to_update > 0:
                        data["curr_player"] = Server.current_player
                        Server.current_player_to_update -= 1
                    if Server.players_to_update > 0:
                        data["players"] = Server.players
                        Server.players_to_update -= 1
                    if Server.board_to_update > 0:
                        data["board"] = Server.board_squares
                        Server.board_to_update -= 1
                    if Server.card_piles_to_update > 0:
                        data["discard"] = Server.discard_pile
                        data["red"] = Server.red_cards
                        data["blue"] = Server.blue_cards
                        Server.card_piles_to_update -= 1
                    if data:
                        print("Sending " + str(data) + " to " + ip[0])
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


def start_server(count, server, game_board, red_cards, blue_cards):
    Server.player_count = count
    Server.board_squares = game_board
    Server.red_cards = red_cards
    Server.blue_cards = blue_cards
    Server.card_piles_to_update = count
    sock.listen(Server.player_count)
    print("Waiting for Connection, Server Started at " + server)
    while True:
        connect, addr = sock.accept()
        print(addr[0] + " has Connected")
        start_new_thread(threaded_client, (connect, addr))
